import pytest


class TestHuman:


    @pytest.mark.positive
    def test_increase_age(self, create_human):
        human = create_human
        human.grow()
        actual_age = human.age
        expected_age = 26
        assert actual_age == expected_age, "The human age is not increased."

    @pytest.mark.negative
    def test_increase_age_over_limit(self, create_human_over_age_limit):
        human = create_human_over_age_limit
        human.grow()
        actual_age = human.age
        expected_age = 100
        assert actual_age == expected_age, "The human age exceeds the limit."

    @pytest.mark.negative
    def test_increase_dead_human_age(self, create_dead_human):
        human = create_dead_human
        with pytest.raises(Exception):
            human.grow(), "The age of the dead human is increased."

    @pytest.mark.positive
    def test_change_gender(self, create_human):
        human = create_human
        human.change_gender("male")
        actual_gender = human.gender
        expected_gender = "male"
        assert actual_gender == expected_gender, "The human gender is not changed."

    @pytest.mark.negative
    def test_change_gender_to_invalid(self, create_human):
        human = create_human
        with pytest.raises(Exception):
            human.change_gender("neko-tyan"), "The gender validation is not performed."

    @pytest.mark.negative
    def test_change_dead_human_gender(self, create_dead_human):
        human = create_dead_human
        with pytest.raises(Exception):
            human.change_gender("male"), "The validation of human status is not performed."

    @pytest.mark.negative
    def test_change_gender_to_existed(self, create_human):
        human = create_human
        with pytest.raises(Exception):
            human.change_gender("female"), "Already existing gender can be set."

    @pytest.mark.positive
    def test_get_age(self, create_human):
        human = create_human
        actual_age = human.age
        expected_age = 25
        assert actual_age == expected_age, "Returned age is not equal to human age."

    @pytest.mark.positive
    def test_get_gender(self, create_human):
        human = create_human
        actual_gender = human.gender
        expected_gender = "female"
        assert actual_gender == expected_gender, "Returned gender is not equal to human gender."
