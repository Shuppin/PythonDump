PRISONERS = 10
WARDENS = PRISONERS
counter = 1
cells = []

# 1 = Unlocked
# 2 = Locked

for i in range(0,PRISONERS):
    cells.append(1)

#for x in range(1, WARDENS+1):
#    for i, cell in enumerate(cells):
#        print(cell)
#        if i % x:
#            cells[i] = 2
#           print(cells[i])

x = 1
print(cells)
for i, cell in enumerate(cells):
        if x % (i + 1):
            cells[i-1] = 2

print(cells)
