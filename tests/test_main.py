from source.main import wild_braces


def test_there_are_exactly_2_parentheses():
    #arange
    example = "()"

    #act
    expected = True
    result = wild_braces(example)

    #assert
    assert result == expected

def test_there_is_only_1_parenthes():
    #arange
    example = "("

    #act
    expected = False
    result = wild_braces(example)

    #assert
    assert result == expected

def test_there_are_2_pairs_of_parentheses_and_braces():
    #arange
    example = "()[]"

    #act
    expected = True
    result = wild_braces(example)

    #assert
    assert result == expected

def test_there_are_2_pairs_of_parentheses_and_braces():
    #arange
    example = "([])"

    #act
    expected = True
    result = wild_braces(example)

    #assert
    assert result == expected

def test_there_are_2_pairs_of_mixed_parentheses_and_braces():
    #arange
    example = "([)]"

    #act
    expected = True
    result = wild_braces(example)

    #assert
    assert result == expected

def test_one_brace_is_missing():
    #arange
    example = "([)"

    #act
    expected = False
    result = wild_braces(example)

    #assert
    assert result == expected
