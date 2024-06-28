from src.decorators import log


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(3, 3)
    captured = capsys.readouterr()
    assert captured.out == "6\n"


def test_log_type_error(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function("3", 3)
    captured = capsys.readouterr()
    assert captured.out == "<class 'TypeError'>: can only concatenate str (not \"int\") to str\n"


def test_log_with_filename(capsys):
    @log(filename="file_for_test_decorators")
    def my_function(x, y):
        return x + y

    my_function(4, 4)
    captured = capsys.readouterr()
    assert captured.out == "8\n"


def test_log_with_filename_type_error(capsys):
    @log(filename="file_for_test_decorators")
    def my_function(x, y):
        return x + y

    my_function("4", 4)
    captured = capsys.readouterr()
    assert captured.out == ""
