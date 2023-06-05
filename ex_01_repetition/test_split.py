from app import split_string_into_lines

class TestSplit:
    def test_empty_string(self):
        assert split_string_into_lines("") == [""]

    def test_single_line_string(self):
        assert split_string_into_lines("Hello, world!") == ["Hello, world!"]

    def test_multi_line_string(self):
        assert split_string_into_lines(
            "Hello, world!\nHow are you today?\nIt is a beautiful day!"
        ) == ["Hello, world!", "How are you today?", "It is a beautiful day!"]

    def test_type(self):
        assert type(split_string_into_lines("")) == list
