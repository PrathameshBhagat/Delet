f= open('demo.txt','r')
txt=f.read()
c=0
for i in txt.split():
    c=c+1

print('Total number of Words are',c)
