# lst = list(map(int,input("Enter list: ").split()))
# odd_list=[]
# even_list=[]
# for i in lst:
#     if i%2==0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# even_list.sort(reverse=True)
# odd_list.sort()
# res=even_list+odd_list
# print(res)

lst = list(map(int,input("Enter list: ").split()))
lst.sort()
lst1=[]
for i in lst:
    if i%2==0:
        lst1.insert(0,i)
    else:
        lst1.append(i)
print(lst1)