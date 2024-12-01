# Use the help function to see what each function does.
# Delete this when you are done.


# Define the Vehicle class.
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
# Your code goes here
v = Vehicle()
# printing all the attributes and methods in object v
print(dir(v))
