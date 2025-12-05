# we need to check the four cardinal directions to see if there's less than 4 rolls of paper

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)] 


file = "input.txt"
with open(file) as f:
    lines = [line.strip() for line in f.readlines()]

ROW = len(lines)
COL = len(lines[0])
result = 0
for x in range(ROW):
    for y in range(COL):
        # Only count paper rolls (@), not empty spaces
        if lines[x][y] != "@":
            continue
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy 
            if 0 <= nx < ROW and 0 <= ny < COL and lines[nx][ny] == "@":
                count += 1
        # Accessible if fewer than 4 adjacent rolls
        if count < 4:
            result += 1

print(result) 
