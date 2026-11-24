# Presenter Guide: Introduction to Git Workshop

This guide supports the full workshop format for Revolution Data Platforms (RDP), a hands-on session paced for about 2.5 hours, including three short breaks, in a 3 hour booking, run remotely on Microsoft Teams. Every command below matches `docs/tutorial.md`, so attendees who follow the tutorial see the same commands in the same order.

The deck includes spaced retrieval checkpoints: 13 "Rewind" questions and 3 "Draw it" group drawings on a shared whiteboard, for a small group of about 10 people. The question pack is in [quiz-questions.md](quiz-questions.md).

## 1. Format at a glance

| Format | Length | Deck | Attendee activity | Presenter activity |
| --- | --- | --- | --- | --- |
| Full workshop: hands-on, remote | About 2.5 hours including three short breaks, in a 3 hour booking | `presentation/introduction-to-git-workshop.pptx` and `presentation/introduction-to-git-workshop.pdf` (59 slides) | Follow `docs/tutorial.md` on their own machine, answer the Rewind questions and draw on a shared whiteboard. | Demo briefly, then let attendees work. Run the checkpoints. |

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
- [ ] To show the sign-in during your demonstration, delete the `git:https://github.com` entry in Windows Credential Manager beforehand. If you have never signed in on this machine, there is no entry to delete.

Checkpoint setup:

- [ ] **Mentimeter account.** Create a free account at mentimeter.com. The free plan allows 50 participants per month across all presentations. Check your account's current limit before the session, because Mentimeter's free plan terms depend on when the account was created.
- [ ] **Check the quiz.** In the Introduction to Git Workshop Mentimeter, slide 1 is the title, the self-assessment is slides 2 to 6, the warm-up question is slide 7, and the 13 Rewind questions are on slides 10 to 26, with text slides and leaderboards between the batches. Add leaderboard is switched on only for the warm-up and questions 5, 7 and 13, which is what creates the leaderboard slides 8, 15, 19 and 27. Leave these switches as they are, because turning one off deletes its leaderboard slide. Open it and check the answers against [quiz-questions.md](quiz-questions.md). One presentation gives one leaderboard for the whole day.
- [ ] **Rehearse alone.** Run through the quiz yourself on one device. Every participant counts toward the monthly 50, so do not rehearse with colleagues.
- [ ] **Join code.** The self-assessment, warm-up and 13 Rewind slides show the join code 1509 1500. Before the session, check the code in Mentimeter's Share panel, and if it has changed, update the slides with Find and Replace in PowerPoint. The QR code opens the presentation's own link, so it does not depend on the code.
- [ ] **Share the right tab.** Attendees answer at menti.com while you share the Mentimeter browser tab in Teams. Keep it open in its own tab or window. Run the self-assessment (Mentimeter slides 2 to 6), the warm-up question (slide 7) and its leaderboard (slide 8), then park on slide 9 until Part 2. During each Rewind batch, keep the Mentimeter tab shared and read the answers from the speaker notes or [quiz-questions.md](quiz-questions.md). Show the deck's Rewind slides only if Mentimeter fails.
- [ ] **Teams Polls backup.** Before the meeting, create the same 13 questions as Multiple Choice Quiz polls in the meeting's Polls tab, so they are ready if Mentimeter fails. This poll type marks correct answers but has no points or leaderboard, so say the answer aloud. If Mentimeter fails at the start, skip the self-assessment and ask the warm-up question aloud.
- [ ] **Whiteboard.** The drawings use Microsoft Whiteboard in the Teams meeting. Check that your Teams licence includes it. Start it in the meeting (Share, then Whiteboard) at the start of Part 2, and label three areas Part 1, Part 2 and Part 3 so each drawing has its own space. Test beforehand with a second person that attendees can edit the board, not just view it. If they cannot edit, ask them what to draw and draw it yourself.

Ask attendees beforehand:

- [ ] Install Git from git-scm.com and confirm `git --version` shows 2.28 or newer.
- [ ] Install Python 3 and confirm `python --version`.
- [ ] Create a GitHub account.
- [ ] Windows attendees can use PowerShell or Git Bash. Both work with Git for Windows.
- [ ] Have a phone or second device ready for the quiz, because the screen is full of terminal and tutorial windows.
- [ ] Attendees can pair up for the Section 11 review step.

## 3. Timing and structure

The workshop is paced for about 2.5 hours, including three short breaks, and the rest of the 3 hour booking is buffer. The time boxes below are a guide, not a strict schedule: extend a work block when most people are still going.

The plan has about 31 minutes of presenting (including the close, which is mostly questions), 70 minutes of hands-on work, 33 minutes of checkpoints, 7 minutes for the self-assessment and 15 minutes of breaks.

Each part follows the same pattern: a short demo, then a work block where attendees work through the tutorial sections on their own while you watch the Teams chat. The Rewind questions and the drawing run at the start of the next part and cover the part before it.

| Block | Starts at | Time box | Slides | What happens |
| --- | --- | --- | --- | --- |
| Opening | 0:00 | 5 min | 1 to 5 | Cover, session plan, before you start, the workshop repository and how to use the materials. |
| Self-assessment and warm-up | 0:05 | 7 min | 6 to 7 | Slide 6 shows the Mentimeter join code and QR code. Run the self-assessment (Mentimeter slides 2 to 6), then the warm-up question on Mentimeter slide 7 with deck slide 7 on screen. |
| Part 1 demo | 0:12 | 8 min | 8 to 15 | What Git does, the three areas, then a one-minute demo of Sections 1 to 4 and Conventional Commits. |
| Part 1 work | 0:20 | 15 min | 16 | Attendees do Sections 1 to 4. |
| Break | 0:35 | 5 min | 17 | Optional. Extend it, shorten it or skip it depending on the time. |
| Part 2 checkpoints | 0:40 | 11 min | 18 to 25 | Rewinds 1 to 5 (about 5 min) and Draw it: Part 1 (about 6 min: 3 to draw, 2 for two or three people to explain, 1 for the model answer). |
| Part 2 demo | 0:51 | 5 min | 26 to 28 | Section 5, signing in and Section 6. |
| Part 2 work | 0:56 | 20 min | 29 | Attendees do Sections 5 and 6. |
| Break | 1:16 | 5 min | 30 | Optional. Extend it to 10 minutes if the group is tired, or skip it if you are running late. |
| Part 3 checkpoints | 1:21 | 9 min | 31 to 35 | Rewinds 6 and 7 (about 2 min) and Draw it: Part 2 (about 7 min). |
| Part 3 demo | 1:30 | 8 min | 36 to 43 | Branches and merging, the pull request flow and a short demo of Sections 7 to 12. |
| Part 3 work | 1:38 | 35 min | 44 | Attendees do Sections 7 to 12. |
| Break | 2:13 | 5 min | 45 | Optional. The last break. Skip it if you are past about 2 hours 30 minutes. |
| Wrap-up checkpoints | 2:18 | 13 min | 46 to 54 | Rewinds 8 to 13 (about 6 min) and Draw it: Part 3 (about 7 min). |
| Close | 2:31 | 5 min | 55, 58, 59 | Troubleshooting, recap and questions. Undo commands and the fork route (slides 56 and 57) are optional. |

The plan ends at about 2:36. Start times assume every block uses its full time box.

The blocks add up to about 2 hours 36 minutes, including three 5-minute breaks, which leaves about 24 minutes of the 3 hour booking as buffer. Without the breaks the plan is about 2 hours 21 minutes. The work blocks are 15, 20 and 35 minutes: Part 1 is a few short local commands, Part 2 depends mostly on signing in, and Part 3 has the most steps. The tutorial itself is estimated at 2 to 3 hours of hands-on time, and the work blocks give 70 minutes, so expect people to need more time, especially for signing in and Section 8. Use the buffer to extend a work block rather than cutting a checkpoint, and skip a break first if time is short. Anything unfinished can be completed afterwards with `docs/tutorial.md`.

If you run long, skip the breaks, starting with the last one, and the optional slides 56 and 57, keep all three drawings, and trim the Rewinds to the ones that target the strongest misconceptions (3, 5, 8 and 12).

Running a part:

1. Show the demo slides for the part. Demo each section for about a minute and let attendees run it themselves.
2. Show the "Your turn" slide, start a timer and tell attendees to work through the tutorial. Ask them to type each command themselves and copy only fiddly items such as URLs, email addresses and the Section 8 code. Walk the Teams chat and answer questions.
3. At the start of the next part, run the Rewind questions about the part before, then the drawing, then the next demo.

The full deck runs to 59 slides in this order:

| Slide | Title | Slide | Title |
| --- | --- | --- | --- |
| 1 | Cover | 31 | Part 3 divider |
| 2 | Session plan | 32 | Rewind 6 (Section 5) |
| 3 | Before you start | 33 | Rewind 7 (Section 6) |
| 4 | The workshop repository | 34 | Draw it: Part 2 |
| 5 | How to use the materials | 35 | Model answer: Part 2 |
| 6 | Self-assessment | 36 | Branches and merging |
| 7 | Warm-up question | 37 | Section 7: Creating a branch |
| 8 | Part 1 divider | 38 | Section 8: Changing and committing |
| 9 | What Git does | 39 | Section 9: Pushing the branch |
| 10 | The three areas | 40 | The pull request flow |
| 11 | Section 1: Your Git identity | 41 | Section 10: Opening a pull request |
| 12 | Section 2: Creating a repository | 42 | Section 11: Reviewing and merging |
| 13 | Section 3: Staging files | 43 | Section 12: Cleaning up |
| 14 | Section 4: Your first commit | 44 | Your turn: Part 3 |
| 15 | Conventional Commits | 45 | Break |
| 16 | Your turn: Part 1 | 46 | Rewind 8 (Section 7) |
| 17 | Break | 47 | Rewind 9 (Section 8) |
| 18 | Part 2 divider | 48 | Rewind 10 (Section 9) |
| 19 | Rewind 1 (Section 1) | 49 | Rewind 11 (Section 10) |
| 20 | Rewind 2 (Section 2) | 50 | Rewind 12 (Section 11) |
| 21 | Rewind 3 (Section 3) | 51 | Rewind 13 (Section 12) |
| 22 | Rewind 4 (Section 4) | 52 | Draw it: Part 3 |
| 23 | Rewind 5 (Conventional Commits) | 53 | Model answer: fast-forward and merge commit |
| 24 | Draw it: Part 1 | 54 | Model answer: squash merge |
| 25 | Model answer: Part 1 | 55 | Troubleshooting |
| 26 | Section 5: An empty GitHub repository | 56 | Optional: Undo commands |
| 27 | Signing in to GitHub | 57 | Optional: contributing through a fork |
| 28 | Section 6: Linking and pushing | 58 | Recap and next steps |
| 29 | Your turn: Part 2 | 59 | Questions |
| 30 | Break |  |  |

Checkpoint facilitation:

- **Warm-up.** After the overview slides, show slide 6 so everyone can join the Mentimeter with the code or QR code. Run the self-assessment (Mentimeter slides 2 to 6), then the warm-up question on Mentimeter slide 7 while deck slide 7 is on screen, and show its leaderboard on Mentimeter slide 8. Then park Mentimeter on slide 9 until Part 2. The warm-up is not one of the 13 Rewinds.
- **Rewind.** Rewinds run in batches at the start of the next part, so each question covers an earlier part than the one you are about to teach. Run Rewinds 1 to 5 at the start of Part 2, 6 and 7 at the start of Part 3, and 8 to 13 in the wrap-up. This is delayed retrieval practice and never a check on what you just taught. Keep the Mentimeter tab shared for the whole batch and open each question in turn. Each question has a 15-second answer timer. When it ends, show the result and say the answer in one sentence. The answer and the misconception it targets are in the speaker notes and in [quiz-questions.md](quiz-questions.md). The deck's Rewind slides are the backup if Mentimeter fails, and they show no answer.
- **Draw it.** Share the Teams whiteboard and give everyone the time box on the slide to add to one drawing. Suggest each person takes one piece, such as one area or one step. Then ask two or three people to explain their piece, fix anything wrong together, and show the model answer on the next slide. If the group prefers, each person can draw their own version in a separate part of the board and explain it instead. Rewind 13 comes just before the Part 3 drawing and asks why `git branch -d` warns after a squash merge, so use the drawing to show it.
- **Leaderboard.** The Mentimeter has a leaderboard slide after the warm-up and after each batch, the last one at the end (slides 8, 15, 19 and 27). Each comes from the Add leaderboard switch on the question before it, and every other question has the switch off. Park on the "Back to the workshop" text slide between batches so the next questions are not shown early.

Facilitation tips:

- Slides 4 and 5, "The workshop repository" and "How to use the materials", take about three minutes together during the opening. Say that the workshop repository holds the learning materials, and that attendees read them on GitHub or download them. Ask everyone to open the tutorial in the browser now, next to their terminal, and to confirm that they will work in a new folder of their own called `git-workshop-demo`, created in Section 2, plus an empty GitHub repository of their own, created in Section 5. Say clearly that the main-route exercises do not run inside a clone of the workshop repository. The only time attendees clone the workshop repository is for the optional fork appendix, which uses `main.py` and `examples/main_updated.py`.
- Conventional Commits. Slide 15 shows the pattern `type(scope): description`, where the type says what kind of change it is, the optional scope says which part of the code it touches and the description says what the change does. The scope is optional, so `feat: add basic calculator` is a complete and valid message. The description is required. Say that the tutorial has a full table of types and that teams can agree on their own set. Add the length guideline: aim for 50 characters or fewer in the first line, and never more than 72, because GitHub cuts off longer first lines. The examples panel on that slide shows real messages from this repository, such as `docs(workshop): support PowerShell as well as Git Bash`, and attendees can browse the whole history in the repository's commits on GitHub.
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
