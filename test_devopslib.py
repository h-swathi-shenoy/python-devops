from devopslib.random_fruit import random_fruits,meal


def test_random_fruits():
    fruit_choice = random_fruits()
    assert fruit_choice in ["moosambi", "orange", "watermelon"]

def test_meal():
    meal_ret = meal("milk")
    assert "milk" in meal_ret
