import os
import sys
import re


if len(sys.argv)<=1:
	print("enter correct file locations(2)")
	exit(1)

f = os.getcwd()+'/'+sys.argv[1]
g = os.getcwd()+'/'+sys.argv[2]
#R=open("result.txt","w")


A=open(f,encoding='utf8')
B=open(g,encoding='utf8')
linesA=A.readlines()
linesB=B.readlines()
cveA=[]
cveB=[]
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


print("\nCommon cve")
print('─' * 20)
print(*cveCommon)
print("\nCVE exclusive to A(First argument you provided)")
print('─' * 20)
print(*cveExclusiveA)
print("\nCVE exclusive to B(Second argument you provided")
print('─' * 20)
print(*cveExclusiveB)


A.close()
B.close()
