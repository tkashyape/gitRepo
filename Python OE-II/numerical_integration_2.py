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
   a = 1.5     # Upper limit
   b = 3.0     # Lower limit
   
   # Gauss Quadrature points and weights
   z_L = [0.000000, 0.774597, -0.774597]     # Points   
   A_L = [0.888889, 0.555556, 0.555556]      # Weights
   
   # x in terms of z
   x_L = []
   for i in range(len(z_L)):
      x1 = ((b+a)/2.0) + ((b-a)/2.0) * z_L[i]
      x_L.append(x1)

   x_input_L = [1.2, 1.7, 2.0, 2.4, 2.9, 3.3]
   fx_input_L = [-0.36236, 0.12884, 0.41615, 0.73739, 0.97096, 0.98748]
   
   I = 0.0
   
   for i in range(len(x_L)):
      x1 = x_L[i]
      fx1 = 0.0
      A1 = A_L[i]
      print "x1 " + str(x1) + " A1 " + str(A1)
      
      for j in range(len(x_input_L)-1):
         x_low = x_input_L[j]
         x_up = x_input_L[j+1]
         
         if (x_low <= x1) and (x1 <= x_up):
            fx1 = fx_input_L[j] + (fx_input_L[j+1]-fx_input_L[j])*(x1-x_low)/(x_up-x_low)
            print "fx1 " + str(fx1)
            I += A1 * fx1         
   I *= (b-a)/2.0  
   print "Integration = " + str(I)

   #----------------------------------------------------------------------------------------------------
   stopClock = time.time()
   clockTime_L = FH.calculate_clock_time(stopClock - startClock)
   print "\n***** Total time to run this program: " + str(clockTime_L[0]) + ":" + str(clockTime_L[1]) + ":"  + str(clockTime_L[2])

   print "\n***** Program Ended! *****\n"

#--------------------------------------------------------------------------------------------------