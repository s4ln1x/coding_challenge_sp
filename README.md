# coding_challenge_sp
Repository containing the code requested for completing the code challenge for sp

## Problem statement
Using the language of your choice, write code that will use the GitHub API to retrieve a summary of all opened, closed,
and in draft pull requests in the last week for a given repository and send a summary email to a configurable email
address. Choose any public target GitHub repository you like that has had at least 3 pull requests in the last week.
Format the content email as you see fit, with the goal to allow the reader to easily digest the events of the past week.
If sending email is not an option, then please print to console the details of the email you would send (From, To,
Subject, Body).

## Usage

```shell
❯ python3 github_sp.py                                                                                                   
usage: github_sp.py [-h] --github-authentication-token GITHUB_AUTH_TOKEN --github-repository GITHUB_REPOSITORY --github-owner GITHUB_OWNER [--email EMAIL]
github_sp.py: error: the following arguments are required: --github-authentication-token, --github-repository, --github-owner

```