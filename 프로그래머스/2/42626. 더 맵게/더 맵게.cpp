#include <algorithm>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    make_heap(scoville.begin(), scoville.end(), greater<int>());

    while (scoville.size() > 1) {
        int first = scoville.front();
        if (first >= K)
            break;
        pop_heap(scoville.begin(), scoville.end(), greater<int>());
        scoville.pop_back();
        
        int second = scoville.front();
        pop_heap(scoville.begin(), scoville.end(), greater<int>());
        scoville.pop_back();

        scoville.push_back(first + second * 2);
        push_heap(scoville.begin(), scoville.end(), greater<int>());
        
        answer++;
    }
    if (scoville.front() < K) {
        return -1;
    }
    return answer;
}