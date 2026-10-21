---
name: random-word
version: 1.0.0
description: Guides a lateral-thinking session using the "random word" technique (Edward de Bono's random stimulus). Draws a word unrelated to the problem with a script that uses real randomness, links it to the focus word or problem through chains of stepping stones, and generates new ideas, deferring judgment to a separate evaluation phase. Use this skill whenever the user mentions "random word", "random stimulus", "lateral thinking", "De Bono", or "PO", or asks for unconventional ideas, help breaking a creative block, connecting unrelated concepts, or a brainstorm different from the usual kind, even if they never name the technique.
---

# Random word (lateral thinking)

This skill runs a short, deliberate creativity session based on the chapter "The random stimulus" in Edward de Bono's _Lateral Thinking_. For the full rationale and more examples read `references/de-bono-method.md`; for the connection moves with examples, `references/moves.md`.

## The idea in two lines

Reasoning from inside a problem keeps leading to the same conclusions, because the mind organizes information into rigid patterns. A word **unrelated** to the problem, held in attention next to it, forces the mind to connect the two and opens entry points or analogies that direct reasoning would not find. The less the word has to do with the problem, the more useful it tends to be.

## Why a script draws the word

A language model does not pick at random: it tends to propose "creative" words, or words that already fit the focus, and that cancels the effect. So the word always comes from `scripts/draw.py`. Never choose, suggest or replace it yourself, even if the word that came up seems poor or too close to the focus.

## Modes

- **Guided (default):** pause at two points so the person can take part. Use this unless they say otherwise.
- **Direct:** if they ask for something like "quick", "all at once" or "no questions", run the whole flow in a single reply.

## Flow

### 0. Fix the focus

You need a word or a concrete problem. If the person has not given one, ask for it in a single question. Write it verbatim as "Focus: …" and do not rephrase it afterwards. The classic failure is bending the problem to fit the word that came up, and then the word stops provoking anything.

### 1. Draw

Run the script, passing the focus so a word already in it cannot come up:

```bash
python3 scripts/draw.py --focus "<focus>"
```

The output is a single word. Present it as `PO <word>`, the particle De Bono uses to mark a stimulus that needs no justification and no judgment. If the word has several meanings, say briefly which one you are using.

If the person prefers a **physical object** (the book notes it offers more angles than a word, because you think about its form and not just its function), run `python3 scripts/draw.py --physical-object`. It returns a formal rule ("the blue object closest to you") and the person tells you which object it turned out to be.

**One word per session.** If they ask for another because this one "doesn't work", explain that swapping until one fits amounts to choosing the one that confirms their current view. The alternative is another session at another time, or a different focus.

**Pause point 1 (guided mode):** before connecting, ask whether they want to throw out the first associations themselves or have you go ahead. Their own links are often more valuable than yours because they come from their context. If they offer some, build on them.

### 2. Connect with chains

Build 3 to 5 chains (the equivalent of the method's 3 minutes; if the person is co-creating, suggest timing 3 minutes). Each chain starts at the random word and moves through stepping stones until it touches the focus:

`word — stepping stone — stepping stone → idea`

Use a **different move** in each chain (associative chain, attribute transfer, wordplay, antithesis, physical object); they are described in `references/moves.md`. Include at least one bold or absurd chain: according to the method, a wrong or senseless idea can be the stepping stone to a good one.

While generating, **do not judge or discard**. Each step does not need to be logical; sometimes the link to the word only shows up after the idea exists.

### 3. Close each chain with a concrete idea

End each chain with one idea applicable to the focus, in a single sentence. If a chain produces nothing usable, keep it with a provisional idea or mark it "dead end": part of the value is in having walked the path.

### 4. Pause and evaluate (judgment arrives here, not before)

**Pause point 2 (guided mode):** show the raw ideas and ask which criterion they want to evaluate with (for example: feasibility, originality, cost, speed). In direct mode, pick a reasonable criterion yourself and say which.

Then switch to vertical thinking: pick the 2 or 3 most promising ideas, explain why, what it would take to test them, and propose a concrete first step for each. Discarded ideas are not deleted; they stay on the list.

### 5. Close

Summarize in three lines: the word, the best idea and the next step. If there is interest, mention that the method suggests practicing for 3 minutes a day and that it improves with a calm confidence that "something will turn up", without urgency.

## Output format

Use this structure so the session is easy to reread:

```
**Focus:** …
**Random word:** PO …

**Chains**
1. word — stepping stone — stepping stone → idea
2. …

**Raw ideas**
- …

**Evaluation** (criterion: …)
1. Idea → why, what is missing, first step
```

## Short example

Focus: _reduce food waste in a restaurant._ Drawn word: **umbrella**.

1. umbrella — protects from what falls — protect the product before it spoils → cover and rotate first whatever expires soonest, with color-coded date labels.
2. umbrella — opens and closes — adjustable size → dishes with adjustable portions ("half portion" as a normal option).
3. umbrella — gets forgotten and ends up in lost and found — a place for the unclaimed → an end-of-day surplus shelf with a late-hours discount.

Evaluation with the criterion "speed of testing": idea 3 can be tried this week without changing the kitchen.

## Variants (only if the person asks)

- **One problem, several words:** draw with `--n 3` and run one short session per word, separately; then compare whether different words led to similar approaches.
- **One word, several problems:** a single word applied to each problem in separate turns (do not present them all at once, to avoid jumping ahead).
- **Your own list:** the script accepts `--file my_list.txt` with one word per line.

## What to avoid

- Choosing or "improving" the drawn word.
- Rephrasing the focus after seeing the word.
- Evaluating while chains are being generated.
- Stretching the connection phase out of boredom: when the flow runs dry, close it and evaluate.
- Forcing a "reasonable" link. The connection can be a pun or the opposite of the word; there is no single correct way to use it.
