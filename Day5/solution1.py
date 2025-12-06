file = "input.txt"
ranges = [] 
ingredients = []    


with open(file) as f:
    while True:
        line = f.readline().strip()
        if line != "":
            start, end = line.split("-")
            ranges.append([int(start), int(end)])
        else:
            ingredients = f.readlines() 
            break 
    

ingredients = [int(ingredient.strip()) for ingredient in ingredients]
ranges.sort() # sort the ranges based on start value
merged = []  

for i in range(len(ranges)):
    if not merged:
        merged.append(ranges[i])
        continue 
    
    curr = ranges[i] 
    # we already sorted the ranges by starting point.
    if curr[0] <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], curr[1])
    else:
        merged.append(curr) 

# Before we merge let's count how many total ingredients are considered fresh 

possible_fresh = 0

for interval in merged:
    start, end = interval
    possible_fresh += end - start + 1 

print(possible_fresh)
# Now we perform binary search 

fresh = 0
for ingredient in ingredients:
    l, r = 0, len(merged) - 1

    while l <= r:
        mid = (l + r) // 2 
        if merged[mid][0] <= ingredient <= merged[mid][1]:
            fresh += 1
            break  
        elif ingredient > merged[mid][1]:
            l = mid + 1 
        else: 
            r = mid - 1 
print(fresh)
    

