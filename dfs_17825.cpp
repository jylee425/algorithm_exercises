#include<iostream>
using namespace std;

int ans = 0;
int arr[10]; // 주사위
int mal[4]; // 현재 말의 위치
int map[35]; // 윷놀이 판
int turn[35]; // - 판에서 방향 전환
bool check[35]; // - 현 위치에 말이 있는지 확인
int score[35]; // - 윷놀이 판의 점수

void dfs(int cnt, int sum) {
    if (cnt == 10) {
        if (sum > ans) ans = sum;

        return;
    }

    for (int i = 0; i < 4; i++) {
        int prev = mal[i];
        int now = prev;
        int move = arr[cnt];

        if (turn[now] > 0) {
            now = turn[now];
            move -= 1;
        }

        while (move--) {
            now = map[now];
        }

        if (now != 21 && check[now] == true) continue;

        check[prev] = false;
        check[now] = true;
        mal[i] = now;

        dfs(cnt + 1, sum + score[now]);

        mal[i] = prev;
        check[prev] = true;
        check[now] = false;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    for (int i = 0; i < 10; i++) {
        cin >> arr[i];
    }

    // 맵 초기화
    for (int i = 0; i < 21; i++) 
        map[i] = i + 1;
    map[21] = 21;
    for (int i = 22; i < 27; i++) 
        map[i] = i + 1;
    map[28] = 29; map[29] = 30; map[30] = 25;
    map[31] = 32; map[32] = 25; map[27] = 20;

    turn[5] = 22; turn[10] = 31; turn[15] = 28;
    turn[25] = 26;

    for (int i = 0; i < 21; i++) 
        score[i] = i * 2;
    score[22] = 13; score[23] = 16; score[24] = 19;
    score[31] = 22; score[32] = 24; score[28] = 28;
    score[29] = 27; score[30] = 26; score[25] = 25;
    score[26] = 30; score[27] = 35;


    dfs(0, 0);

    cout << ans << "\n";
    return 0;
}
