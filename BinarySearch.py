def binary_search(arr, target):

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

if __name__ == "__main__":
    arr = [1, 5, 10, 20, 28, 3, 11]
    arr.sort()
    print(binary_search(arr, 5))
    print(binary_search(arr, 1))
    print(binary_search(arr, 28))
    print(binary_search(arr, 2))
