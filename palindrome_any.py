# We open dna.fasta as 'file'. NOTE: dna.fasta is assumed to be in the same folder as this .py file.

file = open("dna.fasta")

# The second element in the list produced by file.readlines() will contain the DNA sequence.

dna_sequence = file.readlines()[1]

# We can close the file after reading it.

file.close()


def palindrome_2():

    """
    Returns the number of palindromic sites (of any length) in the DNA sequence given in dna.fasta

    INPUT(S)
        None

    OUTPUT(S)
        count - int

    """

    # We initialise the count of palindromic sites as zero.

    count = 0

    # We define a dictionary containing the complementary base pairs.

    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}

    # The shortest possible palindrome is 2 base pairs long (e.g., 5'-AT-3') and the longest possible palindrome
    # is the DNA sequence itself. Thus, we can find the total number of possible palindromes by iteratively increasing
    # the window length (denoted by 'L') from 2 to len(dna_sequence).

    for L in range(2, len(dna_sequence) + 1):

        # We "slide" a window of 'L' nucleotides from the 5' end to the 3' end of the sequence. The last window will
        # be dna_sequence[len(dna_sequence)-L : len(dna_sequence)]. Each window corresponds to a potential 'L'
        # base pair long palindromic site.

        for i in range(len(dna_sequence) - L + 1):

            # We define the potential palindromic site being tested as the current window's sequence.

            potential_palindrome = dna_sequence[i: i + L]

            # We find the reverse complement of the potential palindrome by finding its complementary strand using the
            # dictionary defined earlier and then reversing the output by string slicing.

            reverse_complement = "".join([complement[base] for base in potential_palindrome])[::-1]

            # If the potential palindrome and its reverse complement have the same sequence, it is a true palindromic
            # site. We can increment the count by 1.

            if potential_palindrome == reverse_complement:
                count += 1

    # We can return the final count of palindromic sites.

    return count


# We call palindrome_2() and print its result.

print(palindrome_2())
