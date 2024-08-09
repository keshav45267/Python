bp=eval(input("enter the basic pay"))
hra= (8*bp)/100
da=(50*bp)/100
fma=1000
total_claim=bp+hra+da+fma
print(total_claim)
gs=total_claim*12
print(gs)

pf=10*bp/100
od=500
if gs<=500000:
    
    tax=pf+od
    print('tax=0')
elif gs>500000 and gs<=700000:
    tax=((gs-500000)*0.1)+pf+od
    
    
elif gs>700000 and gs<=1000000:  
    tax=20000+((gs-700000)*0.2)+pf+od
    
elif gs>1000000:
    tax= tax=20000+60000+((gs-1000000)*0.3)+pf+od  
print("tax=",(tax/12))
net_salary=total_claim-(tax/12)
print("net salary=",net_salary)