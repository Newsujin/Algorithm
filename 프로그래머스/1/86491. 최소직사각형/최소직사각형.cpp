#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max_w = 0;
    int max_h = 0;

    for (const vector<int>& size : sizes) {
        int w = max(size[0], size[1]);
        int h = min(size[0], size[1]);

        max_w = max(max_w, w);
        max_h = max(max_h, h);
    }
    return max_h * max_w;
}