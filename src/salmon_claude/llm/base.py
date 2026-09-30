from typing import Any, Protocol

from salmon_claude.llm.types import LlmResponse


class LLMProvider(Protocol):
    """任何模型提供者（假模型 / 真模型）都必须满足的接口。"""

    async def chat(self, messages: list[dict[str, Any]]) -> LlmResponse:
        """给模型发一轮消息，返回一次完整响应。"""
        ...
