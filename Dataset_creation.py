import random
import math
vE = 5
i = 0
while(i<600):
    v0 = random.uniform(1,6.495)
    w = 0
    P_ped = random.randint(30,100)
    if vE > v0:
        P_mot = P_ped*(vE-v0)/v0
    elif vE <= v0:
        P_mot = P_ped/(v0+vE)
    else:
        P_mot = 0
    P_motr = random.uniform(P_mot-1,P_mot+1)
    print('input - ', round(v0,4), round(w,4) ,P_ped, '  output - ', round(P_motr,4))
    # print('output - ', round(P_motr,4))
    i = i+1
k = 0
while(k<900):
    v0 = random.uniform(1,6.495)
    w = random.uniform(0,0.3)
    P_ped = random.randint(30,100)
    if vE > v0:
        P_mot = (P_ped*(vE-v0)/v0) + (P_ped*(vE/(v0*0.52))*(w/math.sqrt(w**2+1)))
    elif vE <= v0:
        P_mot = P_ped/(v0+vE) + (P_ped*(vE/(v0*0.52))*(w/math.sqrt(w**2+1)))
    else:
        P_mot = 0
    P_motr = random.uniform(P_mot-1,P_mot+1)
    print('input - ', round(v0,4), round(w,4) ,P_ped, '  output - ', round(P_motr,4))
    k = k+1
