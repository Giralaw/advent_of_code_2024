#include <bits/stdc++.h>
using namespace std;


// cpp solution by errichto -- https://www.youtube.com/watch?v=0H524GLePNc
// code NOT mine
// was looking for a live work through of day 2 in cpp, will refer to this
// and his other stuff when getting a sense for how to do aoc-type cpp coding

int main() {
    int n = 1000;
    int answer = 0;
    for (int i = 0; i < n; i ++) {
        vector<int> a;
        while (true) {
            int x;
            scanf("%d", &x);
            a.push_back(x);
            char c;
            scanf("%c", &c);
            if (c == '\n') {
                break;
            }
        }
        int k = (int) a.size();
        bool ok = true;
        bool only_inc = true;
        bool only_dec = true;

        for (int j = 0; j < k -1; j ++) {
            int diff = a[j+1] - a[j];
            if (diff > 0) {
                only_dec = false;
            }
            if (diff < 0) {only_inc = false;
            }
            if (!(1 <= abs(diff) && abs(diff) <= 3)) {
                ok = false;
                break;
            }
        }
        if (ok && (only_inc || only_dec)) {
            answer++;
        }
    }
    printf("%d\n", answer);
}