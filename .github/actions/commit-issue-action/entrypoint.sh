#!/bin/sh

API="https://api.github.com"

create_issue()
{
  urls=""
  for u in $commiturls; do
    urls=$urls'<br />'"$u"
  done
  title="New commit to $INPUT_SOURCEREPO"
  body="There was a new commit/commits to $INPUT_SOURCEREPO, please check the newly updated codebase. Here are the recent commits: $urls"
  labels=$INPUT_ISSUELABELS
  json=$(jq -nc --arg l "$labels" --arg t "$title" --arg b "$body" '$l | split(", ") | {title: $t, body: $b, labels: .}')
  issue=$(curl -sS -X POST "$API/repos/$INPUT_TARGETREPO/issues" -H "authorization: token $GITHUB_TOKEN" -H "Content-Type: application/json" -d "$json")
  created=$?
  if [ $created -ne 0 ]; then
    echo "Error with request: $issue"
    exit $created
  else
    echo "Issue created in $INPUT_TARGETREPO"
    issueURL=$(jq -n "$issue" | jq -r '.html_url')
    return 0
  fi
}

check_commits()
{
  commits=$(curl -sS "$API/repos/$INPUT_SOURCEREPO/commits?since=$(date -u -d '1 hour ago' +"%Y-%m-%dT%H:%M:%SZ")&until=$(date -u +"%Y-%m-%dT%H:%M:%SZ")")
  check=$?
  if [ $check -ne 0 ]; then
    echo "Error with request: $commits"
    exit $check
  fi
  if [ "$(echo $commits)" = "[ ]" ]; then
    return 1
  else
    commiturls=$(jq -n "$commits" | jq -r ".[] | .html_url")
    return 0
  fi
}

main()
{
  echo "Checking for recent commits to $INPUT_SOURCEREPO"
  check_commits
  found=$?
  if [ $found -eq  0 ]; then
    echo "There is a new commit to $INPUT_SOURCEREPO! Creating issue in $INPUT_TARGETREPO."
    create_issue
    result=$?
    if [ $result -eq 0 ]; then
      echo ::set-output name=issue_url::$issueURL
      exit 0
    fi
  else
    echo "No recent commits found. Response code was $found"
    exit 0
  fi
}

#begin here
main
