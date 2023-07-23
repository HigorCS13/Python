frase = input ('Entre uma frase: ')

i = 0
most_show = ''
num_show = 0

while i < len(frase):
	l_now = frase[i]
	l_count = frase.count(l_now)

	if l_now == ' ':
		i += 1
		continue

	num_show_now = l_count

	if num_show < num_show_now:
		num_show = num_show_now
		most_show = l_now

	i += 1
print(f'A letra que mais apareceu foi "{most_show}", por {num_show} vezes.')