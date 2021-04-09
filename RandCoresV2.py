import random

class RandCores:
    
    def __init__(self):
        self.rgb = []
        self.cores = []
        
c = RandCores()

for i in range(6):
    c.cores.append(random.randint(1,15))
    cores = c.cores[i]
    if cores == 10 or cores == 11 or cores == 12 or cores == 13 or cores == 14 or cores == 15:
        c.cores[i] = ''.join(hex(c.cores[i]).split('0x'))

hex = '#'
c.rgb.append(hex)
c.rgb.append(''.join(map(str, c.cores)))
print(''.join(c.rgb),)