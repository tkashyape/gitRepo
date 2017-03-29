from file_io import *
#--------------------------------------------------------------------------------------------------
# Read input file containing integration function data
def read_integration_function_data(inputFileName):

   print "\n***** Reading file containing integration function data *****\n"
   time.sleep(1)

   # Read input file to get lower limit, upper limit, x, f(x)
   inputData = FH.read_data_file(inputFileName,1)

   # Get data from input file
   for i in range(len(inputData)):

      data = inputData[i].split(';')

      if data[0] == "lowerLimit":
         lowerLimit = float(data[1].strip())
      elif data[0] == "upperLimit":
         upperLimit = float(data[1].strip())
      elif data[0] == "x":
         x = data[1].strip().split(',')
      elif data[0] == "fx":
         fx = data[1].strip().split(',')

   integrationData = [lowerLimit, upperLimit, x, fx]

   # Check user input
   print "\n Lower Limit: " + str(lowerLimit)
   print "\n Upper Limit: " + str(upperLimit)
   print "\n x: ", x
   print "\n f(x): ", fx, "\n"

   return integrationData

#--------------------------------------------------------------------------------------------------
def get_user_input():

   # Get user input

   # Get name of the file containing function data and limits of integration
   inputFileName = raw_input("\n Give file name containing function data: \n")
   inputFileName = inputFileName.strip()

   # Select method to solve LAE
   methodSelection_Str = "\n Select method of integration: \n"
   methodSelection_Str += "\n 1. Trapezoidal Rule \n"
   methodSelection_Str += "\n 2. Simpson's Rule \n"
   methodSelection_Str += "\n 3. Gauss Quadrature \n"
   methodSelection_Str += "\n 0. To end the program \n"

   availableMethods_L = [0, 1, 2, 3]

   # Set loop until appropriate method is selected
   methodSelectionStatus = False

   while not methodSelectionStatus == True:

      solutionMethod = int(raw_input(methodSelection_Str))

      if solutionMethod in availableMethods_L:

         methodSelectionStatus = True

      else:
         print "\n Select method only from provided options!"

   return inputFileName, solutionMethod

#--------------------------------------------------------------------------------------------------
# Calculate function vaalue by interpolation
def calculate_function_value_by_interpolation(x_input_L, fx_input_L, x1):

   fx1 = 0.0      # Initialize function value to be ineterpolated

   for i in range(len(x_input_L)-1):

      # Initialize range for interpolation
      x_low = float(x_input_L[i])
      x_high = float(x_input_L[i+1])

      fx_low = float(fx_input_L[i])
      fx_high = float(fx_input_L[i+1])

      # If the current value is in between the selected range for interpolation
      if (x_low <= x1) and (x1 <= x_high):

         fx1 = fx_low + (fx_high - fx_low)*(x1-x_low)/(x_high-x_low)

   return fx1

#--------------------------------------------------------------------------------------------------
# Calculate integration using Gauss-Quadrature
def calculate_integration_by_Trapezoidal_Rule(lowerLimit, upperLimit, x_input_L, fx_input_L):

   samplingPoints = 100     # Number of sampling points for integration

   integrationRange = upperLimit - lowerLimit
   domainWidth = integrationRange/samplingPoints

   x1_L = []      # List to store sampling points
   fx1_L = []     # List to store function values for sampling points

   x1 = lowerLimit      # Initialize sampling point from the lower limit
   x1_L.append(x1)

   for i in range(samplingPoints):

      # Calculate function value by  inerpolation
      fx1 = calculate_function_value_by_interpolation(x_input_L, fx_input_L, x1)
      fx1_L.append(fx1)

      x1 += domainWidth    # update sampling point
      x1_L.append(x1)

   I = fx1_L[0] + fx1_L[-1]      # Initialize integration by adding first and last function value

   # Loop to add intermediate function values
   for i in range(samplingPoints-2):

      I += fx1_L[i+1] * 2

   I *= domainWidth/2.0

   return I

#--------------------------------------------------------------------------------------------------
# Calculate integration using Gauss-Quadrature
def calculate_integration_by_Simpsons_Rule(lowerLimit, upperLimit, x_input_L, fx_input_L):

   samplingPoints = 11     # Number of sampling points for integration

   integrationRange = upperLimit - lowerLimit
   domainWidth = integrationRange/samplingPoints

   x1_L = []      # List to store sampling points
   fx1_L = []     # List to store function values for sampling points

   x1 = lowerLimit      # Initialize sampling point from the lower limit
   x1_L.append(x1)

   for i in range(samplingPoints):

      # Calculate function value by  inerpolation
      fx1 = calculate_function_value_by_interpolation(x_input_L, fx_input_L, x1)
      fx1_L.append(fx1)

      x1 += domainWidth    # update sampling point
      x1_L.append(x1)

   I = fx1_L[0] + fx1_L[-1]      # Initialize integration by adding first and last function value

   # Loop to add intermediate function values
   for i in range(0,samplingPoints-3,2):

      I += fx1_L[i+1] * 4
      I += fx1_L[i+2] * 2

   I *= domainWidth/2.0

   return I

#--------------------------------------------------------------------------------------------------
# Calculate integration using Gauss-Quadrature
def calculate_integration_by_Gauss_Quadrature(lowerLimit, upperLimit, x_input_L, fx_input_L):

   # Gauss Quadrature points and weights
   z_L = [0.000000, 0.774597, -0.774597]     # Points
   A_L = [0.888889, 0.555556, 0.555556]      # Weights

   # Using transformation of x in terms of z, calculate points
   x_L = []

   for i in range(len(z_L)):

      x1 = ((upperLimit+lowerLimit)/2.0) + ((upperLimit-lowerLimit)/2.0) * z_L[i]
      x_L.append(x1)

   I = 0.0

   for i in range(len(x_L)):

      x1 = x_L[i]
      A1 = A_L[i]

      fx1 = -cos(x1)    # Calculate function value

      print "Point: " + str(x1) + " Weight: " + str(A1) + " Function value: " + str(fx1)

      I += A1 * fx1     # Update integration value (sum)

   I *= (upperLimit-lowerLimit)/2.0    # Apply scale factor (only once)

   return I

#--------------------------------------------------------------------------------------------------
