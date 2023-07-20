plaintext=str(input("Enter the plaintext="))
c=0
i=0
s=0
x=" "
list1=[]
newlist=[]
l1=[c for c in plaintext]
intr=[ord(c) for c in plaintext]

for i in range(0, len(intr)):
    count=0
    while(intr[i]!=0):
        rem= int(intr[i]%10)
        if(rem==0):
            x="0000"
        if(rem==1):
            x="0001"
        if(rem==2):
            x="0010"
        if(rem==3):
            x="0011"
        if(rem==4):
            x="0100"
        if(rem==5):
            x="0101"
        if(rem==6):
            x="0110"
        if(rem==7):
            x="0111"
        if(rem==8):
            x="1001"
        intr[i]=intr[i]//10
        list1.insert(count,x)
        count=count+1
        x=" "
    if(count==2):
        list1.insert(2,"0000")

list1.reverse()
sb=' '.join(map(str, list1))

print("Plaintext=", plaintext,"\nBits=",sb)

list12=[sb[i:i+12]for i in range(0,len(sb),12)]

print("Twelve bits=", list12)
