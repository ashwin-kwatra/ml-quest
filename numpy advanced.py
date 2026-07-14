import numpy as np 
arr2=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
arr=np.arange(1,10)

#transpose :
print(arr2.T,"\n")
print(np.transpose(arr2),"\n")  # row , column exchnage

print(arr2.ravel(),"\n")  # kat peet ke 1d bna deta h

#stazcking
a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)

print(np.hstack((a1,a2)),"\n")  # horizonjtal stack 9side by side
print(np.vstack((a1,a2)),"\n") # upar neeche
a = np.random.randint(1,100,24).reshape(6,4)
print(a,"\n")
# row wise ( axis na do toh yehi default hai)
print(np.sort(a,axis=1),"\n")
a = np.random.randint(1,100,24).reshape(6,4)
print(a,"\n") # column wise
print(np.sort(a,axis=0),"\n")

print(np.append(arr,10),"\n")
print(np.append(arr2,np.ones((4,1),dtype=int)),"\n") # because we did not specify axis , it just convert to 1d and added
print(np.append(arr2,np.ones((arr2.shape[0],1)),axis=1),"\n")
print(np.append(arr2,np.ones((1,arr2.shape[1])),axis=0),"\n")
# all changes are temproory , not affect real thing for now

# comparing python list with numpy speed/space
import time
import numpy as np
import sys 
'''
a=[i for i in range(100000000)]
b=[i for i in range(100000000,200000000)]
c=[]
start=time.time()
for i in range(len(a)):
    c.append(a[i]+b[i])
print(time.time()-start)

a=np.arange(100000000)
b=np.arange(100000000,200000000)
c=[]
start=time.time()
c=a+b
print(time.time()-start)
'''
a=np.arange(10000000,dtype=np.int8)
print(sys.getsizeof(a))
# we can change datatype to reduce size
a=[i for i in range(10000000)]
print(sys.getsizeof(a))
# specific/fancy indexing ( give a list of numbers)
a= np.arange(12).reshape(4,3)
print(a)
print(a[[0,2,3]])
#aplly condition on an np array , we get an array of true/false that we can use to get elemtns
a=np.random.randint(1,100,50).reshape(5,10)
print(a)
print(a[a>50])
#bitwise operator bevause boolean value
print(a[(a>50) & (a%2==0)])



