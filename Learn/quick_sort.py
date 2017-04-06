def quick_sort(array):
	if len(array) <= 1:
		return array
	less = []
	greater = []
	pivot = array.pop()
	for x in array:
		if x < pivot:
			less.append(x)
		else:
			greater.append(x)
	return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
	result = quick_sort([5, 8, 4, 3, 7, 9])
	print(result)


