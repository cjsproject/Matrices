def adjugate(A, m=None):
    # Initialize
    sign = 1
    previous = pivot = 1

    # Bareiss formula
    def do_pivot(a, b, c, d, e):
        q, r = divmod(a * d - b * c, e)
        assert r == 0
        if m is None:
            return q
        return q % m

    # Assert square matrix
    n = len(A)
    assert all(len(row) == n for row in A)

    # Build augmented matrix
    am = [list(map(int, row)) + [0] * i + [1] + [0] * (n - i - 1)
          for i, row in enumerate(A)]

    # Iterate diagonally
    for j in range(n):

        # Test pivot
        if am[j][j] == 0:

            # Find pivot
            for i in range(j, n):
                if am[i][j] != 0:
                    break

            # Non-invertible detection
            else:
                return 0, [[0] * n for _ in range(n)]

            # Switch rows
            am[j], am[i] = am[i], am[j]
            sign *= -1

        # Get pivot
        previous, pivot = pivot, am[j][j]

        # Set zeros
        for i, row in enumerate(am):
            if i == j:
                continue
            am[i] = [
                do_pivot(pivot, y, row[j], x, previous)
                for x, y in zip(row, am[j])]

    # Determinant
    determinant = sign * pivot
    if m is not None:
        determinant %= m

    # Return
    return determinant, [row[n:] for row in am]


arr_a = [[1, 5],
         [3, 6]]

det, adj = adjugate(arr_a)

print(det, adj)
