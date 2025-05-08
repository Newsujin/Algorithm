#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    // 먼저 정렬
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());

    // 여벌이 있지만 도난당한 학생 처리 (자기 것만 사용 가능)
    vector<int> real_lost, real_reserve;

    for (int l : lost) {
        if (find(reserve.begin(), reserve.end(), l) == reserve.end()) {
            real_lost.push_back(l);
        }
    }

    for (int r : reserve) {
        if (find(lost.begin(), lost.end(), r) == lost.end()) {
            real_reserve.push_back(r);
        }
    }

    // 체육복 빌려주기
    for (int r : real_reserve) {
        auto it = find(real_lost.begin(), real_lost.end(), r - 1);
        if (it != real_lost.end()) {
            real_lost.erase(it);
            continue;
        }

        it = find(real_lost.begin(), real_lost.end(), r + 1);
        if (it != real_lost.end()) {
            real_lost.erase(it);
            continue;
        }
    }

    return n - real_lost.size();  // 체육수업 가능한 학생 수
}

int main() {
    int n = 5;
    vector<int> lost = {2, 4};
    vector<int> reserve = {1, 3, 5};

    int result = solution(n, lost, reserve);
    cout << result << endl;  // 출력: 5
    return 0;
}