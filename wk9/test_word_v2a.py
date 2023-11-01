from wordcount_v2 import f1,f2
from histogram import f3
import pytest

@pytest.mark.parametrize("file_str",[' ', r'.\text.txt',r'.\test.txt',r'.\test_empty.txt'])
def test_f1(file_str):

    words = f1(file_str)
    assert isinstance(words,dict) or words=='File not found'


@pytest.mark.parametrize('input',['dadf', {}])
def test_f2(input):
    lst = f2(input)
    assert isinstance(lst, list)


@pytest.mark.parametrize("file_str",[' ', r'.\text.txt',r'.\test.txt',r'.\test_empty.txt'])
def test_f3_integration_f1_f2(file_str):
    status = 0
    words = f1(file_str)
    if isinstance(words,dict):
        list = f2(words)
        status = 1
    else:
        status = 2

    if status == 1:
        f3(list)
    assert status in [1,2]











