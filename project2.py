
plain=str(input("Enter the text:"))
c=0
i=0
s=0
x=" "
list=[]
new=[]
l=[c for c in plain]
result=[ord(c) for c in plain]
for i in range(0,len(result)):
    count=0
    while(result[i]!=0):
        rem=int(result[i]%10)
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
            x="1000"
        if(rem==9):
            x="1001"
        result[i]=result[i]//10
        list.insert(count,x)
        count=count+1
        x=" "
    if(count==2):
        list.insert(2,"0000")

list.reverse()
sin=''.join(map(str,list))

print("Plaintext=",plain,"\nBits",sin)

list1=[sin[i:i+12]for i in range(0, len(sin),12)]

print("Twelve bits",list1)

for i in range(len(list1)):
    if(list1[i][0:4]=="0000"):
        new.insert(i,list1[i][4:12])
    else:
        new.insert(i,list1[i])
print("new list",new)

x=" "
for i in range(len(new)):
    if((new[i][0:4] == "0000")):
        x+="0"
    if((new[i][0:4] == "0001")):
        x+="1"
    if((new[i][0:4] == "0010")):
        x+="2"
    if((new[i][0:4] == "0011")):
        x+="3"
    if((new[i][0:4] == "0100")):
        x+="4"
    if((new[i][0:4] == "0101")):
        x+="5"
    if((new[i][0:4] == "0110")):
        x+="6"
    if((new[i][0:4] == "0111")):
        x+="7"
    if((new[i][0:4] == "1000")):
        x+="8"
    if((new[i][0:4] == "1001")):
        x+="9"

    if((new[i][4:8] == "0000")):
        x+="0"
    if((new[i][4:8] == "0001")):
        x+="1"
    if((new[i][4:8] == "0010")):
        x+="2"
    if((new[i][4:8] == "0011")):
        x+="3"
    if((new[i][4:8] == "0100")):
        x+="4"
    if((new[i][4:8] == "0101")):
        x+="5"
    if((new[i][4:8] == "0110")):
        x+="6"
    if((new[i][4:8] == "0111")):
        x+="7"
    if((new[i][4:8] == "1000")):
        x+="8"
    if((new[i][4:8] == "1001")):
        x+="9"


    if((new[i][8:12] == "0000")):
        x+="0"
    if((new[i][8:12] == "0001")):
        x+="1"
    if((new[i][8:12] == "0010")):
        x+="2"
    if((new[i][8:12] == "0011")):
        x+="3"
    if((new[i][8:12] == "0100")):
        x+="4"
    if((new[i][8:12] == "0101")):
        x+="5"
    if((new[i][8:12] == "0110")):
        x+="6"
    if((new[i][8:12] == "0111")):
       x+="7"
    if((new[i][8:12] == "1000")):
       x+="8"
    if((new[i][8:12] == "1001")):
        x+="9"
print("\n",chr(int(x)))
x=" " 
