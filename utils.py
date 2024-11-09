import functools
import builtins


def pretty_print_list_in_func(func):
    """Modifies print() behavior within function to print elements of list on separate lines with index"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_print = builtins.print

        def print_llist(*args, **kwargs) -> None:
            if len(args) == 1 and isinstance(llist := args[0], list):
                row_count = len(llist)
                for idx, row in enumerate(llist):
                    original_print(f"{str(idx).rjust(len(str(row_count)))}: {row}")
            else:
                original_print(*args, **kwargs)

        try:
            builtins.print = print_llist
            return func(*args, **kwargs)
        finally:
            builtins.print = original_print

    return wrapper


def pretty_print_returned_list(func):
    """Prints elements of list returned by function on separate lines with index"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            row_count = len(result)
            for idx, row in enumerate(result):
                print(f"{str(idx).rjust(len(str(row_count)))}: {row}")

        return result

    return wrapper
