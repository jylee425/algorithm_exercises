#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;
 
typedef struct {17135.
    int x;
    int y;
    int dist;
} enemy;
 
int N, M, D, answer, tmp_answer;
int board[16][16];
int copy_board[16][16];
bool visited[16][16];
bool selected[16];
vector<pair<int, int>> q;
vector<int> archor;
 
int bigger(int a, int b) { 
  if (a > b) return a; else return b;
}

bool enemy_less(enemy x, enemy y) {
    if (x.dist <= y.dist) {
        if (x.dist == y.dist) {
            if (x.y < y.y) {
                return true;
            } else {
              return false;
            }
        } else { // x.dist < y.dist
            return true;
        }
    } else { // x.dist > y.dist
        return false;
    }
}

int distance(int x, int y, int xx, int yy) {
    return abs(x - xx) + abs(y - yy);
}
 
void input() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    //freopen("input.txt", "r", stdin);
    
    cin >> N >> M >> D;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> board[i][j];
        }
    }
}
 
void copy() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            copy_board[i][j] = board[i][j];
        }
    }
}
 
bool check() {
    bool flag = true;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (copy_board[i][j] == 1) {
                q.push_back(pair<int, int>(i, j));
                flag = false;
            }
        }
    }
    return flag;
}
 
void greedy() {
    pair<int, int> targets[3];
 
    // select the enemy
    for (int i = 0; i < archor.size(); i++) {
        int x = N;
        int y = archor[i];
        vector<enemy> candidates;
 
        for (int j = 0; j < q.size(); j++) {
            int xx = q[j].first;
            int yy = q[j].second;
 
            int dist = distance(x, y, xx, yy);
            if (dist <= D) {
                enemy tmp;
                tmp.x = xx;
                tmp.y = yy;
                tmp.dist = dist;
                candidates.push_back(tmp);
            }
        }
 
        if (candidates.size() >= 1) {
            sort(candidates.begin(), candidates.end(), enemy_less);
            targets[i].first = candidates[0].x;
            targets[i].second = candidates[0].y;
        }
        else {
            targets[i].first = -1;
            targets[i].second = -1;
        }
    }
 
    // kill the enemy
    for (int i = 0; i < 3; i++) {
        int x = targets[i].first;
        int y = targets[i].second;
        
        if (x == -1 && y == -1) continue;
        if (visited[x][y] == false) {
            visited[x][y] = true;
            copy_board[x][y] = 0;
            tmp_answer++;
        }
    }
}
 
void move() {
    for (int i = q.size() - 1; i >= 0; i--) {
        int x = q[i].first;
        int y = q[i].second;
 
        if (copy_board[x][y] == 0) continue;
        if (x == N - 1) {
            copy_board[x][y] = 0;
        }
        else {
            copy_board[x][y] = 0;
            copy_board[x + 1][y] = 1;
        }
    }
}
 
void turn() {
    copy();
    while (1)
    {
        q.clear();
        memset(visited, false, sizeof(visited));
 
        if (check() == true) break;
        greedy();
        move();
    }
}
 
void simulate(int idx, int cnt) {
    if (cnt == 3) {
        tmp_answer = 0;
        turn();
        answer = bigger(answer, tmp_answer);
        return;
    }
 
    for (int i = idx; i < M; i++) {
        if (selected[i] == true) continue;
        selected[i] = true;
        archor.push_back(i);
        simulate(i, cnt + 1);
        archor.pop_back();
        selected[i] = false;
    }
}
 
int main(void) {
    input();
    simulate(0, 0);
    cout << answer << "\n";
 
    return 0;
}
