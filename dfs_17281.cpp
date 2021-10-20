#include <iostream>
#include <algorithm>
#include <cstring>
#pragma warning (disable : 4996)

using namespace std;

int N;
int pred[51][10] = { 0 };
int runner = 0;
int answer = -1;

int bigger(int a, int b) { if (a > b) return a; else return b; }

void input() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	//freopen("input.txt", "r", stdin);

	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> pred[i][j];
		}
	}
}

int move(int* base, int hit) {
	//cout << "move " << hit << " with base: ";
	//for (int b = 0; b < 4; b++) cout << base[b] << " ";
	//cout << "\n";

	int score = 0; 
	int in = 4 - hit;

	switch (hit) {
	case 1:
	case 2:
	case 3:
	case 4:
		for (int b = 3; b > -1; b--) {
			if (b >= in && base[b] == 1) {
				score += 1;
				base[b] = 0;
			}
			else if (b < in && base[b] == 1) {
				base[b + hit] = 1;
				base[b] = 0;
			}
		}
		break;
	default:
		score = -1;
		break;
	}

	return score;
}

int game(int* selected) {
	//cout << "in game\n";

	int score = 0;
	int runner = 0;

	for (int t = 0; t < N; t++) {
		int base[20] = { 0, 0, 0, 0 };
		int out = 0;
		while (out < 3) {
			base[0] = 1;
			int tmp = move(base, pred[t][selected[runner]]);

			if (tmp >= 0) {
				score += tmp;
			} else {
				out += 1;
			}

			runner = (runner + 1) % 9;
		}
	}
	return score;
}

void simulate(int cnt, int *selected) {
	//cout << "in simulation \nselected: [ ";
	//for (int s = 0; s < 9; s++) {
	//	cout << selected[s] << " ";
	//}
	//cout << "] \n\n";

	if (cnt >= 9) {
		int tmp = game(selected);
		answer = bigger(answer, tmp);
		return;
	}
	else {
		for (int p = 0; p < 9; p++) {
			if (p == 3) continue;

			if (selected[p] < 0) {
				selected[p] = cnt;
				simulate(cnt+1, selected);
				selected[p] = -1;
			}
		}
	}
}

int main() {
	input();

	int selected[10];
	memset(selected, -1, sizeof(int) * 10);
	selected[3] = 0; 
	simulate(1, selected);

	cout << answer << "\n";
	return 0;
}
