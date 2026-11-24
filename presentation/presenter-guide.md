# Presenter Guide: Introduction to Git Workshop

This guide supports the full workshop format for Revolution Data Platforms (RDP), a hands-on session of 2 to 2.5 hours plus buffer, run remotely on Microsoft Teams. Every command below matches `docs/tutorial.md`, so attendees who follow the tutorial see the same commands in the same order.

The deck includes spaced retrieval checkpoints: 13 quick-fire "Rewind" questions and 3 "Draw it" group drawings on a shared whiteboard, for a small group of about 10 people. The question pack is in [quiz-questions.md](quiz-questions.md).

## 1. Format at a glance

| Format | Length | Deck | Attendee activity | Presenter activity |
| --- | --- | --- | --- | --- |
| Full workshop: hands-on, remote | 2 to 2.5 hours, plus buffer | `presentation/introduction-to-git-workshop.pptx` and `presentation/introduction-to-git-workshop.pdf` (55 slides) | Follow `docs/tutorial.md` on their own machine, answer the Rewind questions and draw on a shared whiteboard. | Demo briefly, then let attendees work. Run the checkpoints. |

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
- [ ] **Check the quiz.** The 13 questions are in the Git Skills Self-Assessment Mentimeter, on slides 7 to 25 after the six survey slides, with text slides and leaderboards between the batches. Open it and check the answers against [quiz-questions.md](quiz-questions.md). One presentation gives one leaderboard for the whole day.
- [ ] **Rehearse alone.** Run through the quiz yourself on one device. Every participant counts toward the monthly 50, so do not rehearse with colleagues.
- [ ] **Join code.** The 13 Rewind slides show the join code 1509 1500. If you rebuild the Mentimeter presentation, its code changes, so update the slides with Find and Replace in PowerPoint.
- [ ] **Share the right tab.** Attendees answer at menti.com while you share the Mentimeter browser tab in Teams. Keep it open in its own tab or window, Run the self-assessment (slides 1 to 6) first, then park on slide 7 until Part 2.
- [ ] **Teams Polls backup.** In the Teams meeting, create the same 13 questions under Polls using the Multiple Choice Quiz type. This type has no scoring, so say the answer aloud.
- [ ] **Whiteboard.** The drawings use the Microsoft Whiteboard that comes with the Teams enterprise licence. Start it in the meeting (Share, then Whiteboard) at the start of Part 2, and label three areas Part 1, Part 2 and Part 3 so each drawing has its own space. Test beforehand with a second person that attendees can edit the board, not just view it. If they cannot edit, ask them what to draw and draw it yourself.

Ask attendees beforehand:

- [ ] Install Git from git-scm.com and confirm `git --version` shows 2.28 or newer.
- [ ] Install Python 3 and confirm `python --version`.
- [ ] Create a GitHub account.
- [ ] Windows attendees can use PowerShell or Git Bash. Both work with Git for Windows.
- [ ] Have a phone or second device ready for the quiz, because the screen is full of terminal and tutorial windows.
- [ ] Attendees can pair up for the Section 11 review step.

## 3. Timing and structure

The workshop is built for 2 to 2.5 hours, and the rest of the time is buffer. The time boxes below are a guide, not a strict schedule: extend a work block when most people are still going. Aim for about 30 minutes of presenting, about 85 minutes of hands-on work and about 30 minutes of checkpoints.

Each part follows the same pattern: a short demo, then a work block where attendees work through the tutorial sections on their own while you watch the Teams chat. The quick-fire questions and the drawing run at the start of the next part and cover the part before it.

| Block | Time box | Slides | What happens |
| --- | --- | --- | --- |
| Self-assessment and warm-up | 7 min | 1 to 2 | Run the Mentimeter self-assessment (its slides 1 to 6) before the course materials. Slide 2 is the warm-up question, the same one as Mentimeter slide 4. |
| Opening | 5 min | 3 to 6 | Session plan, before you start, the workshop repository and how to use the materials. |
| Part 1 demo | 10 min | 7 to 14 | What Git does, the three areas, then a one-minute demo of Sections 1 to 4 and Conventional Commits. |
| Part 1 work | 25 min | 15 | Attendees do Sections 1 to 4. |
| Part 2 checkpoints | 11 min | 16 to 23 | Rewinds 1 to 5 (about 5 min) and Draw it: Part 1 (about 6 min). |
| Part 2 demo | 5 min | 24 to 26 | Section 5, signing in and Section 6. |
| Part 2 work | 25 min | 27 | Attendees do Sections 5 and 6. |
| Part 3 checkpoints | 8 min | 28 to 32 | Rewinds 6 and 7 (about 2 min) and Draw it: Part 2 (about 6 min). |
| Part 3 demo | 8 min | 33 to 40 | Branches and merging, the pull request flow and a short demo of Sections 7 to 12. |
| Part 3 work | 35 min | 41 | Attendees do Sections 7 to 12. |
| Wrap-up checkpoints | 12 min | 42 to 50 | Rewinds 8 to 13 (about 6 min) and Draw it: Part 3 (about 6 min). |
| Close | 5 min | 51, 54, 55 | Troubleshooting, recap and questions. Undo commands and the fork route (slides 52 and 53) are optional. |

The blocks add up to about 2 hours 35 minutes. The tutorial itself is estimated at 2 to 3 hours of hands-on time, and the work blocks give 85 minutes, so expect people to need more time, especially for signing in and Section 8. Use the buffer to extend a work block rather than cutting a checkpoint. Anything unfinished can be completed afterwards with `docs/tutorial.md`.

If you run long, skip the optional slides 52 and 53, keep all three drawings, and trim the Rewinds to the ones that target the strongest misconceptions (3, 5, 8 and 12).

Running a part:

1. Show the demo slides for the part. Demo each section for about a minute and let attendees run it themselves.
2. Show the "Your turn" slide, start a timer and tell attendees to work through the tutorial. Ask them to type each command themselves and copy only fiddly items such as URLs, email addresses and the Section 8 code. Walk the Teams chat and answer questions.
3. At the start of the next part, run the Rewind questions about the part before, then the drawing, then the next demo.

The full deck runs to 55 slides in this order:

| Slide | Title | Slide | Title |
| --- | --- | --- | --- |
| 1 | Cover | 29 | Rewind 6 (Section 5) |
| 2 | Warm-up question | 30 | Rewind 7 (Section 6) |
| 3 | Session plan | 31 | Draw it: Part 2 |
| 4 | Before you start | 32 | Model answer: Part 2 |
| 5 | The workshop repository | 33 | Branches and merging |
| 6 | How to use the materials | 34 | Section 7: Creating a branch |
| 7 | Part 1 divider | 35 | Section 8: Changing and committing |
| 8 | What Git does | 36 | Section 9: Pushing the branch |
| 9 | The three areas | 37 | The pull request flow |
| 10 | Section 1: Your Git identity | 38 | Section 10: Opening a pull request |
| 11 | Section 2: Creating a repository | 39 | Section 11: Reviewing and merging |
| 12 | Section 3: Staging files | 40 | Section 12: Cleaning up |
| 13 | Section 4: Your first commit | 41 | Your turn: Part 3 |
| 14 | Conventional Commits | 42 | Rewind 8 (Section 7) |
| 15 | Your turn: Part 1 | 43 | Rewind 9 (Section 8) |
| 16 | Part 2 divider | 44 | Rewind 10 (Section 9) |
| 17 | Rewind 1 (Section 1) | 45 | Rewind 11 (Section 10) |
| 18 | Rewind 2 (Section 2) | 46 | Rewind 12 (Section 11) |
| 19 | Rewind 3 (Section 3) | 47 | Rewind 13 (Section 12) |
| 20 | Rewind 4 (Section 4) | 48 | Draw it: Part 3 |
| 21 | Rewind 5 (Conventional Commits) | 49 | Model answer: fast-forward and merge commit |
| 22 | Draw it: Part 1 | 50 | Model answer: squash merge |
| 23 | Model answer: Part 1 | 51 | Troubleshooting |
| 24 | Section 5: An empty GitHub repository | 52 | Optional: Undo commands |
| 25 | Signing in to GitHub | 53 | Optional: contributing through a fork |
| 26 | Section 6: Linking and pushing | 54 | Recap and check-in |
| 27 | Your turn: Part 2 | 55 | Questions |
| 28 | Part 3 divider |  |  |

Checkpoint facilitation:

- **Warm-up.** Run the Mentimeter self-assessment (slides 1 to 6) before the course materials. Slide 2 of the deck shows the same question as Mentimeter slide 4, so show it while that question is open. It is not one of the 13 Rewinds.
- **Rewind.** Rewinds run in batches at the start of the next part, so each question covers an earlier part than the one you are about to teach. Run Rewinds 1 to 5 at the start of Part 2, 6 and 7 at the start of Part 3, and 8 to 13 in the wrap-up. This is delayed retrieval practice and never a check on what you just taught. Open the matching Mentimeter question, allow 45 to 60 seconds, show the result and say the answer in one sentence. The answer and the misconception it targets are in the speaker notes and in [quiz-questions.md](quiz-questions.md). The slide shows no answer.
- **Draw it.** Share the Teams whiteboard and give everyone the time box on the slide to add to one drawing. Suggest each person takes one piece, such as one area or one step. Then ask each person to explain their piece, fix anything wrong together, and show the model answer on the next slide. If the group prefers, each person can draw their own version in a separate part of the board and explain it instead. Rewind 13 comes just before the Part 3 drawing and asks why `git branch -d` warns after a squash merge, so use the drawing to show it.
- **Leaderboard.** The Mentimeter has a leaderboard slide after each batch and a final one at the end. Park on the "Back to the workshop" text slide between batches so the next questions are not shown early.

Facilitation tips:

- Slides 5 and 6, "The workshop repository" and "How to use the materials", take about three minutes together at the start of Part 1. Say that the workshop repository holds the learning materials, and that attendees read them on GitHub or download them. Ask everyone to open the tutorial in the browser now, next to their terminal, and to confirm that they will work in a new folder of their own called `git-workshop-demo`, created in Section 2, plus an empty GitHub repository of their own, created in Section 5. Say clearly that the main-route exercises do not run inside a clone of the workshop repository. The only time attendees clone the workshop repository is for the optional fork appendix, which uses `main.py` and `examples/main_updated.py`.
- Conventional Commits. Slide 18 shows the pattern `type(scope): description`, where the type says what kind of change it is, the optional scope says which part of the code it touches and the description says what the change does. The scope is optional, so `feat: add basic calculator` is a complete and valid message. The description is required. Say that the tutorial has a full table of types and that teams can agree on their own set. Add the length guideline: aim for 50 characters or fewer in the first line, and never more than 72, because GitHub cuts off longer first lines. The examples panel on that slide shows real messages from this repository, such as `docs(workshop): support PowerShell as well as Git Bash`, and attendees can see the whole history with `git log --oneline` after cloning the workshop repository.
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
