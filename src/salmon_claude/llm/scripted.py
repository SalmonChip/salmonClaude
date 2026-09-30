from typing import Any

from salmon_claude.llm.types import LlmResponse


class ScriptedProvider:

    def __init__(self, replies: list[LlmResponse]) -> None:
        """预设响应列表，并准备一个空列表记录每次收到的请求。"""
        self.replies = list(replies)  # 复制一份，防止外部那个列表被误改
        self.requests: list[list[dict[str, Any]]] = []  # 记录每次 chat 收到的 messages

    async def chat(self, messages: list[dict[str, Any]]) -> LlmResponse:
        """给模型发一轮消息，返回一次完整响应。"""
        self.requests.append(messages)
        if not self.replies:
            raise RuntimeError ("No replies preloaded!")
        return self.replies.pop(0)
        