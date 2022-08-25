def common_member(a,b):
    a_set=set(a)
    b_set=set(b)
    if(a_set & b_set):
        print(a_set & b_set)
    else:
        print("No same elements")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_member(a,b)
list2=[8,6,4,3,1,2]
even_nos=[num for num in list2 if num%2==0]
print("Even numbers :",even_nos)