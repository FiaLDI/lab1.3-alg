
def leniarPoisk(a, b):
    for i in range(len(a)):
        if a[i] == b:
            return i
    return -1

if __name__ == '__main__':
    import time
    for i in range(100, 1000, 100):
        a = [j for j in range(i)]
        b = 0
        for o in range(len(a), i + 1000):
            start = time.perf_counter()
            leniarPoisk(a, o)
            end = time.perf_counter()
            b += end - start
        print(f"{i} {(b / (i + 1000-1)):.8f}")
