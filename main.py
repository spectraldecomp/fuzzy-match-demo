from rapidfuzz import process


# Dummy list of fake company name strings in 3
# distinct groups but with slight
# variations in spelling and punctuation
strings = [
    "Acme, Inc.",
    "Acme Inc",
    "Acme, Inc",
    "Acme Inc.",
    "Acme, Incorporated",
    "Acme Incorporated",
    "Acme, Incorporated.",
    "Acme Incorporated.",
    "Acme, Inc. & Co.",
    "Acme Inc & Co",
    "Acme, Inc & Co",
    "Acme Inc. & Co",
    "Acme, Incorporated & Co.",
    "Acme Incorporated & Co.",
    "Acme, Incorporated. & Co.",
    "Acme Incorporated. & Co.",
    "Acme, Inc. and Co.",
    "Acme Inc and Co",
    "Acme",
    "Acme, LLC",
    "AMCE",
    "ACMOSON",
    "fghn",
    "Fellow God Hello Now",
    "Fellow God Hello Now, Inc.",
    "Fellow God Hello Now Inc",
    "Fellow God Hello Now, Inc",
    "Fellow God Now Inc.",
    "FGHN INC",
    "Granted Now Inc",
    "Granted Now, Inc.",
    "Granted Now Inc.",
    "GNI INC",
    "GNI, Inc.",
    "GNI Inc.",
    "Granted Now Incorporated"
    ]

# We now wish to sort the list of strings into 3 groups based
# off of several provided keywords. We will use process.extract.

# First, we will create a list of keywords to search for

keywords = ["Acme", "Granted Now", "Fellow God Hello Now"]

# Next, we will create a list of lists to store the results

results = [[], [], []]

# Now, we will iterate through the list of keywords and use
# process.extract to find the best match for each keyword

# process.extract returns a list of tuples with 3 elements:
# 1. The best match for the keyword
# 2. The score of the best match
# 3. The index of the best match in the original list

for i in range(len(keywords)):
    results[i] = process.extract(keywords[i], strings, limit=len(strings))

#We will print the results

for i in range(len(keywords)):
    print("Keyword: " + keywords[i])
    print("Results: " + str(results[i]))
    print("")

# Clearly, the results are not perfect. We can see that there are slight errors on the borders. Still,
# only 1 or 2 companies are misclassified. We now have three lists with the correct matches for each keyword
# mostly at the front of the list. Let's make the lists a bit less verbose.

# We will create a new list to store the results

results2 = [[], [], []]

# We will iterate through the results and append the first element of each tuple to the new list

for i in range(len(keywords)):
    for j in range(len(results[i])):
        results2[i].append(results[i][j][0])

# We will print the results

for i in range(len(keywords)):
    print("Keyword: " + keywords[i])
    print("Results: " + str(results2[i]))
    print("")

# It is up to the user to determine the cutoff points for each list.

