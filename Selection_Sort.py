arr = [200,30,62,3,55]
size = len(arr)

def selection_sort(arr, size):
    for ind in range(size):
        Min_index = ind

        for j in range (ind+1, size):
            if arr[j]<arr[Min_index] :
                Min_index = j

        (arr[ind],arr[Min_index]) = (arr[Min_index],arr[ind])

selection_sort(arr,size)
print(arr)