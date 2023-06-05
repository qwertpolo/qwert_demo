from app import split_string_into_lines
import pytest


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("", [""]),
        ("Hello, world!", ["Hello, world!"]),
        (
            """Hello, world!\nHow are you today?\nIt is a beautiful day!""",
            ["Hello, world!", "How are you today?", "It is a beautiful day!"],
        ),
    ],
)
class TestSplit:
    def test_value(self, input_string, expected_output):
        assert split_string_into_lines(input_string) == expected_output

    def test_type(self, input_string, expected_output):
        assert type(split_string_into_lines(input_string)) == list
