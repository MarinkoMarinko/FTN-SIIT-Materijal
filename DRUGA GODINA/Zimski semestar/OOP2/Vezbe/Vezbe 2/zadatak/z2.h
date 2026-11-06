#include<iostream>
#include<vector>

using namespace std;

template <typename T>
void printEvenThenOdd(vector<T> v) {
    for (int i = 0; i < v.size(); i+=2) {
        cout << v[i] << " ";
    }

    for(int i = 1; i < v.size(); i+=2) {
        cout << v[i] << " ";
    }
}