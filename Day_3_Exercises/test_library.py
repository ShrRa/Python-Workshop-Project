def test_add_book():
    from Library import Library, Book

    author='Arthur C. Doyle'
    title='Sherlock Holmes'
    lib=Library()
    b=lib.add_book(author, title)
    assert b == Book(author, title)

def test_add_duplicate_book():
    from Library import Library, Book
    import pytest

    author='Arthur C. Doyle'
    title='Sherlock Holmes'
    lib=Library()
    lib.add_book(author, title)
    with pytest.raises(KeyError):
        error_expected = lib.add_book(author, title)