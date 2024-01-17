import random

sky = [] # create empty list sky
rows, cols = 10, 20 #define the number or rows and columns

for _ in range(rows):
    row = []
    for _ in range(cols):
        row.append('*' if random.random() < 0.1 else ' ') #probability=10%, random() generates numbers=[0,1)
    sky.append(row)

for row in sky:
    print("".join(row))