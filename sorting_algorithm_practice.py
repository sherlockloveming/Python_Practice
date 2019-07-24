#Selection Sort
c=[5,9,3,6,10,4,2,25,15,1]
for j in range(0,len(c)-1):
  smallest=j
  minvalue=c[smallest]

  for i in range(j+1,len(c)):
    if c[i]<minvalue:
      smallest=i
      minvalue=c[smallest]

    c[j],c[smallest]=s[smallest],c[j]

#=================================================#

#Insertion Sort
a=[4,1,7,10,3,8,5,2,9]
for j in range(0,len(a)):
  key=a[j]
  i=j-1
  while i>=0 and a[i]>key:
    a[i+1]=a[i]
    i=i-1
  a[i+1]=key
