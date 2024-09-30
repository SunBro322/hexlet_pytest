from hexlet_pytest.example import reverser


def test_reverse():
    assert reverser("Hexlet") == "telxeH"


def test_reverse_for_empty_string():
    assert reverser('') == ''
