# Implementation of Union-find algorithms
I have solved this assignment in Python.

- Quick-union
    For quick-union I considered a zero-based list of 10 elements. 
    - union(4, 3)
    - union(3, 8)
    - union(6, 5)
    - union(9, 4)
    - union(2, 1)
    - union(5, 0)
    - union(7, 2)
    - union(6, 1)
    - union(7, 3)

The result was: `[1, 8, 1, 8, 3, 0, 5, 1, 8, 8]`

- Weighted-union
    For weighted-union I considered a zero-based list of 10 elements.
    - union(4, 3)
    - union(3, 8)
    - union(6, 5)
    - union(9, 4)
    - union(2, 1)
    - union(5, 0)
    - union(7, 2)
    - union(6, 1)
    - union(7, 3)

The result was: `[6, 2, 6, 4, 6, 6, 6, 2, 4, 4]`
