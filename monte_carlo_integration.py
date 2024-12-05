def monte_carlo_integration():

    """
    Prints the value of e obtained by evaluating the integral analytically, and also prints an estimated value of e
    by evaluating the integral of f(x) = 1/x between x = 0.5 and x = 2 using Monte Carlo integration.

    INPUT(s)
        None

    OUTPUT(s)
        None

    """

    # We need the random and math libraries to evaluate the integral.

    import random
    import math

    # We set a random seed to ensure replicability.

    random.seed(3051)

    # We use 100000 random points for our Monte Carlo integration.

    N = 100000

    # We keep a count of the number of points that lie under the curve.

    under = 0

    # We generate 100000 random points within a rectangle given by 0.5 <= x <= 2 and 0 <= y <= 2.

    for i in range(N):
        x = random.uniform(0.5, 2)
        y = random.uniform(0, 2)

        # If the random point lies under the curve, we increment the count.

        if y <= 1 / x:
            under += 1

    # The area of the rectangle from which we are sampling is given by (2 - 0.5) x 2.

    area_of_rectangle = (2 - 0.5) * 2

    # The area under the curve is given by the area of the rectangle multiplied by the probability of a random point
    # being found under the curve.

    area_under_curve = area_of_rectangle * (under / N)

    # The analytical solution of the integral is ln(2) - ln(0.5), which can be simplified to 2ln(2).
    # The value of e can be obtained by evaluating 2^(2ln(2)). This is because:
    # I = 2ln(2)
    # => I/2 = ln(2)
    # => e^(I/2) = 2
    # => e = 2^(2/I)
    # => e = 2^(2/2ln(2))

    analytical_solution = 2 * math.log(2)
    actual_e = 2 ** (2 / analytical_solution)
    print(f"The analytically obtained value of e is {actual_e}")

    # We can use the estimated area to get an estimate of e.

    estimate_of_e = 2 ** (2 / area_under_curve)
    print(f"The Monte Carlo estimated value of e is {estimate_of_e}")


# We call the function to obtain the results.

monte_carlo_integration()
