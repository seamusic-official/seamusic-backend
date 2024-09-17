def get_page(start: int, size: int) -> int:
    return start // size if start % size == 0 else start // size + 1


def get_has_previous(start: int, size: int) -> bool:
    return start - size >= 0


def get_has_next(total: int, start: int, size: int) -> bool:
    return start + size < total
