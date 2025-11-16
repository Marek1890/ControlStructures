###
# Sums numbers entered by user
#
total_sum=0
count=0
while True:
    n=int(input("Enter a number (0 to stop): "))
    if n==0:
        break
    total_sum+=n
    count+=1
if count>0:
    print("Sum:",total_sum,"Mean:",total_sum/count)
else:
    print("No numbers entered")