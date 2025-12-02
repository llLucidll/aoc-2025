# split each number into. If the length is not even then the ID is valid by default.

ranges = input("Enter the ranges: ").split(",")
result = 0
for r in ranges:
    left, right = r.split("-")
    # easy check to reduce program run time.
    if len(left) % 2 != 0 and len(right) % 2 != 0:
        continue
    left = int(left)
    right = int(right)

    for id in range(left, right + 1):
        string = str(id)
        # skip odd numbers
        if len(string) % 2 != 0:
            continue 
        l, r = string[0:(len(string)//2)], string[(len(string)//2): ]
        if l == r:
            result += id 

print(result)
