def merge_list(arr1:list, arr2:list):
    try:
        new_arr = arr1 + arr2
        for i in range(0, len(new_arr)):
            min = i

            for j in range(i + 1, len(new_arr)):
                if new_arr[j] < new_arr[min]:
                    min = j

            temp = new_arr[i]
            new_arr[i] = new_arr[min]
            new_arr[min] = temp
        return new_arr
    
    except:
        print("Error! Please input 2 lists of integers")

# print(merge_list([1,4,3], [6,3,7]))