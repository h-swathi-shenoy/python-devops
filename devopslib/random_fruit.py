from random import choices


def random_fruits():
    fruits = ["moosambi", "orange", "watermelon"]
    return choices(fruits)[0]

def meal(beverage):
    fruit = random_fruits()
    print(f"Your fruit is {fruit}")
    if fruit == 'orange':
        return f"Your meal is a {fruit} and {beverage}"
    else:
        return f"Kitchen closed as {beverage} not available"

