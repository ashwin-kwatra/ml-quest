import numpy as np 
a=np.array(4)
print(a.ndim)
#ndim = checking rank or dimension of tensor

arr=np.array([1,2,3,4],dtype=float)
#,dtype karnee se ham data type define kar skte h

print(arr.ndim)
# this tensor is 1 dimension but the list/vector is 4 dimension because it has 4 things

arr2=np.array([[1,2,3,4],[12,2,3,4],[3,2,3,4]])
print(arr2.ndim)
# this si 2d tensor/matrix

print(np.arange(1,11,1)) #just like python range

print(np.arange(1,11,2))
print(np.arange(1,11,1).reshape(2,5)) #turns it into matrix or other type of data

# print(np.arange(1,11,1).reshape(3,3)) this wont work cuz 10 elemt dont fit in 3x3

print(np.ones((3,2)))# makes a array of ones or zeroes
print(np.zeros((2,3)))

print(np.random.random((2,2))) # random numbers between 1,0

print(np.linspace(1,10,3)) #makes n number of points between start and end at equal space
print(np.linspace(-10,10,7))

print(np.identity(3)) #makes identity matrix ( diagonal 1 rest zero "I")

#                                           attributes:
print(arr2.ndim) #dimension or array
print(arr2.size) # total elemt
print(arr2.itemsize) #size of item
print(arr2.shape) #shape
print(arr.dtype) #datatype of item

header='''                            these are ways to make an array above
                        now we make chnages'''

print(arr2.astype(np.int32),arr2.dtype) #turns the default int64 to int16 ( DOES NOT CHANGE IT ONLY CREATES A COPY) , depends on use case

header='''                              scalar operations (opeartion on every single elemnt and returns an array)'''
print(arr*2)
print(arr+1)
print(arr**2)
print(arr>2) #all elemtns above 2 will give true , others give false , retunred value is a array of bool not bool
print(arr==1)

header='''                     vector calculus     '''

a1=np.identity(3)
a2=np.ones((3,3))
a3=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a1+a3)
print(a1-a3)
print(a2*a3) # its not doing cross multiplication or cross or dot product , shapes must be same to work

a1=np.random.random((3,3))
a1=np.round(a1*100) #rounds up and makes it integer

print(np.max(a1))
print(np.min(a1))
print(np.sum(a1))
print(np.prod(a1))
# mean , median , std , var , sin , cos , tan (mean ,median , standard deviation , variance)
# o is collumn and 1 is row 
print(a1)
print(np.max(a1,axis=0)) # maximum number in that column
print(np.min(a1,axis=1)) # minimum number in that row
print(np.dot(a1,a2))#dot product
print(np.log(a1))
print(np.exp(a1))

#floor and ciel and round that turn float to int
print(np.floor(a1))
print(np.ceil(a1))
print(np.round(a1))

#slicing
#JUST LIKE PYTHON BUT EK HI DABBE M COMMA LGAKE
print(a3)
print(a3[1,2])
print(arr[1:3]) # index 1 to index 3 , not inluding index 3
print(a3[0:2,0]) #2nd dimension ka 0 to 2 slice aur 1st dimension ki sirf 0th
print(a3[0,:]) # trick top find rows and columns
print(a3[:,0]) 

# looping :
for i in a3:
    print(i)
# isme every elemt = 1 less dimension
for i in np.nditer(a3):
    print(i)
# isme nd array or 1d mein conver tkrke sab ek ek krke print krta h