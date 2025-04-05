def liner_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

if __name__ == "__main__":
    arr = [1, 5, 10, 20, 28, 3, 11]
    arr.sort()
    print(liner_search(arr, 5))
    print(liner_search(arr, 1))
    print(liner_search(arr, 28))
    print(liner_search(arr, 2))