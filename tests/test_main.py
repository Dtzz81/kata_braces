from source.main import wild_braces


def test_there_are_exactly_2_parentheses():
    #arange
    string = "()"

    #act
    expected = True
    result = wild_braces()

    #assert
    assert result == expected
