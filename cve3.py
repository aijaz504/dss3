import os
import sys
import re

# usage example for windows : cve.py \Anchore\A_mongo.txt \Clair\C_mongo.txt
# usage example for linux : python3 cve.py /Anchore/A_mongo.txt /Trivy/T_mongo.txt

if len(sys.argv)<=1:
	print("enter correct file locations(2)")
	exit(1)

f = os.getcwd()+'/'+sys.argv[1]
g = os.getcwd()+'/'+sys.argv[2]
h = os.getcwd()+'/'+sys.argv[3]

#R=open("result.txt","w")

#f = os.getcwd()+"\\Anchore\\A_mongo.txt"
#g = os.getcwd()+"\\Clair\\C_mongo.txt"
#print(f)
#print(os.getcwd())
A=open(f,encoding='utf8')
B=open(g,encoding='utf8')
C=open(g,encoding='utf8')


linesA=A.readlines()
linesB=B.readlines()
linesC=C.readlines()

cveA=[]
cveB=[]
cveC=[]
cveD=[]
cveCommon=[]
for m in linesA:
    #print(m)
    try:
        i=m.index("CVE-")
        c=m[i:i + 17].strip()
        if c not in cveA:
            cveA.append("CVE"+re.sub("[^\d\-]", "",c))
    except:
        continue
for m in linesB:
    try:
        i = m.index("CVE-")
        c = m[i:i + 17].strip()
        if c not in cveB:
            cveB.append("CVE"+re.sub("[^\d\-]", "",c))
    except:
        continue
        
for m in linesC:
    #print(m)
    try:
        i=m.index("CVE-")
        c=m[i:i + 17].strip()
        if c not in cveA:
            cveC.append("CVE"+re.sub("[^\d\-]", "",c))
    except:
        continue
        
        
totalCVE = cveA + cveB + cveC

# to remove duplicated from list 
result = [] 
[result.append(x) for x in totalCVE if x not in result] 

# printing list after removal 

print ("Total CVE: ") 
print('─' * 120)
print(str(result))

'''
print("\nTotal CVE of A and B")
print('─' * 20)
print(*totalCVE)
'''
       
cveExclusiveA=[]
cveExclusiveB=[]
for x in range(len(cveA)):
    if cveA[x] in cveB:
        if cveA[x] not in cveCommon:
            cveCommon.append(cveA[x])
    else:
        if cveA[x] not in cveExclusiveA:
            cveExclusiveA.append(cveA[x])
for x in range(len(cveB)):
    if cveB[x] not in cveA:
        if cveB[x] not in cveExclusiveB:
            cveExclusiveB.append(cveB[x])

#stacked view
'''
print("\nTotal CVE in A")
print('─' * 20)
print(*cveA)
print("\nTotal CVE in B")
print('─' * 20)
print(*cveB)



print("\nCommon cve")
print('─' * 20)
print(*cveCommon)
print("\nCVE exclusive to A")
print('─' * 20)
print(*cveExclusiveA)
print("\nCVE exclusive to B")
print('─' * 20)
print(*cveExclusiveB)
'''


A.close()
B.close()
