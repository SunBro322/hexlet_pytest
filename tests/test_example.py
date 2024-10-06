from hexlet_pytest.example import reverser


def test_reverse():
    assert reverser("Hexlet") == "telxeH"


def test_reverse_for_empty_string():
    assert reverser('') == ''


def test_reverse_with_files():
    files = 'in.txt'
    with open(files, 'r') as f, open('out.txt', 'r+')as a:
        value = f.read()
        a.write(reverser(value))
        a.seek(0)
        read_value = a.read()
        assert read_value == "telxeH"


