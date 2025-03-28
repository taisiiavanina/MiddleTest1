import pytest
from Compare import write_to_file


@pytest.fixture
def file_setup(tmpdir):
    # Створюємо тимчасові файли для тестування
    return tmpdir


def test_write_to_file(file_setup):
    same_lines = ["Hello", "World"]
    diff_lines = ["Python", "Test"]

    write_to_file(file_setup.join("same_test.txt"), same_lines)
    write_to_file(file_setup.join("diff_test.txt"), diff_lines)

    with open(file_setup.join("same_test.txt"), 'r') as f:
        content = f.read()
        assert "Hello" in content
        assert "World" in content

    with open(file_setup.join("diff_test.txt"), 'r') as f:
        content = f.read()
        assert "Python" in content
        assert "Test" in content
