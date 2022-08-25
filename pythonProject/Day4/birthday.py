dict={"siva":'13-08-2000',"rajesh":'20-06-2000',"sai ":'14-06-2001',"ganesh":'21-07-1999',"pawan":'28-05-2000'}
print(">>>welcome to birthdays dictionary.we know birthdays of :")
for name in dict:
    print(name)
print("who's birthday do want to know ?")
name= input()
if name in dict:
    print(name + 'has born on' +dict[name])
else:
    print("we don't have " + name + "born")