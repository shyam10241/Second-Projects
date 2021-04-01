
def insertion_sort(arr):
    print("insertion sort :",arr)
    l=len(arr)
    for i in range(l-1):
        for j in range(i+1,0,-1):
            if arr[j]<arr[i]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
            i=i-1
            return arr
insert=[66,99,4,98,12]
var=insertion_sort(insert)
print(var)
