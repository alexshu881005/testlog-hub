def is_out_of_spec(value, low, high):
    """Value 超出[low, high] 回傳True。"""
    #TODO1
    try:
        v = float(value)
    except (ValueError, TypeError):
        return False
    #TODO2
    if low is not None and v < low:
       return True
    #TODO3
    if high is not None and v > high:
       return True
    #TODO4
    return False

print(is_out_of_spec(3.3, 3.2, 3.4))   # 預期 False
print(is_out_of_spec(3.5, 3.2, 3.4))   # 預期 True
print(is_out_of_spec("", 3.2, 3.4))    # 預期 False
print(is_out_of_spec(100, None, 3.4))  # 預期 True