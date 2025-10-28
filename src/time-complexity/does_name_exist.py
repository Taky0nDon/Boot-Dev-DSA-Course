def does_name_exist(first_names: list[str], last_name: list[str], full_name: str) -> bool:
    # O(n^2)
    for first_name in first_names:
        for last_name in last_names:
            if f"{first_name} {last_name}" == full_name:
                return True
    return False

