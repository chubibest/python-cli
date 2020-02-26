import pytest
from pgbackup import cli

path = 'path/to/file'

def test_error_without_arguments():
    """
    Throws an error when no arguments are provided
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([])


def test_no_error_with_arguments():
    """
    Does not throw an error if argument are provided
    """
    parser = cli.create_parser()
    args = parser.parse_args([path])

    assert args.path == path

def test_with_export_flag():
    """
    Export value equals true when --export flag is set
    """

    parser = cli.create_parser()
    args = parser.parse_args([path, '--export'])
    assert args.export == true
