












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
print(all_coin_denominations)
print(amount)