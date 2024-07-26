#!/bin/bash

# Exit on any error
set -e
set -x  # Enable debugging output

# Set environment variables
export GITHUB_TOKEN=your_github_token
export GITHUB_REPO=github.com/diegoabeltran16/generative-ai-for-beginners.git
export GITLAB_TOKEN=your_github_token
export GITLAB_REPO=gitlab.com/otros3114624/generative-ai-for-beginners.git

# Configure Git credential helper to store credentials temporarily 
git config --global credential.helper cache

# Print environment variables for debugging
echo "GITHUB_REPO: ${GITHUB_REPO}"
echo "GITLAB_REPO: ${GITLAB_REPO}"

# Verify that environment variables are set
if [ -z "$GITHUB_REPO" ]; then
  echo "Error: GITHUB_REPO is not set"
  exit 1
fi

if [ -z "$GITLAB_REPO" ]; then
  echo "Error: GITLAB_REPO is not set"
  exit 1
fi

# Configure Git
git config --global user.email "diegobeltran1016@gmail.com"
git config --global user.name "Diego Alejandro Beltran"

# Remove remotes if they exist (to ensure clean state)
git remote remove github || true
git remote remove gitlab || true

# Add GitHub as a remote
git remote add github "https://${GITHUB_TOKEN}@${GITHUB_REPO}"
echo "GitHub remote added."

# Add GitLab as a remote
git remote add gitlab "https://${GITLAB_TOKEN}@${GITLAB_REPO}"
echo "GitLab remote added."

# Fetch all branches from both remotes
echo "Fetching branches from GitHub..."
git fetch github || echo "Failed to fetch from GitHub. Check the repository URL and token permissions."
echo "Fetching branches from GitLab..."
git fetch gitlab || echo "Failed to fetch from GitLab. Check the repository URL and token permissions."

# Ensure changes are committed locally
echo "Checking for local changes..."
git status
if ! git diff-index --quiet HEAD --; then
  echo "Staging all changes..."
  git add -A  # Add all changes (tracked, untracked, and deletions)
  echo "Committing local changes..."
  git commit -m "Automated commit by sync script"
fi

# Merge changes from GitHub to GitLab
echo "Merging changes from GitHub to GitLab..."
git checkout main
if git pull github main; then
  echo "Pulled changes from GitHub successfully."
else
  echo "Failed to pull changes from GitHub."
fi
if git push gitlab main; then
  echo "Pushed changes to GitLab successfully."
else
  echo "Failed to push changes to GitLab."
fi

# Merge changes from GitLab to GitHub
echo "Merging changes from GitLab to GitHub..."
if git pull gitlab main; then
  echo "Pulled changes from GitLab successfully."
else
  echo "Failed to pull changes from GitLab."
fi
if git push github main; then
  echo "Pushed changes to GitHub successfully."
else
  echo "Failed to push changes to GitHub."
fi

# Handle conflicts if any
echo "Handling conflicts (if any)..."
if git merge --strategy-option theirs; then
  echo "Merged conflicts using 'theirs' strategy."
else
  echo "No conflicts to merge or merge failed."
fi
if git push github main; then
  echo "Final push to GitHub successful."
else
  echo "Final push to GitHub failed."
fi
if git push gitlab main; then
  echo "Final push to GitLab successful."
else
  echo "Final push to GitLab failed."
fi

echo "Sync process completed."
