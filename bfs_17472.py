#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>
#include <vector>
#pragma warning (disable : 4996)

using namespace std;
int N, M;
int board[11][11], num;
int visited[11][11];
int dir[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
vector< pair<int, pair<int,int>> > bridge;
int linked[11][11], selected[100];
int answer;

int smaller(int a, int b) { if (a < b) return a; else return b; }

void copy(int src[][11], int dst[][11]) {
	for (int n = 0; n < N; n++) {
		for (int m = 0; m < M; m++) {
			src[n][m] = dst[n][m];
		}
	}

}

void input() {
	for (int i = 0; i < 11; i++) {
		memset(board[i], 0, sizeof(int) * 11);
		memset(visited[i], 0, sizeof(int) * 11);
		memset(linked[i], 0, sizeof(int) * 11);
	}
	memset(selected, 0, sizeof(int) * 100);

	cin >> N >> M;
	for (int n = 0; n < N; n++) {
		for (int m = 0; m < M; m++) {
			cin >> board[n][m];
		}
	}

	return;
}

void count(int n, int m) {
	while (true) {
		if (board[n][m] != 0 && visited[n][m] == 0)
			break;

		n += 1;
		if (n >= N) {
			n = 0;
			m += 1;

			if (m >= M)	return;
		}
	}

	num += 1;
	pair<int, int> now;
	queue< pair<int, int> > q;
	q.push(pair<int, int>(n, m));
	visited[n][m] = 1;
	board[n][m] = num;
	while (!q.empty()) {
		now = q.front();
		q.pop();

		int tx, ty;
		for (int i = 0; i < 4; i++) {
			tx = now.first + dir[i][0];
			ty = now.second + dir[i][1];

			if (tx < 0 || tx >= N || ty < 0 || ty >= M) continue;
			if (visited[tx][ty] == 1) continue;
			if (board[tx][ty] == 0) continue;

			q.push(pair<int, int>(tx, ty));
			visited[tx][ty] = 1;
			board[tx][ty] = num;
		}
	}

	//for (int x = 0; x < N; x++) {
	//	for (int y = 0; y < M; y++) {
	//		cout << board[x][y] << " ";
	//	}
	//	cout << "\n";
	//} cout << "\n";

	if (n < N) count(n + 1, m);
	else count(n, m + 1);

	return;
}

void link(int n, int m) {
	//cout << "in link\n";

	while (true) {
		if (board[n][m] != 0 && visited[n][m] == 0)
			break;

		n += 1;
		if (n >= N) {
			n = 0;
			m += 1;

			if (m >= M)	return;
		}
	}

	//cout << n << " " << m << " (island " << board[n][m] << "): \n";
	visited[n][m] = 1;
	
	int src = board[n][m], dst;
	for (int d = 0; d < 4; d++) {
		//cout << d << ": ";
		int tx = n, ty = m, tl = 0;
		while (true) {
			tx = tx + dir[d][0];
			ty = ty + dir[d][1];
			dst = board[tx][ty];

			//cout << "(" << tx << "," << ty << ") ";

			if (tx < 0 || tx >= N || ty < 0 || ty >= M) break;
			if (dst == src) break;
			if (dst != 0 && dst != src && tl >= 2) {
				//cout << "linked to " << board[tx][ty];
				bridge.push_back(pair<int, pair<int, int>>(tl, pair<int, int>(src, dst)));
				break;
			}
			if (dst != 0) break;

			tl = tl + 1;
		} //cout << "\n";
	} //cout << "\n";

	if (n < N) link(n + 1, m);
	else link(n, m + 1);

	return;
}

bool check() {
	queue<int> q;
	int nn = 0;
	int vvv[11] = { 0, };
	int src, dst;

	for (int k = 0; k < bridge.size(); k++) {
		if (selected[k] == 1) {
			src = bridge[k].second.first;
			vvv[src] = 1;
			q.push(src);
			break;
		}
	} 

	while (!q.empty()) {
		src = q.front();
		q.pop();

		nn = 0;
		for (int s = 1; s <= num; s++) {
			if (vvv[s] == 1) {
				nn += 1;
			}
		}

		if (nn >= num) {
			return true;
		}

		for (dst = 1; dst <= num; dst++) {
			if (src == dst) continue;
			if (linked[src][dst] == 0) continue;
			if (vvv[dst] == 1) continue;
			
			vvv[dst] = 1;
			q.push(dst);
		}
	}

	return false;
}

int compute() {
	int res = 0;
	for (int k = 0; k < bridge.size(); k++) {
		if (selected[k]) {
			res += bridge[k].first;
		}
	}

	return res;
}

void simulate(int idx, int cnt) {

	if (cnt >= 1) {
		bool checker = check();
		//cout << "in simulate: ";
		//for (int k = 0; k < bridge.size(); k++) {
		//	cout << selected[k] << " ";
		//} cout << "(" << checker<< ")\n";
		if (checker) {
			int tmp = compute();

			//cout << tmp << "\n";
			answer = smaller(answer, tmp);

		}
	}

	for (int v = idx; v < bridge.size(); v++) {
		if (selected[v] == 1) continue;

		if (linked[bridge[v].second.first][bridge[v].second.second] == 0) {
			selected[v] = 1;
			linked[bridge[v].second.first][bridge[v].second.second] = 1;
			linked[bridge[v].second.second][bridge[v].second.first] = 1;

			simulate(v, cnt + 1);

			selected[v] = 0;
			linked[bridge[v].second.first][bridge[v].second.second] = 0;
			linked[bridge[v].second.second][bridge[v].second.first] = 0;
		}
	}
	
	return;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	//freopen("input.txt", "r", stdin);

	for (int i = 0; i < 1; i++) {
		answer = 10 * 10 * 10;
		num = 0;

		input();

		count(0, 0);
		//for (int x = 0; x < N; x++) {
		//	for (int y = 0; y < M; y++) {
		//		cout << board[x][y] << " ";
		//	}
		//	cout << "\n";
		//} cout << "\n";

		for (int i = 0; i < 11; i++) {
			memset(visited[i], 0, sizeof(int) * 11);
		}
		link(0, 0);

		//for (int v = 0; v < bridge.size(); v++) {
		//	cout << "(" << bridge[v].second.first << ", " << bridge[v].second.second << " (" << bridge[v].first << "))" <<" ";
		//} cout << "\n";

		simulate(0, 0);

		if (answer == 10 * 10 * 10) cout << -1 << "\n";
		else cout << answer << "\n";

		bridge.clear();
	}

	return 0;
}
