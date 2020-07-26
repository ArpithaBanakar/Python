till_ninteen = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,3,6,6,5,5,5,7,6,6]
hundred = 7
thousand = 8
total = 0
for i in range(1,1000):
    u = i%10
    t = int(((i%100)-u) /10)
    h = int(((i%1000)-(t*10)-u) /100)
    print(h,t,u)

    if i < 20:                                                          
        total += to_19[i]
    elif h != 0 and (t != 0 or u != 0):                                 
        if t == 0 or t == 1:                                            
            total += to_19[h] + hundred + 3 + to_19[(t * 10) + u]
        else:                                                           
            total += to_19[h] + hundred + 3 + tens[t] + to_19[u]
    elif t == 0 and u == 0:                                            
        total += to_19[h] + hundred
    else:                                                              
        total +=  tens[t] + to_19[u]

print(total+thousand)
