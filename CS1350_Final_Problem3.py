def safe_get_element(my_list, index, default_value=None):
    """
    Safely get an element from a list at the given index.
    Returns default_value if any error occurs.
    """
    try:
        return my_list[index]
    except IndexError:
        return default_value
    except TypeError:
        return default_value
    except Exception:
        return default_value

