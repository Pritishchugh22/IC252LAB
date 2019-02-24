def fn(i):
    x , y = i
    return y

f=open('/home/tushar/IC252LAB/ic252_lab1_data/movieLists/list1.txt','r')
movies = f.readlines()
I = [(int(i[3:5]), int(i[8:10])) for i in movies]
I.sort(key = fn)
res = [I[0]]

for j in range(1,len(I)):        
    start, end =I[j]
    if (res[-1][1]<= start):
        res.append(I[j])
print(res)       
        
f.close()