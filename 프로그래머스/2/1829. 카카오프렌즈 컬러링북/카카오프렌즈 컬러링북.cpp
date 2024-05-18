#include <vector>

using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int cnt, target;

void dfs(int i, int j, vector<vector<bool>>& visited, vector<vector<int>>& picture) {
    visited[i][j] = true;
    cnt++;
    for (int dir = 0; dir<4; dir++) {
        int nx = i + dx[dir], ny = j + dy[dir];
        if (nx < 0 || ny < 0 || nx >= visited.size() || ny >= visited[0].size()) continue;
        if (visited[nx][ny] || picture[nx][ny] != target) continue;
        dfs(nx, ny, visited, picture);
    }
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int row = picture.size(), col = picture[0].size();
    vector<int> answer(2, 0);
    vector<vector<bool>> visited(row, vector<bool>(col, false));
    
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (!visited[i][j] && picture[i][j]) {// 방문하지 않았고 색칠하는 부분이면
                answer[0]++;
                cnt = 0; target = picture[i][j];
                dfs(i, j, visited, picture);
                answer[1] = max(answer[1], cnt);
            }
        }
    }
    
    return answer;
}