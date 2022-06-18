
#from ecommerce.shopping import sales
#from ..customer import contact
#from ecommerce.customer import contact
#import sales
#from sales import calc_shipping, calc_tax


def calc_tax():
    pass


def calc_shipping():
    pass


# calc_shipping()
# calc_tax()

# Importing all objects using * is bad practice because it can overwrite the files own functions with the same name

# Second option is

# sales.calc_shipping()


# When we run app.py  a new folder will appear called __pycache__
# That is the compiled module inside app.py, will result in faster loading of module

print("Module search path")

# Subdirectories
# Ecommerce

# In order to fix issue of unable to find add __init__.py to subdirectory

# A package is holder of 1 or more modules

# Pre fix with eccomerce.sales

# ecommerce.sales.calc_tax()

# Better method is to use from ecommerce.sales import calc_tax()

# calc_tax()

# or

#from ecommerce import sales

# sales.

# If the package has grown to be very big you can create sub packages which is a folder inside a folder that is the package

# MUST CREATE __INIT__ FILE

#from ecommerce.shopping import sales

#!!
# Importing modules from sibling sub packages
# We can use an absolute or relative statement to do so


# contact.contact_customer()

# This is the absolute method


# contact.contact_customer()

# It is best practice to use the absolute method unless it becomes to cluttersome


# ecommerce
# ---shopiing >> sales....calc_shipping()
# ---customer >> contact....customer_contact()


# We can use the dir function to see all the available functions that have already been created and that we may use
# Useful for debudding


# print(dir(sales))
# This will list all attributes and methods in an object inlcuding magic attributes and built functions

# print()
#print("Executing modules as scripts")
