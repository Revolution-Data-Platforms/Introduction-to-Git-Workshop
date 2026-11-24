# Quiz Question Pack: Introduction to Git Workshop

Thirteen quick-fire "Rewind" questions for the workshop deck. Each one covers an earlier part than the one being taught, never the current one, so it doubles as spaced practice. Questions are conceptual and do not depend on command syntax.

The quiz is built in the Git Skills Self-Assessment Mentimeter, on slides 7 to 25 after the six survey slides, in the launch order below, so a single leaderboard builds up across the whole session. See the setup checklist in [presenter-guide.md](presenter-guide.md).

## When to run them

Run the questions in three batches, each about the part just finished:

- Questions 1 to 5 at the start of Part 2, about Part 1.
- Questions 6 and 7 at the start of Part 3, about Part 2.
- Questions 8 to 13 in the wrap-up, about Part 3.

In the Git Skills Self-Assessment Mentimeter, the quiz follows the six survey slides. Run the survey slides first, then park on slide 7 until Part 2.

- Slide 7: "Back to the workshop" text slide. Park here until Part 2.
- Slides 8 to 12: questions 1 to 5, then slide 13, a leaderboard.
- Slide 14: text slide. Park here until Part 3.
- Slides 15 and 16: questions 6 and 7, then slide 17, a leaderboard.
- Slide 18: text slide. Park here until the wrap-up.
- Slides 19 to 24: questions 8 to 13, then slide 25, the final leaderboard.

The text slides give you a safe place to stop between batches, so the next questions are not shown early. Each question also has Add leaderboard switched on, so a leaderboard may show after every question. Switch it off per slide under Edit, then Quiz settings, if it slows the pace.

## Warm-up question

The self-assessment includes a teaser, "What best describes a Git commit?" (Mentimeter slide 4). Deck slide 2 shows the same question with four options, A to D. The correct answer is A, a snapshot of the project at a point in time. Keep the Mentimeter version to the same four options.

## Rebuilding the Mentimeter quiz

The quiz is already built in the Git Skills Self-Assessment presentation. To rebuild it, create one presentation in a free Mentimeter account and add 13 **Quiz competition** (multiple choice) questions, in the order below.
2. Paste the question and the four options exactly as written. Mark the correct option and set the timer to 45 seconds.
3. Keep scoring on. Add a text slide before each batch and a leaderboard slide after it.
4. The 13 Rewind slides show the join code 1509 1500. If you rebuild the presentation, copy its new join code into the slides with Find and Replace in PowerPoint.
5. Rehearse alone, on one device. Every participant counts toward the free plan's monthly limit of 50, so avoid rehearsing with colleagues. Check Mentimeter's current free plan limits before the session.

## Backup: Teams meeting Polls

If Mentimeter fails, create each question in advance under **Polls** in the Teams meeting, using the **Multiple Choice Quiz** type, and launch them from the same slide. This type has no scoring or leaderboard, so say the correct answer aloud after each poll closes.

## Questions in launch order

| Launch order | Slide | Covers | Correct |
| --- | --- | --- | --- |
| 1 | 17 | Section 1 | B |
| 2 | 18 | Section 2 | C |
| 3 | 19 | Section 3 | A |
| 4 | 20 | Section 4 | D |
| 5 | 21 | Conventional Commits | B |
| 6 | 29 | Section 5 | D |
| 7 | 30 | Section 6 | C |
| 8 | 42 | Section 7 | A |
| 9 | 43 | Section 8 | A |
| 10 | 44 | Section 9 | C |
| 11 | 45 | Section 10 | D |
| 12 | 46 | Section 11 | B |
| 13 | 47 | Section 12 | A |

### Question 1: Section 1

Deck slide 21. Run at the start of Part 2.

**Why does Git need your name and email?**

- A. To log you in to GitHub
- B. To record who made each commit (correct)
- C. To send notifications about your repository
- D. To decide who may push

Why: Misconception (A): the name and email are not your GitHub login. Git writes them into each commit. Signing in to GitHub comes later, in Section 5.

### Question 2: Section 2

Deck slide 21. Run at the start of Part 2.

**You delete the hidden `.git` folder. What happens?**

- A. Your files are deleted along with the history
- B. Nothing, because Git keeps a backup elsewhere
- C. The history is gone but your files stay (correct)
- D. Only the staging area is cleared

Why: Git keeps the whole history inside .git, and your files live beside it. Option A is the common fear. Option B is wrong because no backup exists.

### Question 3: Section 3

Deck slide 21. Run at the start of Part 2.

**You edit `main.py` after `git add main.py`. Is the new edit staged?**

- A. No, only the version you added is staged (correct)
- B. Yes, Git now tracks the file, so the edit is staged too
- C. Yes, but only after you save the file
- D. No, and the version you added is discarded

Why: Misconception (B): staging does not track a file, it stores a snapshot of the version you added. Run `git add` again to stage the new edit. git status shows the file as both staged and not staged.

### Question 4: Section 4

Deck slide 21. Run at the start of Part 2.

**You changed two files but staged only one. What goes in the commit?**

- A. Both files, because both changed
- B. Nothing, until every changed file is staged
- C. Whichever file you edited last
- D. Only the staged file (correct)

Why: A commit takes only what is staged. The other file's changes stay in the working directory for a later commit.

### Question 5: Conventional Commits

Deck slide 21. Run at the start of Part 2.

**Which Conventional Commits type fits a typo fix in the README?**

- A. fix, because a typo is a mistake
- B. docs (correct)
- C. chore
- D. refactor

Why: Misconception (A): fix means a bug in the code, not any kind of mistake. A change that only touches documentation is docs.

### Question 6: Section 5

Deck slide 30. Run at the start of Part 3.

**Why create the GitHub repository empty?**

- A. A README on GitHub would overwrite your local files
- B. An empty repository uploads faster
- C. GitHub only accepts one push to a new repository
- D. A README made on GitHub is a commit you do not have, so your first push is rejected (correct)

Why: Option A is the common worry. Nothing is overwritten. The push is rejected because GitHub has a commit your computer does not have.

### Question 7: Section 6

Deck slide 30. Run at the start of Part 3.

**After `git push`, what is on GitHub?**

- A. Your working folder, kept in sync as you edit
- B. Your staged changes as well as your commits
- C. Copies of your commits (correct)
- D. Nothing until you open a pull request

Why: Misconception (A): working files do not sync. Only committed work is pushed, and staged changes stay on your computer (B).

### Question 8: Section 7

Deck slide 47. Run at the wrap-up.

**What is a branch?**

- A. A label that points to a commit (correct)
- B. A copy of all your files
- C. A separate repository on GitHub
- D. A folder on your computer

Why: Misconception (B): a branch is not a copy of the files. It is a movable label on a commit, which is why creating one is instant.

### Question 9: Section 8

Deck slide 47. Run at the wrap-up.

**You commit on the feature branch. What happens to `main`?**

- A. Nothing, main stays where it was (correct)
- B. main gets the new commit too
- C. main is locked until the branch is merged
- D. Git marks main as out of date

Why: Only the branch you are on moves. Option B is the common mistake.

### Question 10: Section 9

Deck slide 47. Run at the wrap-up.

**You pushed your branch. Has `main` on GitHub changed?**

- A. Yes, GitHub merges pushed branches into main
- B. Yes, but only if there are no conflicts
- C. No, only your branch was uploaded (correct)
- D. Only after you refresh the page

Why: main on GitHub changes only when someone merges the pull request. GitHub never merges for you (A and B).

### Question 11: Section 10

Deck slide 47. Run at the wrap-up.

**What does opening a pull request do?**

- A. It merges your branch into main
- B. It uploads your commits to GitHub
- C. It deletes your branch after review
- D. It proposes a merge for review, and nothing is merged yet (correct)

Why: The push already uploaded the commits (B). A pull request asks for the merge and starts the review. Nothing merges until someone selects merge.

### Question 12: Section 11

Deck slide 47. Run at the wrap-up.

**`main` has not moved since you branched, and you merge. What happens?**

- A. Git always creates a merge commit
- B. Fast-forward: main moves to your last commit, with no new commit (correct)
- C. Git refuses, because the branches differ
- D. Git squashes your commits into one

Why: Misconception (A): a merge does not always create a merge commit. When main has not moved, Git just moves the label forward.

### Question 13: Section 12

Deck slide 47. Run at the wrap-up.

**Why does `git branch -d` warn after a squash merge?**

- A. Your commits were replaced by one new commit on main (correct)
- B. The branch is still checked out
- C. GitHub already deleted the remote branch
- D. Squash merges leave the branch unpushed

Why: A squash merge adds one new commit to main and leaves your branch commits out of main's history, so Git thinks the branch is not merged. Check the pull request is merged, then use git branch -D.
