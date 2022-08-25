def myfile():
    try:
        a=open("siva.txt","r")
        print(a.read())
    except(FileNotFoundError):
        return "file not exists"
k=myfile()
print(k)