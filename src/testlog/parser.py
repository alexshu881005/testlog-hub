import csv




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


def read_log(path):
    """讀取測試log,回傳(limits, rows)"""
    low_row = None
    high_row = None
    rows = []
    
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            #TODO B
            if row["SN"] == "LowLimit":
                low_row= row
            elif row["SN"] == "HighLimit":
                high_row = row
            else:
                rows.append(row)
            #TODO C:
        limits = {}
        return limits , rows