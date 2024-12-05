def birthday_problem(n):

    """
    Returns the probability that at least two people in a group of size n share a birthday, using a Monte Carlo
    simulation.

    INPUT(s)
        n - int

    OUTPUT(s)
        p - float

    """

    # We need the random library to perform the Monte Carlo simulation.

    import random

    # We set a random seed to ensure replicability of results.

    random.seed(3051)

    # We run 10000 independent trials and keep a track of the number of trials in which at least one shared
    # birthday was found.

    num_trials = 10000
    shared_birthdays = 0

    for experiment in range(1, num_trials + 1):

        # We maintain a count of the number of people in the group who have a given day of the year as their birthday.

        dates = {i: 0 for i in range(1, 367)}

        # For each person in the group, we randomly assign a birthday and update the count in the dictionary dates.

        for person in range(n):
            birthday = random.randint(1, 366)
            dates[birthday] += 1

            # If at any point the count of a particular date is more than 1, a shared birthday has been found and
            # we can move on to the next trial after updating the count of shared birthdays.

            if dates[birthday] == 2:
                shared_birthdays += 1
                break

    # The required probability is the number of trials in which a shared birthday was found divided by the total
    # number of trials conducted.

    p = shared_birthdays / num_trials

    # We return the value of the probability.

    return p
