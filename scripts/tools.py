import json
import os


def main():
    print(f'env: {os.environ}')


if __name__ == '__main__':
    with open('event.json') as event_fd:
        event = json.loads(event_fd.read())
    print(event)
    main()
