"""Tests of the gym calculator (R1)."""

from calculator import GymCalculator


def test_valid_basic_plan():
    """R1: the BASIC plan costs 30."""
    assert GymCalculator.get_plan_price("BASIC") == 30


def test_invalid_plan():
    """R1: an unknown plan returns -1."""
    assert GymCalculator.get_plan_price("GOLD") == -1
