import json
import os
import subprocess


def get_pull_request_sha_range(event):
    base_sha = event['event']['pull_request']['base']['sha']
    subprocess.check_call(['git', 'fetch', 'origin', base_sha])
    this_sha = event['event']['pull_request']['head']['sha']
    subprocess.check_call(['git', 'fetch', 'origin', this_sha])
    return base_sha, this_sha


def get_push_sha_range(event):
    base_sha = event['event']['before']
    subprocess.check_call(['git', 'fetch', 'origin', base_sha])
    this_sha = event['event']['after']
    subprocess.check_call(['git', 'fetch', 'origin', this_sha])
    return base_sha, this_sha


def main(event):
    """
    :param event: github event, https://docs.github.com/en/developers/webhooks-and-events/events/github-event-types
    :return:
    """
    # print(f'env: {os.environ}')
    event_name = event['event_name']
    event_name_to_sha_range = {'pull_request': get_pull_request_sha_range, 'pust': get_push_sha_range}
    if event_name not in event_name_to_sha_range:
        raise ValueError(event_name)
    get_sha_range = event_name_to_sha_range[event_name]
    base_sha, this_sha = get_sha_range(event)
    diff_files = subprocess.check_output(['git', '--no-pager', 'diff', '--name-only', base_sha, this_sha])
    print(diff_files.decode().split())


if __name__ == '__main__':
    with open(os.environ['GITHUB_EVENT_PATH']) as event_fd:
        event = json.loads(event_fd.read())
    print(event)
    main(event)
