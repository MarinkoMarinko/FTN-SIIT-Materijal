def fibo(n):            
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)


# 1 1 2 3 5 8 13
if __name__ == "__main__":
    n = 7
    print(fibo(n))