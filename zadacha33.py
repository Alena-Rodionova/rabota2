import sys

a=list(input())
print(a)
t=len(a)
for i in a:
    if i=="ф":
        print("Это слово редкое!")
        sys.exit()
    else:
        t=t-1
if t==0:
    print("Это слово не редкое:(")