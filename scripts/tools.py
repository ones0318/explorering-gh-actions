import json
import os
import subprocess


def main(event):
    """
    :param event: github event, https://docs.github.com/en/developers/webhooks-and-events/events/github-event-types
    :return:
    """
    print(f'env: {os.environ}')
    this_event = event['event']
    diff_files = subprocess.check_output(['git', '--no-pager', 'diff', '--name-only', this_event['before'], this_event['after']])
    print(diff_files)


if __name__ == '__main__':
    with open('event.json') as event_fd:
        event = json.loads(event_fd.read())
    print(event)
    main(event)
