#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#pragma warning (disable:4996)

using namespace std;
void input();
int find();
void send(int pp);
void check();
bool compare(pair<int, int> a, pair<int, int> b);

int taxi_x, taxi_y;
int N, M, fuel;
int board[22][22] = { 0 };
pair< pair<int, int>, pair<int, int> > rider[401];
bool picked[401] = { false };
int dir[4][2] = { {0,1}, {0,-1}, {1,0}, {-1,0} }; 

void input() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	//freopen("input.txt", "r", stdin);

	cin >> N >> M >> fuel;

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> board[i][j];
		}
	}
	
	cin >> taxi_x >> taxi_y;

	for (int i = 0; i < M; i++) {
		pair< pair<int, int>, pair<int, int> > tmp;
		cin >> tmp.first.first >> tmp.first.second >> tmp.second.first >> tmp.second.second;
		rider[i] = tmp;
	}
}

bool compare(pair<int, int> a, pair<int, int> b) {
	if (a.second == b.second) {  //fuel
		if (rider[a.first].first.first == rider[a.first].first.first) {
			return rider[a.first].first.second < rider[a.first].first.second;
		}
		else
			return rider[a.first].first.first < rider[a.first].first.first;
	}
	else {                 
		return a.second < b.second;
	}

}

// bfs
int find() {
	int pp = -1;
	int cur_x = 0, cur_y = 0;
	int used = 0;

	bool picked_tmp[401] = { false };
	bool visited[21][21] = { false };

	queue<pair<int, pair<int, int>>> q;
	q.push(pair<int, pair<int, int>>(0, pair<int, int>(taxi_x, taxi_y)));

	vector<pair<int, int>> buffer;

	while (!q.empty()) {
		used = q.front().first;
		cur_x = q.front().second.first;
		cur_y = q.front().second.second;
		//cout << "now: " << cur_x << " " << cur_y << " with used " << used << "\n";
		q.pop();

		// whether here is person
		for (pp = 0; pp < M; pp++) {
			if (cur_x == rider[pp].first.first && cur_y == rider[pp].first.second && !picked[pp]
				&& !picked_tmp[pp] ) {
				buffer.push_back(pair<int, int>(pp, used));
				picked_tmp[pp] = true;
			}
		}
		
		// to other
		for (int i = 0; i < 4; i++) {
			int next_x = cur_x + dir[i][0];
			int next_y = cur_y + dir[i][1];

			//cout << "next: " << next_x << " " << next_y << " using " << used + 1 << "\n";
			if (next_x < 1 || next_x > N || next_y < 1 || next_y > N) continue;
			if (visited[next_x][next_y]) continue;
			if (board[next_x][next_y] == 1) continue;

			q.push(pair<int, pair<int, int>>(used + 1, pair<int,int>(next_x, next_y)));
			visited[next_x][next_y] = true;
		}

	}

	if (buffer.size() < 1) {
		cout << -1;
		exit(0);
	}
	
	sort(buffer.begin(), buffer.end(), compare);
	pp = buffer[0].first;
	picked[pp] = true;
	//cout << "person " << pp+1 << ": (" << rider[pp].first.first << ", " << rider[pp].first.second << ")\n";

	used = buffer[0].second;
	fuel -= used;
	check();
	taxi_x = rider[pp].first.first; taxi_y = rider[pp].first.second;
	//cout << "out find with (" << cur_x << ", " << cur_y << ")\n";
	return pp;
}

// bfs
void send(int pp) {
	//cout << "in send with (" << taxi_x << ", " << taxi_y << ") to (" << rider[pp].second.first << ", " << rider[pp].second.second << ")\n";
	int cur_x = 0, cur_y = 0;
	int used = 0;

	bool visited[21][21] = { false };

	queue<pair<int, pair<int, int>>> q;
	q.push(pair<int, pair<int, int>>(0, pair<int, int>(taxi_x, taxi_y)));

	while (!q.empty()) {
		used = q.front().first;
		cur_x = q.front().second.first;
		cur_y = q.front().second.second;
		visited[cur_x][cur_y] = true;
		//cout << "now: " << cur_x << " " << cur_y << " with used " << used << "\n";
		q.pop();

		// whether here is person
		bool arrive = false;
		if (cur_x == rider[pp].second.first && cur_y == rider[pp].second.second) {
			arrive = true;
			break;
		}
		if (arrive) break;

		// to other
		for (int i = 0; i < 4; i++) {
			int next_x = cur_x + dir[i][0];
			int next_y = cur_y + dir[i][1];

			//cout << "next: " << next_x << " " << next_y << " using " << used+1 << "\n";
			if (next_x < 1 || next_x > N || next_y < 1 || next_y > N) continue;
			if (visited[next_x][next_y]) continue;
			if (board[next_x][next_y] == 1) continue;

			q.push(pair<int, pair<int, int>>(used + 1, pair<int, int>(next_x, next_y)));
			visited[next_x][next_y] = true;
		}

	}

	fuel -= used;
	check();
	fuel += used * 2;
	taxi_x = cur_x; taxi_y = cur_y;
	//cout << "arrived at (" << cur_x << ", " << cur_y << ")\n";
	return;
}

void check() {
	//cout << "fuel: " << fuel << "\n";
	if (fuel < 0) {
		cout << -1;
		exit(0);
	}
}

int main() {
	input();

	int pp = -1;
	for (int mm = 0; mm < M; mm++) {
		pp = find();
		//cout << "process " << mm << ": to person " << pp+1 << "\n";
		send(pp);
	}
	cout << fuel;
	return 0;
}
