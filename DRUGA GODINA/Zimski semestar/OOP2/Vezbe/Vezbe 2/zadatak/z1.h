#include <iostream>
#include <vector>

using namespace std;

template <typename T>
void printReverse(vector<T> v) {
    for (int i = v.size() - 1; i >= 0; i--) {
        cout << v[i] << " ";
    }
}