arr1 = [[1,2,3],
        [3,4,5],
        [5,6,8]]

arr2 = [[10,10,10],
        [10,10,10],
        [10,10,10]]



for i in range(0,len(arr1)):
    for j in range(0,len(arr1)):
        print(arr1[i][j]+arr2[i][j],",",end = "")
    print("\n")