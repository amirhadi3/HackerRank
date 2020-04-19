def staircase(n):
    for i in range(1, n + 1):
        print(f'%{n - i}s' % '', end='')
        for j in range(1, i + 1):
            print('#', end='')
        print()


staircase(6)
