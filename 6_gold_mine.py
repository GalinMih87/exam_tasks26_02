location = int(input())
sreden_dobiv = 0

for i in range(location):
    ochakvan_dobiv_na_den = float(input())
    days = int(input())
    for n in range(days):
        dobiv_na_den = int(input())
        sreden_dobiv += dobiv_na_den
        sredno = sreden_dobiv / days
        if location > 1:
            sreden_dobiv += dobiv_na_den
            sredno = (sreden_dobiv / days) / location
if sredno >= ochakvan_dobiv_na_den:
    diff = abs(sredno - ochakvan_dobiv_na_den)
    print(f"Good job! Average gold per day: {sredno:.2f}.")
    print(f"You need {diff:.2f} gold.")
else:
    diff = abs(sredno - ochakvan_dobiv_na_den)
    sredno = sreden_dobiv / days
    print(f"You need {diff:.2f} gold.")



