from salmon_claude.llm.types import LlmResponse, ToolCallBlock, UsageStats


def test_usage_stats_total():
    # 断言：UsageStats(10, 20).total() 等于 30
    assert UsageStats(10, 20).total() == 30


def test_tool_calls_not_shared():
    # 造两个 LlmResponse(stop_reason="end_turn")
    # 往第一个的 tool_calls 里 append 一个 ToolCallBlock(...)
    # 断言：第二个的 tool_calls 还是空列表 []
    resp1 = LlmResponse(stop_reason="end_turn")
    resp2 = LlmResponse(stop_reason="end_turn")
    resp1.tool_calls.append(ToolCallBlock(id="123", name="read_file", input={"path": "README.md"}))
    assert resp2.tool_calls == []
