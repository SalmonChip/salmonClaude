from salmon_claude.core.context import ExecutionContext


def test_messages_not_shared():
    # 造两个 ExecutionContext
    ctx1 = ExecutionContext(run_id="123", goal="你好", max_steps=10)
    ctx2 = ExecutionContext(run_id="456", goal="你好", max_steps=10)
    # 往第一个的 messages 里 append 一个消息
    ctx1.messages.append({"role": "user", "content": "你好"})
    # 断言：第二个的 messages 还是空列表 []
    assert ctx2.messages == []


def test_is_done():
    ctx = ExecutionContext(run_id="123", goal="你好", max_steps=10)
    assert ctx.is_done() is False   
    ctx.mark_success("你好")
    assert ctx.is_done()
    assert ctx.status == "success"
    assert ctx.result == "你好"


def test_mark_success():
    ctx = ExecutionContext(run_id="123", goal="你好", max_steps=10)
    ctx.mark_success("你好")
    assert ctx.status == "success"
    assert ctx.result == "你好"
    assert ctx.is_done() is True


def test_mark_failed():
    ctx = ExecutionContext(run_id="123", goal="你好", max_steps=10)
    ctx.mark_failed("你好")
    assert ctx.status == "failed"
    assert ctx.reason == "你好"
