def diet_planner():

    """
    Prints (and returns) all those combinations of food items from the mess menu that satisfy the criteria stipulated
    by the dietitian. The combinations CAN INCLUDE duplicates/triplicates/... of a single type of food item.

    INPUT(S)
        None

    OUTPUTS(S)
        all_good_combinations - tuple

    """

    # We define a dictionary for each nutrient, with each containing the corresponding nutritional content in each
    # of the 6 food items. This will help in assessing the total nutritional content in any combination of food items.

    carbs = {"Rice": 195, "Veg Curry": 50, "Cheeseburger": 203, "Potato Chips": 78, "Roti": 76, "Soft Drink": 98}
    fats = {"Rice": 12, "Veg Curry": 36, "Cheeseburger": 95, "Potato Chips": 78, "Roti": 20, "Soft Drink": 7}
    proteins = {"Rice": 12, "Veg Curry": 42, "Cheeseburger": 150, "Potato Chips": 25, "Roti": 34, "Soft Drink": 8}
    vitamins = {"Rice": 5, "Veg Curry": 23, "Cheeseburger": 63, "Potato Chips": 14, "Roti": 14, "Soft Drink": 9}
    minerals = {"Rice": 7, "Veg Curry": 3, "Cheeseburger": 27, "Potato Chips": 12, "Roti": 6, "Soft Drink": 21}

    # We define a list of food items. This will be the basis for generating all possible combinations.

    food_items = ["Rice", "Veg Curry", "Cheeseburger", "Potato Chips", "Roti", "Soft Drink"]

    # The list of all combinations will start with a list of the individual food items.

    all_combinations = [[[item] for item in food_items]]

    # all_combinations will look like [[['Rice'],['Veg Curry'],['Cheeseburger'],['Potato Chips'],['Roti'],
    # ['Soft Drink']]].

    # We also create a separate list that will only contain "good" combinations (according to the dietitian).

    good_combinations = []

    # We will check if the individual food items satisfy the dietitian's criteria when eaten on their own.

    good_items = []

    for item in all_combinations[-1]:

        item = item[0]

        # We find the nutrient count of the item by using the dictionary defined earlier.

        carbs_count = carbs[item]
        fats_count = fats[item]
        proteins_count = proteins[item]
        vitamins_count = vitamins[item]
        minerals_count = minerals[item]

        # If the counts satisfy the dietitian's criteria, we will append the item to the list of good items.
        # We convert it to tuple format to match the desired output.

        if carbs_count <= 300 and fats_count <= 150 and 80 <= proteins_count <= 500 and 10 <= vitamins_count <= 100 and 10 <= minerals_count <= 50:
            good_items.append(tuple([item]))

    # We append the list of good items (i.e., good individual items) to the overall list of good combinations.

    good_combinations.append(good_items)

    # We iteratively increase the number of items in a combination as long as good combinations are found.

    while len(good_combinations[-1]) != 0:

        # We define a list that will contain all combinations of 'n' items at the end of each iteration.
        # For example, at the end of the first iteration, the list will contain all possible pairs of items.
        # This will then be appended to the list of all combinations.

        combos_of_n = []

        # We also maintain a list of each combination represented as a list of numbers. For example, the
        # combination ['Rice','Rice','Roti'] will be represented as [2,0,0,0,1,0], with their counts in the same index
        # positions as they appear in the list of food items. This will help ensure that identical combinations
        # are not considered. For example, if ['Rice','Rice','Roti'] has already been considered, we should
        # not consider ['Rice','Roti','Rice'] as a new combination. These two combinations will have the same
        # numerical representation - [2,0,0,0,1,0].

        combo_counts = []

        # We also maintain a list of good combinations of size 'n'. This will help us decide when to terminate
        # our iteration.

        good_combos_of_n = []

        # We will use the latest combination of items to create new combinations. For example, to create all possible
        # triples, we will use the already existing list of pairs (which is present as the last element in the list
        # of all combinations).

        for combination in all_combinations[-1]:

            # To create a combination of size 'n', we can just add 1 food item to an already existing combination of
            # size 'n-1'. By iterating through all combinations of size 'n-1' and iterating through all food items,
            # we can create all combinations of size 'n'.

            for item in food_items:

                possible_combination = combination + [item]
                food_count = [possible_combination.count(food_item) for food_item in food_items]

                # We append the new combination of size 'n' to the list of combinations of size 'n' if it is not
                # already present in the list. We can then check if it is a good combination.

                if food_count not in combo_counts:

                    combos_of_n.append(possible_combination)
                    combo_counts.append(food_count)

                    # We initialise the nutrient count of the combination with zeros.

                    carbs_count = 0
                    fats_count = 0
                    proteins_count = 0
                    vitamins_count = 0
                    minerals_count = 0

                    # We iterate through each food item in the combination and add its individual nutritional value to
                    # the overall counts.

                    for food_item in possible_combination:

                        carbs_count += carbs[food_item]
                        fats_count += fats[food_item]
                        proteins_count += proteins[food_item]
                        vitamins_count += vitamins[food_item]
                        minerals_count += minerals[food_item]

                    # If the overall counts satisfy the dietitian's criteria, we will append the combination to the
                    # list of good combinations. We convert it to tuple format to match the desired output.

                    if carbs_count <= 300 and fats_count <= 150 and 80 <= proteins_count <= 500 and 10 <= vitamins_count <= 100 and 10 <= minerals_count <= 50:
                        good_combos_of_n.append(tuple(possible_combination))

        # We append the list of combinations of size 'n' to the overall list of combinations.

        all_combinations.append(combos_of_n)

        # We append the list of good combinations of size 'n' to the overall list of good combinations.

        good_combinations.append(good_combos_of_n)

    # Once the iteration is terminated, good_combinations looks like [[good_combos_of_1],[good_combos_of_2],
    # [good_combos_of_3],...]. We have to concatenate the elements together to make it a continuous list.

    all_good_combinations = []
    for good_combination in good_combinations:
        all_good_combinations += good_combination

    # all_good_combinations looks like [good_combos_of_1, good_combos_of_2, good_combos_of_3,...]

    # We convert the list of all good combinations to a tuple of tuples.

    all_good_combinations = tuple(all_good_combinations)

    # We print and return all the good combinations.

    print(all_good_combinations)

    return all_good_combinations


# We call diet_planner() to see the output.

diet_planner()
