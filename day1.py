#practising the questions solving finding maximum 



arr=[12,13,15,1,19]
max=[]

def maxxer_(arr):
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]> max:
            max=arr[i]
    return max

print(maxxer_(arr))

# coded by ai and optimize code
arr = [12, 13, 15, 1, 19]

def find_max(arr):
    # start with the first element as max
    max_val = arr[0]
    for num in arr[1:]:   # loop directly from the 2nd element
        if num > max_val:
            max_val = num
    return max_val

print(find_max(arr))  # Output: 19

