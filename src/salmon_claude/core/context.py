from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionContext:
    """一次 run 的工作记忆与状态。"""

    # ↓ 字段声明（8 个）
    run_id: str
    goal: str
    max_steps: int
    messages: list[dict[str, Any]] = field(default_factory=list)
    step: int = 0
    status: str = "running"
    reason: str | None = None
    result: str | None = None
    
    def is_done(self) -> bool:
        """status 不再是 "running" 就说明结束了。"""
        return self.status != "running"

    def mark_success(self, result: str) -> None:
        """标记本次 run 成功，并保存最终结果。"""
        self.status = "success"
        self.result = result

    def mark_failed(self, reason: str) -> None:
        """标记本次 run 失败，并保存失败原因。"""
        self.status = "failed"
        self.reason = reason

