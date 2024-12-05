# We import the re module.

import re

# We open the words.txt file and create a list of words.

f = open("words.txt")
content = f.read()
f.close()
word_list = content.split()

# a.

# We have to find the number of words that start with a vowel and ends with a consonant.
# ^[aeiou] ensures that the word starts with a vowel and [^aeiou]$ ensures that the word ends with a consonant.
# \w* denotes that any letters can occur in between.

r = re.compile("^[aeiou]\w*[^aeiou]$")
print(f"The number of words that start with a vowel and ends with a consonant is {len(list(filter(r.search, word_list)))}.")

# b.

# We have to find the number of words that contain at least 3 a’s.
# a\w*a\w*a ensures that there are at least 3 a's in the word. \w* allows any letters to occur in between them.

r = re.compile("a\w*a\w*a")
print(f"The number of words that contain at least 3 a’s is {len(list(filter(r.search, word_list)))}.")

# c.

# We have to find the number of words that have repeated alphabets consecutively.
# (\w) captures an alphabet and \\1 ensures that the same alphabet occurs consecutively.

r = re.compile("(\w)\\1")
print(f"The number of words that have repeated alphabets consecutively is {len(list(filter(r.search, word_list)))}.")

# d.

# We have to find the number of words that start and end with the same vowel.
# ^([aeiou]) ensures that the word starts with a vowel and also captures it.
# \\1$ ensures that the word ends with the same vowel.
# \w* allows any letters to be present in between.

r = re.compile("^([aeiou])\w*\\1$")
print(f"The number of words that start and end with the same vowel is {len(list(filter(r.search, word_list)))}.")
