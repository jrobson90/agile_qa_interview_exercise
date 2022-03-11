from jack_src.main.main import vowel_and_consonant_calculator
import pytest

pytestmark = [pytest.mark.all]


class VowelCalculatorTests:

    @pytest.mark.negative_test
    def test_more_than_four_words_not_accepted(self):
        """This test verifies that no more than four words cen be accepted."""
        actual_result = vowel_and_consonant_calculator("yes, no, maybe, banana, monkey")
        expected_result = None
        assert actual_result == expected_result, f"Actual: {actual_result}, Expected: {expected_result}."

    @pytest.mark.negative_test
    def test_only_digits_not_accepted(self):
        """This test verifies that numbers are not accepted."""
        actual_result = vowel_and_consonant_calculator("1, 2, 3")
        expected_result = []
        assert actual_result == expected_result, f"Actual: {actual_result}, Expected: {expected_result}."

    def test_digits_not_accepted(self):
        """This test verifies that numbers are not accepted, but words are and then calculates the number of vowels
        and consonants."""
        actual_result = vowel_and_consonant_calculator("cat, 2, dog")
        expected_result = [{'word': 'cat', 'vowels': 1, 'consonants': 2}, {'word': 'dog', 'vowels': 1, 'consonants': 2}]
        assert actual_result == expected_result, f"Actual: {actual_result}, Expected: {expected_result}."

    def test_four_words_accepted(self):
        """This test verifies that four words are accepted and then calculates the number of vowels and consonants."""
        actual_result = vowel_and_consonant_calculator("yes, no, maybe, banana")
        expected_result = [{'word': 'yes', 'vowels': 1, 'consonants': 2},
                           {'word': 'no', 'vowels': 1, 'consonants': 1},
                           {'word': 'maybe', 'vowels': 2, 'consonants': 3},
                           {'word': 'banana', 'vowels': 3, 'consonants': 3}]
        assert actual_result == expected_result, f"Actual: {actual_result}, Expected: {expected_result}."

    @pytest.mark.xfail(reason="The test should return an empty list but instead attempts to find the number of vowels "
                              "and consonants in special characters.")
    @pytest.mark.negative_test
    def test_special_characters_not_accepted(self):
        """This test verifies that special characters are not accepted. This test purposely fails and expects the
        function to return nothing, however the function tries to find the vowels and consonants in the special
        characters."""
        actual_result = vowel_and_consonant_calculator("!, ?, %")
        expected_result = []
        assert actual_result == expected_result, f"Actual: {actual_result}, Expected: {expected_result}."
