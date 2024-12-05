def numways(n):

    """
    Returns the number of unique ways a person can reach the end of a staircase with 'n' stairs given that the
    person can only take 1, 2, or 3 steps at a time.

    INPUT(S)
        n - int

    OUTPUT(S)
        ways[n] - int

    EXAMPLES(S)
        numways(2) = 2              (2),(1,1)
        numways(3) = 4              (3),(2,1),(1,2),(1,1,1)
        numways(4) = 7              (3,1),(2,2),(2,1,1),(1,3),(1,2,1),(1,1,2),(1,1,1,1)

    """

    # If the input is zero or negative, we can return 0 as the situation is impossible. This is an edge case.

    if n <= 0:
        return 0

    # We define the base cases using a dictionary.

    ways = {1: 1, 2: 2, 3: 4}

    # To compute the number of ways to cover 'n' steps, we can create 3 sub-cases:
    # Case 1 - The person takes exactly 1 step first. This means the person has to complete 'n-1' steps.
    # Case 2 - The person takes exactly 2 steps first. This means the person has to complete 'n-2' steps. Note that
    #          the person takes these 2 steps at once, not (1,1).
    # Case 3 - The person takes exactly 3 steps first. This means the person has to complete 'n-3' steps. Note that
    #          the person takes these 3 steps at once, not (2,1) or (1,2) or (1,1,1).
    # Thus, the total number of ways to cover 'n' steps is the number of ways to cover 'n-1' steps, 'n-2' steps, and
    # 'n-3' steps independently. This can be represented as a recurrence relation:
    # numways(n) = numways(n-1) + numways(n-2) + numways(n-3)

    # To avoid repeated recursive calls, we store the outputs of numways(i) for i in 4,5,6,...,n in the earlier
    # defined dictionary. This memoisation ensures that the runtime is O(n).

    for i in range(4, n+1):
        ways[i] = ways[i-1] + ways[i-2] + ways[i-3]             # Recurrence relation

    # We can return numways(n)

    return ways[n]
