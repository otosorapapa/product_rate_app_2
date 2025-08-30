"""Cost calculation formulas used in the app.

All functions are pure and operate on :class:`~core.models.Master` and
:class:`~core.models.Scenario` objects using :class:`decimal.Decimal` for
financial accuracy.
"""
from __future__ import annotations
from decimal import Decimal, ROUND_HALF_UP, getcontext
from .models import Master, Scenario, Result

getcontext().prec = 28  # high precision for intermediate calculations
ROUND_TO = Decimal("0.000001")  # six decimal places


def _annual_operating_hours(master: Master) -> Decimal:
    """Return annual operating hours based on master settings."""
    return (
        Decimal(master.annual_operating_days)
        * master.operating_hours_per_day
        * Decimal(master.equipment_count)
    )


def compute_rates(master: Master, scenario: Scenario) -> Result:
    """Compute required rate and break-even rate.

    Parameters
    ----------
    master: Master
        Cost and operating parameters assumed constant for the facility.
    scenario: Scenario
        Utilisation parameters which may vary between simulations.
    """
    annual_hours = _annual_operating_hours(master)
    actual_hours = annual_hours * scenario.availability_rate * scenario.yield_rate
    numerator = (
        master.direct_labor_cost
        + master.direct_expenses
        + master.indirect_cost
        + master.depreciation
        + master.maintenance_cost
        + master.admin_cost
        + master.target_profit
    )
    required_rate = (numerator / actual_hours).quantize(ROUND_TO, rounding=ROUND_HALF_UP)
    break_even_rate = (
        master.variable_cost_per_hour + (master.fixed_cost / actual_hours)
    ).quantize(ROUND_TO, rounding=ROUND_HALF_UP)
    return Result(
        required_rate=required_rate,
        break_even_rate=break_even_rate,
        actual_operating_hours=actual_hours.quantize(ROUND_TO, rounding=ROUND_HALF_UP),
    )
