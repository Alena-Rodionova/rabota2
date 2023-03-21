import sys

i=0
g=0
p=0
f=0
for i in range(1,11):
    for g in range(1,11):
        t=str(i)+'+'+str(g)+'='
        s=i+g
        print (t,end='')
        r=int(input())
        if r!=s:
            p+=1
            print('Ответ не верный!')
        else:
            f+=1
            print('Ответ верный!')
        if p==3:
            print('Игра окончена:(')
            print('Количество правильных ответов: ',f)
            sys.exit()




