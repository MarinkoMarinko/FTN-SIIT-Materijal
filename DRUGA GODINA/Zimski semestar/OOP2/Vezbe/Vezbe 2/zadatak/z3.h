#include<vector>

using namespace std;

template <typename T>
int countEven(vector<T> v) {
    int cnt = 0;
    for (int i = 0; i < v.size(); i++) {
        if (v[i] % 2 == 0) {
            cnt += 1;
        }
    }
    return cnt;
}

template <typename T>
int countOdd(vector<T> v) {
    return v.size() - countEven(v);
}