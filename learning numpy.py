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