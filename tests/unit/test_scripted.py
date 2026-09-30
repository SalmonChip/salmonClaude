import pytest

from salmon_claude.llm.scripted import ScriptedProvider
from salmon_claude.llm.types import LlmResponse


async def test_returns_replies_in_order():
    provider = ScriptedProvider([ LlmResponse(stop_reason="tool_use"), LlmResponse(stop_reason="end_turn")])
    resp1 = await provider.chat([])
    resp2 = await provider.chat([])

    assert resp1.stop_reason == "tool_use"   # 返回的是对象，取 .stop_reason
    assert resp2.stop_reason == "end_turn"

async def test_records_requests():
    provider = ScriptedProvider([LlmResponse(stop_reason="end_turn")])
    await provider.chat([{"role": "user"}])
    assert provider.requests == [[{"role": "user"}]]   # 直接访问属性


async def test_raises_when_exhausted():
    provider = ScriptedProvider([ LlmResponse(stop_reason="tool_use")])
    await provider.chat([])          # 用掉唯一的响应
    with pytest.raises(RuntimeError):  # 和你代码里的 raise 保持一致
        await provider.chat([])
