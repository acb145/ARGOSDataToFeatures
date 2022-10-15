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

#importing necessary packages
import sys, os, arcpy 
