Peo_Time=list(map(int,input().split()))
closing_time=Peo_Time[1]
people=Peo_Time[0]
list2=[]
list1=[]
for i in range(people):
    cash_Time=list(map(int,input().split()))
    list2.append(cash_Time[0])
    list1.append(cash_Time[1])
selected_amount=[]
selected_time=[]
amount=[]
k=0
cheker=0
count=0
j=0
st=0
if(closing_time<people):
    ranger=people
else:
    ranger=closing_time
for z in range(ranger):
    amount.append(0)
for i in range(len(list2)):
    s=max(list2)
    index1=list2.index(s)
    k=list1[index1]
    selected_amount.append(s)
    selected_time.append(k)
    list2.remove(s)
    list1.pop(index1)
while(j<=len(selected_amount)-1):
    index2=selected_time.index(selected_time[j])
    val2=selected_amount[index2]
    value1=selected_time[index2]
    if(amount[value1]==0):
        amount[value1]=val2
    else:
        for k in range(value1,-1,-1):
            value1=value1-1
            if(value1>=0 and amount[value1]==0):
                amount[value1]=val2
                break
    selected_time[index2]='a'
    selected_amount[index2 ]='b'
    j=j+1
for c in amount:
    st=st+c
print(st)   
