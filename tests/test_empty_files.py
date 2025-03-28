import pytest
from Compare import compare_files

@pytest.fixture
def file_setup(tmpdir):
    # Створення тимчасових файлів для тесту
    file1 = tmpdir.join("file1.txt")
    file2 = tmpdir.join("file2.txt")
    return str(file1), str(file2)

def test_empty_files(file_setup):
    file1, file2 = file_setup
    with open(file1, 'w') as f1, open(file2, 'w') as f2:
        pass

    same_lines, diff_lines = compare_files(file1, file2)

    assert same_lines == []
    assert diff_lines == []
