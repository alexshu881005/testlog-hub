from testlog.parser import is_out_of_spec 

def test_value_within_spec():
    assert is_out_of_spec(3.3,3.2,3.4) is False
    
def test_value_above_high():
    assert is_out_of_spec(3.5,1,3.4) is True
    
def test_empty_value_is_not_judge():
    assert is_out_of_spec("",3.2,3.4) is False

def test_no_low_limit():
    assert is_out_of_spec(100,None,110) is False
    
def test_on_spec():
    assert is_out_of_spec(3.4,3.2,3.4) is False


def test_no_high_limit():
    assert is_out_of_spec(100,99,None) is False