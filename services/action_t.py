from typing import TypedDict


class Action(TypedDict):
    function_name: str
    args: dict[str, any]
