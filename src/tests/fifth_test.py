import pytest

@pytest.fixture
def user_input():
    return "ram"

def test_my_page(user_input):
    print("user is:", user_input)
    assert user_input == "ram"
    