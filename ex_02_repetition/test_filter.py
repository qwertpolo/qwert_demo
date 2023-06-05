from app import filter_lines_starting_with_pipe_space
import pytest


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([], []),
        (["Hello, world!", "How are you today?"], []),
        (
            ["| Hello, world!", "| How are you today?"],
            ["| Hello, world!", "| How are you today?"],
        ),
        (["| Hello, world!", "How are you today?"], ["| Hello, world!"]),
    ],
)
class TestFilter:
    def test_value(self, input_list, expected_output):
        assert filter_lines_starting_with_pipe_space(input_list) == expected_output

    def test_original_list(self, input_list, expected_output):
        original_list = input_list.copy()
        filter_lines_starting_with_pipe_space(input_list)
        assert input_list == original_list
