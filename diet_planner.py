def diet_planner():

    """
    Prints (and returns) all combinations of food items from the mess menu that satisfy the criteria stipulated
    by the dietitian. The combinations will NOT include duplicates/triplicates/... of a single item.

    INPUT(S)
        None

    OUTPUTS(S)
        good_combinations - tuple

    """

    # We define a dictionary for each nutrient, with each containing the corresponding nutritional content in each
    # of the 6 food items. This will help in assessing the total nutritional content in any combination of food items.

    carbs = {"Rice": 195, "Veg Curry": 50, "Cheeseburger": 203, "Potato Chips": 78, "Roti": 76, "Soft Drink": 98}
    fats = {"Rice": 12, "Veg Curry": 36, "Cheeseburger": 95, "Potato Chips": 78, "Roti": 20, "Soft Drink": 7}
    proteins = {"Rice": 12, "Veg Curry": 42, "Cheeseburger": 150, "Potato Chips": 25, "Roti": 34, "Soft Drink": 8}
    vitamins = {"Rice": 5, "Veg Curry": 23, "Cheeseburger": 63, "Potato Chips": 14, "Roti": 14, "Soft Drink": 9}
    minerals = {"Rice": 7, "Veg Curry": 3, "Cheeseburger": 27, "Potato Chips": 12, "Roti": 6, "Soft Drink": 21}

    # We define a list of food items as the basis for generating all possible combinations.

    food_items = ["Rice", "Veg Curry", "Cheeseburger", "Potato Chips", "Roti", "Soft Drink"]

    # The list of combinations will start with a list of the individual food items.

    combinations = [[[item] for item in food_items]]

    # combinations will look like [[['Rice'],['Veg Curry'],['Cheeseburger'],['Potato Chips'],['Roti'],['Soft Drink']]]

    # We iterate from 2 to 6 to create all possible combinations - pairs, triples, and so on.

    for n in range(2, 7):

        # We define a temporary list that will contain all combinations of 'n' items at the end of each iteration.
        # For example, at the end of the first iteration, the list will contain all possible pairs of items.
        # This will then be appended to the complete list of combinations.

        combo_of_n = []

        # We will use the latest combination of items to create new combinations. For example, to create all possible
        # triples, we will use the already existing list of pairs (which is present as the last element in the list
        # of combinations).

        for combination in combinations[-1]:

            # To create a combination of size 'n', we can just add 1 food item to an already existing combination of
            # size 'n-1'. By iterating through all combinations of size 'n-1' and iterating through all possible
            # food items that can be added, we can create all combinations of size 'n'. The food items that can be
            # added must have an index (in the list of food items) greater than the last item in the combination of
            # size 'n-1'. For example, consider the pair ['Rice','Cheeseburger']. To this, we can only add those
            # food items with a greater index than 'Cheeseburger' - 'Potato Chips', 'Roti', 'Soft Drink'.
            # The combination ['Rice','Veg Curry','Cheeseburger'] would have already been created when the combination
            # ['Rice','Veg Curry'] was being considered.

            # We obtain the index of the last food item in the current combination of size 'n-1' being considered

            last_item = combination[-1]
            last_item_index = None
            for index in range(len(food_items)):
                if food_items[index] == last_item:
                    last_item_index = index
                    break

            # We then iteratively add 1 item to this combination of size 'n-1' by selectively choosing which food
            # items can be added (i.e., those that have a greater index than the last food item in the combination
            # of size 'n-1').

            for item in food_items[last_item_index + 1:]:

                # We append the new combination of size 'n' to the list of combinations of size 'n'.

                combo_of_n.append(combination + [item])

        # We append the list of combinations of size 'n' to the list of combinations.

        combinations.append(combo_of_n)

    # combinations will look like [[combinations of 1],[combinations of 2],[combinations of 3],[combinations of 4],[combinations of 5],[combinations of 6]]

    # To test all combinations, it will be easier if they are present continuously and not as nested lists.
    # We iteratively concatenate to an empty list to get a continuous list of all combinations.

    all_combinations = []
    for combination_set in combinations:
        all_combinations += combination_set

    # all_combinations will look like [combinations of 1,combinations of 2,combinations of 3,combinations of 4,combinations of 5,combinations of 6]

    # We initialise an empty list of 'good' combinations.

    good_combinations = []

    # We iterate through all combinations and test them if they meet the criteria.

    for combination in all_combinations:

        # We initialise the nutrient count of the combination with zeros.

        carbs_count = 0
        fats_count = 0
        proteins_count = 0
        vitamins_count = 0
        minerals_count = 0

        # We iterate through each food item in the combination and add its individual nutritional value to
        # the overall count.

        for item in combination:

            carbs_count += carbs[item]
            fats_count += fats[item]
            proteins_count += proteins[item]
            vitamins_count += vitamins[item]
            minerals_count += minerals[item]

        # If the overall counts satisfy the dietitian's criteria, we will append the combination to the list of
        # good combinations. We convert it to tuple format to match the desired output.

        if carbs_count <= 300 and fats_count <= 150 and 80 <= proteins_count <= 500 and 10 <= vitamins_count <= 100 and 10 <= minerals_count <= 50:
            good_combinations.append(tuple(combination))

    # We convert the list of good combinations to a tuple of tuples.

    good_combinations = tuple(good_combinations)

    # We print and return the good combinations.

    print(good_combinations)

    return good_combinations


# We call diet_planner() to see the output.

diet_planner()
