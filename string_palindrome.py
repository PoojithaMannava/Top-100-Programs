s=input()
rev=""
for i in s:
    rev=i+rev
if(rev==s):
    print("It's A Palindrome")
else:
    print("It's Not A Palindrome")
