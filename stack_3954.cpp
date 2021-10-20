#include<iostream>
#include<cstring>
#pragma warning (disable : 4996)
using namespace std;

int sm, sc, si;
int idx, idx_cmd, idx_input, idx_loop;
int memory[100000], loop[100000], visited[100000];
char query_code[100000], query_input[100000];
bool flag;

void init()
{
    idx = idx_cmd = idx_input = 0;
    idx_loop = -1;
    flag = false;
    memset(memory, 0, sizeof(memory));
    memset(loop, -1, sizeof(loop));
    memset(visited, 0, sizeof(visited));
}

void input()
{
    cin >> sm >> sc >> si;
    for (int i = 0; i < sc; i++) cin >> query_code[i];
    for (int i = 0; i < si; i++) cin >> query_input[i];
}

void find_loop()
{
    int stack[100000] = { 0, };
    int idx_stack = 0;
    for (int i = 0; i < sc; i++) {
		if (query_code[i] == '[') {
			stack[idx_stack] = i;
			idx_stack++;
		}
        else if (query_code[i] == ']')
        {
            int set = stack[idx_stack - 1];
            loop[i] = set;
            loop[set] = i;
            idx_stack--;
        }
    }
}

void interpret(char cmd) {
    switch (cmd) {
    case('-'):
        memory[idx] = (memory[idx]-1) % 256;
        break;
    case('+'):
        memory[idx] = (memory[idx]+1) % 256;
        break;
    case('<'):
        idx = (idx -1) & sm;
        break;
    case('>'):
        idx = (idx + 1) & sm;
        break;
    case('['):
		if (memory[idx] == 0) {
			idx_cmd = loop[idx_cmd];
		}
        break;
    case(']'):
        if (memory[idx] != 0) {
            if (idx_cmd > idx_loop) idx_loop = idx_cmd;
            idx_cmd = loop[idx_cmd];
        }
        break;
	case(','):
		if (idx_input < si) {
			memory[idx] = query_input[idx_input];
			idx_input++;
		}
		else {
			memory[idx] = 255;
		}
		break;
	default:
		break;
    }
}

void simulate() {
    find_loop();

    bool end = false;
    for (int i = 0; i < 50000000; i++) {
        if (idx_cmd == sc) {
			end = true;
            break;
        }

        char cmd = query_code[idx_cmd];
        interpret(cmd);
        idx_cmd++;
    }

    if (end) cout << "Terminates\n";
    else cout << "Loops " << loop[idx_loop] << " " << idx_loop << "\n";
	return;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    //freopen("Input.txt", "r", stdin);

    int test_num; cin >> test_num;
    for (int t = 1; t <= test_num; t++)
    {
        init();
        input();
        simulate();
    }

    return 0;
}
