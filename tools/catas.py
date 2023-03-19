from math import sqrt, ceil


def cantor(n : int) -> str:
    i = ceil((-1 + sqrt(1 + 8 * n)) / 2)
    diff = n - i * (i - 1) // 2
    return f'{diff}/{i + 1 - diff}' if not i % 2 else f'{i + 1 - diff}/{diff}'


if __name__ == '__main__':
    print(cantor(121))
