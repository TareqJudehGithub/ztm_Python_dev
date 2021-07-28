def hello_world():
    print('Hello, world!')


hello_world()

print('\n')
n = 2
x = 1
y = 1
z = 1

print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if sum([a, b, c]) != n])