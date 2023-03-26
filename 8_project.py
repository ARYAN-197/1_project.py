N=int(input())
leaves=int(input())
leaf=[]
for z in range(1,leaves+1):
    leaf.append(z)
st=input()
frog_st=st.split(" ")
if N!=len(frog_st):
    print("No. of frogs do not match with no. of strengths mentioned")
else:
    lst=[]
    j=1
    for i in range(0,len(frog_st)):
        frog_st[i]=int(frog_st[i])
        j=1
        for k in range(frog_st[i],leaves+1,frog_st[i]):
            l=frog_st[i]+(j-1)*frog_st[i]
            lst.append(l)
            j+=1
    for l in range(0,leaves):
        if leaf[l] not in lst:
            print(leaf[l])
            break
        else:
            print(0)