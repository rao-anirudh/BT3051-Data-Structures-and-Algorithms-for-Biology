def match_time_format(string):

    """
    Prints the whether or not a given input string is a valid HH:MM time format. (HH can range from 00 to 23,
    MM can range from 00 to 59).

    INPUT(s)
        string - str

    OUTPUT(s)
        None

    """

    # We import the re module.

    import re

    # We check if the input is a valid time format using regular expressions.
    # ^([01]\d|2[0123]) allows HH to start with 0 or 1 followed by any integer OR 2 followed by 0,1,2,3.
    # : denotes the separating colon.
    # [012345]\d$ allows MM to start with 0,1,2,3,4,5 followed by any integer.

    # We print appropriate statements if the input is a valid time format or not.

    if re.search("^([01]\d|2[0123]):[012345]\d$",string) != None:
        print(f"{string} is a VALID time in HH:MM format.")
    else:
        print(f"{string} is an INVALID time in HH:MM format.")
