print('program to print indices of all occurence of a given element in a given list\n please Enetr a list')
l=eval(input())
e=eval(input('enter a element'))
i=0
#this is list to get element value
print(e,"is at index :-",end=' ')
for x in l:
    
    if x==e:
        print(l.index(x,i),end=' ')
        i+=1
        continue
    i+=1
input()
