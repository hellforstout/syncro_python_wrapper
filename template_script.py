#Import syncro_python_wrapper for functions. Import requests for functionality
from syncro_python_wrapper import *

##############################################
#
#     Use set_environment_variables.py to set baseurl and bearertoken
#
################################################

############  Script Example starts below ############

#Testing getUsers() class
allusers = getUsers()

#Print users
print(allusers)

#Print subsection of users
print(allusers[2])