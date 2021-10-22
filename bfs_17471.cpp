#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>
#pragma warning (disable : 4996)

using namespace std;

int N = 0, answer = 100 * 100;
int people[11] = {};
int link[11][11] = {};
int checker = false;

int smaller(int a, int b) { if (a < b) return a; else return b; }

void input() {
	ios::sync_with_stdio;
	cin.tie(NULL); cout.tie(NULL);
	//freopen("input.txt", "r", stdin);

	cin >> N;
	for (int n = 0; n < N; n++) {
		cin >> people[n];
	}

	for (int src = 0; src < N; src++) {
		int num;
		cin >> num;

		int dst;
		for (int l = 0; l < num; l++) {
			cin >> dst;
			link[src][dst - 1] = 1;
			link[dst - 1][src] = 1;
		}
	}

	return;
}

bool check(int* selected) {
	bool ok = false;
	int area_0_count = 0, area_1_count = 0;
	for (int s = 0; s < N; s++) {
		if (selected[s] == 0) area_0_count++;
		else area_1_count++;
	}

	// check for area 1
	bool visited[11];
	memset(visited, false, sizeof(bool) * 11);
	int visited_count = 0;
	queue<int> q;

	for (int s = 0; s < N; s++) {
		if (selected[s] == 1) {
			q.push(s);
			visited[s] = true;
			visited_count++; 
			break;
		}
	}

	while (!q.empty()) {
		int src = q.front();
		q.pop();

		if (visited_count == area_1_count) {
			ok = true;
			break;
		}

		for (int dst = 0; dst < N; dst++) {
			if (!link[src][dst]) continue;
			if (selected[dst] == 0) continue;
			if (visited[dst]) continue;

			visited[dst] = true;
			visited_count++;
			q.push(dst);
		}
	}

	if (ok == false) return false;

	ok = false;
	memset(visited, false, sizeof(bool) * 11);
	visited_count = 0;

	for (int s = 0; s < N; s++) {
		if (selected[s] == 0) { 
			q.push(s);
			visited[s] = true;
			visited_count++; break;
		}
	}

	while (!q.empty()) {
		int src = q.front();
		q.pop();

		if (visited_count == area_0_count) {
			ok = true;
			break;
		}

		for (int dst = 0; dst < N; dst++) {
			if (!link[src][dst]) continue;
			if (selected[dst] == 1) continue;
			if (visited[dst]) continue;

			visited[dst] = true;
			visited_count++;
			q.push(dst);
		}
	}

	return ok;
}

int compute(int *selected) {
	int a = 0, b = 0;
	for (int s = 0; s < N; s++) {
		if (selected[s]) a += people[s];
		else b += people[s];
	}

	int res = (a > b)? a - b : b - a;
	return res;
}

void simulate(int idx, int cnt, int *selected) {
	if (idx > (N / 2)) return;

	if (cnt >= 1 && N - cnt >= 1) {
		if (check(selected)) {
			checker = true;
			int tmp = compute(selected);
			answer = smaller(answer, tmp);
		}
	}

	for (int n = idx; n < N; n++) {
		if (selected[n] < 1) {
			selected[n] = 1;
			simulate(n, cnt + 1, selected);
			selected[n] = 0;
		}
	}
	return;
}

int main() {
	input(); 

	int selected[11];
	memset(selected, 0, sizeof(int) * N);
	simulate(0, 0, selected);

	if (checker) cout << answer << '\n';
	else cout << -1 << '\n';
	return 0;
}

