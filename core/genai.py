"""Generative AI helpers for summary and explanations.

This module provides light wrappers that call OpenAI's API when available
for summarising input data, generating comments and explaining numerical
analysis results.  If the OpenAI client or API key is not configured, the
functions gracefully fall back to simple template-based messages so that the
rest of the application continues to operate without external dependencies.
"""
from __future__ import annotations

import os
from typing import Optional

from .models import Master, Scenario, Result


def _openai_response(prompt: str) -> Optional[str]:
    """Return a response from OpenAI's chat completions API if possible.

    The function checks for the presence of the ``openai`` package and the
    ``OPENAI_API_KEY`` environment variable.  Any import errors or API
    failures result in ``None`` being returned so callers can provide
    fallbacks.
    """
    try:
        from openai import OpenAI  # type: ignore
    except Exception:
        return None

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    client = OpenAI(api_key=api_key)
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=200,
        )
    except Exception:
        return None

    message = completion.choices[0].message
    return getattr(message, "content", None)


def summarize_inputs(master: Master, scenario: Scenario) -> str:
    """Summarise master and scenario data using a language model."""
    prompt = (
        "以下の製造コストデータを50字程度で要約してください:\n"  # noqa: E501
        f"マスター: {master.model_dump()}\nシナリオ: {scenario.model_dump()}"
    )
    response = _openai_response(prompt)
    if response:
        return response.strip()
    return (
        f"人件費は年{master.direct_labor_cost}円、稼働率は{scenario.availability_rate}、"  # noqa: E501
        f"良品率は{scenario.yield_rate}です。"
    )


def explain_result(result: Result) -> str:
    """Provide an automatic explanation of analysis results."""
    prompt = (
        "必要賃率と損益分岐賃率の結果を業務担当者向けに短く説明してください。\n"  # noqa: E501
        f"結果データ: {result.model_dump()}"
    )
    response = _openai_response(prompt)
    if response:
        return response.strip()
    return (
        f"必要賃率は{result.required_rate}円/時で、損益分岐賃率は"  # noqa: E501
        f"{result.break_even_rate}円/時、実稼働時間は{result.actual_operating_hours}時間です。"  # noqa: E501
    )


def generate_comment(result: Result) -> str:
    """Generate a suggestion or comment based on the result numbers."""
    prompt = (
        "以下の結果に対する改善コメントを日本語で提案してください。\n"  # noqa: E501
        f"結果データ: {result.model_dump()}"
    )
    response = _openai_response(prompt)
    if response:
        return response.strip()
    return "コスト構成を見直し、稼働率や良品率の向上を検討してください。"
