#include <iostream>
#include <vector>

using namespace std;

template <typename T>
void inputVector(vector<T>& v) {
    int n;
    cout << "Unesite broj elemenata: ";
    cin >> n;

    T x;

    for (int i = 0; i < n; i++) {
        cout << "Element " << i + 1 << ": ";
        cin >> x;
        v.push_back(x);
    }
}