import pytest
from hr import cli

path = 'path/to/file'

@pytest.fixture
def parser():
    return cli.create_parser()


def test_error_without_arguments(parser):
    """
    Throws an error when no arguments are provided
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])


def test_no_error_with_arguments(parser):
    """
    Does not throw an error if argument are provided
    """
    args = parser.parse_args([path])

    assert args.path == path

def test_with_export_flag(parser):
    """
    Export value equals true when --export flag is set
    and flase when it isn't
    """
    args = parser.parse_args(['/some/path'])
    assert args.export == False

    args = parser.parse_args([path, '--export'])
    assert args.export == True
