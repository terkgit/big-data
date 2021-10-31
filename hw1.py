# Author: Terkel
# Big Data HW 1
import numpy
def main():
    P=[numpy.array([1,1,0]),numpy.array([2,2,4]),numpy.array([1,0,3]),numpy.array([2,3,9])]
    s,n,p_t=create_using_3_first_moments(P)

    # a=[1,0,0]
    # b=[4,5,6]
    # c=numpy.cross(a,b)
    # print(a)
    # print(b)
    # print(c)
    # print(numpy.linalg.norm(a))
    # print(numpy.linalg.norm(b))
    # print(numpy.linalg.norm(c))

def create_using_3_first_moments(P):
    # sum||p-x||^2 = sum||p||^2 + sum||x||^2 -2sum((P^T)x) = sum||p||^2 + n||x||^2 -2(sum(p^T))x
    
    # s = sum||p||^2 , p_t = sum(p^T)
    s=float(0)
    p_t=(numpy.transpose(P[0]))*0
    #print("p[0]*0: " + str(p_t))
    i=int(0)
    for p in P:
        #print("p["+str(i)+"] = "+str(p))
        #i+=1
        temp=numpy.linalg.norm(p)
        s+=(temp*temp)              # s = sum||p||^2
        p_t+=numpy.transpose(p)     #p_t = sum(p^T)
    print("sum||p||^2 = "+str(s))
    print("sum(p^T) = "+str(p_t))

    # n = |P|
    n=len(P)
    print("n = "+str(n))
    return s,n,p_t

main()