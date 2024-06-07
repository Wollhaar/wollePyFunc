# looping in one line iteration
nums = [x for x in range(1,51)]

# loop through list
tags = ["travel", "vacation", "journey"]

hashtags = ["#" + x for x in tags]
print(hashtags)


# loop through list with if condition
users = ["Brandon", "Emma", "Brian",
"Sophia", "Bella", "Ethan",
"Ava", "Benjamin", "Mia", "Chloe"]

group = [x for x in users if x[0] == "B"]

print(group)

# check on string length in iteration
words = ["tree", "button", "cat", "window", "defenestrate"]

# Use a list comprehension to filter out words longer than four letters
vocable_list = [x for x in words if len(x) > 4]

# Display the filtered list
print(vocable_list)
