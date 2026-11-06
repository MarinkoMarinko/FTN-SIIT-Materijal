#ifndef VEZBA03_STD_LIB_FACILITIES_H
#define VEZBA03_STD_LIB_FACILITIES_H

// Portable replacement for the 2010 course support header.
// This file is infrastructure, NOT part of the debugging exercise.
// It intentionally keeps the helper names expected by the original examples.
// The calculator source files have not been repaired.

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <exception>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

// The original teaching material relies on these names in the global namespace.
using namespace std;

// Preserve the original header's checked-vector behaviour so an invalid index
// produces an exception instead of silently invoking undefined behaviour.
struct Range_error : out_of_range {
    int index;
    explicit Range_error(int i)
        : out_of_range("Range error: " + std::to_string(i)), index(i) {}
};

template <class T>
struct Vector : std::vector<T> {
    using base = std::vector<T>;
    using size_type = typename base::size_type;
    using base::base;

    T& operator[](size_type i) {
        if (i >= this->size()) throw Range_error(static_cast<int>(i));
        return base::operator[](i);
    }

    const T& operator[](size_type i) const {
        if (i >= this->size()) throw Range_error(static_cast<int>(i));
        return base::operator[](i);
    }
};

// Kept for compatibility with the original course examples.
#define vector Vector

[[noreturn]] inline void error(const string& message) {
    throw runtime_error(message);
}

[[noreturn]] inline void error(const string& part1, const string& part2) {
    error(part1 + part2);
}

[[noreturn]] inline void error(const string& message, int number) {
    error(message + ": " + std::to_string(number));
}

inline void keep_window_open() {
    cin.clear();
    cout << "Please enter a character to exit\n";
    char ch;
    cin >> ch;
}

inline void keep_window_open(const string& text) {
    if (text.empty()) return;
    cin.clear();
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    for (string input; cout << "Please enter " << text << " to exit\n" && cin >> input; ) {
        if (input == text) return;
    }
}

inline void simple_error(const string& message) {
    cerr << "error: " << message << '\n';
    keep_window_open();
    std::exit(1);
}

template<class Result, class Argument>
Result narrow_cast(const Argument& value) {
    Result result = static_cast<Result>(value);
    if (static_cast<Argument>(result) != value) error("info loss");
    return result;
}

inline int randint(int maximum) { return std::rand() % maximum; }
inline int randint(int minimum, int maximum) {
    return randint(maximum - minimum) + minimum;
}

#endif  // VEZBA03_STD_LIB_FACILITIES_H
