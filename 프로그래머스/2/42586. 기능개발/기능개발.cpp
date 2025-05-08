#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> remaining_days;
    
    for (int i = 0; i < progresses.size(); i++) {
        int days = ((100 - progresses[i]) / speeds[i]) + ((100 - progresses[i]) % speeds[i] != 0);
        remaining_days.push(days);
    }

    while (!remaining_days.empty()) {
        int cur = remaining_days.front(); remaining_days.pop();
        int cnt = 1;
        while (!remaining_days.empty() && cur >= remaining_days.front()) {
            remaining_days.front(); remaining_days.pop();
            cnt++;
        }
        answer.push_back(cnt);
    }
    return answer;
}