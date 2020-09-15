f = open("demofile3.txt", "w")
x=8801832529775
for i in range(47):
    f.write(str(x)+"\n")
    x+=1

f.close()
