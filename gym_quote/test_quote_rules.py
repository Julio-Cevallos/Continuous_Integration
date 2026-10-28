"""Tests of validation, subtotal and rounding (R2, R3, R7)."""

import pytest

from quote_rules import (
    INVALID,
    is_valid_selection,
    subtotal,
    group_discount,
    special_offer,
    premium_surcharge,
    round_result
)

# ---------- R2: validation ----------
def test_premium_extra_with_premium_plan_is_valid():
    """R2: a premium extra is allowed with the PREMIUM plan."""
    assert is_valid_selection("PREMIUM", ["SPA"], 1)


def test_premium_extra_with_basic_plan_is_invalid():
    """R2: a premium extra with BASIC is invalid."""
    assert not is_valid_selection("BASIC", ["SPA"], 1)


def test_premium_extra_with_standard_plan_is_invalid():
    """R2: a premium extra with STANDARD is invalid."""
    assert not is_valid_selection("STANDARD", ["SPECIALIZED_PROGRAM"], 1)


def test_non_premium_extras_work_with_any_plan():
    """R2: non premium extras are allowed with any plan."""
    assert is_valid_selection("BASIC", ["GROUP_CLASSES", "PERSONAL_TRAINING"], 1)


def test_no_extras_is_valid():
    """R2: zero extras is valid."""
    assert is_valid_selection("BASIC", [], 1)


def test_unknown_extra_makes_selection_invalid():
    """R2: an unknown extra is invalid."""
    assert not is_valid_selection("PREMIUM", ["SAUNA"], 1)


def test_unknown_plan_makes_selection_invalid():
    """R1: an unknown plan is invalid."""
    assert not is_valid_selection("GOLD", [], 1)


def test_repeated_extras_are_invalid():
    """Assumption: a repeated extra is invalid."""
    assert not is_valid_selection("PREMIUM", ["SPA", "SPA"], 1)


def test_zero_members_is_invalid():
    """R3: the number of members is at least 1."""
    assert not is_valid_selection("BASIC", [], 0)


def test_negative_members_is_invalid():
    """R3: negative members is invalid."""
    assert not is_valid_selection("BASIC", [], -3)


# ---------- R3: subtotal ----------
def test_subtotal_basic_no_extras_one_member():
    """R3: BASIC, no extras, 1 member."""
    assert subtotal("BASIC", [], 1) == 30


def test_subtotal_standard_with_personal_training():
    """R3: STANDARD with PERSONAL_TRAINING, 1 member."""
    assert subtotal("STANDARD", ["PERSONAL_TRAINING"], 1) == 70


def test_subtotal_multiplies_by_members():
    """R3: the subtotal is multiplied by the members."""
    assert subtotal("BASIC", ["GROUP_CLASSES"], 2) == 90


def test_subtotal_premium_two_extras_two_members():
    """R3: PREMIUM with GROUP_CLASSES and SPA, 2 members."""
    assert subtotal("PREMIUM", ["GROUP_CLASSES", "SPA"], 2) == 230


def test_subtotal_premium_three_extras_four_members():
    """R3: PREMIUM with three extras, 4 members."""
    extras = ["SPA", "SPECIALIZED_PROGRAM", "PERSONAL_TRAINING"]
    assert subtotal("PREMIUM", extras, 4) == 660


def test_subtotal_of_invalid_selection_raises():
    """R3: the subtotal of an invalid selection raises an error."""
    with pytest.raises(ValueError):
        subtotal("BASIC", ["SPA"], 1)


# R4: Group discount
def test_group_discount():
    """R4: Tests the 10% discount for groups of 2 or more members."""
    assert group_discount(100, 1) == 100
    assert group_discount(100, 2) == 90


# R5: Special offer
def test_special_offer():
    """R5: Tests the special offers at different price thresholds."""
    assert special_offer(450) == 400
    assert special_offer(300) == 280
    assert special_offer(200) == 200
    assert special_offer(400) == 380


# R6: Premium surcharge
def test_premium_surcharge():
    """R6: Tests the 15% surcharge for premium extras."""
    assert premium_surcharge(100, []) == 100
    assert premium_surcharge(100, ["SPA"]) == pytest.approx(115)
    assert premium_surcharge(100, ["GROUP_CLASSES"]) == 100


# ---------- R7: rounding ----------
def test_rounds_half_up():
    """R7: 121.5 becomes 122."""
    assert round_result(121.5) == 122


def test_rounds_down_below_half():
    """R7: 121.4 becomes 121."""
    assert round_result(121.4) == 121


def test_rounds_up_above_half():
    """R7: 625.6 becomes 626."""
    assert round_result(625.6) == 626


def test_whole_number_stays_the_same():
    """R7: a whole number does not change."""
    assert round_result(81.0) == 81


def test_invalid_result_is_minus_one():
    """R7: the result of an invalid selection is -1."""
    assert INVALID == -1
