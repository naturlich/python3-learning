'''

insertion sort

'''

def insertion_sort(nums):
	for i in range(0, len(nums), 1):
		val = nums[i]
		for j in range(i, 0, -1):
			if val < nums[j -1]:
				tmp = nums[j -1]
				nums[j -1] = val
				nums[j] = tmp

numbers = [2, 3, 1, 6, 2, 1, 1, 2, 5]
#numbers = [2, 3, 1]
print(numbers)
insertion_sort(numbers)
print(numbers)
