def search(list1,key):
    for i in range(len(list1)):
        if key==list1[i]:
            print("key found at index: ",i)
            break
        else:
            print("not found")
list1=[2,4,5,6,1,7,8,9,11]
key=int(input("enter key: "))
search(list1,key)