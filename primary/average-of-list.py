numbers = [10, 20, 30]
def get_sum(nums):
    total = 0
    for n in nums:
        total += n
        return total
sum_of_numbers = get_sum(numbers)
print("Sum is:",sum_of_numbers)

def get_average(nums):
    total = 0
    for n in nums:
        total +=n
    return total/len(nums)
average = get_average(numbers)
print("Average is:", average)