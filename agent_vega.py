def agent_vega(chamber):

    """
    Returns the count of possible prism locations in the chamber.

    INPUT(S)
        chamber - list

    OUTPUT(S)
        count - int

    EXAMPLES(S)
        agent_vega([['#', '.', '.'], ['#','.', '.'], ['#','.', '.']]) = 6
        agent_vega([['#', '.', '#'], ['#', '.', '#'], ['#', '.', '#']]) = 0

    """

    # We define the dimensions of the chamber.

    N = len(chamber[0])

    # We create a scoring matrix of size (N+1) x (N+1) with the rightmost column and the bottommost row as padding.
    # This prevents an IndexError that may arise later. This takes O(n+n) = O(n) time.

    scores = [[""] * N + ["F"] for i in range(N)]
    scores += [["F"] * (N + 1)]

    # We initialise the count of valid prism positions as 0.

    count = 0

    # We start from the right bottom element and work our way through the chamber row-by-row (from bottom to top).
    # We iterate through each row from right to left. This takes O(n*n) = O(n^2) time.

    for i in range(N - 1, -1, -1):

        # We define the current row being checked.

        row = chamber[i]

        for j in range(N - 1, -1, -1):

            # We define the current element being checked.

            element = row[j]

            # If there is a blocker in that cell, we set its score as 'B' (for blocked).

            if element == "#":
                scores[i][j] = "B"

            else:

                # If the element to the right is a blocker or is itself blocked to the right, we set the score
                # of the element as 'RB' (for right blocked).

                if scores[i][j + 1] == "B" or "RB" in scores[i][j + 1]:
                    scores[i][j] += "RB"

                # If the element to the bottom is a blocker or is itself blocked to the bottom, we set the score
                # of the element as 'DB' (for down blocked).

                if scores[i + 1][j] == "B" or "DB" in scores[i + 1][j]:
                    scores[i][j] += "DB"

                # If the element to the right is not a blocker and is not right blocked itself and if the element to
                # the bottom is not a blocker and is not down blocked itself, the current element is a valid position.
                # We set its score as 'F' (for free) and update the count of positions.

                elif scores[i][j + 1] != "B" and scores[i + 1][j] != "B" and "RB" not in scores[i][j + 1] and "DB" not in scores[i + 1][j]:
                    scores[i][j] = "F"
                    count += 1

    # We return the count of valid positions.

    return count

    # The overall time complexity is O(n + n^2) = O(n^2)
