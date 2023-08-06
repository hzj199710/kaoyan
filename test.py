import sys



a = '0xAA'


dict_n = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


res = 0
for i in range(len(a)-1, 1, -1):
    temp = 0
    if a[i] in dict_n:
        temp = dict_n[a[i]]
    else: 
        temp = int(a[i])
    res = res *16 + temp
print(res)