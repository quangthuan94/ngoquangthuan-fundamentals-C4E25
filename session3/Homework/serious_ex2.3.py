sheep_size = [10, 56, 4, 9, 100, 347, 25, 142, 347, 92]
print("Hello, my name is Thuan and these are my sheep size\n", sheep_size)
m = max(sheep_size)
print("Now biggest sheep has size", m, "let's shear it")
for (i,x) in enumerate(sheep_size):  # lay vi tri cua max number
    if x == m:
        sheep_size[i] = 8
print("After shearing, here is my flock\n", sheep_size)