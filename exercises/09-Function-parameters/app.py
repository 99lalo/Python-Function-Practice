# Your code goes here:
def render_person(name, date, color, age, gender):
    person = (name + " is a " + str(age) + " years old " + gender + " born in " + date + " with " + color + " eyes")
    return person

# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))