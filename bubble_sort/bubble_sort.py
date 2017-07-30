'''

bubble sort

'''

def bubble_sort(nums):
	for i in range(len(nums) - 1, 0, -1):
		for j in range(0, i, 1):
			if (nums[j] > nums[j + 1]):
				tmp = nums[j + 1];
				nums[j + 1] = nums[j]
				nums[j] = tmp


numbers = [2, 3, 1, 6, 2, 1, 1, 2, 5]

print(numbers)
bubble_sort(numbers)
print(numbers)
