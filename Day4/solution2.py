from collections import deque

file = "input.txt"

with open(file) as f:
    lines = f.readlines()
    
    lines = [line.strip() for line in lines]

result = 0
ROW = len(lines)
COL = len(lines[0])
converted = set() # used to keep track of changed paper rolls
freq = [[0 for _ in range(COL)] for _ in range(ROW)] 

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
result = 0
queue = deque() 
# queue based peel approach 
for x in range(ROW):
    for y in range(COL):
        if lines[x][y] == "@":
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy 
            
                if 0 <= nx < ROW and 0 <= ny < COL and lines[nx][ny] == "@":
                    count += 1

            if count < 4:
                queue.append((x, y))
            else:
                freq[x][y] = count 

while queue:
    x, y = queue.popleft()
    # if we already processed this previously (duplicates can exist as multiple rolls can have same neighbour)
    if (x,y) in converted:
        continue
    converted.add((x,y))
    result += 1
    freq[x][y] = 0
    for dx, dy in directions:
        nx, ny = dx + x, dy + y
        if 0 <= nx < ROW and 0 <= ny < COL and lines[nx][ny] == "@":
            freq[nx][ny] -= 1
            if freq[nx][ny] < 4:
                queue.append((nx, ny))


print(result)