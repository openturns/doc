from openturns import *
import numpy as np
#
#===================================================================
#
# Number of input random variables
dim=10
#
# Definition of the physical model
class myfunction(OpenTURNSPythonFunction):
    def __init__(self):
        OpenTURNSPythonFunction.__init__(self, dim, 1)
    def _exec(self, X):

        # Length of bar 3 (deterministic)
        L = 5.   # in m

        # Extract input variables from X
        E1,E2,E3,S1,S2,S3,P,Theta,alpha1,alpha2 = X

        # Degrees to radians
        theta_rad=Theta*np.pi/180.0
        alpha1_rad=alpha1*np.pi/180.0
        alpha2_rad=alpha2*np.pi/180.0

        # Vertical and horizontal loads
        Pv=-1.*P*np.cos(theta_rad)
        Ph=P*np.sin(theta_rad)

        # Intermediate variables
        alphav=(np.sin(alpha2_rad+alpha1_rad)/np.sin(alpha2_rad))*(1.0/((E3*S3/(np.cos(alpha1_rad)*E1*S1))+(E3*S3/(np.cos(alpha2_rad)*E2*S2))*(np.sin(alpha1_rad)/np.sin(alpha2_rad))**2+(np.sin(alpha2_rad+alpha1_rad)/np.sin(alpha2_rad))**2))

        alphah=(np.sin(alpha1_rad)/(np.sin(alpha2_rad)**2*np.cos(alpha2_rad)*E2*S2)+(np.sin(alpha1_rad+alpha2_rad)*np.cos(alpha2_rad))/(np.sin(alpha2_rad)**2*E3*S3))/(1.0/(np.cos(alpha1_rad)*E1*S1)+((np.sin(alpha1_rad)/np.sin(alpha2_rad))**2)*(1.0/(np.cos(alpha2_rad)*E2*S2))+((np.sin(alpha1_rad+alpha2_rad)/np.sin(alpha2_rad))**2)*(1.0/(E3*S3)))

        # Horizontal and vertical displacements
        deltah=(alphah**2/(E1*S1*np.cos(alpha1_rad))+((alphah*np.sin(alpha1_rad)/np.sin(alpha2_rad)-1.0/np.sin(alpha2_rad))**2)/(E2*S2*np.cos(alpha2_rad))+((alphah*np.sin(alpha1_rad+alpha2_rad)/np.sin(alpha2_rad)-np.cos(alpha2_rad)/np.sin(alpha2_rad))**2)/(E3*S3))*Ph*L
        deltav=(alphav**2/(E1*S1*np.cos(alpha1_rad))+(alphav**2*np.sin(alpha1_rad)**2)/(E2*S2*np.cos(alpha2_rad)*np.sin(alpha2_rad)**2)+((1.0-alphav*np.sin(alpha2_rad+alpha1_rad)/np.sin(alpha2_rad))**2)/(E3*S3))*Pv*L

        # L2-norm of the displacement vector
        Y = np.sqrt(deltah**2+deltav**2)

        return [Y]
#
#===================================================================
#
# For test: evaluate the model at the nominal input parameters
#
if __name__ == "__main__":
    #
    truss_model = NumericalMathFunction(myfunction())
    #
    Xnom = NumericalPoint(([2100.e6,2100.e6,2100.e6,0.0015,0.0015,0.0015,2500.,45.,45.,45.]))
    Ynom = truss_model(Xnom)
    #
    print "" ; print "Value of the displacement (m):", Ynom[0] ; print ""
