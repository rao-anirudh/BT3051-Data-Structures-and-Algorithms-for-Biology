def primer_design(seq="ATGGCAATCAAGTCATTGGAATCGTTCCTTTTCGAAAGAGGTCTAGTAGG"):

    """
    Returns a list of possible 20 nucleotide primers, that satisfy certain criteria related to GC content
    and melting temperature for a given gene sequence.

    INPUT(S)
        seq - str

    OUTPUT(S)
        primers - list

    """

    # We initialise a list of valid primers

    primers = []

    # We "slide" a window of 20 nucleotides from the 5' end to the 3' end of the sequence. The last window will
    # be seq[len(seq)-20 : len(seq)]. Each window corresponds to a potential 20 nucleotide long primer.

    for i in range(len(seq) - 20 + 1):

        # We define the potential primer being tested as the current window's sequence.

        potential_primer = seq[i:i+20]

        # We count the occurrences of G,C,A,T in the potential primer by initialising their counts as
        # zero and then iterating through every nucleotide in the potential primer.

        g = 0
        c = 0
        a = 0
        t = 0

        for nucleotide in potential_primer:
            if nucleotide == "G":
                g += 1
            elif nucleotide == "C":
                c += 1
            elif nucleotide == "A":
                a += 1
            elif nucleotide == "T":
                t += 1

        # We calculate the GC content as a ratio of the number of guanine and cytosine nucleotides to the total
        # number of nucleotides, i.e., 20.

        gc_content = (g + c) / 20

        # We calculate the melting temperature using the formula T_m = 4(G+C) + 2(A+T)

        t_m = (4 * (g + c)) + (2 * (a + t))

        # We check if the GC content is within the range [40%,60%] (both inclusive) and if the melting temperature
        # is in the range [52,56] (both inclusive).

        if 0.4 <= gc_content <= 0.6 and 52 <= t_m <= 56:

            # If the potential primer satisfies the required criteria, we append it to the list of possible primers.

            primers.append(potential_primer)

    # We can then return the list of possible primers.

    return primers


# We call primer_design() and print its output.

print(primer_design())
