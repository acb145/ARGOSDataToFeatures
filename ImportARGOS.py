##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2022
## Author: Andrew Brantley, acb145@duke.edu (for ENV859)
##---------------------------------------------------------------------
#%% Importing packages and setting input variables
#importing necessary packages
import sys, os, arcpy 

#setting imports variables
# Set input variables (Hard-wired)
inputFile = 'V:/Lessons/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "V:/Lessons/ARGOSTracking/Scratch/ARGOStrack.shp"

#%% Construct a while loop to iterate through all lines in the datafile
# Open the ARGOS data file for reading
inputFileObj = open(inputFile,'r')

# Get the first line of data, so we can use a while loop
lineString = inputFileObj.readline()
while lineString:
    
    # Set code to run only if the line contains the string "Date: "
    if ("Date :" in lineString):
        
        # Parse the line into a list
        lineData = lineString.split()
        
        # Extract attributes from the datum header line
        tagID = lineData[0]
        obsDate = lineData[3]
        obsTime = lineData[4]
        obsLC = lineData[7]
        
        # Extract location info from the next line
        line2String = inputFileObj.readline()
        
        # Parse the line into a list
        line2Data = line2String.split()
        
        # Extract the date we need to variables
        obsLat = line2Data[2]
        obsLon= line2Data[5]
        
        # Print results to see how we're doing
        print (tagID,obsDate,obsTime,obsLC,"Lat:"+obsLat,"Long:"+obsLon)
        
    # Move to the next line so the while loop progresses
    lineString = inputFileObj.readline()
    
#Close the file object
inputFileObj.close()