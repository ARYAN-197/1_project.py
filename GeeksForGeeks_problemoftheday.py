# takes N as total no. of frogs
N=int(input())
# takes the input for no. of leaves
leaves=int(input())
leaf=[]
# arranges all no. till leaves in a list to compare it with strength of frogs
for z in range(1,leaves+1):
    leaf.append(z)
# takes the strength of frogs as input and later converts it into list and later to integer as its component
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
        # with help of AP it forms a list(lst) with all specific leaves on which the frogs will step
        for k in range(frog_st[i],leaves+1,frog_st[i]):
            l=frog_st[i]+(j-1)*frog_st[i]
            lst.append(l)
            j+=1
    # compares lst and leaf and finds the difference and print difference as output
    for l in range(0,leaves):
        if leaf[l] not in lst:
            print(leaf[l])
            break
        # in case if frog steps on all leaves, It will give 0 as output
        else:
            print(0)
