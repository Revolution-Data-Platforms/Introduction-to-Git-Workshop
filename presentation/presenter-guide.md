# Presenter Guide: Introduction to Git Workshop

This guide supports both workshop formats for Revolution Data Platforms (RDP). Every command below matches `docs/tutorial.md`, so attendees who follow the tutorial see the same commands in the same order.

## 1. Formats at a glance

| Format | Length | Deck | Attendee activity | Presenter activity |
| --- | --- | --- | --- | --- |
| A. Overview | 45 minutes | `presentation/introduction-to-git-45-min.pptx` and `presentation/introduction-to-git-45-min.pdf` (14 slides) | Watch the demo. Do the full tutorial afterwards. | Explain concepts, then run the live demo. |
| B. Full workshop | 2 to 3 hours | `presentation/introduction-to-git-workshop.pptx` and `presentation/introduction-to-git-workshop.pdf` (28 slides) | Follow `docs/tutorial.md` on their own machine. | Walk the room, troubleshoot, run the check-in assessment. |

Deck file paths are relative to the repository root. Both decks ship as a PowerPoint file and a PDF.

## 2. Before the session checklist

Presenter setup:

- [ ] Latest Git installed. Run `git --version`. It must be 2.28 or newer.
- [ ] Signed in to GitHub in the browser, under the presenter account.
- [ ] An empty GitHub repository named `git-workshop-demo` under the presenter account. No README, no `.gitignore`, no licence. An empty repository means the first push has nothing to clash with.
- [ ] Terminal font size large, light theme. Attendees must read the screen from the back of the room.
- [ ] Python 3 installed. Run `python --version`. On macOS or Linux use `python3 --version`. On Windows use `py --version`.
- [ ] Both decks open and ready to present.
- [ ] Tutorial link ready to share. See guide Section 8 (Links).
- [ ] The tutorial Section 8 refactored code copied to the clipboard or into a scratch file, ready to paste.
- [ ] Run `git config --global --list` and note your real name and email first, so you can restore them after the demo.
- [ ] To show the sign-in during the demo, delete the `git:https://github.com` entry in Windows Credential Manager beforehand. If you have signed in on this machine before, nothing appears.

Ask attendees beforehand:

- [ ] Install Git from git-scm.com and confirm `git --version` shows 2.28 or newer.
- [ ] Install Python 3 and confirm `python --version`.
- [ ] Create a GitHub account.
- [ ] Windows attendees use Git Bash, which is installed with Git for Windows. Commands are written for Git Bash, macOS and Linux.
- [ ] Attendees can pair up for the Section 11 review step.

## 3. Format A: 45-minute timing

| Time | Slides | What to say and do |
| --- | --- | --- |
| 0:00 to 0:15 | 1 to 6 | Slide 2 starts "How Git works" right at 0:00, so run through slides 1 to 6 together. The welcome takes about 3 minutes of this block: name, RDP context, show the session plan, and say attendees will watch the demo now and work through the tutorial later. Then cover what Git does, the three areas, commits and history, branch and merge, using the diagram slides. Talk about the ideas, not the syntax. |
| 0:15 to 0:20 | 7 to 8 | GitHub remotes, signing in, pull request flow. Name the three sign-in options: Git Credential Manager, personal access token, SSH. |
| 0:20 to 0:38 | 9 to 11 | Live demo. Follow Section 4 of this guide, command by command. |
| 0:38 to 0:42 | 12 to 13 | Common problems, then how to do the full workshop. Send the tutorial link. |
| 0:42 to 0:45 | 14 | Questions. Leave the demo repository visible so people can look at it. |

## 4. Live demo script

The demo takes 18 minutes. The blocks below add up to 18. Run the terminal at a readable font size and narrate each command before you press Enter.
### Block A. Set up Git (2 minutes)

```bash
git config --global user.name "Demo Presenter"
git config --global user.email "demo.presenter@example.com"
git config --global init.defaultBranch main
git config --global --list
```
Point out: Git needs to know who you are before it will let you commit. Use the demo values above so your own name and email do not land in the demo commits. `init.defaultBranch` needs Git 2.28 or newer. Without it, many installs, including Git for Windows, still create a branch called `master`.
### Block B. Create the repository (1 minute)

```bash
mkdir git-workshop-demo
cd git-workshop-demo
git init
ls -la
```
Point out: the hidden `.git` folder appeared. It holds the whole history and settings. Delete `.git` and the folder is ordinary again. In PowerShell use `Get-ChildItem -Force` instead of `ls -la`.
### Block C. Create and stage the file (2 minutes)

Create `main.py` in the folder with your editor. Paste the Simple Calculator content from Section 3 of the tutorial.

```bash
git status
git add main.py
git status
```
Point out: the first status shows `main.py` as untracked. The second shows it under changes to be committed. The staging area lets you choose exactly what goes into the next commit.
### Block D. First commit (1 minute)

```bash
git commit -m "Add basic calculator"
git log --oneline
git status
```
Point out: a commit is a snapshot with a message, an author and a date. `git log --oneline` shows a shortened ID. Status says nothing to commit, working tree clean.
### Block E. Link to GitHub and push (3 minutes)

```bash
git remote add origin https://github.com/you/git-workshop-demo.git
git branch -M main
git push -u origin main
git remote -v
git branch -vv
```
Point out: replace the URL with the presenter account URL. `git branch -M main` is safe if the branch is already called `main`. `-u` links the local branch to the remote branch, so later pushes need no arguments.

Signing in: with Git Credential Manager a "Connect to GitHub" dialog appears in the terminal first. The browser opens after you choose **Sign in with your browser**. Switch to the browser tab so the room can see it, then come back to the terminal. If you have signed in on this machine before, nothing appears. To show the sign-in during the demo, delete the `git:https://github.com` entry in Windows Credential Manager beforehand.
### Block F. Branch, change and commit (4 minutes)

```bash
git branch
git switch -c feature/refactor-calculator
git branch
```

Point out: the asterisk marks the current branch. `main` stays as it was while you work on the branch.

Replace the contents of `main.py` with the tutorial Section 8 refactored code.

```bash
python main.py
git status
git diff
git add main.py
git commit -m "Refactor calculator into functions" \
  -m "- Extract addition into add()" \
  -m "- Read numbers from user input" \
  -m "- Show an error for invalid input"
git log --oneline
```
Point out: run the program and enter 5 and 3, then 2.5 and 1.5, then abc to show the error message. Use `py main.py` or `python3 main.py` if `python` is not found. `git diff` shows the change before it is staged. In PowerShell put the whole commit command on one line instead of using `\` at line ends.
### Block G. Push the branch and open the pull request (2 minutes)

```bash
git push -u origin feature/refactor-calculator
git branch -r
```
Point out: a pull request needs the branch to exist on GitHub. GitHub shows a banner offering to open one.

In the browser: open the repository, select **Compare & pull request**, set base to `main` and compare to `feature/refactor-calculator`, add the title and description from Section 10 of the tutorial (title: Refactor calculator with input validation), then select **Create pull request**.

Point out: a pull request proposes merging one branch into another. It gives people a place to review and discuss the change.
### Block H. Review and merge (1 minute)

In the browser: open the **Files changed** tab and read the diff. Use the merge button and confirm the merge.

Point out: you are the author, so you can comment but you cannot approve your own pull request. Name the three merge options: create a merge commit, squash and merge, rebase and merge. Choose **Squash and merge**. Say squash and merge combines the branch commits into one new commit on `main`.
### Block I. Clean up (2 minutes)

```bash
git switch main
git pull
git log --oneline --graph
git branch -d feature/refactor-calculator
git push origin --delete feature/refactor-calculator
git fetch --prune
git branch -a
```
Point out: `main` now has the refactored file. The graph shows history. `git branch -d` removes the local branch. The next command removes the remote branch. `git fetch --prune` tidies up stale remote-tracking branches. After a Squash or Rebase merge, your commits are replaced by new ones on `main`.

Expect this: `git branch -d` prints a warning such as "warning: deleting branch 'feature/refactor-calculator' that has been merged to 'refs/remotes/origin/feature/refactor-calculator', but not yet merged to HEAD". If the remote-tracking branch is already gone, Git refuses instead with "error: the branch 'feature/refactor-calculator' is not fully merged". Both are expected after a squash merge. Confirm the PR shows as merged on GitHub, and if Git refused, use `git branch -D feature/refactor-calculator`.

## 5. Format B: full workshop timing by part

| Part | Time | Slides | Focus |
| --- | --- | --- | --- |
| 1 | 0:00 to 0:45 | 3 to 10 | Before you start, then Git on your computer: identity, repository, staging, first commit. |
| 2 | 0:45 to 1:20 | 11 to 14 | Connect to GitHub: empty repository, signing in, link and push. |
| Break | 1:20 to 1:30 | none | Ten minute break. |
| 3 | 1:30 to 2:30 | 15 to 23 | Branches and pull requests: branch, change, commit, push, open, review, merge, clean up. |
| Wrap | 2:30 to 2:45 | 24 to 28 | Troubleshooting, undo commands, fork route, check-in assessment, questions. |

Facilitation tips:

- Signing in is the slow part. Walk the room during Part 2. Watch for browsers showing a password prompt. GitHub stopped accepting account passwords for Git operations on 13 August 2021.
- `master` versus `main`. Some attendees see `master` because Git is older than 2.28 or `init.defaultBranch` is not set. The fix is `git branch -M main`.
- PowerShell versus Git Bash. `ls -la` fails in PowerShell because `ls` is an alias for `Get-ChildItem`. Use `Get-ChildItem -Force`, or use Git Bash for the whole tutorial.
- Pushing to the wrong remote. Check `git remote -v`. If `origin` already exists, change the URL with `git remote set-url origin <url>`.
- Rejected push because the repository was created with a README. GitHub then has a commit the attendee does not have. Run `git pull --rebase origin main`, then `git push -u origin main`.

Shortening to 2 hours: skip the undo commands slide and the fork route slide. Run the check-in assessment as a discussion rather than a whiteboard exercise. Keep the ten minute break.
## 6. Resetting after the demo

1. Delete the local folder. Run `rm -rf git-workshop-demo` in Git Bash, or `Remove-Item -Recurse -Force git-workshop-demo` in PowerShell.
2. On GitHub, delete the `git-workshop-demo` repository. Open **Settings**, scroll to **Danger Zone**, select **Delete this repository**, then confirm. Create it again with no README, no `.gitignore` and no licence. Use a new name such as `git-workshop-demo-2` if you prefer to skip the deletion.
3. On a shared machine, undo the global config changes. The demo used the demo values `Demo Presenter` and `demo.presenter@example.com`, so put your own values back. Record the previous values first with `git config --global --list` before the demo starts. To remove a setting use `git config --global --unset user.name`, `git config --global --unset user.email` or `git config --global --unset init.defaultBranch`. Restore the original values with `git config --global user.name "Original Name"` and `git config --global user.email "original@example.com"` if you noted them.
## 7. Fallback when GitHub or the network fails

Keep the demo moving with a local bare repository standing in for GitHub.

```bash
git init --bare ../demo-remote.git
git remote set-url origin ../demo-remote.git
git push -u origin main
```

Use `git remote set-url origin ../demo-remote.git` because `origin` already exists from the GitHub block (use `git remote add origin ../demo-remote.git` only if no origin exists yet).

Then run the branch, change, commit and push blocks as normal, using the same remote path for the branch push. Merge locally with:

```bash
git switch main
git merge feature/refactor-calculator
git log --oneline --graph
git branch -d feature/refactor-calculator
git fetch --prune
```

For the pull request, show the pull request flow diagram slide instead of the GitHub interface. Say that a pull request is the conversation and review step, and that the bare repository stands in for the remote while the network is down. Clean up with `rm -rf ../demo-remote.git` afterwards.
## 8. Links

Links are relative to this `presentation/` folder.

- Tutorial: [docs/tutorial.md](../docs/tutorial.md)
- Check-in assessment: [docs/check-in-assessment.md](../docs/check-in-assessment.md)
- Diagrams: [presentation/diagrams/](diagrams/). The `.drawio.svg` files open and edit in [draw.io](https://www.drawio.com).
- README: [README.md](../README.md)
