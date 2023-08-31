from github import Github, Auth
from datetime import datetime

import argparse

parser = argparse.ArgumentParser(description='Get a summary of the latest Pull Request into your inbox')

parser.add_argument('--github-authentication-token',
                     dest='github_auth_token',
                     type=str,
                     required=True,
                     help='GitHub authentication token')
parser.add_argument('--github-repository',
                    dest='github_repository',
                    type=str,
                    required=True,
                    help='GitHub repository')
parser.add_argument('--github-owner',
                    dest='github_owner',
                    type=str,
                    required=True,
                    help='GitHub owner')
parser.add_argument('--email',
                    type=str,
                    help='Email address')

args = parser.parse_args()

github_auth = Auth.Token(args.github_auth_token)
github_api = Github(auth=github_auth)
today = datetime.utcnow()

pull_requests_opened = list()
pull_requests_closed = list()
draft_pull_requests = list()

# Then play with your GitHub objects:
for pull in github_api.get_user(args.github_owner).get_repo(args.github_repository).get_pulls(sort='created', direction='desc'):
    time_delta = today - pull.created_at
    if time_delta.days <= 1:
        if pull.draft:
            draft_pull_requests.append(pull)
        elif pull.state == "open":
            pull_requests_opened.append(pull)
        elif pull.state == "close":
            pull_requests_closed.append(pull)
        else:
            print(f"Pull request {pull.html_url} is no needed")

def print_pull_requests(pull_requests: list) -> None:
    """

    :param pull_requests: List of PullRequest objects
    :return: None
    """
    for pr in pull_requests:
        print("-"*80)
        print("|" + f"Title: {pull.title}".center(78) + "|")
        print("|" + f"Url: {pull.html_url}".center(78) + "|")
        print("|" + f"PR creator username: {pull.user.login}".center(78) + "|")
        print("|" + f"PR Date of creation: {pull.created_at}".center(78) + "|")
        print("-"*80)


print('List of open PRs in the last week:')
print_pull_requests(pull_requests_opened)
print('List of close PRs in the last week:')
print_pull_requests(pull_requests_closed)
print('List of draft PRs in the last week:')
print_pull_requests(draft_pull_requests)