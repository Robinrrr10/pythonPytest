import pytest

class TestUserFlow:
    
    @pytest.mark.homepage
    def test_for_group_example(self):
        print("Test of group")
        
    @pytest.mark.aboutpage
    def test_for_group_example2(self):
        print("Test of group")