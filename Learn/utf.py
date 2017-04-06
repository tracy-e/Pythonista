try:
	with open('file.txt', 'r') as f:
		print(f.read())
except Exception as e:
	print('read file error: ', e)

print('\n')

with open('file.txt', 'r', encoding='utf-8') as f:
	content = f.read()
	print(content)
