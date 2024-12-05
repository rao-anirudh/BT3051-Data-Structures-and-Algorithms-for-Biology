def ellipse_area():
    """
    Prints the estimate for the area of the ellipse (x/2)^2 + (y/1)^2 = 1 using different numbers of random points
    ranging from 10 to 10000, and displays a plot of percentage relative error versus the number of points used.

    INPUT(s)
        None

    OUTPUT(s)
        None

    """

    # We will need to import some libraries to estimate the area and visualise the error.

    import random
    import matplotlib.pyplot as plt
    import math

    # We set a random seed to ensure replicability of results.

    random.seed(3051)

    # The true area of the ellipse is given by pi x a x b, where a = 2 and b = 1.

    analytical_solution = math.pi * 2 * 1

    # We maintain a list of percentage relative errors.

    errors = []

    # We iterate through different number of random points to be used to estimate the area.

    for N in range(10, 10001, 10):

        # We keep a count of the number of random points that lie within the ellipse.

        inside = 0

        # We generate N random points sampled from uniform distributions along the x and y axes.

        for i in range(N):
            x = random.uniform(0, 2)    # 0 <= x <= 2
            y = random.uniform(0, 1)    # 0 <= y <= 1

            # If the point lies inside the quadrant of the ellipse, we update the count.

            if ((x ** 2) / 4) + y ** 2 <= 1:
                inside += 1

        # The area of the rectangle from which we are sampling is 2 x 1.

        area_of_rectangle = 2 * 1

        # The ellipse has 4 identical quadrants.

        no_of_quadrants = 4

        # The area of the whole ellipse is the area of 1 quadrant times 4. The area of 1 quadrant is given by
        # the area of the rectangle multiplied by the probability of a random point being found inside the quadrant.

        area_of_ellipse = no_of_quadrants * area_of_rectangle * (inside / N)

        # We print the estimated area.

        print(f"Number of points = {N}    Area estimated = {area_of_ellipse}")

        # We append the percentage relative error of the estimate.

        errors.append(100*abs(area_of_ellipse - analytical_solution)/analytical_solution)

    # We visualise the change in percentage relative error with varying number of random points.

    plt.plot(range(10, 10001, 10), errors)
    plt.title("Percentage relative error in estimate of ellipse area \n with varying number of random points")
    plt.xlabel("Number of random points")
    plt.ylabel("Percentage relative error in estimate of ellipse area")
    plt.axhline(0, ls="--", c="r", lw=0.5)
    plt.show()


# We call the function to observe the results.

ellipse_area()
