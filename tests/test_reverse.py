from pyhood.reverse import _reverse

def test_reverse_sentence():
    assert _reverse("! dlroW olleH") == "Hello World !"

def test_reverse_empty_string():
    assert _reverse("") == ""

def test_reverse_single_character():
    assert _reverse("a") == "a"

def test_reverse_spaces():
    assert _reverse("hello world") == "dlrow olleh"
