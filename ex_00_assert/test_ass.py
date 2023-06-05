from app import ass

class TestAssFunction:
    def test_addition_two_arguments(self):
        assert ass(2, 3, operator='+') == 5

    def test_multiplication_two_arguments(self):
        assert ass(2, 3, operator="*") == 6

    def test_exponentiation_two_arguments(self):
        assert ass(2, 3, operator="**") == 8

    def test_addition_multiple_arguments(self):
        assert ass(2, 3, 4, 5,  operator='+') == 50

    def test_multiplication_multiple_arguments(self):
        assert ass(2, 3, 4, 5, operator="*") == 120

    def test_exponentiation_multiple_arguments(self):
        assert ass(2, 3, 4, operator="**") == 4096

    def test_associativity_addition(self):
        assert ass(2, 3, 4) == ass(4, 3, 2)

    def test_associativity_multiplication(self):
        assert ass(2, 3, 4, operator="*") == ass(4, 3, 2, operator="*")

    def test_associativity_exponentiation(self):
        # Test zwróci wynik negatywny.
        assert ass(2, 3, 4, operator="**") == ass(4, 3, 2, operator="**")

    def test_default_operator(self):
        assert ass(2, 3, 4) == ass(2, 3, 4, operator="+")
