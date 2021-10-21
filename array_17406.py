#include <iostream>
#include <algorithm>
#include <cstring>
#pragma warning (disable : 4996);

using namespace std;

int N, M, K;
int arr[51][51] = { 0, }, backup[51][51] = { 0, };
int query[7][3] = { 0, };
int selected[7] = { 0, };
int answer = 100 * 50 * 50;

int smaller(int a, int b) { if (a < b) return a; else return b; }

void input() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	//freopen("input.txt", "r", stdin);

	cin >> N >> M >> K;
	for (int n = 1; n <= N; n++) {
		for(int m = 1; m <= M; m++) {
			cin >> backup[n][m];
		}
	}

	for (int k = 0; k < K; k++) {
		cin >> query[k][0] >> query[k][1] >> query[k][2];
	}
	return;
}

void copy(int dst[][51], int src[][51]) {
	for (int n = 1; n <= N; n++) {
		for (int m = 1; m <= M; m++) {
			dst[n][m] = src[n][m];
		}
	}
}

void rotate(int R, int C, int S) {
	int res[51][51] = { 0, };
	copy(res, arr);

	// r,c 기준으로 s만큼 떨어진 곳의 각 4 변을 한칸씩 미는 방법
	for (int s = 1; s <= S; s++) {
		// 왼쪽
		//cout << "Left\n";
		for (int x = R - s; x <= R + s - 1; x++) {
			//cout << x << " " << C - s << ": " << res[x][C - S] << " " << arr[x + 1][C - S] << "\n";
			res[x][C - s] = arr[x+1][C - s];
		}


		// 위쪽
		//cout << "Top\n";
		for (int y = C - s + 1; y <= C + s; y++) {
			//cout << R - s << " " << y << ": " << res[R - S][y] << " " << arr[R - S][y - 1] << "\n";
			res[R - s][y] = arr[R - s][y-1];
		}


		// 오른쪽
		//cout << "Right\n";
		for (int x = R - s; x <= R + s - 1; x++) {
			//cout << x << " " << C + s << ": " << res[x][C + S] << " " << arr[x - 1][C + S] << "\n";
			res[x+1][C + s] = arr[x][C + s];
		}


		// 아래쪽
		//cout << "Down\n";
		for (int y = C + s; y >= C - s + 1; y--) {
			//cout << R + S << " " << y << ": " << res[R + S][y] << " " << arr[R + S][y + 1] << "\n";
			res[R + s][y-1] = arr[R + s][y];
		}

		
	}

	copy(arr, res);
	return;
}

int compute() {
	int res = 100 * 50 * 50;
	copy(arr, backup);

	for (int k = 0; k < K; k++) {
		int* kk = query[selected[k]];
		rotate(kk[0], kk[1], kk[2]);
	}

	for (int x = 1; x <= N; x++) {
		int tmp = 0;
		for (int y = 1; y <= M; y++) {
			tmp += arr[x][y];
		}
		res = smaller(res, tmp);
	}

	return res;
}

void dfs(int cnt) {
	if (cnt >= K) {
		int tmp = compute();
		answer = smaller(answer, tmp);
		return;
	}
	else {
		for (int k = 0; k < K; k++) {
			if (selected[k] < 0) {
				selected[k] = cnt;
				dfs(cnt + 1);
				selected[k] = -1;
			}
		}
	} 
}


int main() {
	input();

	memset(selected, -1, sizeof(int) * 7);
	dfs(0);

	cout << answer << '\n';
	return 0;
}
