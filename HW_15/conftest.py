import pytest
import random
from homeTask15.human import Human
gender = ["male", "female"]


@pytest.fixture()
def create_human():
    return Human("Alex", 25, random.choice(gender))


@pytest.fixture()
def create_human_over_age_limit():
    return Human("Alex", 100, random.choice(gender))


@pytest.fixture()
def create_dead_human():
    human = Human("Alex", 100, random.choice(gender))
    human.grow()
    return human
