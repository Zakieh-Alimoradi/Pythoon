t_anar=int(input())
t=input()


doone=[int(i) for i in t.split(" ")]
target=int(input())



x=0
y=0
for i in range(t_anar):
    y=doone[i]
    for j in range(t_anar):
        if i==j:
            break
        elif doone[j]+y==target:
                x+=1


print(x)