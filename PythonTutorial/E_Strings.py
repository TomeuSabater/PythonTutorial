'''
Created on 17 oct 2023

CESUR
Python Strings

@author: Tomeu Sabater
'''


#-- STRINGS #########################################################################################

#-- How to  the characters ' and " in strings 
print("#-- Scape symbols in strings")
print("Hello it's a good new")  # You can write ' between "
print('My name starts with "T"') # You can write " between '
print("You can print \"") # You can scape a symbol using \
print("You can scape with the \"\\\" symbol")

#-- Assign String to variable
print("#-- Assign strings to variables")
x_string = str("Hello it's a good new")
print(x_string)
print(type(x_string))

#-- Assign multiple String to variables can be done using ''' or """"
a_longString = str(''' 
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
''')
print(a_longString)

another_longString = str(""" 
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
""")
print(another_longString)

#-- Strings, as many other programming languages, are arrays of characters
mi_nombre = str("Tomeu Sabater") #-- Define and initialize
print(mi_nombre[0])
print(mi_nombre[1])
print(mi_nombre[2])
print(mi_nombre[3])
print(mi_nombre[4])
print(mi_nombre[5])
print(mi_nombre[6])

#-- Looping through string
#-- You can create an automatic loop throug strings
print("#-- String loop")
for letra in mi_nombre:
    print(letra)

#-- String length
print("#-- String length")
print(len(mi_nombre)) #-- Prints the string lenght

length_mi_nombre = int(len(mi_nombre)) #-- Another example of string lenght
print(length_mi_nombre)

#-- Check if a certain phrase or character is present in a string
print("#-- Check for certain phrase or character")
print("Tomeu" in mi_nombre)  #-- Must print True
if "Tomeu" in mi_nombre:
    print("\"Tomeu\" sí está en mi_nombre")

#-- To check if a certain phrase or character is NOT present in a string
print("Juan" in mi_nombre) #-- Must print False
if "Juan" not in mi_nombre:
    print("Juan no está en mi_nombre")


#-- SLICING STRINGS ##################################################################################
print("#-- Slicing Strings")
print(mi_nombre[6:13])  # From position 6 to position 13 (not included) 
mi_nombre_pila = mi_nombre[0:5] # From first position to position 5 (not included) 
mi_nombre_apellido = mi_nombre[6:13] # From position 6 to position 13 (not included)
print("mi nombre es : " + mi_nombre_pila)
print("mi apellido es: " + mi_nombre_apellido)

#-- Slice from start / end
print(mi_nombre[:5]) #-- Slice from start to position 5 (not included) 
print(mi_nombre[6:]) #-- Slice from position 6 the end

#-- You can slice using combinations
print(mi_nombre[len(mi_nombre)-1:]) #-- Slice the last character

#-- MODIFY STRINGS ###################################################################################
print("#-- Modifying Strings")
#-- Uppder and lower case
print(mi_nombre.upper()) #-- This prints the string in upper case
print(mi_nombre.lower()) #-- This prints the string in lower case

MI_NOMBRE_UPPER = str(mi_nombre.upper()) #-- Transform to upper case
mi_nombre_lower = str(mi_nombre.lower()) #-- Transform to lower case
print(MI_NOMBRE_UPPER)
print(mi_nombre_lower)

#-- Remove Whitespaces
mi_nombre_spaces = str("     Tomeu    Sabater     ")
print(mi_nombre_spaces)
mi_nombre_no_spaces = str(mi_nombre_spaces.strip()) #-- Remove whitespace before and/or after the text
print(mi_nombre_no_spaces) #-- Only removes whitespaces before and/or after, not inside the text

#--- Replace 
mi_nombre_oficial = mi_nombre.replace("Tomeu","Bartolomé")
print(mi_nombre)
print(mi_nombre_oficial)

mi_nombre_oficial_no_tildes = mi_nombre_oficial.replace('é','e')
print(mi_nombre) 
print(mi_nombre_oficial) 
print(mi_nombre_oficial_no_tildes) 

#--- Split
mi_nombre_split = mi_nombre.split(" ") #-- Split in two strings, after/before the whitespace
print(mi_nombre_split) 
print(type(mi_nombre_split)) #-- The result is a list of strings

mi_nombre_completo = "Tomeu Sabater Bosch" #-- Split in three strings
mi_nombre_completo_split = mi_nombre_completo.split(" ")
print(mi_nombre_completo_split) 


#--- STRING CONCATENATION  ######################################################################




