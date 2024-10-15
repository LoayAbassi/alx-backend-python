#!/usr/bin/env python3
"""
# The types of the elements of the input are not known
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """_summary_

    Args:
        lst (typing.Sequence[typing.Any]): _description_

    Returns:
        typing.Union[typing.Any, None]: _description_
    """
    if lst:
        return lst[0]
    else:
        return None
