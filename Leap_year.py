n=int(input())
if((n%100!=0 and n%4==0)or n%400==0):
    print("Leap year")
else:
    print("Not aLeap year") 
