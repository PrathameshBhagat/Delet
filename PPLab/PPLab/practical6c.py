f= open('Xyz.txt','r')
txt=f.readline()
c=0

for i in txt.split():
 if i.lower() == 'python':
