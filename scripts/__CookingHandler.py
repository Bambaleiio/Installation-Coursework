from typing import Never

class PopQueue:

    def __init__(self, size: int = 2) -> None:
        self.ptr_: int = 0
        self.buf_: list[None] = [None] * size

    def push(self, item):
        temp_ = self.buf_[self.ptr_]
        self.buf_[self.ptr_] = item
        self.ptr_ = self.ptr_+1 if self.ptr_+1 < len(self.buf_) else 0
        return temp_


class _CookingHandler:
    _PopQueue : PopQueue = PopQueue(2)
    _OPs : dict = {}

    @staticmethod
    def set_dict(_dict : dict)-> None:
        _CookingHandler._OPs = _dict

    @staticmethod
    def uncook(op) -> None:
        op.allowCooking = False

    @staticmethod
    def cook(op) -> None:
        op.allowCooking = True

    @staticmethod
    def set_uncook(op_name: str) -> None:
        _CookingHandler._PopQueue.push(op_name)
        active_ops: list[Never] = [
            name
            for name in _CookingHandler._PopQueue.buf_
            if name is not None
        ]

        for name, op in _CookingHandler._OPs.items():
            if name in active_ops:
                _CookingHandler.cook(op)
            else:
                _CookingHandler.uncook(op)