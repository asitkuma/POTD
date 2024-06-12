PROBLEM STATEMENT.
Today's problem statement is very simple, you need to find , how many times 4 as a digit occurs between 0 to n.

NOW THE THOUGH PROCESS BEGIN.
what will be the answer if the value of n is 50.. it should be 14 or 15?..  Let me tell you it would be 14, because question doesn't tell you to find the total number of 4 occurs in each number, it's simply tell u to find the total number of 4 occurs between a given range, that simple means for 44, the count should be 1, it should not be 2. right.... done..
If we will see then should we really need to start from 0?? obviously not , it should be from 4 to n.
4 can be present at any place , it can be at first place or second place etc. 
#FINALLY WE COMPLETED THE THOUGHT PROCESS

NOW WE WILL JUMP INTO THE SOLUTION,

-> What is the buteforce approach that comes into brain,  

Intialize a count varaible count=0 which will count the total nuber of 4 occurs between the given range.
We will iterate a loop for i in range(4,n+1): this will go from 4 to n. here n+1 signifies <=n 
Convert the number into string and check if 4 occurs or not 
for j in str(i)
if '4' ==j
count++
break
then fianlly return count.
If we will analysis the ans, we are performing linear search. in order to find the 4 
TIME COMPLEXITY AND SPACE COMPLEXITY FOR THIS BRUTEFORCE APPROACH
Intialize the count:- O(1)
for i in range(4,n) :- O(n-4) , but we will count as O(n)
for j in str(i):- O(len(digit)) total Tc become O(n)*O(len(digit)) if we ignore the tc for conversion from int to str..
if u have doubt how to convert a number into string then u can write th following code like 
 str1=""
while number!=0:
str1=str(number%10)+str1
number//=10
Tc for this code is O(logn)  
Let me tell u a trick to know O(logn) time complexity, if anything u find divided by 10 then time compleity for that problem will be logn
And if we will talk about space complexity it will be O(1). 
This solution is also acceptable, if u feel comfortable with this solution then u might choose this.
NOW DISCUSS ABOUT THE EFFICIENT APPROACH
If we will carefully observe then do we need to convert into string? thik for a while . cant we solve the question without conversion??...Ofcourse we can. as like i descibed how to convert a number into string there is the solution.. while u r converting why can t u just check if 4 is there or not directly?.. Cool i think we done it...  

for i ->4 to n
while i!=0
if i%10==4
count++
break
i/=10
finally done with return count..
TIME COMPLEXITY AND SPACE COMPLEXITY FOR THIS EFFICIENT APPROACH
Initialize the count count=0 O(1)
for i-> 0 to 4 O(n)
while j !=0:  this while loop will take O(logn) time complexity.
if j%10==4
count+=1
break
j//=10
Finally Tc is O(nlogn)
Although we didnt use any kind of extra space except a constant variable which is 'count' and that will take O(1)  
 

 

Finally done.. if u think it this is helpful for u .. and if u want to comment everyday as like this .. then please lemme know in comment .. and this is all for today.





class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        # ans=0
        # for i in range(4,n+1):
        #     for j in str(i):
        #         if j=='4':
        #             ans+=1
        #             break
        # return ans
        count=0
        for i in range(4,n+1):
            j=i
            while j!=0:
                if j%10==4:
                    count+=1
                    break
                j//=10
        return count
        
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends
























