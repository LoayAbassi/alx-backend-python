# learning about annotation
annotations are just hints for developers and static analysis tools
they don't enforce types at runtime


1. variables

    x: int = 5
    name: str = "Alice"

2. functions

    def greet(name: str) -> str:
        return f"Hello, {name}"

3. optional : can be type or None

    from typing import Optional
    def greet(name: Optional[str] = None) -> str:
        if name is None:
            return "Hello, stranger"
        else:
            return f"Hello, {name}"

4. union : multiple types

    from typing import Union
    def process_data(data: Union[int, str]) -> None:
        if isinstance(data, int):
            print(f"Data is an integer: {data}")
        elif isinstance(data, str):
            print(f"Data is a string: {data}")

5. literals : specifying needed data

    from typing import Literal
    def handle_status(status: Literal['success', 'failure']) -> None:
        if status == 'success':
            print("Operation was successful.")
        elif status == 'failure':
            print("Operation failed.")
6. Iterable:

An Iterable is any object that you can loop through, like with a for loop. It doesn’t need to support indexing.

    from typing import Iterable
    def process_items(items: Iterable[int]) -> None:
        for item in items:
            print(item)


7. Sequence:

A Sequence is an iterable with a specific order. You can access elements using their index, like a list or tuple.

    from typing import Sequence
    def process_sequence(seq: Sequence[int]) -> None:
        print(seq[0])  # Access by index

### notes

when dealing with callable functions like 8
it's a function that returns a function that returns a value
can be called by functionName(value1)(value2) // for 8.py
