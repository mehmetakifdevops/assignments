
prim_list = []
for i in range(1,101):
    count = 0
    for k in range(1, i+1):
        if i % k == 0:
            count += 1
            
    if count == 2:
        prim_list.append(i)
       
print(prim_list)