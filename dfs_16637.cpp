#include <iostream>
#include <algorithm>
using namespace std;
#pragma warning (disable:4996)

int N, answer = -1000000000;
string line;

int cal(int a, int b, char oper)
{
	switch (oper)
	{
	case '+': return a + b;
	case '*': return a * b;
	case '-': return a - b;
	}

	return 0;
}


void backtracking (int idx, int pre_result)
{
	if (idx > N - 1)
	{
		answer = max(answer, pre_result);
		return;
	}

	char oper = (idx == 0) ? '+' : line[idx - 1];

	// 묶는 경우
	if (idx + 2 < N)
	{
		int tied = cal(line[idx] - '0', line[idx + 2] - '0', line[idx + 1]);
		backtracking(idx + 4, cal(pre_result, tied, oper));
	}
	
	// 안 묶는 경우
	backtracking(idx + 2, cal(pre_result, line[idx] - '0', oper));
}

void input() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	//freopen("input.txt", "r", stdin);

	cin >> N;
	cin >> line;
}


int main() {
	input();
	backtracking(0, 0);
	cout << answer << "\n";
	
	return 0;
}
