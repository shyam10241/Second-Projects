
def linear_search(arr,search):
    print(arr)
    l=len(arr)
    x=True
    for i in range(l):
        if arr[i]==search:
            x=False
            p=i+1
            print("Position is :",p)
    if x:
        print("element not found")
arr=[23,54,87,12,65,90,34,78]
search=90
linear_search(arr,search)
