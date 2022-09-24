import csv
# Mean
with open("BLAH.csv") as f:
  reader=csv.reader(f)
  lis=list(reader)
lis.pop(0)

sum=0
height=[]

for i in range(len(lis)):
    height.append(lis[i][1])

height.sort()



if(len(height)%2==0):
    print(len(height)/2)
    med1=float(height[len(height)//2])
    med2=float(height[len(height)//2+1])
    avg=(med1+med2)/2
    print("Median is "+str(avg))
else:
    med=float(height[len(height)//2+1])
    print("Median is "+str(med))