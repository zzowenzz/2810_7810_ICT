from wordcount_v1 import f1

import pytest

file_names = [' ', r'.\text.txt','wrong_file']
@pytest.mark.parametrize("file_str",file_names)
def test_f1(file_str):

    try:
        output = f1(file_str)
        flag_right = isinstance(output, dict) or output=='IO_error'
        error = not flag_right
    except:
        error = True

    assert not error



