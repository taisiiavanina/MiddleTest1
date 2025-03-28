import pytest
from Compare import compare_files

@pytest.fixture
def file_setup(tmpdir):
    # Створюємо тимчасові файли для тестування
    file1 = tmpdir.join("file1.txt")
    file2 = tmpdir.join("file2.txt")
    file1.write("Hello\nWorld\nPython\n")
    file2.write("Hello\nWorld\nTest\n")
    return str(file1), str(file2)

@pytest.mark.parametrize("file1_content, file2_content, expected_same, expected_diff", [
    ("Hello\nWorld\nPython\n", "Hello\nWorld\nTest\n", ["Hello", "World"], ["Python", "Test"]),
    ("One\nTwo\nThree\n", "Two\nThree\nFour\n", ["Two", "Three"], ["One", "Four"]),
    ("A\nB\nC\n", "A\nB\nC\n", ["A", "B", "C"], [])
])
def test_compare_files(file_setup, file1_content, file2_content, expected_same, expected_diff):
    file1, file2 = file_setup
    with open(file1, 'w') as f1, open(file2, 'w') as f2:
        f1.write(file1_content)
        f2.write(file2_content)

    same_lines, diff_lines = compare_files(file1, file2)

    assert same_lines == expected_same
    assert diff_lines == expected_diff
