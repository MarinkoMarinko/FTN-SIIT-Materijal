def c_u_f(c):
    return 9 / 5 * c + 32

if __name__ == "__main__":
    for c in range(-10, 50, 10):
        print(f"{c} C -> {c_u_f(c):.1f} F")