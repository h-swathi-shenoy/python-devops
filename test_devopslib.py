from devopslib.random_fruit import random_fruits


def test_random_fruits():
    fruit_choice = random_fruits()
    assert fruit_choice in ["moosambi", "orange", "watermelon"]
