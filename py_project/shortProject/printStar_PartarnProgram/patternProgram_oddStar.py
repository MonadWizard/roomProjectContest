inp = int(input("input number of row : "))
k = 1
for i in range(1, inp + 1):
    for j in range(1, k + 1):
        print("#", end=" ")
    k = k + 2
    print()  #new line

""" we arrange row and column wise so we need two loop one for row and another for column.
we also need another function name range .
"""
# range(0,11)         #it print 0 to 10    cause o is included and 11 is excluded
