#removing duplaicate number after sorting numbers
# arr_y=[1,2,3,3,0,6,7,2]
# temp=0

# for i in range(0,len(arr_y)-1):
#     for j in range(i,len(arr_y)):
#         if arr_y[i]<arr_y[j]:
#             temp=arr_y[i]
#             arr_y[j]=arr_y[i]
# print(arr_y)
arr_y = [1, 2, 3, 3, 0, 6, 7, 2]

# Step 1: Sort array
for i in range(len(arr_y)):
    for j in range(i+1, len(arr_y)):
        if arr_y[i] > arr_y[j]:
            arr_y[i], arr_y[j] = arr_y[j], arr_y[i]

# Step 2: Remove duplicates
unique_arr = []
for num in arr_y:
    if num not in unique_arr:
        unique_arr.append(num)

print(unique_arr)   # Output: [0, 1, 2, 3, 6, 7]
