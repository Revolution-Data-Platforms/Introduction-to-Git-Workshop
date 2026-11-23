# Presenter Guide: Introduction to Git Workshop

This guide supports the full workshop format for Revolution Data Platforms (RDP), a hands-on session of about 3 hours, run remotely on Microsoft Teams. Every command below matches `docs/tutorial.md`, so attendees who follow the tutorial see the same commands in the same order.

The deck includes spaced retrieval checkpoints: 13 quick-fire "Rewind" questions and 3 "Draw it" pair exercises. The question pack is in [quiz-questions.md](quiz-questions.md).

## 1. Format at a glance

| Format | Length | Deck | Attendee activity | Presenter activity |
| --- | --- | --- | --- | --- |
| Full workshop: hands-on, remote | About 3 hours | `presentation/introduction-to-git-workshop.pptx` and `presentation/introduction-to-git-workshop.pdf` (51 slides) | Follow `docs/tutorial.md` on their own machine, answer the Rewind questions and draw in pairs. | Walk the rooms, troubleshoot, run the checkpoints. |

Deck file paths are relative to the repository root. The deck ships as a PowerPoint file and a PDF.

## 2. Before the session checklist

Presenter setup:

- [ ] Latest Git installed. Run `git --version`. It must be 2.28 or newer.
- [ ] Signed in to GitHub in the browser, under the presenter account.
- [ ] An empty GitHub repository named `git-workshop-demo` under the presenter account, for your own demonstration. No README, no `.gitignore`, no licence. An empty repository means the first push has nothing to clash with.
- [ ] Terminal font size large, light theme. Attendees must read the shared screen.
- [ ] Python 3 installed. Run `python --version`. On macOS or Linux use `python3 --version`. On Windows use `py --version`.
- [ ] The deck open and ready to present.
- [ ] Tutorial link ready to share. See guide Section 7 (Links).
- [ ] Workshop repository link ready to share. See guide Section 7 (Links).
- [ ] The tutorial Section 8 refactored code ready in a scratch file, so you can paste it if you show that step.
- [ ] Run `git config --global --list` and note your real name and email first, so you can restore them after your demonstration.
- [ ] To show the sign-in during your demonstration, delete the `git:https://github.com` entry in Windows Credential Manager beforehand. If you have signed in on this machine before, nothing appears.

Checkpoint setup:

- [ ] **Mentimeter account.** Create a free account at mentimeter.com. The free plan allows 50 participants per month across all presentations, so check its current limits before the session.
- [ ] **Build the quiz.** Create one Mentimeter presentation with 13 Quiz competition questions, in launch order, from [quiz-questions.md](quiz-questions.md). One presentation gives one leaderboard for the whole day.
- [ ] **Rehearse alone.** Run through the quiz yourself on one device. Every participant counts toward the monthly 50, so do not rehearse with colleagues.
- [ ] **Join code.** In PowerPoint, replace `[join code]` on the 13 Rewind slides with the real code (Find and Replace). The PDF keeps the placeholder.
- [ ] **Share the right tab.** Attendees answer at menti.com while you share the Mentimeter browser tab in Teams. Keep it open in its own tab or window.
- [ ] **Teams Polls backup.** In the Teams meeting, create the same 13 questions under Polls using the Multiple Choice Quiz type. This type has no scoring, so say the answer aloud.
- [ ] **Breakout rooms.** About 30 people means about 15 pairs. Set up the rooms in the Teams meeting, and ask a co-organizer to help visit rooms if one is available.
- [ ] **Whiteboard.** The drawings use the Microsoft Whiteboard that comes with the Teams enterprise licence. In each room, one person selects Share, then Whiteboard, then starts a new whiteboard. Test this in a breakout room with a second person before the session. If Whiteboard does not appear for attendees, they draw on paper and show it to the camera.

Ask attendees beforehand:

- [ ] Install Git from git-scm.com and confirm `git --version` shows 2.28 or newer.
- [ ] Install Python 3 and confirm `python --version`.
- [ ] Create a GitHub account.
- [ ] Windows attendees can use PowerShell or Git Bash. Both work with Git for Windows.
- [ ] Have a phone or second device ready for the quiz, because the screen is full of terminal and tutorial windows.
- [ ] Attendees can pair up for the Section 11 review step. Pairs for the drawings are assigned by the breakout rooms.

## 3. Full workshop timing by part

The times below assume every checkpoint runs, and total about 3 hours 10 minutes. A Rewind takes about 1 minute. A drawing takes 6 to 8 minutes: 3 or 4 minutes of drawing, then one or two pairs share their screen, then the model answer.

| Part | Time | Slides | Focus |
| --- | --- | --- | --- |
| 1 | 0:00 to 0:50 | 3 to 17 | Before you start, the workshop repository and the materials, then Git on your computer: identity, repository, staging, first commit and Conventional Commits. Rewinds 1 to 4 run after the Section 2, Section 3, Section 4 and Conventional Commits slides, so each question is about the section before. Slides 4 and 5 take about three minutes together. |
| 2 | 0:50 to 1:35 | 18 to 25 | Draw it: Part 1 (slides 19 and 20), then the empty repository with Rewind 5 (slide 22), signing in, and link and push with Rewind 6 (slide 25). |
| Break | 1:35 to 1:45 | none | Ten minute break. Show the Mentimeter leaderboard. |
| 3 | 1:45 to 3:00 | 26 to 42 | Draw it: Part 2 (slides 27 and 28), then branches and pull requests, with Rewinds 7 to 12 each after the first slide of the following section. |
| Wrap | 3:00 to 3:10 | 43 to 51 | Draw it: Part 3 (slides 43 to 45), a quick skim of troubleshooting (slide 46), Rewind 13 (slide 47), then the recap and questions. Undo commands and the fork route (slides 48 and 49) are optional. |

To finish in 3 hours, use these in order until it fits:

1. Skip the optional slides 48 and 49.
2. Run the odd-numbered Rewinds only (1, 3, 5, 7, 9, 11 and 13). This saves about 6 minutes. Skip the even-numbered Rewind slides.
3. Shorten the break to 5 minutes.

Keep all three drawings. There is no separate recap discussion, because the Rewinds and drawings already provide the retrieval practice.

The full deck runs to 51 slides in this order:

| Slide | Title | Slide | Title |
| --- | --- | --- | --- |
| 1 | Cover | 27 | Draw it: Part 2 |
| 2 | Session plan | 28 | Model answer: Part 2 |
| 3 | Before you start | 29 | Branches and merging |
| 4 | The workshop repository | 30 | Section 7: Creating a branch |
| 5 | How to use the materials | 31 | Rewind 7 (Section 6) |
| 6 | Part 1 divider | 32 | Section 8: Changing and committing |
| 7 | What Git does | 33 | Rewind 8 (Section 7) |
| 8 | The three areas | 34 | Section 9: Pushing the branch |
| 9 | Section 1: Your Git identity | 35 | Rewind 9 (Section 8) |
| 10 | Section 2: Creating a repository | 36 | The pull request flow |
| 11 | Rewind 1 (Section 1) | 37 | Section 10: Opening a pull request |
| 12 | Section 3: Staging files | 38 | Rewind 10 (Section 9) |
| 13 | Rewind 2 (Section 2) | 39 | Section 11: Reviewing and merging |
| 14 | Section 4: Your first commit | 40 | Rewind 11 (Section 10) |
| 15 | Rewind 3 (Section 3) | 41 | Section 12: Cleaning up |
| 16 | Conventional Commits | 42 | Rewind 12 (Section 11) |
| 17 | Rewind 4 (Section 4) | 43 | Draw it: Part 3 |
| 18 | Part 2 divider | 44 | Model answer: fast-forward and merge commit |
| 19 | Draw it: Part 1 | 45 | Model answer: squash merge |
| 20 | Model answer: Part 1 | 46 | Troubleshooting |
| 21 | Section 5: An empty GitHub repository | 47 | Rewind 13 (Section 12) |
| 22 | Rewind 5 (Conventional Commits) | 48 | Optional: Undo commands |
| 23 | Signing in to GitHub | 49 | Optional: contributing through a fork |
| 24 | Section 6: Linking and pushing | 50 | Recap and check-in |
| 25 | Rewind 6 (Section 5) | 51 | Questions |
| 26 | Part 3 divider |  |  |

Checkpoint facilitation:

- **Rewind.** Each Rewind appears after the first slide of the next section, so attendees are already working on something new when it asks about the section before. It is delayed retrieval practice and never a check on what you just taught. Open the matching Mentimeter question, allow 45 to 60 seconds, show the result and say the answer in one sentence. The answer and the misconception it targets are in the speaker notes and in [quiz-questions.md](quiz-questions.md). The slide shows no answer.
- **Draw it.** Send pairs to breakout rooms for the time box on the slide. Bring everyone back, ask one or two pairs to share their screen and explain, then show the model answer on the next slide. Rewind 13 comes after the Part 3 drawing and the troubleshooting slide, and asks again why `git branch -d` warns after a squash merge. Treat it as a quick confirmation.
- **Leaderboard.** Show the Mentimeter leaderboard at the break and at the end.
- **Platform notes.** The Mentimeter free plan and Teams Polls are the only quiz tools. Whiteboard and paper are the only drawing tools.

Facilitation tips:

- Slides 4 and 5, "The workshop repository" and "How to use the materials", take about three minutes together at the start of Part 1. Say that the workshop repository holds the learning materials, and that attendees read them on GitHub or download them. Ask everyone to open the tutorial in the browser now, next to their terminal, and to confirm that they will work in a new folder of their own called `git-workshop-demo`, created in Section 2, plus an empty GitHub repository of their own, created in Section 5. Say clearly that the main-route exercises do not run inside a clone of the workshop repository. The only time attendees clone the workshop repository is for the optional fork appendix, which uses `main.py` and `examples/main_updated.py`.
- Conventional Commits. Slide 17 shows the pattern `type(scope): description`, where the type says what kind of change it is, the optional scope says which part of the code it touches and the description says what the change does. The scope is optional, so `feat: add basic calculator` is a complete and valid message. The description is required. Say that the tutorial has a full table of types and that teams can agree on their own set. Add the length guideline: aim for 50 characters or fewer in the first line, and never more than 72, because GitHub cuts off longer first lines. The examples panel on that slide shows real messages from this repository, such as `docs(workshop): support PowerShell as well as Git Bash`, and attendees can see the whole history with `git log --oneline` after cloning the workshop repository.
- Signing in is the slow part. Walk the room during Part 2. Watch for browsers showing a password prompt. GitHub stopped accepting account passwords for Git operations on 13 August 2021.
- `master` versus `main`. Some attendees see `master` because Git is older than 2.28 or `init.defaultBranch` is not set. The fix is `git branch -M main`.
- PowerShell versus Git Bash. `ls -la` fails in PowerShell because `ls` is an alias for `Get-ChildItem`. Use `Get-ChildItem -Force`, or run the command in Git Bash. The tutorial shows a **Git Bash, macOS or Linux** block and a **Windows PowerShell** block wherever the commands differ, and everything else works in either shell.
- Pushing to the wrong remote. Check `git remote -v`. If `origin` already exists, change the URL with `git remote set-url origin <url>`.
- Rejected push because the repository was created with a README. GitHub then has a commit the attendee does not have. Run `git pull --rebase origin main`, then `git push -u origin main`.

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
