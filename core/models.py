"""Pydantic data models for the cost simulation app."""
from __future__ import annotations
from decimal import Decimal
from pydantic import BaseModel, Field


class Master(BaseModel):
    """Cost master data and operating parameters."""

    direct_labor_cost: Decimal = Field(ge=0)
    direct_expenses: Decimal = Field(ge=0)
    indirect_cost: Decimal = Field(ge=0)
    depreciation: Decimal = Field(ge=0)
    maintenance_cost: Decimal = Field(ge=0)
    admin_cost: Decimal = Field(ge=0)
    target_profit: Decimal = Field(ge=0)
    variable_cost_per_hour: Decimal = Field(ge=0)
    fixed_cost: Decimal = Field(ge=0)
    annual_operating_days: int = Field(ge=0)
    operating_hours_per_day: Decimal = Field(ge=0)
    equipment_count: int = Field(ge=1)


class Scenario(BaseModel):
    """Scenario parameters that may vary for simulations."""

    availability_rate: Decimal = Field(ge=Decimal("0"), le=Decimal("1"))
    yield_rate: Decimal = Field(ge=Decimal("0"), le=Decimal("1"))


class Result(BaseModel):
    """Computation results."""

    required_rate: Decimal
    break_even_rate: Decimal
    actual_operating_hours: Decimal
