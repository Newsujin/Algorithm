#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> jobs) {
    sort(jobs.begin(), jobs.end());

    int answer = 0;
    int idx = 0;
    int cur_time = 0;
    int jobs_len = jobs.size();

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    while (idx < jobs_len || !pq.empty()) {
        while (idx < jobs_len && jobs[idx][0] <= cur_time) {
            pq.push({jobs[idx][1], jobs[idx][0]});
            idx++;
        }

        if (!pq.empty()) {
            int duration = pq.top().first;
            int start = pq.top().second;
            pq.pop();

            cur_time += duration;
            answer += cur_time - start;
        }
        else {
            cur_time = jobs[idx][0];
        }
    }
    return answer / jobs_len;
}