#include<iostream>
#include<vector>
#pragma warning(disable : 4996)
using namespace std;
int N;
int B, C;
vector<int> A;
long long answer;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	//freopen("input.txt", "r", stdin);
	cin >> N;
	while (N--) {
		int tmp;
		cin >> tmp;
		A.push_back(tmp);
	}

	cin >> B >> C;
	for (int i = 0; i < A.size(); i++) {
		int person = A[i] - B;
		answer++;
		if (person <= 0) {
			continue;
		}

		if (person % C > 0) {
			answer++;
		}
		answer += person / C;
	}

	cout << answer;

}
