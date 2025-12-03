# We use a monotonic stack to keep track of this

file = "input.txt"


with open(file) as f:
    banks = f.readlines()

result = 0
stack = []
for bank in banks:
    bank = bank.strip()
    # we need to use the monotonic stack to find the maximum number of inputs.
    for i in range(len(bank)):
        remaining = len(bank) - i - 1  
        current = bank[i]
        # if the current value is greater than the last value in the stack
        # and we have enough values to get to 12 values in the stack
        if current > stack[-1] and remaining >= (12 - len(stack) - 1):
            stack.pop()
            stack.append(current)
        # if we cannot afford to replace the current stack top and must keep appending.
        else:
            stack.append(current)

    value = 0
    for val in range(0, len(stack)):
        value += stack[val] * 10**(len(stack) - val)
    
    result += value 

print(result)