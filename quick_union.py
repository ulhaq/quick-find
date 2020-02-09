arr = []


def quick_union(N: int):
    global arr
    arr = [i for i in range(0, N)]
    print(arr)


def root(i: int) -> int:
    while i != arr[i]:
        i = arr[i]
    return i


def connected(p: int, q: int) -> bool:
    return root(p) == root(q)


def union(p: int, q: int):
    i = root(p)
    j = root(q)
    arr[i] = j


if __name__ == '__main__':
    quick_union(10)
    union(4, 3)
    union(3, 8)
    union(6, 5)
    union(9, 4)
    union(2, 1)
    print(connected(8, 9))
    print(connected(5, 4))
    union(5, 0)
    union(7, 2)
    union(6, 1)
    union(7, 3)
    
    print(arr)
