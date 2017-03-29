#-------------------------------------------------------------------------------------------------------
#
# Filename        :  file_io.py
# Version         :  1.1
# Issue date      :  24-04-2014
# Project         :  A350XWB
# Author          :  Sham Gurav
#
#-------------------------------------------------------------------------------------------------------
# Release Changes    | Date         | Author       | Checker      | Changes
# 1.0                | 11-12-2013   | GURA3543     | -            | Initial
# 1.1                | 24-04-2014   | GURA3543     | -            | New methods added
#-------------------------------------------------------------------------------------------------------
# Purpose: To handle various input & output file operations
#-------------------------------------------------------------------------------------------------------
import os,sys,time,copy,re,string,gc
from math import *
from string import *
#-------------------------------------------------------------------------------------------------------
# Class defines various methods to handle files
class FileIO:

   def __init__(self, printOutput):
      self.printOutput = printOutput

   #--------------------------------------------------------------------------------------------------
   def print_output(self, outputMessage):
      if self.printOutput:
         print outputMessage

   #--------------------------------------------------------------------------------------------------
   def read_file(self,fileName):
      self.print_output("***** Reading Input File: " + fileName + " *****")
      file = open(fileName,'r')
      data = file.read()
      file.close()
      return data

   #--------------------------------------------------------------------------------------------------
   def write_file(self,fileName,data):
      self.print_output("***** Writing Output File: " + fileName + " *****")
      file = open(fileName,'w')
      file.write(data)
      file.close()

   #--------------------------------------------------------------------------------------------------
   def read_data_file(self,fileName,method=0):

      #fileSizeMb = os.stat(fileName).st_size/(1024.0*1024.0)

      file = open(fileName,'r')
      if (method == 1):
         self.print_output("***** Reading Input File: " + fileName + " *****")
         data = file.readlines()
         newData = []
         for line in data:
            if not line.strip():
               continue
            else:
               newData.append(line)
         data = newData
      else:
         self.print_output("***** Reading Input File: " + fileName + " *****")
         data = file.read()
      file.close()
      return data

   #--------------------------------------------------------------------------------------------------
   def read_csv_data_file(self,fileName):
      dataFile = self.read_data_file(fileName,1)
      data_L = []
      for i in range(len(dataFile)):
         data = dataFile[i].split(',')
         data_L.append(data)
      return data_L

   #--------------------------------------------------------------------------------------------------
   def write_data_file(self,fileName,data,append=0):
      if (append == 1):
         self.print_output("***** Writing Output File (Append): " + fileName + " *****")
         file = open(fileName,'a')
      else:
         self.print_output("***** Writing Output File (Overwrite): " + fileName + " *****")
         file = open(fileName,'w')
      file.write(data)
      file.close()

   #--------------------------------------------------------------------------------------------------
   def check_data_file_present(self,fileName,maxWaitingTime=0):
      fileExist = True
      waitingTime = 0
      self.print_output("***** Checking if file exist: " + fileName + " *****")
      while not os.path.isfile(fileName):
         if waitingTime > maxWaitingTime:
            self.print_output("***** File: " + fileName + " does not exist *****")
            fileExist = False
            break
         else:
            self.print_output("***** Waiting for file: " + fileName + " *****")
            time.sleep(1)
            waitingTime += 1  # wait for 5 secs & check again
      return fileExist

   #--------------------------------------------------------------------------------------------------
   def delete_file(self,fileName,windows=1):
      if self.check_data_file_present(fileName):
         if (windows == 1):
            os.system('del ' + fileName)
         else:
            os.system('rm -f ' + fileName)
         self.print_output("***** File: " + fileName + " deleted *****")

   #--------------------------------------------------------------------------------------------------
   def split_fileName(self,fileName):
      fileSplit = fileName.split('.')
      filePre = fileSplit[0]
      # If filename contains more than one dots
      if len(fileSplit) > 2:
         for i in range(len(fileSplit)-2):
            filePre += "."
            filePre += fileSplit[i+1]
      filePost = fileSplit[-1]
      return filePre, filePost

   #--------------------------------------------------------------------------------------------------
   def write_data_list_to_text_file(self,fileName,data_L):
      # Here data is in the form of a list-of-list
      # [['1','2','3'],['s','p','gurav']]
      output_S = ""
      for i in range(len(data_L)):
         data = data_L[i]
         for j in range(len(data)):
            output_S += "{:30}".format(data[j])
         output_S += "\n"
      self.write_file(fileName,output_S)

   #--------------------------------------------------------------------------------------------------
   def write_solution_array_to_text_file(self,fileName,data_A):
      # Here data is in the form of an array
      # ([0.1 1.2 0.9])
      output_S = ""
      for i in range(len(data_A)):
         output_S += "{:10}".format("X"+str(i+1)+" = "+str(data_A[i]))
         output_S += "\n"
      self.write_file(fileName,output_S)

   #--------------------------------------------------------------------------------------------------
   # Create directory if it does not exist
   def check_and_create_directory(self,directoryName):

      # Check if output directory exists & if it does not then create
      if not os.path.isdir(directoryName):
         try:
            os.makedirs(directoryName)
         except OSError:
            print "***** Problem creating directory: {} *****\n".format(directoryName)
         else:
            self.print_output("***** Creating directory: {} *****\n".format(directoryName))

   #--------------------------------------------------------------------------------------------------
   # Get list of directories present at the given path (directory)
   def get_directory_list(self,directoryName):

      # Set backslash at the end of directory path
      if not directoryName[-1] == "\\":
         directoryName += "\\"

      file_L = []
      directory_L = []
      item_L = os.listdir(directoryName)     # Get list of all files and folders in the given directory

      # Separate directories from files in this directory
      for item in item_L:
         if os.path.isdir(directoryName + item):
            directory_L.append(item)
         else:
            file_L.append(item)

      return [directory_L, file_L]

   #--------------------------------------------------------------------------------------------------
   # Add directory path to file names
   def add_path_to_filename(self,fileNames_L,directoryName):

      if not directoryName[-1] == "\\":
         directoryName += "\\"

      for i in range(len(fileNames_L)):
         # Check if file name is provided with full path of directory, then add path of the given folder to it
         if not ("\\" in fileNames_L[i]):
            fileNames_L[i] = directoryName + fileNames_L[i]

      return fileNames_L

   #--------------------------------------------------------------------------------------------------
   # Add directory path to file names
   def filter_file_list(self,fileNames_L,extension,suffix):

      newFileNames_L = []

      for f in fileNames_L:

         filePre, filePost = self.split_fileName(f)

         if (suffix in filePre) and (extension == filePost):
            newFileNames_L.append(f)

      return newFileNames_L

   #--------------------------------------------------------------------------------------------------
   # Add directory path to file names
   def calculate_clock_time(self,secs):

      totalTime_S = ""
      mins = 0
      hrs = 0

      if 60.0 < secs < (60.0*60.0):  # One minute to one hour
         mins = int(secs/60.0)
         secs -= mins * 60.0
      elif (60.0*60.0) < secs:    # More than one hour
         hrs = int(secs/(60.0*60.0))
         secs -= hrs * (60.0*60.0)
         mins = int(secs/60.0)
         secs -= mins * 60.0

      return [hrs, mins, int(secs)]

#-------------------------------------------------------------------------------------------------------
class SmallUtils:

   def split_string_based_on_no_chars(self,inputData_S,noChars):
      outputData_L = []
      for i in range(0,len(inputData_S),noChars):
         outputData_L.append(inputData_S[i:i+noChars])
      return outputData_L

#-------------------------------------------------------------------------------------------------------
# Handle for text file operations using FileIO class
FH = FileIO(False)

# Handle for small utilities using SmallUtils class
UTH = SmallUtils()

#-------------------------------------------------------------------------------------------------------
