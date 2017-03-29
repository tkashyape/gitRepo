#--------------------------------------------------------------------------------------------------
#
# Filename        :  numerical_integration.py
# Version         :  1.0
# Issue date      :  01-01-2017
# Project         :  WCE
# Author          :  Sham Gurav
#
#--------------------------------------------------------------------------------------------------
# Release Changes    | Date         | Author       | Checker      | Changes
# 1.0                | 01-01-2017   | Sham         | -            | Initial
#--------------------------------------------------------------------------------------------------
# Purpose         :  Integrate function numerically
#--------------------------------------------------------------------------------------------------
from file_io import *
#--------------------------------------------------------------------------------------------------
# Main method
if __name__ == "__main__":

   startClock = time.time()

   print "\n\n***** Carry out integration numerically *****\n\n"

   #----------------------------------------------------------------------------------------------------
   # Get user input

   # Limits of integration
   a = 1.5     # Lower limit
   b = 3.0     # Upper limit

   # Gauss Quadrature points and weights
   z_L = [0.000000, 0.774597, -0.774597]     # Points
   A_L = [0.888889, 0.555556, 0.555556]      # Weights

   # Using transformation of x in terms of z, calculate points
   x_L = []

   for i in range(len(z_L)):

      x1 = ((b+a)/2.0) + ((b-a)/2.0) * z_L[i]
      x_L.append(x1)

   I = 0.0

   for i in range(len(x_L)):

      x1 = x_L[i]
      A1 = A_L[i]

      fx1 = -cos(x1)    # Calculate function value

      print "Point: " + str(x1) + " Weight: " + str(A1) + " Function value: " + str(fx1)

      I += A1 * fx1     # Update integration value (sum)

   I *= (b-a)/2.0    # Apply scale factor (only once)

   print "Integration: " + str(I)

   #----------------------------------------------------------------------------------------------------
   stopClock = time.time()
   clockTime_L = FH.calculate_clock_time(stopClock - startClock)
   print "\n***** Total time to run this program: " + str(clockTime_L[0]) + ":" + str(clockTime_L[1]) + ":"  + str(clockTime_L[2])

   print "\n***** Program Ended! *****\n"

#--------------------------------------------------------------------------------------------------