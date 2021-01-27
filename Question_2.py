import numpy as np
import matplotlib.pyplot as plt
import math as math


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ


A = np.array([0,0])
C = np.array([5.5,0])
#the equation of AD will be as y = tan(50)x

#x_d = math.sqrt((6**2)/(1+(math.tan((math.pi)*5/18))**2))
#y_d = (math.tan((math.pi)*5/18))*x_d



D = np.array([3.22,4.45])
B=np.array([1.68 , -2.378])
AC = line_gen(A,C)
AD = line_gen(A,D)
CD = line_gen(C,D)
CB= line_gen(C,B)
AB=line_gen(A,B)
#circ_D = circ_gen(0,4.5)
#plt.plot((x_1,x_2,x_3),(y_1,y_2, y_3))



plt.plot(AC[0,:],AC[1,:])
plt.plot(AD[0,:],AD[1,:])
plt.plot(CD[0,:],CD[1,:])
plt.plot(CB[0,:],CB[1,:])
plt.plot(AB[0,:],AB[1,:])


plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.06), C[1] * (1 - 0.2) , 'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 -0.1) , 'D')




plt.plot()
plt.grid()
plt.axis("equal")
plt.show()
