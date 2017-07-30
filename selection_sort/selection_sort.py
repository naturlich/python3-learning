'''

selection sort

'''

def selection_sort(nums):
	for i in range(len(nums), 0, -1):
		max_val_idx = 0
		for j in range(0, i, 1):
			if nums[j] > nums[max_val_idx]:
				max_val_idx = j
		tmp = nums[i -1]
		nums[i - 1] = nums[max_val_idx]
		nums[max_val_idx] = tmp

numbers = [2, 3, 1, 6, 2, 1, 1, 2, 5]

print(numbers)
selection_sort(numbers)
print(numbers)
