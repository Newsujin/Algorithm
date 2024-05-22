#include <string>
#include <vector>
using namespace std;

string friends;
bool visited[8];
int answer;

void dfs(int cnt, char arr[], vector<string> data) {
    // 배치가 완료된 경우
    if (cnt == 8) {
        // 입력 arr 파싱
        for (int i = 0; i < data.size(); i++) {
            char f1 = data[i][0];
            char f2 = data[i][2];
            char op = data[i][3];
            int len = data[i][4] - '0';
            len++;

            // 두 프렌즈 위치 찾기
            int idx, iidx;
            idx = iidx = -1;
            for (int j = 0; j < 8; j++) {
                if (arr[j] == f1) idx = j;
                if (arr[j] == f2) iidx = j;
                if (idx != -1 && iidx != -1) break;
            }

            // 각 연산자별로 만족하지 않는 경우 return
            if (op == '=' && abs(idx - iidx) != len) return;
            if (op == '<' && abs(idx - iidx) >= len) return;
            if (op == '>' && abs(idx - iidx) <= len) return;
        }
        answer++;
        return;
    }
    // 프렌즈 순열 생성
    for (int i = 0; i < 8; i++) {
        if (visited[i] == true) continue;
        visited[i] = true;
        arr[cnt] = friends[i];
        dfs(cnt + 1, arr, data);
        visited[i] = false;
    }
}

int solution(int n, vector<string> data) {
    friends = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
    char arr[8] = {'\0'};
    answer = 0;
    dfs(0, arr, data);
    return answer;
}