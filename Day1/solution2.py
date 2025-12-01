class CircularDial:
    def __init__(self):
        self.dial = 50 # starting value of dial
    
    def rotate(self, direction, value):
        count = 0
        if direction == "R":
            # Count how many times we cross a multiple of 100
            # Range is (dial, dial + value]
            # Multiples of 100 in (dial, dial + value] is floor((dial+value)/100) - floor(dial/100)
            # Since dial is always 0-99, floor(dial/100) is 0.
            count = (self.dial + value) // 100
            self.dial = (self.dial + value) % 100
        elif direction == "L":
            # Count how many times we cross a multiple of 100 going down
            # Range is [dial - value, dial)
            # We want to count multiples of 100 (0, -100, etc) in [dial - value, dial)
            # This is floor((dial - 1)/100) - floor((dial - value - 1)/100)
            count = (self.dial - 1) // 100 - (self.dial - value - 1) // 100
            self.dial = (self.dial - value) % 100
        return count

lock = CircularDial()
password = 0

# Changed to input1.txt as that seems to be the available input file
for line in open("input.txt"):
    command = line.strip()
    direction = command[0]
    value = int(command[1:])
    
    password += lock.rotate(direction, value)

print(password)