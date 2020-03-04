from argparse import ArgumentParser

def create_parser ():
    parser = ArgumentParser()
    parser.add_argument('path', help='Path to file')
    parser.add_argument('--export', action='store_true')
    return parser
