from typing import Literal

def handle_status(status: Literal['success', 'failure']) -> None:
    if status == 'success':
        print("Operation was successful.")
    elif status == 'failure':
        print("Operation failed.")

handle_status('successs')  # Output: Operation was successful.
handle_status('failures')  # Output: Operation failed.
# handle_status('pending')  # This will raise a type error if checked with a type checker.
