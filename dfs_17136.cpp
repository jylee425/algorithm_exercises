#include <iostream>
#include <queue>
#include <algorithm>
#pragma warning (disable : 4996)
using namespace std;

int board[11][11] = {0};
int paper_cnt[5] = { 0,0,0,0,0 };
int answer = 101;

int smaller(int a, int b){
  if (a<b) return a;
  else return b;
}

bool check(int x, int y, int size)
{
  //cout << "check size " << size << "\n";
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			if (board[x + i][y + j] == 0) {
        //cout << "false\n";
        return false;
      }
    }
	}
  //cout << "true \n";
	return true;
}

void attach(int x, int y, int s, int t) {
	for (int i = 0; i < s; i++)
		for (int j = 0; j < s; j++)
				board[x + i][y + j] = t;
}

void simulate(int x, int y, int cnt)
{
  //cout << "in: (" << x << ", " << y << ")\n";

	// find 1
	while (board[x][y] == 0) {
    y += 1;
		if (y >= 10) {
      y = 0;
      x += 1;

			if (x >= 10) {
				answer = smaller(answer, cnt);
				return;
			}
		}
	}
  //cout << "found 1 in (" << x << ", " << y << ")\n";

  // pruning
	if (answer <= cnt)
		return;

	// try attach for size (5,4,3,2,1)
	for (int ss = 5; ss > 0; ss--)
	{
		if (x + ss > 10 || y + ss > 10) continue;
    if (paper_cnt[ss] == 5) continue;

		if (check(x, y, ss)) {
      //cout << "attaching size " << ss << " to (" << x << ", " << y << ")\n";
			attach(x, y, ss, 0);
			paper_cnt[ss] += 1; 
			simulate(x, y, cnt + 1); 

			attach(x, y, ss, 1);
			paper_cnt[ss] -= 1;
		}
	}
}

void input() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  //freopen("input.txt", "r", stdin);
  //freopen("output.txt", "w", stdout);

  for(int x=0; x<10; x++){
    for(int y=0; y<10; y++) {
      cin >> board[x][y];
    }
  }
}

int main() {
  input();
  simulate(0, 0, 0);

  if (answer == 101)
    cout << -1 << "\n"; 
  else
    cout << answer << "\n";
  return 0;
}
