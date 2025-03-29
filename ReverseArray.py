class ReverseArray:
    @staticmethod
    def reverse(array):
        left = 0
        right = len(array) -1
        while(left < right):
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left = left + 1
            right = right -1
        return array

output = ReverseArray.reverse([1,2,3,4,5,6,7,8,9,10])
print(output)