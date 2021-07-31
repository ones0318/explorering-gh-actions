import os
import sys


def main():
    print(f'env: {os.environ}')


if __name__ == '__main__':
    print(f'argv: {sys.argv}')
    main()
