def say_hello():
    n, a, b = map(int, input().split())
    sulf = 1
    panel = a * b * 2 * sulf
    all1 = n * panel
    print(all1)


say_hello()
