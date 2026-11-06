class Complex {
    private:
        double real;
        double imag;

    public:
        Complex(): real(0), imag(0) { }

        Complex(double real, double imag): real(real), imag(imag) { }

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

        Complex add(const Complex& b) {
            return Complex(this->real + b.getReal(), this->imag + b.getImag());
        }

        Complex sub(const Complex& b) {
            return Complex(this->real - b.getReal(), this->imag - b.getImag());
        }

        Complex mul(const Complex &c) {
            return Complex(
                this->real * c.getReal() - this->imag * c.getImag(),
                this->real * c.getImag() + this->imag * c.getReal()
            );
        }

        Complex conj() const {
            return Complex(this->real, -this->imag);
        }
};