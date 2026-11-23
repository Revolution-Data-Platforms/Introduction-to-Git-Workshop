# Quiz Question Pack: Introduction to Git Workshop

Thirteen quick-fire "Rewind" questions for the workshop deck. Each one asks about the section before the current one, never the current one, so it doubles as spaced practice. Questions are conceptual and do not depend on command syntax.

Build them as one Mentimeter quiz in the launch order below, so a single leaderboard builds up across the whole session. See the setup checklist in [presenter-guide.md](presenter-guide.md).

## How to build the Mentimeter quiz

1. Create one presentation in a free Mentimeter account and add 13 **Quiz competition** (multiple choice) questions, in the order below.
2. Paste the question and the four options exactly as written. Mark the correct option and set the timer to 45 to 60 seconds.
3. Keep scoring on, and show the leaderboard at the break and at the end.
4. Copy the join code (the number shown at menti.com) into the `[join code]` placeholder on the 13 Rewind slides with Find and Replace in PowerPoint. The PDF keeps the placeholder.
5. Rehearse alone, on one device. Every participant counts toward the free plan's monthly limit of 50, so avoid rehearsing with colleagues. Check Mentimeter's current free plan limits before the session.

## Backup: Teams meeting Polls

If Mentimeter fails, create each question in advance under **Polls** in the Teams meeting, using the **Multiple Choice Quiz** type, and launch them from the same slide. This type has no scoring or leaderboard, so say the correct answer aloud after each poll closes.

## Questions in launch order

| Launch order | Slide | Covers | Correct |
| --- | --- | --- | --- |
| 1 | 10 | Section 1 | B |
| 2 | 12 | Section 2 | C |
| 3 | 14 | Section 3 | A |
| 4 | 16 | Section 4 | D |
| 5 | 21 | Conventional Commits | B |
| 6 | 24 | Section 5 | D |
| 7 | 29 | Section 6 | C |
| 8 | 32 | Section 7 | A |
| 9 | 34 | Section 8 | A |
| 10 | 36 | Section 9 | C |
| 11 | 39 | Section 10 | D |
| 12 | 41 | Section 11 | B |
| 13 | 43 | Section 12 | A |

### Question 1: Section 1

Deck slide 10. Shown at the start of the next section.

**Why does Git need your name and email?**

- A. To log you in to GitHub
- B. To record who made each commit (correct)
- C. To send notifications about your repository
- D. To decide who may push

Why: Misconception (A): the name and email are not your GitHub login. Git writes them into each commit. Signing in to GitHub comes later, in Section 5.

### Question 2: Section 2

Deck slide 12. Shown at the start of the next section.

**You delete the hidden `.git` folder. What happens?**

- A. Your files are deleted along with the history
- B. Nothing, because Git keeps a backup elsewhere
- C. The history is gone but your files stay (correct)
- D. Only the staging area is cleared

Why: Git keeps the whole history inside .git, and your files live beside it. Option A is the common fear. Option B is wrong because no backup exists.

### Question 3: Section 3

Deck slide 14. Shown at the start of the next section.

**You edit `main.py` after `git add main.py`. Is the new edit staged?**

- A. No, only the version you added is staged (correct)
- B. Yes, Git now tracks the file, so the edit is staged too
- C. Yes, but only after you save the file
- D. No, and the version you added is discarded

Why: Misconception (B): staging does not track a file, it stores a snapshot of the version you added. Run `git add` again to stage the new edit. git status shows the file as both staged and not staged.

### Question 4: Section 4

Deck slide 16. Shown at the start of the next section.

**You changed two files but staged only one. What goes in the commit?**

- A. Both files, because both changed
- B. Nothing, until every changed file is staged
- C. Whichever file you edited last
- D. Only the staged file (correct)

Why: A commit takes only what is staged. The other file's changes stay in the working directory for a later commit.

### Question 5: Conventional Commits

Deck slide 21. Shown at the start of the next section.

**Which Conventional Commits type fits a typo fix in the README?**

- A. fix, because a typo is a mistake
- B. docs (correct)
- C. chore
- D. refactor

Why: Misconception (A): fix means a bug in the code, not any kind of mistake. A change that only touches documentation is docs.

### Question 6: Section 5

Deck slide 24. Shown at the start of the next section.

**Why create the GitHub repository empty?**

- A. A README on GitHub would overwrite your local files
- B. An empty repository uploads faster
- C. GitHub only accepts one push to a new repository
- D. A README made on GitHub is a commit you do not have, so your first push is rejected (correct)

Why: Option A is the common worry. Nothing is overwritten. The push is rejected because GitHub has a commit your computer does not have.

### Question 7: Section 6

Deck slide 29. Shown at the start of the next section.

**After `git push`, what is on GitHub?**

- A. Your working folder, kept in sync as you edit
- B. Your staged changes as well as your commits
- C. Copies of your commits (correct)
- D. Nothing until you open a pull request

Why: Misconception (A): working files do not sync. Only committed work is pushed, and staged changes stay on your computer (B).

### Question 8: Section 7

Deck slide 32. Shown at the start of the next section.

**What is a branch?**

- A. A label that points to a commit (correct)
- B. A copy of all your files
- C. A separate repository on GitHub
- D. A folder on your computer

Why: Misconception (B): a branch is not a copy of the files. It is a movable label on a commit, which is why creating one is instant.

### Question 9: Section 8

Deck slide 34. Shown at the start of the next section.

**You commit on the feature branch. What happens to `main`?**

- A. Nothing, main stays where it was (correct)
- B. main gets the new commit too
- C. main is locked until the branch is merged
- D. Git marks main as out of date

Why: Only the branch you are on moves. Option B is the common mistake.

### Question 10: Section 9

Deck slide 36. Shown at the start of the next section.

**You pushed your branch. Has `main` on GitHub changed?**

- A. Yes, GitHub merges pushed branches into main
- B. Yes, but only if there are no conflicts
- C. No, only your branch was uploaded (correct)
- D. Only after you refresh the page

Why: main on GitHub changes only when someone merges the pull request. GitHub never merges for you (A and B).

### Question 11: Section 10

Deck slide 39. Shown at the start of the next section.

**What does opening a pull request do?**

- A. It merges your branch into main
- B. It uploads your commits to GitHub
- C. It deletes your branch after review
- D. It proposes a merge for review, and nothing is merged yet (correct)

Why: The push already uploaded the commits (B). A pull request asks for the merge and starts the review. Nothing merges until someone selects merge.

### Question 12: Section 11

Deck slide 41. Shown at the start of the next section.

**`main` has not moved since you branched, and you merge. What happens?**

- A. Git always creates a merge commit
- B. Fast-forward: main moves to your last commit, with no new commit (correct)
- C. Git refuses, because the branches differ
- D. Git squashes your commits into one

Why: Misconception (A): a merge does not always create a merge commit. When main has not moved, Git just moves the label forward.

### Question 13: Section 12

Deck slide 43. Shown at the start of the next section.

**Why does `git branch -d` warn after a squash merge?**

- A. Your commits were replaced by one new commit on main (correct)
- B. The branch is still checked out
- C. GitHub already deleted the remote branch
- D. Squash merges leave the branch unpushed

Why: A squash merge adds one new commit to main and leaves your branch commits out of main's history, so Git thinks the branch is not merged. Check the pull request is merged, then use git branch -D.
