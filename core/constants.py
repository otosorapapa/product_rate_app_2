"""Application-wide constants and default assumptions.

All numeric defaults are Fermi estimates for a mid-sized factory in Japan.
Values are documented so that they can be reviewed and adjusted later.
"""
from decimal import Decimal
from .models import Master, Scenario

# Default master data for cost structure (JPY) and operating parameters.
# These numbers assume a plant with 10 machines or personnel.
DEFAULT_MASTER = Master(
    direct_labor_cost=Decimal("30000000"),  # 人件費 (年間)
    direct_expenses=Decimal("10000000"),    # 直接経費 (年間)
    indirect_cost=Decimal("15000000"),      # 間接費配賦 (年間)
    depreciation=Decimal("5000000"),        # 減価償却費 (年間)
    maintenance_cost=Decimal("4000000"),    # 設備維持費 (年間)
    admin_cost=Decimal("6000000"),          # 一般管理費配賦 (年間)
    target_profit=Decimal("5000000"),       # 目標営業利益 (年間)
    variable_cost_per_hour=Decimal("1200"), # 変動費 (円/時)
    fixed_cost=Decimal("36000000"),         # 固定費 (年間)
    annual_operating_days=240,               # 稼働日/年
    operating_hours_per_day=Decimal("8"),   # 稼働時間/日
    equipment_count=10,                     # 稼働設備台数 or 人員
)

# Default scenario parameters for utilisation and quality.
DEFAULT_SCENARIO = Scenario(
    availability_rate=Decimal("0.75"),  # 稼働率
    yield_rate=Decimal("0.97"),         # 良品率
)
