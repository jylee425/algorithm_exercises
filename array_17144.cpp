#include <iostream>
#pragma warning (disable:4996)

using namespace std;
int R, C, T;
int board[51][51], backup[51][51];
int c0, c1;
int dir[4][2] = { {-1, 0}, {1, 0}, {0, 1}, {0, -1} };

void copy(int dst[][51], int src[][51]) {
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++) {
			dst[r][c] = src[r][c];
		}
	}
}

void input() {
	board[51][51] = { 0, };

	cin >> R >> C >> T;
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++) {
			cin >> backup[r][c];
		}
	}

	for (int r = 0; r < R; r++) {
		if (backup[r][0] == -1) {
			c0 = r;
			c1 = r + 1;
			break;
		}
	}

}

void spread() {
	copy(board, backup);
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++) {
			if (backup[r][c] > 0) {
				//cout << backup[r][c] << " ";
				float amount = backup[r][c] / 5;
				//cout << amount << "\n";

				int count = 0;
				for (int i = 0; i < 4; i++) {
					int tr = r + dir[i][0];
					int tc = c + dir[i][1];

					if (tr < 0 || tr >= R || tc < 0 || tc >= C) continue;
					if (tc < 1 && (tr == c0 || tr == c1)) continue;

					//cout << "(" << tr << " " << tc << ") " << amount << " ";
					board[tr][tc] += int(amount);
					board[r][c] -= int(amount);
					count += 1;
				} //cout << "\n";
			}
		}
	}
	copy(backup, board);
}

void clean() {
	copy(board, backup);
	// 윗칸
	for (int c = C-2; c > 0; c--) {
		board[c0][c+1] = backup[c0][c];
	} board[c0][1] = 0;
	for (int c = 0; c < C-1; c++) {
		board[0][c] = backup[0][c+1];
	} 
	for (int r = 0; r < c0; r++) {
		board[r][C - 1] = backup[r + 1][C - 1];
	}
	for (int r = c0-1; r > 0; r--) {
		board[r][0] = backup[r - 1][0];
	}

	// 아랫칸
	for (int c = C - 2; c > 0; c--) {
		board[c1][c + 1] = backup[c1][c];
	} board[c1][1] = 0;
	for (int c = 0; c < C - 1; c++) {
		board[R-1][c] = backup[R - 1][c + 1];
	}
	for (int r = c1; r < R; r++) {
		board[r+1][C - 1] = backup[r][C - 1];
	}
	for (int r = R-1; r > c1+1; r--) {
		board[r-1][0] = backup[r][0];
	}

	copy(backup, board);
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(NULL);
	//freopen("input.txt", "r", stdin);

	for (int t = 0; t < 1; t++) {
		int answer = 0;

		input();

		for (int tt = 0; tt < T; tt++) {

			spread();

			clean();

		}

		answer = 0;
		for (int x = 0; x < R; x++) {
			for (int y = 0; y < C; y++) {
				answer += backup[x][y];
			}
		}
		cout << answer + 2 << "\n";
	}


	return 0;
}
