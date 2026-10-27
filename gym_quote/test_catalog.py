"""Tests of the catalog (R1, R2)."""

from catalog import plan_price, extra_price, is_premium_extra


def test_plan_prices_match_table():
    """R1: each plan has the price of the table."""
    assert plan_price("BASIC") == 30
    assert plan_price("STANDARD") == 45
    assert plan_price("PREMIUM") == 70


def test_plan_name_ignores_case_and_spaces():
    """R1: the plan name is normalized."""
    assert plan_price("  premium ") == 70


def test_unknown_plan_is_invalid():
    """R1: any other plan is invalid."""
    assert plan_price("GOLD") is None


def test_non_text_plan_is_invalid():
    """R1: a plan that is not text is invalid."""
    assert plan_price(None) is None


def test_extra_prices_match_table():
    """R2: each extra has the price of the table."""
    assert extra_price("GROUP_CLASSES") == 15
    assert extra_price("PERSONAL_TRAINING") == 25
    assert extra_price("SPA") == 30
    assert extra_price("SPECIALIZED_PROGRAM") == 40


def test_premium_flags_match_table():
    """R2: only SPA and SPECIALIZED_PROGRAM are premium."""
    assert not is_premium_extra("GROUP_CLASSES")
    assert not is_premium_extra("PERSONAL_TRAINING")
    assert is_premium_extra("SPA")
    assert is_premium_extra("SPECIALIZED_PROGRAM")


def test_unknown_extra_is_invalid():
    """R2: an unknown extra is invalid."""
    assert extra_price("SAUNA") is None
    assert not is_premium_extra("SAUNA")
