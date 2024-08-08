#!/usr/bin/env python3

import subprocess
import sys

def run(arr):
    result = subprocess.run(arr, capture_output=True, text=True)
    return result.stdout.strip()

def shell(arr):
    return run(['bash'] + arr)

team = shell(['./team', sys.argv[1]])
if not team:
    print('Could not find team', file=sys.stderr)
    exit(1)
title = sys.argv[2]
assignee = shell(['./user', sys.argv[3]])
if not assignee:
    print('Could not find assignee', file=sys.stderr)
    exit(1)
state = shell(['./state', sys.argv[4]])
if not state:
    print('Could not find workflow state', file=sys.stderr)
    exit(1)
project = shell(['./project', sys.argv[5]]) if sys.argv[5] != 'NA' else 'null'
if not project:
    print('Could not find project', file=sys.stderr)
    exit(1)
estimate = sys.argv[6]
labels = ','.join([shell(['./label', l]) for l in sys.argv[7:]])
description = input()

# print(team)
# print(title)
# print(assignee)
# print(state)
# print(project)
# print(estimate)
# print(labels)
# print(description)

arr = [
    "node",
    ".",
    f"createIssue({{teamId: {team}, title: '{title}', assigneeId: {assignee}, stateId: {state}, labelIds: [{labels}], projectId: {project}, estimate: {estimate}, description: '{description}'}})",
    "r"
]
result = subprocess.run(arr, stdout=sys.stdout, stderr=sys.stderr)
exit(result.returncode)

