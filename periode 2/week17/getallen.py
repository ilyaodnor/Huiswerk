import random

A = random.randint(-1000, 1000)
B = random.randint(-1000, 1000)
C = random.randint(-1000, 1000)
D = random.randint(-1000, 1000)

lijst = [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D')]

lijst.sort()

print(f'getal {lijst[0][0]} ({lijst[0][1]}) is wat het is, '
      f'getal {lijst[1][0]} ({lijst[1][1]}) is groter, '
      f'getal {lijst[2][0]} ({lijst[2][1]}) is nog groter, '
      f'maar getal {lijst[3][0]} ({lijst[3][1]}) is het grootst!')