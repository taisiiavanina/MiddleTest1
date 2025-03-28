import pytest
from Compare import compare_files

@pytest.fixture
def file_setup(tmpdir):
    # Створення тимчасових файлів для тесту
    file1 = tmpdir.join("file1.txt")
    file2 = tmpdir.join("file2.txt")
    return str(file1), str(file2)

def test_large_files(file_setup):
    file1, file2 = file_setup
    content1 = "\n".join(["Line {}".format(i) for i in range(1000)])
    content2 = "\n".join(["Line {}".format(i) for i in range(500, 1500)])

    with open(file1, 'w') as f1, open(file2, 'w') as f2:
        f1.write(content1)
        f2.write(content2)

    same_lines, diff_lines = compare_files(file1, file2)

    assert len(same_lines) == 500
    assert len(diff_lines) == 1000
