import math 

def read_input(filename):
    """
    Reads the input file and returns a list of strings (rows).
    Preserves trailing spaces and pads all rows to the maximum length.
    """
    with open(filename, 'r') as f:
        lines = [line.strip('\n') for line in f]

    if not lines:
        return []

    max_len = max(len(line) for line in lines)
    # Pad lines to ensure rectangular grid
    padded_lines = [line.ljust(max_len) for line in lines]
    return padded_lines

def parse_columns(rows):
    """
    Transposes the list of rows into a list of columns.
    """
    if not rows:
        return []
    
    num_cols = len(rows[0])
    columns = []
    for c in range(num_cols):
        col_chars = [row[c] for row in rows]
        columns.append("".join(col_chars))
    
    return columns

def get_blocks(columns):
    """
    Splits the list of columns into blocks separated by empty columns.
    An empty column is one that consists entirely of spaces.
    """
    blocks = []
    current_block = []
    
    
    for col in reversed(columns):
        if col.strip() == "":
            if current_block:
                blocks.append(current_block)
                current_block = []
        else:
            current_block.append(col)
            
    if current_block:
        blocks.append(current_block)
        
    return blocks

def solve_block(block_columns):
    """
                       
    Returns:
        int: The result of the calculation.
    """
    
    numbers = []
    operator = None

    for col in block_columns:
        # Find operator if present
        if col[-1] in "+*":
            operator = col[-1]
            col = col[:-1] 
        # Extract digits
        digits = col.split()
        for digit in digits:
            numbers.append(int(digit))
        
        if operator == "+":
            return sum(numbers)
        elif operator == "*":
            return math.prod(numbers)
        
def main():
    input_file = "input.txt"
    rows = read_input(input_file)
    columns = parse_columns(rows)
    blocks = get_blocks(columns)
    
    total = 0
    for i, block in enumerate(blocks):
        result = solve_block(block)
        total += result
        
    print(total)

if __name__ == "__main__":
    main()
