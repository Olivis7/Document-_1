

n=int(input())

st=""
while n>0:
          st=str(n%2)+st
          n=n//2
print(st)
for i in range(3):
          if st.count("0")>st.count("1"):st+="1"
          elif st.count("0")<st.count("1"): st+="0"
          else:st+=st[len(st)-1]
          print(st)          

c=(int(st,2))
print(c)
if c%4==0: print("y")
