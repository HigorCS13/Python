name = 'Higor'
tam = len(name)
x = 0
new_name =''

while x < tam:
	new = (f'*{name[x]}')
	new_name += new
	x += 1
new_name += '*'
print(new_name)