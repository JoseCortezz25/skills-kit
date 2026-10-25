---
name: prerequisite-descent
description: Guides learning of a concept by going down through its prerequisites to something the learner already knows, then climbing back up reconnecting everything. Use it when someone says they do not understand something, lacks context, wants to learn "from the basics", or when an explanation opens another "and what is that?" question.
license: MIT
metadata:
  version: 0.1.0
  author: JoseCortezz25
---

# Prerequisite descent

The core of the method. It rests on the idea that often a person does not understand something because an earlier piece is missing, and not because they are unable to understand it. This skill finds the missing piece, teaches it, and climbs back to the original concept. Speak following the `teacher-voice` skill.

## Before starting

1. Look for `learning/<topic>/`. If it exists, read `map.md`, `session.md`, and `glossary.md`. If it does not, use `topic-map` first (or a minimal version if the learner is in a hurry: a one-sentence idea, the direct prerequisites, and a single diagram).
2. Check `learning/review.md`. If there are due cards, offer to review them (five at most) before continuing, and respect the answer if the learner prefers to leave them for later.
3. Get the current date from the system (for example `date +%F`) and do not assume it.

## The cycle

### 1. Explain briefly

Explain the concept in 3 to 6 lines with one analogy. No more. Do not add details or edge cases yet.

### 2. Bring the prerequisites to light

Close the explanation by naming one to three pieces you took for granted, and ask which ones feel shaky. Example: "I assumed you know what memory is and what a value is. Do you want to revisit either one?"

This makes explicit what is usually hidden and leaves the decision to go down in the learner's hands.

### 3. Decide whether to go down

- If they say they understand it, run a minimal check (see `check-and-review`) before moving on. "Yes, I get it" is not enough.
- If they say something does not click, first try **one** different reformulation with another analogy. Sometimes the problem is the explanation and not a missing prerequisite.
- If the reformulation is not enough, or the learner names an unknown term, go down.

### 4. Go down

Before going down, make sure the node passes the prerequisite test: **can the node above be understood without this?** If the answer is yes, it is a tangent. Note it in the "Parked" section of `session.md` and keep going. Only go down for what is truly needed.

When going down:
- Push the new node onto the stack in `session.md`.
- Show the path in one line at the top of the message once depth is 2 or more. Example: "You came from: Mutability > References. Now: RAM."
- Ask "do you already have this?" with a concrete question, not an abstract "do you know it?". Example: "If I tell you a value lives in memory, what do you picture memory to be here?" The learner's answer says more than a yes or a no.
- If they already master it, that node is the **floor** (status `known`). Start climbing.
- If not, repeat the cycle with that node: explain briefly, surface prerequisites, decide.

### 5. Depth limit

When the stack reaches 4 levels, stop and say so: "We have gone four levels down. Do you want to keep going, or climb back up with what we have and come back to this later?" Endless descent is the main risk of this method.

### 6. Climb

Climb one level at a time. At each level:
1. Connect in one or two sentences how the lower piece explains the upper one.
2. Ask for a small check in the learner's own words. Example: "With what you just saw about memory, how would you explain what a variable really holds?"
3. If they answer well, mark the node `understood` and go up. If not, give hints from what they already have before giving the answer.

When you reach the original concept, have them explain the whole thing in their own words and give back, in a single prose paragraph, the chain they walked through. Example: "A variable holds a reference, which is an address in memory. That is why copying a list copies the address and not the contents, and both names end up pointing at the same list."

### 7. Close the stretch

When a concept is finished:
- Update `map.md` (statuses), `session.md` (stack and next step), `glossary.md` (new terms), and `learning/review.md` (1 to 3 cards per node, following `check-and-review`).
- Do not narrate the updates during the conversation. At the end of the stretch, a single line ("I saved the progress and three questions to review") is enough.
- If the agent cannot write files, deliver the updated blocks at the end so the learner can save them.

## Golden rules

- **One new concept per turn.** If there are two, split the turn.
- **The learner chooses the direction.** Offer, do not impose. Propose two or three paths at most.
- **No undefined terms.** If you use a technical word the learner has not seen, define it in parentheses and add it to the glossary.
- **If the learner gets frustrated,** slow down and go back to a level where they felt comfortable. Mention what they already achieved.
- **If the learner switches topic mid-descent,** save the stack in `session.md` so it can be resumed.
- **Do not invent prerequisites.** If you are not sure what something depends on, say so and check before teaching it.

## Example walkthrough (summarized)

Question: "Why does changing a copy of a list also change the original?"

1. Short explanation: two names can point to the same list. Prerequisites named: variable and reference.
2. The learner says "reference" is not clear. One reformulation is not enough, so go down.
3. Reference needs memory. Floor question: "What do you picture the computer's memory to be?" They answer well and that node becomes `known`.
4. Climb: memory explains reference (an address). Check: "What does the variable really hold?" They answer in their own words.
5. Climb: reference explains the behavior of copies. The learner summarizes it and receives the whole chain in one paragraph.
6. Three cards are saved and the map is updated.
