import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Normal


class Actor(nn.Module):
    def __init__(self, state_dim, action_dim, hidden_dim=256):
        super(Actor, self).__init__()
        self.fc1 = nn.Linear(state_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, action_dim)
        self.action_var = torch.ones((action_dim,)) * 0.5

    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        mean = torch.tanh(self.fc3(x))  # Assuming actions are in the range [-1, 1]

        return mean

    def sample_action(self, state):
        mean = self.forward(state)
        std = self.action_var
        dist = Normal(mean, std)
        action = dist.sample()
        log_prob = dist.log_prob(action)

        return action, log_prob


class Critic(nn.Module):
    def __init__(self, state_dim, action_dim, hidden_dim=256):
        super(Critic, self).__init__()
        self.fc1 = nn.Linear(state_dim + action_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, 1)

    def forward(self, state, action):
        x = torch.cat([state, action], dim=-1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        value = self.fc3(x)

        return value


class DDPG:
    def __init__(
        self, state_dim, action_dim, hidden_dim=256, actor_lr=1e-3, critic_lr=1e-3
    ):
        self.actor = Actor(state_dim, action_dim, hidden_dim)
        self.critic = Critic(state_dim, action_dim, hidden_dim)

        self.target_actor = Actor(state_dim, action_dim, hidden_dim)
        self.target_critic = Critic(state_dim, action_dim, hidden_dim)

        self.target_actor.load_state_dict(self.actor.state_dict())
        self.target_critic.load_state_dict(self.critic.state_dict())

        # optimizers
        self.actor_optimizer = torch.optim.Adam(self.actor.parameters(), lr=actor_lr)
        self.critic_optimizer = torch.optim.Adam(self.critic.parameters(), lr=critic_lr)

    def select_action(self, state):
        state = torch.FloatTensor(state).unsqueeze(0)
        action, _ = self.actor.sample_action(state)
        return action.detach().cpu().numpy()[0]

    def train(self, replay_buffer, batch_size=64, gamma=0.99):
        if len(replay_buffer) < batch_size:
            return

        # Sample a batch from the replay buffer
        states, actions, rewards, next_states, dones = replay_buffer.sample(batch_size)

        states = torch.FloatTensor(states)
        actions = torch.FloatTensor(actions)
        rewards = torch.FloatTensor(rewards).unsqueeze(1)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones).unsqueeze(1)

        # Update Critic
        with torch.no_grad():
            next_actions, _ = self.target_actor.sample_action(next_states)
            target_q = self.target_critic(next_states, next_actions)
            target_q = rewards + (1 - dones) * gamma * target_q

        current_q = self.critic(states, actions)
        critic_loss = F.mse_loss(current_q, target_q)

        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()

        # Update Actor
        actions_pred, log_probs = self.actor.sample_action(states)
        actor_loss = -self.critic(states, actions_pred).mean() + log_probs.mean()

        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        self.actor_optimizer.step()

        # Update target networks
        self.update_target_networks()
        return actor_loss.item(), critic_loss.item()

    def update_target_networks(self, tau=0.005):
        for target_param, param in zip(
            self.target_actor.parameters(), self.actor.parameters()
        ):
            target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)
        for target_param, param in zip(
            self.target_critic.parameters(), self.critic.parameters()
        ):
            target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)
