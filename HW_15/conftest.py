import pytest

from human import Human


@pytest.fixture()
def create_human():
    return Human("Daisy", 25, "female")


@pytest.fixture()
def create_human_over_age_limit():
    return Human("Daisy", 100, "female")

@pytest.fixture()
def create_dead_human():
    human = Human("Daisy", 100, "female")
    human.grow()
    return human


