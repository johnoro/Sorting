def insertion_sort(arr):
  for i in range(1, len(arr)):
    temp = arr[i]
    j = i
    while j > 0 and temp < arr[j-1]:
      arr[j] = arr[j-1]
      j -= 1
    arr[j] = temp
  return arr


print(insertion_sort([1, 3, 6, 2, 13, 41, 7]))

# TO-DO: Complete the selection_sort() function below 
def selection_sort(l):
	list_length = len(l)
	# loop through n-1 elements
	for i in range(0, list_length-1):
		cur_index = i
		smallest_index = cur_index
		# TO-DO: find next smallest element
		# (hint, can do in 3 loc); what's loc?
		while cur_index < list_length:
			if l[cur_index] < l[smallest_index]:
				# TO-DO: swap
				l[smallest_index], l[cur_index] = l[cur_index], l[smallest_index]
			cur_index += 1
	return l


print(insertion_sort([1, 3, 6, 2, 13, 41, 7]))

# TO-DO: implement the Bubble Sort function below
def bubble_sort(arr):
	swapped = False
	for i in range(0, len(arr) - 1):
		if arr[i+1] < arr[i]:
			arr[i], arr[i+1] = arr[i+1], arr[i]
			swapped = True
	if swapped:
		return bubble_sort(arr)
	return arr


print(bubble_sort([1, 3, 6, 2, 13, 41, 7]))

# STRETCH: implement the Count Sort function below
def count_sort(arr):
	if arr is None or len(arr) == 0:
		return []
	if min(arr) < 0:
		return "Error, negative numbers not allowed in Count Sort"
	
	counts = []
	sorted_nums = []
	for n in range(0, max(arr)+1):
		counts.append(0)
		sorted_nums.append(0)
	for n in arr:
		counts[n] += 1
	for i in range(1, len(counts)):
		counts[i] += counts[i-1]
	
	for i in range(len(arr)):
		sorted_nums[counts[arr[i]] - 1] = arr[i]
		counts[arr[i]] -= 1

	for i in range(len(arr)):
		arr[i] = sorted_nums[i]
	return arr

print(count_sort([1, 3, 6, 2, 13, 41, 7]))
