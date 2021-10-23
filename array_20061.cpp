#include <iostream>
#include <queue>
#include <cstring>
#include <algorithm>
#pragma warning (disable : 4996)
using namespace std;

int N, answer;
int red[4][4], blue[4][6], green[6][4];
int tt[10001], xx[10001], yy[10001];

void input() {
    answer = 0, N =0;
    for (int i = 0; i < 4; i++) {
        memset(red[i], 0, sizeof(int) * 4);
    }
    for (int i = 0; i < 4; i++) {
        memset(blue[i], 0, sizeof(int) * 6);
    }
    for (int i = 0; i < 6; i++) {
        memset(green[i], 0, sizeof(int) * 4);
    }
    memset(tt, 0, sizeof(int) * 10001);
    memset(xx, 0, sizeof(int) * 10001);
    memset(yy, 0, sizeof(int) * 10001);

    cin >> N;
    for (int n = 0; n < N; n++) {
        cin >> tt[n] >> xx[n] >> yy[n];
    }
}

void output(int n) {
    cout << "blue:\n";
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 6; j++) {
            cout << blue[i][j] << ' ';
        } cout << "\n";
    } cout << "\n";

    cout << "green:\n";
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 4; j++) {
            cout << green[i][j] << ' ';
        } cout << "\n";
    } cout << "\n";
}

void special(int n) {
    int count;

    // green
    count = 0;
    for (int i = 0; i < 2; i++) {
        if (green[i][0] == 0 && green[i][1] == 0 && green[i][2] == 0 && green[i][3] == 0) continue;

        count += 1;
    }
    for (int i = 6 - 1; i > 2 - 1; i--) {
        for (int j = 0; j < 4; j++) {
            green[i][j] = green[i - count][j];
        }
    }
    for (int i = count; i > -1; i--) {
        for (int j = 0; j < 4; j++) {
            green[i][j] = 0;
        }
    }

    // blue
    count = 0;
    for (int j = 0; j < 2; j++) {
        if (blue[0][j] == 0 && blue[1][j] == 0 && blue[2][j] == 0 && blue[3][j] == 0) continue;

        count += 1;
    }
    for (int j = 6 - 1; j > 2 - 1; j--) {
        for (int i = 0; i < 4; i++) {
            blue[i][j] = blue[i][j - count];
        }
    }
    for (int i = count; i > -1; i--) {
        for (int j = 0; j < 4; j++) {
            blue[j][i] = 0;
        }
    }

    return;
}

void score() {
    //cout << "in score: ";

    //green
    for (int i = 6 - 1; i > 2 - 1; i--) {
        while (true) {
            if ((green[i][0] == 0 || green[i][1] == 0 || green[i][2] == 0 || green[i][3] == 0)) break;

            answer += 1;
            green[i][0] = green[i][1] = green[i][2] = green[i][3] = 0;
            for (int ii = i; ii > 0; ii--) {
                for (int j = 0; j < 4; j++) {
                    green[ii][j] = green[ii - 1][j];
                }
            }
        }
    }

    //blue
    for (int j = 6 - 1; j > 2 - 1; j--) {
        while (true) {
            if ((blue[0][j] == 0 ||blue[1][j] == 0 || blue[2][j] == 0 || blue[3][j] == 0)) break;

            answer += 1;
            blue[0][j] = blue[1][j] = blue[2][j] = blue[3][j] = 0;
            for (int jj = j; jj > 0; jj--) {
                for (int i = 0; i < 4; i++) {
                    blue[i][jj] = blue[i][jj-1];
                }
            }
        }
    }

   // cout << answer << "\n";
}

void move(int n) {
    int shape = tt[n];
    int x = xx[n], y = yy[n];
    bool flag;

    switch (shape) {
    case(1):
        //red
        red[x][y] = 1;

        //green
        flag = false;
        for (int i = 0; i < 5; i++) {
            if (green[i+1][y] == 0) continue;

            flag = true;
            green[i][y] = 1; 
            break;
        }
        if (!flag) {
            green[5][y] = 1;
        }

        //blue
        flag = false;
        for (int j = 0; j < 5; j++) {
            if (blue[x][j+1] == 0) continue;

            flag = true;
            blue[x][j] = 1; 
            break;
        } 
        if (!flag) {
            blue[x][5] = 1;
        }
        break;
    case(2):
        //red
        red[x][y] = red[x][y + 1] = 1;

        //green
        flag = false;
        for (int i = 0; i < 5; i++) {
            if (green[i+1][y] == 0 && green[i+1][y+1] == 0) continue;

            flag = true;
            green[i][y] = green[i][y+1] = 1;
            break;
        }
        if (!flag) {
            green[5][y] = green[5][y + 1] = 1;
        }

        //blue
        flag = false;
        for (int j = 0; j < 4; j++) {
            if (blue[x][j + 1] == 0 && blue[x][j + 2] == 0) continue;

            flag = true;
            blue[x][j] = blue[x][j + 1] = 1;
            break;
        }
        if (!flag) {
            blue[x][4] = blue[x][5] = 1;
        }

        break;
    case(3):
        //red
        red[x][y] = red[x + 1][y] = 1;

        //green
        flag = false;
        for (int i = 0; i < 4; i++) {
            if (green[i + 1][y] == 0 && green[i + 2][y] == 0) continue;

            flag = true;
            green[i][y] = green[i + 1][y] = 1;
            break;
        }
        if (!flag) {
            green[4][y] = green[5][y] = 1;
        }

        //blue
        flag = false;
        for (int j = 0; j < 5; j++) {
            if (blue[x][j + 1] == 0 && blue[x + 1][j + 1] == 0) continue;
            
            flag = true;
            blue[x][j] = blue[x + 1][j] = 1;
            break;
        }
        if (!flag) {
            blue[x][5] = blue[x + 1][5] = 1;
        }
        break;
    }
    return;
}

int count() {
    int res = 0;

    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 4; j++) {
            res += green[i][j];
        } 
    } 

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 6; j++) {
            res += blue[i][j];
        }
    }

    return res;
}

void simulate() {
    for (int n = 0; n < N; n++) {
       // cout << "turn is now " << n << " (" << tt[n] << ", " << xx[n] << ", " << yy[n] << ")\n";
        for (int i = 0; i < 4; i++) {
            memset(red[i], 0, sizeof(int) * 4);
        }

        move(n);

       // cout << "red:\n";
       // for (int i = 0; i < 4; i++) {
       //     for (int j = 0; j < 4; j++) {
       //         cout << red[i][j] << ' ';
       //     } cout << "\n";
       // } cout << "\n";

      //  cout << "move:\n";     output(n);
        score();
      //  cout << "score:\n";     output(n);
        special(n);
      //cout << "special:\n";     output(n);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    for (int ttt = 0; ttt < 2; ttt++) {
        input();

        simulate();

        cout << answer << "\n";
        cout << count() << "\n";
    }
    return 0;
}
