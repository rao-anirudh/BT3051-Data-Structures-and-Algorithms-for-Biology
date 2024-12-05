def maxstud(n, skills):

    """
    Returns the maximum possible number of students can be included in a balanced study group.

    INPUT(S)
        n - int
        a - list

    OUTPUT(S)
        maxsize - int

    EXAMPLES(S)
        maxstud(5, [1,2,3,4,6]) = 5
        maxstud(4, [5,1,8,7]) = 3

    """

    # First we convert the list of skills into a set to retain the unique elements and then convert it back
    # into a list. This takes O(n) time.

    set_of_skills = list(set(skills))

    # We then sort the list of unique skills in ascending order. This takes O(nlogn) time.

    set_of_skills.sort()

    # We create a dictionary to keep count of the number of times a skill occurs in the original list. This takes
    # O(n + n) = O(n) time.

    counts = {skill: 0 for skill in set_of_skills}
    for skill in skills:
        counts[skill] += 1

    # If there is only 1 unique skill, we can simply return the number of times that skill occurs as this is the only
    # possible group that can be formed.

    if len(set_of_skills) == 1:
        return counts[set_of_skills[0]]

    # We initialise the size of the largest group possible as 0.

    max_size = 0

    # We iterate through the unique skills to determine the largest group size. In the worst case, this will take
    # O(n) time if the original list only has unique elements.

    for i in range(len(set_of_skills)):

        # We define the current skill being tested and the number of times it occurs in the original list.

        skill = set_of_skills[i]
        size = counts[skill]

        # If we have not reached the end of the list of unique skills, we can incrementally test skills that occur
        # to the right of the current skill being tested.

        if i != len(set_of_skills) - 1:

            # We define the index of the next skill being tested.

            j = i + 1

            # We iterate as long as the skill difference between the two skills is lesser than or equal to 5. We update
            # the size with the count of the valid skill. In the worst case, this takes 5 steps (e.g.,1->2->3->4->5->6).
            # The loop will break after this as the skill difference will exceed 5.

            while set_of_skills[j] - skill <= 5:
                size += counts[set_of_skills[j]]
                j += 1

                # We break out of the loop if we reach the end of the list of unique skills.

                if j == len(set_of_skills):
                    break

        # If the size of the group created is greater than the current maximum size, we update it.

        if size > max_size:
            max_size = size

    # We return the size of the largest group.

    return max_size

# The overall time complexity is O(n + nlogn + n + 5n) = O(nlogn)
