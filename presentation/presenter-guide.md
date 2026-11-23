# Presenter Guide: Introduction to Git Workshop

This guide supports the full workshop format for Revolution Data Platforms (RDP), a hands-on session of 2 to 3 hours. Every command below matches `docs/tutorial.md`, so attendees who follow the tutorial see the same commands in the same order.

## 1. Format at a glance

| Format | Length | Deck | Attendee activity | Presenter activity |
| --- | --- | --- | --- | --- |
| Full workshop: hands-on | 2 to 3 hours | `presentation/introduction-to-git-workshop.pptx` and `presentation/introduction-to-git-workshop.pdf` (31 slides) | Follow `docs/tutorial.md` on their own machine. | Walk the room, troubleshoot, run the check-in assessment. |

Deck file paths are relative to the repository root. The deck ships as a PowerPoint file and a PDF.

## 2. Before the session checklist

Presenter setup:

- [ ] Latest Git installed. Run `git --version`. It must be 2.28 or newer.
- [ ] Signed in to GitHub in the browser, under the presenter account.
- [ ] An empty GitHub repository named `git-workshop-demo` under the presenter account, for your own demonstration. No README, no `.gitignore`, no licence. An empty repository means the first push has nothing to clash with.
- [ ] Terminal font size large, light theme. Attendees must read the screen from the back of the room.
- [ ] Python 3 installed. Run `python --version`. On macOS or Linux use `python3 --version`. On Windows use `py --version`.
- [ ] The deck open and ready to present.
- [ ] Tutorial link ready to share. See guide Section 7 (Links).
- [ ] Workshop repository link ready to share. See guide Section 7 (Links).
- [ ] The tutorial Section 8 refactored code ready in a scratch file, so you can paste it if you show that step.
- [ ] Run `git config --global --list` and note your real name and email first, so you can restore them after your demonstration.
- [ ] To show the sign-in during your demonstration, delete the `git:https://github.com` entry in Windows Credential Manager beforehand. If you have signed in on this machine before, nothing appears.

Ask attendees beforehand:

- [ ] Install Git from git-scm.com and confirm `git --version` shows 2.28 or newer.
- [ ] Install Python 3 and confirm `python --version`.
- [ ] Create a GitHub account.
- [ ] Windows attendees can use PowerShell or Git Bash. Both work with Git for Windows.
- [ ] Attendees can pair up for the Section 11 review step.

## 3. Full workshop timing by part

| Part | Time | Slides | Focus |
| --- | --- | --- | --- |
| 1 | 0:00 to 0:45 | 3 to 13 | Before you start, then the workshop repository and how to use the materials, then Git on your computer: identity, repository, staging, first commit and Conventional Commits. Slides 4 and 5 take about three minutes together. The optional point-out for slide 13 is that the examples panel shows real messages from this repository. |
| 2 | 0:45 to 1:20 | 14 to 17 | Connect to GitHub: empty repository, signing in, link and push. |
| Break | 1:20 to 1:30 | none | Ten minute break. |
| 3 | 1:30 to 2:30 | 18 to 26 | Branches and pull requests: branch, change, commit, push, open, review, merge, clean up. |
| Wrap | 2:30 to 2:45 | 27 to 31 | Troubleshooting, undo commands, fork route, check-in assessment, questions. |

The full deck runs to 31 slides in this order:

| Slide | Title | Slide | Title |
| --- | --- | --- | --- |
| 1 | Cover | 17 | Section 6: Linking and pushing |
| 2 | Session plan | 18 | Part 3 divider |
| 3 | Before you start | 19 | Branches and merging |
| 4 | The workshop repository | 20 | Section 7: Creating a branch |
| 5 | How to use the materials | 21 | Section 8: Changing and committing |
| 6 | Part 1 divider | 22 | Section 9: Pushing the branch |
| 7 | What Git does | 23 | The pull request flow |
| 8 | The three areas | 24 | Section 10: Opening a pull request |
| 9 | Section 1: Your Git identity | 25 | Section 11: Reviewing and merging |
| 10 | Section 2: Creating a repository | 26 | Section 12: Cleaning up |
| 11 | Section 3: Staging files | 27 | Troubleshooting |
| 12 | Section 4: Your first commit | 28 | Undo commands |
| 13 | Conventional Commits | 29 | Optional: contributing through a fork |
| 14 | Part 2 divider | 30 | Recap and check-in |
| 15 | Section 5: An empty GitHub repository | 31 | Questions |
| 16 | Signing in to GitHub | | |

Facilitation tips:

- Slides 4 and 5, "The workshop repository" and "How to use the materials", take about three minutes together at the start of Part 1. Say that the workshop repository holds the learning materials, and that attendees read them on GitHub or download them. Ask everyone to open the tutorial in the browser now, next to their terminal, and to confirm that they will work in a new folder of their own called `git-workshop-demo`, created in Section 2, plus an empty GitHub repository of their own, created in Section 5. Say clearly that the main-route exercises do not run inside a clone of the workshop repository. The only time attendees clone the workshop repository is for the optional fork appendix, which uses `main.py` and `examples/main_updated.py`.
- Conventional Commits. Slide 13 shows the pattern `type(scope): description`, where the type says what kind of change it is, the optional scope says which part of the code it touches and the description says what the change does. The scope is optional, so `feat: add basic calculator` is a complete and valid message. The description is required. Say that the tutorial has a full table of types and that teams can agree on their own set. Add the length guideline: aim for 50 characters or fewer in the first line, and never more than 72, because GitHub cuts off longer first lines. The examples panel on that slide shows real messages from this repository, such as `docs(workshop): support PowerShell as well as Git Bash`, and attendees can see the whole history with `git log --oneline` after cloning the workshop repository.
- Signing in is the slow part. Walk the room during Part 2. Watch for browsers showing a password prompt. GitHub stopped accepting account passwords for Git operations on 13 August 2021.
- `master` versus `main`. Some attendees see `master` because Git is older than 2.28 or `init.defaultBranch` is not set. The fix is `git branch -M main`.
- PowerShell versus Git Bash. `ls -la` fails in PowerShell because `ls` is an alias for `Get-ChildItem`. Use `Get-ChildItem -Force`, or run the command in Git Bash. The tutorial shows a **Git Bash, macOS or Linux** block and a **Windows PowerShell** block wherever the commands differ, and everything else works in either shell.
- Pushing to the wrong remote. Check `git remote -v`. If `origin` already exists, change the URL with `git remote set-url origin <url>`.
- Rejected push because the repository was created with a README. GitHub then has a commit the attendee does not have. Run `git pull --rebase origin main`, then `git push -u origin main`.

Shortening to 2 hours: skip the undo commands slide and the fork route slide. Run the check-in assessment as a discussion rather than a whiteboard exercise. Keep the ten minute break.

## 4. Your demonstration during the workshop

Attendees work in their own `git-workshop-demo` folder and their own empty GitHub repository. You demonstrate the same workflow in your own `git-workshop-demo` folder, so nobody copies your commands into a folder they do not own.

Work through the tutorial sections in order and run the same commands on your screen. Explain each command once, let the room run it, then move on. Do not narrate every keystroke. Keep your demonstration repository visible while you walk the room, so people can look at it when they hit a problem.

## 5. Resetting your demonstration repository

1. Delete the local folder.

**Git Bash, macOS or Linux**

```bash
rm -rf git-workshop-demo
```

**Windows PowerShell**

```powershell
Remove-Item -Recurse -Force git-workshop-demo
```

2. On GitHub, delete the `git-workshop-demo` repository. Open **Settings**, scroll to **Danger Zone**, select **Delete this repository**, then confirm. Create it again with no README, no `.gitignore` and no licence. Use a new name such as `git-workshop-demo-2` if you prefer to skip the deletion.
3. On a shared machine, undo the global config changes. If your demonstration used the values `Demo Presenter` and `demo.presenter@example.com`, put your own values back. Record the previous values first with `git config --global --list` before the session starts. To remove a setting use `git config --global --unset user.name`, `git config --global --unset user.email` or `git config --global --unset init.defaultBranch`. Restore the original values with `git config --global user.name "Original Name"` and `git config --global user.email "original@example.com"` if you noted them.

## 6. Fallback when GitHub or the network fails

Keep your demonstration moving with a local bare repository standing in for GitHub.

```bash
git init --bare ../demo-remote.git
git remote set-url origin ../demo-remote.git
git push -u origin main
```

Use `git remote set-url origin ../demo-remote.git` because `origin` already exists from your demonstration repository (use `git remote add origin ../demo-remote.git` only if no origin exists yet).

Then run the branch, change, commit and push steps as normal, using the same remote path for the branch push. Merge locally with:

```bash
git switch main
git merge feature/refactor-calculator
git log --oneline --graph
git branch -d feature/refactor-calculator
git fetch --prune
```

For the pull request, show the pull request flow diagram slide instead of the GitHub interface. Say that a pull request is the conversation and review step, and that the bare repository stands in for the remote while the network is down. Clean up afterwards.

**Git Bash, macOS or Linux**

```bash
rm -rf ../demo-remote.git
```

**Windows PowerShell**

```powershell
Remove-Item -Recurse -Force ../demo-remote.git
```

## 7. Links

Links are relative to this `presentation/` folder.

- Tutorial: [docs/tutorial.md](../docs/tutorial.md)
- Check-in assessment: [docs/check-in-assessment.md](../docs/check-in-assessment.md)
- Diagrams: [presentation/diagrams/](diagrams/). The `.drawio.svg` files open and edit in [draw.io](https://www.drawio.com).
- README: [README.md](../README.md)
- Workshop repository for attendees to read or download: [github.com/Revolution-Data-Platforms/Introduction-to-Git-Workshop](https://github.com/Revolution-Data-Platforms/Introduction-to-Git-Workshop)
