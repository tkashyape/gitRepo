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
from numerical_integration_library import *
#--------------------------------------------------------------------------------------------------
# Main method
if __name__ == "__main__":

   startClock = time.time()

   print "\n\n***** Carry out integration numerically *****\n\n"

   #----------------------------------------------------------------------------------------------------

   # Get user input
   inputFileName, solutionMethod = get_user_input()

   # Read integration function data from file
   integrationData = read_integration_function_data(inputFileName)

   # Limits of integration
   lowerLimit = integrationData[0]     # Lower limit
   upperLimit = integrationData[1]     # Upper limit

   x_input_L = integrationData[2]
   fx_input_L = integrationData[3]

   # Calculate integration
   if solutionMethod == 1:
      # Calculate integration using Trapezoidal Rule
      I = calculate_integration_by_Trapezoidal_Rule(lowerLimit, upperLimit, x_input_L, fx_input_L)
   elif solutionMethod == 2:
      # Calculate integration using Simpson's Rule
      I = calculate_integration_by_Simpsons_Rule(lowerLimit, upperLimit, x_input_L, fx_input_L)
   elif solutionMethod == 3:
      # Calculate integration using Gauss-Quadrature method
      I = calculate_integration_by_Gauss_Quadrature(lowerLimit, upperLimit, x_input_L, fx_input_L)
   else:
      print "\n***** Selected method not available *****"

   print "Integration: " + str(I)

   #----------------------------------------------------------------------------------------------------
   stopClock = time.time()
   clockTime_L = FH.calculate_clock_time(stopClock - startClock)
   print "\n***** Total time to run this program: " + str(clockTime_L[0]) + ":" + str(clockTime_L[1]) + ":"  + str(clockTime_L[2])

   print "\n***** Program Ended! *****\n"

#--------------------------------------------------------------------------------------------------