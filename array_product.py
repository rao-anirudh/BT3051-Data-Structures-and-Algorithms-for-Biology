def minop(n, a):

    """
    Returns the minimum number of operations required to  make the product of the entire input array equal to 1.

    INPUT(S)
        n - int
        a - list

    OUTPUT(S)
        minimum_operations - int

    EXAMPLES(S)
        minop(3, [1,2,1]) = 1
        minop(5, [1,2,3,4,6]) = 11
        minop(4, [-5,-1,8,7]) = 17

    """

    # We initialise the number of operations as 0.

    operations = 0

    # We segregate the input array into positive and negative integers. We also keep count of the number of zeroes.
    # This segregation takes O(n) time.

    negatives = []
    positives = []
    zeros = 0

    for x in a:
        if x < 0:
            negatives.append(x)
        elif x > 0:
            positives.append(x)
        elif x == 0:
            zeros += 1

    # If the number of negative integers is odd and there are no zeroes, we need to convert one of the negative
    # integers to 1 and the other integers to -1. -1 multiplied an even number of times will be equal to 1.
    # In the worst case this will take O(n/2) time.

    if len(negatives) % 2 != 0 and zeros == 0:
        operations += 1 - negatives[0]
        for negative in negatives[1:]:
            operations += -1 - negative

    # If the number of negative integers is even or there is at least 1 zero, we can convert all negative integers
    # to -1 as their combined product will be 1. This will require lesser operations than converting them all to 1.

    else:
        for negative in negatives:
            operations += -1 - negative

    # All the positive integers have to be converted to 1. In the worst case, this will take O(n/2) time.

    for positive in positives:
        operations += positive - 1

    # All the zeros have to be converted to 1 (or -1) and this has to be added to the number of operations.

    minimum_operations = operations + zeros

    # We return the number of operations.

    return minimum_operations

    # The overall time complexity is O(n + n/2 + n/2) = O(n)
