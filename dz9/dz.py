x = [45, 48, 51, 60, 64, 68, 75, 80, 85, 90, 96, 102, 105, 112, 119, 120, 128, 136, 135, 144, 153]
y = [26, 28, 30, 32, 52, 56, 60, 64, 78, 84, 90, 96, 104, 112, 120, 128]
x1 = set(x)
y1 = set(y)
z = list(x1 - y1)
print(z)
