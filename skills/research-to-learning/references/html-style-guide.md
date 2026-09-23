# HTML Rendering Style Guide (optional)

Apply this reference **only** when rendering `output/guia-completa.md` to `output/guia-completa.html`, and only after the Markdown guide and the research corpus are complete. HTML is an optional reading format for the consolidated content; it must not change, shorten, or add content, and it must never be the reason research stops.

A complete runnable shell lives in [`references/report-template.html`](report-template.html). Use it as the starting point for typography, spacing, theme behavior, table of contents, chapter structure, and the source list — adapt the content, do not weaken the rules below.

## Visual direction

Treat the page as a quiet digital book, not a dashboard or a collection of cards.

- Use **light mode as the default**, regardless of the operating system preference. Dark mode may be offered as an optional toggle.
- Use a strict monochrome palette: white or near-white page background, black or near-black primary text, gray only for metadata or secondary text.
- Do not use colored accents, gradients, decorative illustrations, or visual effects that compete with the content.
- Do not use borders, card outlines, rounded containers, drop shadows, or glassmorphism.
- Create hierarchy through typography, whitespace, alignment, scale, and a restrained background tone.
- Prefer a readable serif face for long-form body text and a neutral sans-serif face for headings, labels, controls, and navigation.
- Keep the reading column narrow and comfortable, approximately 45–75 characters per line.
- Use generous vertical rhythm between chapters, sections, paragraphs, figures, and sources.

## Required structure

The rendering must be a self-contained HTML document that works offline and mirrors the Markdown guide:

- a descriptive `<title>`, a clear document heading, and a subtitle;
- metadata: research date, scope, assumed prior knowledge, and estimated reading time;
- a linked table of contents;
- semantic `h1` → `h2` → `h3` heading order;
- the same chapters, in the same dependency order, as `output/guia-completa.md`;
- accessible captions or text alternatives for every diagram and figure;
- the glossary, when the topic introduces specialized vocabulary;
- the uncertainty section: unresolved contradictions and open questions;
- a numbered Sources section with stable internal anchors matching the bibliography.

## Layout rules

Use a centered shell with a responsive width and a narrow reading column. On small screens, reduce horizontal padding without dropping the text size below a comfortable reading size. Keep the table of contents simple: a plain numbered list or short list of links.

Use paragraphs to connect ideas. Use lists and tables only when they improve comprehension or comparison. Use callouts sparingly and without boxes; a change in background tone, an indented paragraph, or a small uppercase label is enough. Use inline SVG only when a visual clarifies a mechanism, process, taxonomy, timeline, or comparison. Label conceptual diagrams as conceptual, and never imply precision without data.

## Theme behavior

The initial render must be light, regardless of the operating system preference. If dark mode is offered: keep the toggle small and accessible, persist the choice with `localStorage`, use an apply-before-paint script to avoid a flash when a saved dark preference exists, preserve the same monochrome hierarchy in both themes, and never make dark mode the initial state.

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

The apply-before-paint script activates dark mode only when the user has explicitly saved that choice. Without a saved choice, the document stays light.

## Integrity between formats

- Every chapter, worked example, citation, and unresolved contradiction present in the Markdown guide must also be present in the rendering, with the same numbering.
- No external runtime dependencies unless the user asks for them: inline the CSS, JavaScript, SVG, and assets.

## Quality checklist

Before delivering the HTML, verify:

- the first render is light mode;
- the document is black, white, and gray only;
- no borders, cards, rounded panels, shadows, or gradients remain;
- the layout is readable on narrow screens and printable;
- table-of-contents links, citations, and source backlinks all resolve;
- headings follow a valid hierarchy;
- the document opens offline without runtime dependencies;
- diagrams have captions or text alternatives;
- every chapter of the Markdown guide is present, and no claim appears that the Markdown guide does not carry.
