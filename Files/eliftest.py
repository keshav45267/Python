# to practice if - elif else
# per > 90  A+
# per > 80 A
# per > 70 B+
# per > 60 B
# per < 60 F

e = 50
h = 95
m = 100
ss = 75
sc = 89
tm = e+h+m+sc+ss
per = (tm/500)*100
print("Percentage : ",per)
if tm>450:
    print('Grade A+')
elif tm>400:
    print('Grade A')
elif tm>350:
    print('Grade B+')
elif tm>300:
    print('Grade B')
elif tm>250:
    print('Grade C')
else:
    print('Grade F')
