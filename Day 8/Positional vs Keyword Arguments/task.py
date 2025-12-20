# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

def greet_with(name, location):
    return f"Hello {name} \nWhat is it like in {location}"

greetings = greet_with(location="England", name="Olumide")
print(greetings)
