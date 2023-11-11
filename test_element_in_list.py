import pytest
from main import element_in_list as e_i_l

class TestClass:
    def test_empty_list(self):
        assert e_i_l([], 0) == 0

    def test_no_element(self):
        assert e_i_l([2,3,4], 1) == 0

    def test_existing_element(self):
        assert e_i_l([2,3,4], 3) == 1

    def test_first_element(self):
        assert e_i_l([2,3,4], 2) == 1

    def test_last_element(self):
        assert e_i_l([2,3,4], 4) == 1
