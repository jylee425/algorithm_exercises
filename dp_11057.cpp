#include <iostream>
#include <numeric>
#define mod 10007
using namespace std;

int DP[1001][10] = { 0 };
int N, sum = 0;

int main() {

	cin >> N;

	for (int i = 0; i < 10; i++) {
		DP[1][i] = 1;
	}

	for (int i = 2; i <= N; i++) {
		for (int j = 0; j < 10; j++) {
			for (int k = j; k < 10; k++) {
				DP[i][k] += DP[i - 1][j] % mod;
			}
		}
	}

	for (int i = 0; i < 10; i++) {
		sum += DP[N][i];
	}

	cout << sum % mod << "\n";
	

	return 0;
}
