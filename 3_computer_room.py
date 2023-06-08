month = input()
count_hours = int(input())
count_people = int(input())
day_or_night = input()
price = 0
price_for_one_hour = 0

if month == "march" or month == "april" or month == "may":
    if day_or_night == "day":
        price_for_one_hour = 10.50
        price = count_hours * 10.50 * count_people
    elif day_or_night == "night":
        price_for_one_hour = 8.40
        price = count_hours * 8.40 * count_people

if month == "june" or month == "july" or month == "august":
    if day_or_night == "day":
        price_for_one_hour = 12.60
        price = count_hours * 12.60 * count_people
    elif day_or_night == "night":
        price_for_one_hour = 10.20
        price = count_hours * 10.20 * count_people

if count_people >= 4:
    price -= price * 0.10
    price_for_one_hour -= price_for_one_hour * 0.10

if count_hours >= 5:
    price -= price * 0.50
    price_for_one_hour -= price_for_one_hour * 0.50

print(f"Price per person for one hour: {price_for_one_hour:.2f}")
print(f"Total cost of the visit: {price:.2f}")

