from wordcount import f1,f2
from histogram import f3


if __name__ == '__main__':
    file_name = r'.\test.txt'
    word_count = f1(file_name)
    word_count_sort = f2(word_count)
    f3(word_count_sort)
