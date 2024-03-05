#Find missing element in a sorted array
#T.C. O(logn)
#S.C. O(1)

#Approach: This approach uses binary search to find the missing element. It calculates the value of mid with index of mid. 
# It does the same thing with low and high. Here the logic is since it's a sorted array, the difference should be 1. 
#If the difference is above it that means there's a missing element.

arr = [1, 2, 3, 4, 6, 7, 8, 9]

low = 0
high = len(arr) - 1

def binsearch(arr, low, high):
    while (high - low) > 1:
        mid = (low + high)//2

        if arr[mid] - mid != arr[low] - low:
            high = mid 
        elif arr[mid] - mid != arr[high] - high:
            low = mid
            
    return arr[low] + 1

print(binsearch(arr, low, high))
        

    
        
