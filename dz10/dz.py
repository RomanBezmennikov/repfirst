x = 'Lore3m ipsum do28lor s2it 4 amet 12,consec639tetur 71 adipi56scing e7li34t'
y = x
z = ''
for i in y:
    if i.isdigit() == True:
        z += i
print(z)

for d in '1234567890':
    x = x.replace(d, '')
print(x)
