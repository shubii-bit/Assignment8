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


Q = np.array([0,0])
R = np.array([4.7,0])
P = np.array([3.6,2.12])
#the equation of AD will be as y = tan(50)x


PQ = line_gen(P,Q)
QR = line_gen(Q,R)
PR = line_gen(P,R)
#circ_D = circ_gen(D,)
#plt.plot((x_1,x_2,x_3),(y_1,y_2, y_3))



plt.plot(PQ[0,:],PQ[1,:])
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1-0),P[1]*(1+0.1),"P")
plt.plot(QR[0,:],QR[1,:])
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1+0.1),Q[1]*(1-0),"Q")
plt.plot(PR[0,:],PR[1,:])
plt.plot(R[0],R[1],"o")
plt.text(R[0]*(1+0.1),R[1]*(1-0),"R")

plt.grid()
plt.axis("equal")
plt.show()
