'''s=eval(input('enter a name:'))
print(s,type(s))
s=int(input("enter a number:"))
if s%2==0:
    print("Even")
else:
    print("Odd")'''


'''ch=input('enter ch:')
if 'A'<=ch<='Z':
    print(True)
else:
    print(False)'''


'''ch=input('enter ch:')
if 'A'<=ch<='B' and 'b'<=ch<='Z':
    print(True)
else:
    print(False)'''


'''num=int(input('enter:'))
if 10<=num<=99:
    print('two digit')
else:
    print('false')'''


'''a=int(input('enter a:')) 
b=int(input('enter b:'))
if a>b:
    print(f'{a} is greater')
else:
    print(f'{b} is greater')'''

'''ch=input('enter ch:')
if 'A'<=ch<='Z':
    print('upper case')
elif 'a'<=ch<='z':
    print('lower case')
elif '0'<=ch<='9':
    print('digit')
else:
    print('special character')'''

'''ch=input('enter ch:')
if ch.isalpha():
    if ch in 'aeiouAEIOU':
        print('it is a vowel')
    else:
        print('it is a consonant')
else:
    print('it is not an alphabet')'''

'''l=eval(input('enter:'))
if type(l)==list:
    if len(l)%2==0:
        print('even')
    elif len(l)%2!=0:
        print('odd')
else:
    print('not a list')'''


'''i=1
while i<=5:
    print(i)
    i+=1
    print('hello')'''


'''l=eval(input('enter:'))
i=0
while i<len(l):
    print(l[i])
    i+=1'''

'''for i in range(1,10):
    print(i)'''


'''a=input('enter:')
out=''
for i in a:
    if 'A'<=i<'Z':
        out=out+chr(ord(i)+32)
    else:
        out+=i
print(out)'''


'''s=[12,10,'hello','good',5j,'byee']
out={}
for i in s:
    if type(i)==str:
        out[i]=i[0]+i[-1]
print(out)'''


'''for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')
    print()'''




        