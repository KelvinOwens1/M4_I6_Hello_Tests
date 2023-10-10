import main


def test_say_hello():
    assert main.say_hello() == "Hello World!"


def test_hey_jamal():
    assert main.hey_you("Jamal") == "Hey, Jamal!"


def test_hey_nate():
    assert main.hey_you("Nate") == "Hey, Nate!"


def test_age_in_2050_born_1990():
    assert main.age_in_2050(1990) == "You are 60 if born in year 2050."
 