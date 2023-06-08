from math import floor

count_processors = int(input())
count_workers = int(input())
working_days = int(input())

total_hours = count_workers * working_days * 8
total_proc = floor(total_hours / 3)


diff = abs(total_proc - count_processors) * 110.10

if count_processors > total_proc:
    print(f"Losses: -> {diff:.2f} BGN")
else:
    print(f"Profit: -> {diff:.2f} BGN")
