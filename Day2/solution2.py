# in part 2, if the ID is made up of a repetition of some subpart of itself, it is invalid
def solve(ranges):
    result = 0
    for r in ranges:
        left, right = r.split("-")
        left, right = int(left), int(right)
        for id in range(left, right + 1):
            string = str(id)
            for length in range(1, len(string) // 2 + 1):
                if len(string) % length != 0:
                    continue 
                current = string[0:length]
                if subarray_check(string, current):
                    result += id 
                    break # exit out of this loop since we already found it to be invalid
    return result 

def subarray_check(string, subarray):
    for i in range(len(subarray), len(string), len(subarray)):
        if string[i:i + len(subarray)] == subarray:
            continue 
        else:
            return False 
    return True 
        




def main():
    ranges = input("Enter the ranges: ").split(",")
    print(solve(ranges))


if __name__ == "__main__":
    main()