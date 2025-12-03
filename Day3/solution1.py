file = "input.txt"
with open(file) as f:
    banks = f.readlines()

result = 0
for bank in banks:
    bank = bank.strip()
    first = int(bank[0])
    first_index = 0
    # Find the highest first value 
    for i in range(1, len(bank) - 1):
        char = bank[i]

        if int(char) > first:
            first = int(char)
            first_index = i
    
    second = -1
    # Find the highest second value 
    for j in range(first_index + 1, len(bank)):
        char = bank[j] 

        if int(char) > second:
            second = int(char)
    
    value = first * 10 + second 
    result += value 

print(result)
