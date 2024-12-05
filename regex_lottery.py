# We import the re module.

import re

# We open and read the Data.txt file.

f = open("Data.txt")
content = f.readlines()
f.close()

# For each line in the file, we remove any numbering and indentations.

new_content = []

for line in content:

    line = re.sub("\d\\.", "", line)   # This removes any numbering like 1., 2., etc.

    # If the line is not entirely made of whitespace, we remove the indentation.

    if len(re.sub("^\s*", "", line)) != 0:
        line = re.sub("^\s*", "", line)

    # We update the content.

    new_content.append(line)

# We write the modified content to a new .txt file.

with open('modified_Data.txt', 'w') as f:
    f.write("".join(new_content))
f.close()

# We go through the content and check who has a valid address that satisfies the criteria.
# We keep track of the current person being checked and remember the valid addresses.

current_name = ""
valid_addresses = {}
for line in new_content:

    # We update the name of the current person being checked if the line contains "Name:".

    if re.search("Name:", line) != None:
        current_name = re.search("Name: (.*)", line).groups()[0]

    # We then check their address.

    elif re.search("Address:", line) != None:
        address = re.search("Address: (.*)", line).groups()[0]

        # If the address does not have any vowels or has more than 3 vowels, it is valid.
        # ^[^aeiou]*$ ensures that the address does not contain any vowels.
        # ([aeiou].*){4,} ensures that the address has at least 4 vowels.
        # If the address is valid, we make a note of it.

        if re.search("^[^aeiou]*$", address, flags=re.IGNORECASE) != None or re.search("([aeiou].*){4,}", address, flags=re.IGNORECASE) != None:
            valid_addresses[current_name] = address

# We then check the email addresses.
# We keep track of the current person being checked and remember the names and addresses of eligible winners.

current_name = ""
winners = {}
for line in new_content:

    # We update the name of the current person being checked if the line contains "Name:".

    if re.search("Name:", line) != None:
        current_name = re.search("Name: (.*)", line).groups()[0]

    # We then check their email address only if they have a valid address.

    elif re.search("Email:", line) != None and current_name in list(valid_addresses.keys()):
        current_email = re.search("Email: (.*)", line).groups()[0]

        # If the email address contains "gmail", it is invalid. Else, it is valid.

        if re.search("gmail", current_email) == None:

            # If the email is valid, we note the address of the eligible winner.

            winners[current_name] = valid_addresses[current_name]


# We print the eligible winners and their addresses.
print("The eligible winners and their addresses are:")
for person, address in winners.items():
    print(f"{person} - {address}")
