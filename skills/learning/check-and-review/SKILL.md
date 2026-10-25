---
name: check-and-review
description: Checks that the learner truly understood and schedules spaced-repetition reviews stored in Markdown files. Use it after explaining a concept, when closing a study session, when the learner says "I got it", or at the start of a session to see what is due for review today.
license: MIT
metadata:
  version: 0.1.0
  author: JoseCortezz25
---

# Check and review

Understanding in the moment and remembering a week later are different things. This skill covers both: it checks comprehension with well-chosen questions and schedules reviews so that what was learned does not evaporate. Speak following the `teacher-voice` skill.

## Checking comprehension

After a concept, do not ask "did you understand?". Ask for one of these tests, **one at a time**:

- **Explain it in your own words** (Feynman technique). The learner explains as if talking to someone who knows nothing.
- **Predict.** "If I run this, what do you think happens and why?"
- **Compare.** "How are X and Y alike, and how do they differ?"
- **Apply to a new case.** An example that has not been covered.
- **Find the error.** A piece of reasoning or code with a hidden flaw.

Pick the test by content type. For ideas, explain or compare. For processes, predict. For techniques, apply.

### How to respond to what the learner says

1. Name what is right first, precisely ("you have it clear that the variable holds an address").
2. Point at the gap with a question that makes it visible before correcting it directly. ("And what would happen if two names had the same address?")
3. If the gap points to a prerequisite, say so and offer to go down with `prerequisite-descent`.
4. Do not move on until the node is reasonably solid, but do not turn this into an exam either. If the learner is already tired, note the gap and continue another day.

### Grading (internal only, never announce a "grade")

- **Clean:** they rebuilt it without help.
- **With help:** they needed a hint.
- **Fail:** they could not, or got the central part wrong.

## Node statuses in `map.md`

- Clean or with-help answer at the end of a stretch: `understood`.
- A card of the node that survives a review at an interval of 7 days or more: `mastered`.
- An `understood` node with a card that fails twice goes back to `in-progress` and is revisited with `prerequisite-descent`.

## Review cards

After each node, create between 1 and 3 cards, no more. Few and good. A card is a question that forces recall or reconstruction. Avoid memorized-definition questions when there is a better way ("why does X happen?" is worth more than "what is X?").

### File `learning/review.md` (global, all topics)

```markdown
---
updated: 2026-10-25
intervals_days: [1, 3, 7, 14, 30, 60, 120]
---

### references-list-copy
- topic: python-variables
- node: reference
- type: explain
- question: If I copy a list with a = b and change a, why does b change?
- key: Both names point to the same address in memory, so there is only one list.
- step: 0
- last: 2026-10-25
- next: 2026-10-26
- failures: 0
```

### How a card moves

`step` is the position in the `intervals_days` list. Get today's date from the system (for example `date +%F`).

- **Clean:** `step` goes up by 1. `next` = today + the interval of the new step.
- **With help:** `step` stays. `next` = today + the interval of that same step.
- **Fail:** `step` goes back to 0, `next` = tomorrow, `failures` goes up by 1.
- With `failures` at 3 or more, the card signals a missing prerequisite. Instead of reviewing it again, offer to go down to that node with `prerequisite-descent`. When it is resolved, reset `failures` to 0.
- Always update `last` with today's date.

### What to do at the start of a session

1. Read `learning/review.md` and filter cards whose `next` is less than or equal to today.
2. If there are some, say it in one sentence ("Today there are 4 reviews, about 5 minutes") and offer to do them first. Five per session at most. If there are more, take the lowest `step` first and the most overdue.
3. Ask the questions one at a time, without showing the key until the learner answers. Then grade and update the card.
4. If the learner wants to leave them for later, leave them and do not insist.

## Closing a session

End with three or four sentences in prose. What was covered, what is solid, what is shaky, and what to review tomorrow or in the next few days. No bullets.

If the agent cannot edit files, deliver the updated content of `review.md` and `map.md` in blocks so the learner can save them.
