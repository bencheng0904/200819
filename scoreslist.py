scores = []
name = []
up = 0
low = 100
a = 0
for i in range(5):
    
    n = int(input('成績：'))
    
    scores.append(n)
    a = a + n
    if n > up:
        up = n
    if n < low:
        low = n
        
print()                  
print('最高分',up)
print('最低分',low)       
print('總分',a)         
print('平均',a/5) 
