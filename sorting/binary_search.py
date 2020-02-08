def binary_search(numbers, value):
    low = numbers[0]
    high = numbers[-1]
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] < value:
            low = mid + 1
        elif numbers[mid] > value:
            high = mid - 1
        else:
            return mid
    return 'Not found'


def binary_search_recursive(numbers, value, low, high):
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] < value:
            low = mid + 1
            return (binary_search_recursive(numbers, value, low, high))
        elif numbers[mid] > value:
            high = mid - 1
            return (binary_search_recursive(numbers, value,low, high))
        else:
            return mid
    return 'Not found'


numbers = [1,2,3,4,5,6,7,8,9]
value = 4
print(binary_search(numbers, value))
print(binary_search_recursive(numbers, value, 0, 8))
