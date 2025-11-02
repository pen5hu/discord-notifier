from typing import Generic, TypeVar

T = TypeVar("T")  # 成功時の型
E = TypeVar("E")  # 失敗時の型


class Result(Generic[T, E]):
    def __init__(self, ok: bool, value: T | None = None, error: E | None = None):
        self.ok = ok
        self.value = value
        self.error = error

    @staticmethod
    def Ok(value: T) -> "Result[T, E]":
        return Result(True, value=value)

    @staticmethod
    def Err(error: E) -> "Result[T, E]":
        return Result(False, error=error)

    def unwrap(self) -> T:
        if self.ok:
            return self.value  # type: ignore
        raise RuntimeError(f"Called unwrap on Err: {self.error}")

    def __repr__(self):
        return f"Ok({self.value})" if self.ok else f"Err({self.error})"
