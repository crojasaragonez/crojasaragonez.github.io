---
title: The Formats Nobody Was Supposed to Write
description: "Three colleagues chose to send me HTML reports last week, though none of them writes code. Formats that once needed a specialist can now start with a clear request."
pubDate: 2026-08-14
---

Three colleagues chose to send me HTML reports last week. Nobody asked them to use HTML.

None of them writes code. None opened a programming editor, and I doubt they could explain a closing tag. They sent a file, I opened it in a browser, and it looked like a proper report. It followed the brand guidelines. It also worked as well on my phone as on my laptop.

Before AI agents, this would have been unusual.

## What "send it in HTML" used to mean

Two years ago, a non-technical colleague choosing HTML for a report would have been unusual.

It meant learning HTML, a markup language, and enough CSS to make the page look right. It also meant installing an editor, writing the markup by hand, and fixing the difference between the intended result and what the browser showed. Nobody does all that for an ordinary report. They send a Word document or a PDF instead.

The format was not the hard part. The hard part was the syntax: the exact punctuation and rules needed to write it.

<figure class="fig">
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="f1t f1d">
<title id="f1t">Producing an HTML report, before agents and with an agent</title>
<desc id="f1d">Before agents, producing an HTML report took five steps: learn HTML and CSS, install and configure an editor, write the markup by hand, debug what the browser shows, and finally ship the report. With an agent it takes two steps: describe the report you want, and ship it.</desc>
<text x="20" y="30" font-size="16" font-weight="600" fill="var(--text)">Before agents</text>
<text x="20" y="50" font-size="12.5" fill="var(--text-muted)">5 steps, weeks of learning</text>
<rect x="20" y="68" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="68" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="88" font-size="14" fill="var(--text)">Learn HTML and CSS</text>
<rect x="20" y="105" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="105" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="125" font-size="14" fill="var(--text)">Install and set up an editor</text>
<rect x="20" y="142" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="142" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="162" font-size="14" fill="var(--text)">Write the markup by hand</text>
<rect x="20" y="179" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="179" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="199" font-size="14" fill="var(--text)">Debug what the browser shows</text>
<rect x="20" y="216" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="216" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="236" font-size="14" fill="var(--text)">Ship the report</text>
<text x="310" y="30" font-size="16" font-weight="600" fill="var(--text)">With an agent</text>
<text x="310" y="50" font-size="12.5" fill="var(--text-muted)">2 steps, one afternoon</text>
<rect x="310" y="68" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="310" y="68" width="3" height="30" fill="var(--accent-soft)"/><text x="328" y="88" font-size="14" fill="var(--text)">Describe the report you want</text>
<rect x="310" y="105" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="310" y="105" width="3" height="30" fill="var(--accent-soft)"/><text x="328" y="125" font-size="14" fill="var(--text)">Ship the report</text>
<rect x="310" y="142" width="270" height="104" rx="2" fill="none" stroke="var(--border)" stroke-dasharray="4 5"/>
<text x="445" y="188" text-anchor="middle" font-size="14" fill="var(--text-muted)">The learning curve is no longer</text>
<text x="445" y="212" text-anchor="middle" font-size="14" fill="var(--text-muted)">on the critical path.</text>
<text x="20" y="290" font-size="12.5" fill="var(--text-muted)">The middle three boxes were never the work. They were the price of admission.</text>
</svg>
<figcaption>Same format, same complexity. Far fewer steps to reach it.</figcaption>
</figure>

HTML is a useful report format. A single file opens on almost any device, can print to PDF, and can include interactive tables or charts. It is also likely to remain readable for a long time. It was not the usual choice for internal documents because writing it often needed a specialist.

That barrier is much lower now.

## Then the same thing happened with LaTeX

LaTeX was an even bigger surprise.

We now use LaTeX-style documents for well-formatted contracts, technical appendices, one-page summaries, and mathematical notation. They can look closer to a book or journal than a standard word-processor document.

Nobody on the team has opened TeXstudio. There is no TeX Live installation, package manager, or long search for the right way to position an image.

> LaTeX was never hard because of the typesetting. It was hard because of everything you had to survive before the typesetting started.

For decades, LaTeX was mostly used in science and academia. Its output was strong, but getting started took time and patience. Many people outside those fields never tried it.

Now a clear sentence can be enough to get started.

## The evidence that this is happening everywhere

I wanted to know if this was only happening around me. It is not.

**Documents are a major use case.** Anthropic's Economic Index found that documents and reports were the largest category of work output in its data, at 20% of work conversations, ahead of code. Many people use these tools to make documents, not programs.

**LaTeX tools are reducing the LaTeX burden.** In June 2025, Overleaf introduced AI writing tools for its more than 20 million users, aimed at reducing time spent working with LaTeX code. Typst, a newer system with simpler markup, is also gaining acceptance in some journals.

**The idea now has a common name.** Collins named “vibe coding” its Word of the Year for 2025: describing the result you want in plain language and letting a machine write the code.

The first number matters most to me. If documents outrank code, many of the people using these tools are not developers.

## Other formats that fell over

HTML and LaTeX are simply the two formats I saw first. They are not alone.

| The format | What used to guard it |
| --- | --- |
| HTML & CSS | a front-end developer |
| LaTeX | TeX Live, TeXstudio, a 300-page manual |
| SVG | a designer and a licensed editor |
| Mermaid & Graphviz | a diagramming tool and its lock-in |

The formats have not changed. The need for a specialist is no longer automatic.

A few worth calling out:

1. **SVG.** People can create publishable vector graphics without using a drawing tool. The image is text, so it can be edited, compared, and tracked in version control.
2. **Mermaid and Graphviz.** These tools turn text into diagrams. MermaidSeqBench, a published benchmark, measures how well models turn a written description into a Mermaid sequence diagram.
3. **Markdown.** It is a simple way to add headings, lists, and structure to a document. Many people use it without thinking of it as a technical format.
4. **Configuration formats.** YAML, JSON, TOML, iCal, GeoJSON, and BibTeX are easy in principle but strict about punctuation. That is a useful kind of task for a model.

These formats become easier when the difficulty is in notation, not in the underlying ideas.

## What is actually being democratized

There is an important limit to this idea.

These tools do not give people good judgment. The reports I received were clear because their authors understood their work. The format became easier; the thinking did not.

What has changed is access to a good format. For decades, choosing the best container for your work often required technical training. If you were not a developer, you usually chose from the options in a toolbar. Formats with more control or longer life sat behind a wall of syntax.

> The wall was never protecting anything valuable. It was just there.

There is one real risk. If someone creates a format they cannot read, they may not be able to check it. A LaTeX document that compiles may still say the wrong thing. An HTML report that renders may still be inaccessible, hard to print, or incorrect. Someone must still know what good looks like. The work has moved from producing the file to reviewing it.

---

For decades, people were told that some formats were not for them. Often, the problem was the tools, not the people.

Three reports in one week came from people who chose a format they may not have considered a year ago. The format was the least interesting part of each report.

## References

- [Digital Science: AI writing tools for 20 million Overleaf users](https://www.digital-science.com/blog/2025/06/digital-science-launches-new-cutting-edge-ai-writing-tools-for-20-million-overleaf-users/)
- [Anthropic Economic Index](https://www.anthropic.com/research/economic-index-june-2026-report)
- [Collins Word of the Year 2025](https://blog.collinsdictionary.com/language-lovers/collins-word-of-the-year-2025-ai-meets-authenticity-as-society-shifts/)
- [MermaidSeqBench](https://arxiv.org/html/2511.14967v1)
- [Typst: a possible LaTeX replacement (LWN)](https://lwn.net/Articles/1037577/)
