"""Validation, subtotal and rounding of the quote (R2, R3, R7)."""

from decimal import Decimal, ROUND_HALF_UP

from catalog import normalize, plan_price, extra_price, is_premium_extra

INVALID = -1


def is_valid_selection(plan, extras, members):
    """Return True if plan, extras and members are a valid selection (R1, R2, R3)."""
    if plan_price(plan) is None or extras is None:
        return False
    if isinstance(members, bool) or not isinstance(members, int) or members < 1:
        return False
    names = []
    for extra in extras:
        if extra_price(extra) is None:
            return False
        names.append(normalize(extra))
    if len(set(names)) != len(names):
        return False
    if normalize(plan) != "PREMIUM" and any(is_premium_extra(n) for n in names):
        return False
    return True


def subtotal(plan, extras, members):
    """R3: (plan price + price of the extras) x members."""
    if not is_valid_selection(plan, extras, members):
        raise ValueError("Invalid selection")
    unit_price = plan_price(plan) + sum(extra_price(e) for e in extras)
    return unit_price * members

def group_discount(amount, members):
    """R4: Apply a 10% discount for 2 or more members."""
    if members >= 2:
        return amount * 0.90
    return amount


def special_offer(amount):
    """R5: Apply one special offer based on the amount."""
    if amount > 400:
        return amount - 50
    if amount > 200:
        return amount - 20
    return amount


def premium_surcharge(amount, extras):
    """R6: Add 15% if at least one selected extra is premium."""
    if any(is_premium_extra(extra) for extra in extras):
        return amount * 1.15
    return amount

def round_result(total):
    """R7: round half up to a whole number. Only used at the end."""
    return int(Decimal(str(total)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
