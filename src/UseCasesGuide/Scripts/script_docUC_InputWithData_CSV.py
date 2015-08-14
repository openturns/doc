from __future__ import print_function
from openturns import *

# Create a sample to be stored
sample = Normal(5).getSample(100)

# Store it with the separator |
sample.exportToCSVFile("sampleFile.csv", "|")

# BEGIN_TEX
###################
# Case 1 : import a CSV file
###################

# We give in argument of the static method ImportFromCSVFile()
# the absolute adress of the file sampleFile.csv
# for example : /tmp/sampleFile.csv
# if only the name sampleFile.csv is fulfilled,
# OpenTURNS looks for the file in the current directory

# Specify the separator at import time: for example "|"
aSample = NumericalSample.ImportFromCSVFile("sampleFile.csv", "|")

# Or change the separator from its default value ";" to the value "|"
# inside the ResourceMap
ResourceMap.Set("csv-file-separator", "|")

# Then Import with the default separator
aSample = NumericalSample.ImportFromCSVFile("sampleFile.csv")


# To see the warning messages
Log.Show(Log.INFO)

###################
# Case 1 : export to a CSV file
###################

# We give in argument of the dynamic method exportToCSVFile
# the absolute path where the storing file mySampleStoredFile.csv
# will be created
# for example : /tmp/mySampleStoredFile.csv
# if only the name mySampleStoredFile.csv is given
# OpenTURNS creates the file in the current directory
# with the separator declared in the RessourceMap
aSample.exportToCSVFile("mySampleStoredFile.csv")

# Export with a specified separator: for example ":"
aSample.exportToCSVFile("mySampleStoredFile.csv", ":")
# END_TEX
