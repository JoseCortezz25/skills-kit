# HTML Style Guide

Use this reference for every report generated with `research-to-learning-html`.

## Visual direction

The report is a quiet digital book, not a dashboard or a collection of cards.

- Use **light mode as the default**. A dark mode toggle may be included as an optional secondary experience.
- Use a strict monochrome palette: white or near-white for the page, black or near-black for primary text, and gray only for metadata and secondary text.
- Do not use colored accents, gradients, decorative illustrations, or visual effects that compete with the content.
- Do not use borders, card outlines, rounded containers, drop shadows, or glassmorphism.
- Create hierarchy through typography, whitespace, alignment, scale, and a restrained background tone.
- Prefer a readable serif face for long-form body text and a neutral sans-serif face for headings, labels, controls, and navigation.
- Keep the reading measure narrow enough for comfortable long-form reading, approximately forty-five to seventy-five characters per line.
- Use generous vertical rhythm between chapters, sections, paragraphs, figures, and source entries.

## Required structure

Every report must be a self-contained HTML document that works offline and contains:

- a descriptive `<title>`;
- a clear document heading and subtitle;
- metadata such as research date, scope, assumptions, and estimated reading time;
- a linked table of contents;
- semantic `h1` → `h2` → `h3` heading order;
- chapters that progress from orientation and foundations to evidence, limits, application, and synthesis;
- accessible captions or text alternatives for diagrams and figures;
- a glossary when the topic introduces specialized vocabulary;
- a numbered Sources section with stable internal anchors;
- a research note describing source selection, date range, evidence limits, and unresolved uncertainty.

Reports should be delivered as HTML even when the research process also produces notes, tables, or intermediate artifacts. Those intermediate artifacts support the work but are not the primary deliverable.

The complete runnable example is [`references/report-template.html`](report-template.html). Use it as a starting point for the document shell, typography, spacing, theme behavior, table of contents, chapter structure, and source list. Adapt the content and sections to the research topic without weakening the visual rules above.

## Layout rules

Use a centered shell with a responsive width and a narrow reading column. On small screens, reduce horizontal padding without reducing text size below a comfortable reading size. Keep the table of contents simple: a plain numbered list or short list of links is preferred.

Use paragraphs to connect ideas. Use lists and tables only when they improve comprehension or comparison. Use callouts sparingly and without boxes; a change in background tone, an indented paragraph, or a small uppercase label is enough.

Use inline SVG only when a visual clarifies a mechanism, process, taxonomy, timeline, or comparison. Label conceptual diagrams as conceptual. Never imply precision without data.

## Theme behavior

The initial render must be light mode, regardless of the operating system preference. If dark mode is offered:

- keep the toggle small and accessible;
- persist the user's choice with `localStorage`;
- use an apply-before-paint script to avoid a flash when a saved dark preference exists;
- preserve the same monochrome hierarchy in both themes;
- never make dark mode the initial state for a new report.

A minimal variable system is enough:

```css
:root {
  color-scheme: light;
  --paper: #fff;
  --ink: #111;
  --muted: #666;
  --soft: #f2f2f2;
}

html.dark {
  color-scheme: dark;
  --paper: #111;
  --ink: #f5f5f5;
  --muted: #aaa;
  --soft: #1c1c1c;
}
```

The apply-before-paint script should only activate dark mode when the user has explicitly saved that choice. Without a saved choice, the document must remain light.

## Quality checklist

Before delivering the HTML, verify:

- the first render is light mode;
- the document is black, white, and gray only;
- no borders, cards, rounded panels, shadows, or gradients remain;
- the layout is readable on narrow screens and printable;
- internal links in the table of contents, citations, and source backlinks resolve;
- headings follow a valid hierarchy;
- the document opens offline without runtime dependencies;
- diagrams have captions or text alternatives;
- important claims are cited and uncertainty is explicit.
