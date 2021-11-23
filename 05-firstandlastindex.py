class Solution:
    def getRange(self,arr,target):
        first = self.binarySearch(arr,0,len(arr)-1,target,True)
        last  = self.binarySearch(arr,0,len(arr)-1,target,False)
        return [first, last]
    def binarySearch(self,arr,low,high,tar,First):
        if high<low:
            return -1
        mid = low + (high-low)//2
        if First:
            if (mid == 0 or tar > arr[mid - 1]) and arr[mid] == tar:
                return mid
            if arr[mid] < tar:
                return self.binarySearch(arr,mid+1,high,tar,True)
            else:
                return self.binarySearch(arr,low,mid-1,tar,True)
        else:
            if (mid == len(arr)-1 or tar < arr[mid+1]) and arr[mid] == tar:
                return mid
            elif arr[mid] > tar:
                return self.binarySearch(arr,low,mid-1,tar,False)
            else:
                return self.binarySearch(arr,mid+1,high,tar,False)
    def binarySearchIterative(self,arr, low,high,tar,First):
        while True:
            if high<low:
                return -1
            mid = low+ (high-low)//2
            print(mid)
            if First:
                if (mid == 0 or tar > arr[mid - 1])and arr[mid]== tar:
                    return mid
                elif arr[mid]<tar:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if (mid == len(arr)-1 or tar < arr[mid + 1])and arr[mid] == tar:
                    return mid
                elif arr[mid] > tar:
                    high = mid - 1
                else:
                    low = mid + 1
arr = [1, 2, 3, 3, 9, 9, 9,9,9, 15]
x = 3
print(Solution().getRange(arr,x))