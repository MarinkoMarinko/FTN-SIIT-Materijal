#include <iostream>
#include <vector>

#include "input.h"
#include "z1.h"
#include "z2.h"
#include "z3.h"

using namespace std;

int main() {
    vector<int> v;
    inputVector(v);
    cout << "1. zahtev: " << endl;
    printReverse(v);
    cout << "\n2. zahtev: " << endl;
    printEvenThenOdd(v);
    cout << "\n3. zahtev: " << endl;
    cout << "Parni: " << countEven(v) << endl;
    cout << "Neparni: " << countOdd(v) << endl;
    return 0;
}