# Your code goes here:
def render_person(name, birthdate, eyecolor, age, gender):
    return str(name) + " is a " + str(age) + " years old " + str(gender) + " born in " + str(birthdate) + " with " + str(eyecolor) + " eyes"


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))