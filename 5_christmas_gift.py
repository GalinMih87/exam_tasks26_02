command = input()
children = 0
adults = 0

while command != "Christmas":
    number = int(command)
    if number <= 16:
        children += 1
    if number > 16:
        adults += 1
    command = input()

total_children = children * 5
total_adults = adults * 15

print(f"Number of adults: {adults}")
print(f"Number of kids: {children}")
print(f"Money for toys: {total_children}")
print(f"Money for sweaters: {total_adults}")
