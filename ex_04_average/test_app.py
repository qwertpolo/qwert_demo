from app import average
import pytest


class TestAverage:
    def test_average_int(self):
        assert average([1, 2, 3, 4, 5]) == 3

    def test_average_float(self):
        assert average([1.5, 2.5, 3.5]) == 2.5

    def test_average_single_element(self):
        assert average([5]) == 5

    def test_average_empty_list(self):
        assert average([]) is None

    def test_average_non_list_argument(self):
        with pytest.raises(TypeError):
            average((1, 2, 3))

    def test_average_multiple_arguments(self):
        with pytest.raises(TypeError):
            average([1, 2, 3], [4, 5, 6])

