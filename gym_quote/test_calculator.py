from calculator import GymCalculator

def test_valid_basic_plan():
    assert GymCalculator.get_plan_price("BASIC") == 30

def test_invalid_plan():
    assert GymCalculator.get_plan_price("GOLD") == -1