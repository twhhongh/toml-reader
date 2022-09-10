#!/usr/bin/python3

import argparse
import re

def extract_username(contents:str) -> str:
    pattern = r"\s*username\s*=\s*(?P<username>\S+)"
    username = re.search(pattern, contents)
    if username.group():
        username = username.groupdict()['username']
    return username


def extract_email(contents:str) -> str:
    pattern = r"\s*email\s*=\s*(?P<email>\S+@\S+)"
    email = re.search(pattern, contents)
    if email.group():
        email = email.groupdict()['email']
    return email


def main(args):

    if args.file:
        with open(args.file, 'r') as f:
            contents = f.read()
            username = extract_username(contents)
            email = extract_email(contents)
    else:
        username = args.username
        email = args.email

    print(f"To: \"{username}\" <{email}>")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help="TOML file")
    parser.add_argument('-u', '--username', type=str, help="Username")
    parser.add_argument('-e', '--email', type=str, help="Email")
    args = parser.parse_args()
    if args.file and (args.username or args.email):
        message = "You cannot use -f with either -u or -e"
        raise Exception(message)
    elif not args.file and not (args.username and args.email):
        message = "Both -u or -e should be provided"
        raise Exception(message)
    main(args)
