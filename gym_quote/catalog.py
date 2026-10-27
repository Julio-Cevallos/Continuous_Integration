"""Catalog of plans and extras of the gym membership (R1, R2)."""

from calculator import GymCalculator

PLANS = GymCalculator.PLAN_PRICES

# name: (price per member, is premium)
EXTRAS = {
    "GROUP_CLASSES": (15, False),
    "PERSONAL_TRAINING": (25, False),
    "SPA": (30, True),
    "SPECIALIZED_PROGRAM": (40, True),
}


def normalize(name):
    """Return the name in uppercase without spaces, or None if it is not text."""
    if not isinstance(name, str):
        return None
    return name.strip().upper()


def plan_price(plan):
    """Return the price of the plan, or None if the plan does not exist."""
    return PLANS.get(normalize(plan))


def extra_price(extra):
    """Return the price of the extra, or None if the extra does not exist."""
    data = EXTRAS.get(normalize(extra))
    return None if data is None else data[0]


def is_premium_extra(extra):
    """Return True if the extra exists and is premium."""
    data = EXTRAS.get(normalize(extra))
    return data is not None and data[1]
