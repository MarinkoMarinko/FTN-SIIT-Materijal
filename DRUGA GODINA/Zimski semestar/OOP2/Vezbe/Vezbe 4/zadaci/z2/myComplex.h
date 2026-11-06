
#include <iostream>

using namespace std;

class Complex {
private:
    double real;
    double imag;

public:
    Complex() : real(0), imag(0) {}

    Complex(double real, double imag) : real(real), imag(imag) {}

    double getReal() const {
        return this->real;
    }

    void setReal(double real) {
        this->real = real;
    }

    double getImag() const {
        return this->imag;
    }

    void setImag(double imag) {
        this->imag = imag;
    }

    Complex operator+(Complex b) const {
        return Complex(
            this->real + b.getReal(),
            this->imag + b.getImag()
        );
    }

    Complex operator-(Complex b) const {
        return Complex(
            this->real - b.getReal(),
            this->imag - b.getImag()
        );
    }

    Complex operator*(Complex b) const {
        return Complex(
            this->real * b.getReal() - this->imag * b.getImag(),
            this->real * b.getImag() + this->imag * b.getReal()
        );
    }

    Complex operator~() const {
        return Complex(this->real, -this->imag);
    }

    // b * 2
    Complex operator*(double x) const {
        return Complex(this->real * x, this->imag * x);
    }

    // 2 * b
    friend Complex operator*(double x, const Complex& b) {
        return b * x;
    }

    friend ostream& operator<<(ostream& out, const Complex& c) {
        out << "(" << c.real << ", " << c.imag << "i)";
        return out;
    }

    friend istream& operator>>(istream& in, Complex& c) {
        in >> c.real >> c.imag;
        return in;
    }
};
