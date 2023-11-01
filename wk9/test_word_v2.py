from wordcount_v1 import f1,f2

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

@pytest.mark.parametrize('input',['dadf', {}])
def test_f2(input):
    lst = f2(input)
    assert isinstance(lst, list)

