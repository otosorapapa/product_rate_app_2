import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from decimal import Decimal
from core.constants import DEFAULT_MASTER, DEFAULT_SCENARIO
from core.formulas import compute_rates


def test_compute_rates_precision():
    result = compute_rates(DEFAULT_MASTER, DEFAULT_SCENARIO)
    assert result.actual_operating_hours == Decimal("13968.000000")
    assert result.required_rate == Decimal("5369.415808")
    assert result.break_even_rate == Decimal("3777.319588")
