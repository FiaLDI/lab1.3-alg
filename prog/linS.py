
def leniarPoisk(a, b):
    for i in range(len(a)):
        if a[i] == b:
            return i
    return -1

if __name__ == '__main__':
    import time
    for i in range(10, 100, 10):
        a = [j for j in range(i)]
        b = 0
        for o in range(len(a) - 1, 1, -1):
            start = time.perf_counter()
            leniarPoisk(a, o)
            end = time.perf_counter()
            b += end - start
        print(f" {(b / (i - 3)):.8f}")