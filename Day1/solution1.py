class CircularDial:
    def __init__(self):
        self.dial = 50 # starting value of dial
    
    def rotate(self, command):
        # command is of the format L/R + an integer
        direction = command[0]
        value = int(command[1:])

        if direction == "L":
            self.dial = (self.dial - value) % 100
        elif direction == "R":
            self.dial = (self.dial + value) % 100

lock = CircularDial()


file = "input.txt"
password = 0

with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        lock.rotate(line.strip())
    
        if lock.dial == 0:
            password += 1

print(password)
