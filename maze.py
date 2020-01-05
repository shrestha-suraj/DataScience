from __future__ import division

start=0
end=33554431

file =open("test.txt","w")
for index in range(start,end):
    temp=list(bin(index))
    temp[1]='0'
    temp="".join(temp)
    zeros=""
    for i in range (0,25-len(temp)):
        zeros=zeros+str(0)
    print zeros+temp
    file.write(zeros+temp+"\n")
file.close()
    
 