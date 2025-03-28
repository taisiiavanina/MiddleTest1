import pytest
from Compare import read_file

@pytest.fixture
def file_setup(tmpdir):
    file1 = tmpdir.join("file1.txt")
    file1.write("Hello\nWorld\nPython\n")
    return str(file1)

def test_read_file(file_setup):
    file1 = file_setup
    lines = read_file(file1)
    assert "Hello" in lines
    assert "World" in lines
    assert "Python" in lines
    assert len(lines) == 3
