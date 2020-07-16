fib_list = [1,1]
sayac = 0
for i in range(8):
    sayac = fib_list[i] + fib_list[i + 1]
    
    fib_list.append(sayac)
 
        
print(fib_list)