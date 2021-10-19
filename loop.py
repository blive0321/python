# ============ foor loop ============
# for in number
sequence = [0, 1, 2, 3, 4, 5]
for i in sequence:
    print (i)

# New line
print()

# for in string
lakers = ["James", "Brook", "Anthony", "Davis", "Howard"]
print ("We have %d players" %len(lakers))
for n in lakers:
    print ("Player :",n)
    print (len(n))

# difference between continue and break
for i in "Hey Jude":
    if i == "u":
        break
    print (i)
# output:
# H
# e
# y

# J

for i in "Hey Jude":
    if i == "u":
        continue
    print (i)
# output:
# H
# e
# y

# J
# d
# e

# ============ while loop ============
i = 1
while i <= 10:
    print (i, end=" ")
    i += 1
# output:
# 1 2 3 4 5 6 7 8 9 10
