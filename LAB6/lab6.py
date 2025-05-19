# Daryl Nelson
# 1021215
# Python 3.13

def minCoinChange(denominations, amount):
    current_combination = []
    track_key = len(denominations) - 1 if len(denominations) > 1 else 0

    while sum(current_combination) < amount or sum(current_combination) > amount:

        if sum(current_combination) < amount:
            current_combination.append(denominations[track_key])
        if sum(current_combination) > amount:
            current_combination.pop()
            track_key -= 1
            try:
                current_combination.append(denominations[track_key])
            except IndexError as i:
                return -1

    return [current_combination, len(current_combination)]



all_coin_denominations = []

with open("coins.txt", 'r') as f:
    for line in f:
        for num in line.strip().split():
            try:
                denomination = int(num)
                all_coin_denominations.append(denomination)
            except ValueError as e:
                continue


amount = all_coin_denominations.pop()

result = minCoinChange(sorted(all_coin_denominations), amount)

if result == -1:
    print(f"Minimum	coins required: {result}")
else:
    combination, min_coins = result
    print(f"Minimum coins required = {min_coins} and Used coins = {combination}")
