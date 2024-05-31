#brute
n=100
str1=""
while n!=0:
    str1=str(n&1)+str1
    n>>=1
for i in range(8-len(str1)):
    str1='0'+str1
one=""
two=""
for i in range(len(str1)):
    if i<4:
        one+=str1[i]
    else:
        two+=str1[i]
two='11110000'
bin_number=0
count=0
for i in range(len(two)-1,-1,-1):
    bin_number+=int(two[i])*(2**count)
    count+=1
print(bin_number)


print(0x0f," ",0xf0)

#optimal
def print_num(number):
    return ((number&15)<<4 | (number&240)>>4)
print(print_num(129))
