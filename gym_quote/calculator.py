"""Gym membership price calculator."""

class GymCalculator:  # pylint: disable=too-few-public-methods
    """Calculates the price of a gym membership."""
    PLAN_PRICES = {
        "BASIC": 30,
        "STANDARD": 45,
        "PREMIUM": 70
    }

    @staticmethod
    def get_plan_price(plan_name: str) -> int:
        """Devuelve el precio base del plan o -1 si no es válido (R1)."""
        return GymCalculator.PLAN_PRICES.get(plan_name, -1)
