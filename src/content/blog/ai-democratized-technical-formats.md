---
title: The Formats Nobody Was Supposed to Write
description: "Three colleagues sent me reports in HTML last week, and none of them writes code. We also produce LaTeX-quality documents without ever opening a LaTeX editor. The formats that used to require a specialist are now just another thing you can ask for."
pubDate: 2026-08-14
---

Three different colleagues sent me reports in HTML last week. Not one of them thought it was a strange thing to be asked for.

None of them writes code. None of them opened a text editor with syntax highlighting, and I doubt any of them could tell me what a closing tag is. They sent the file, I opened it in a browser, and it looked exactly like a report should look. The brand guidelines were followed to the letter. And each one read just as well on my phone as on my laptop, which is something the PDFs I normally receive have never managed.

Before agents, that would have been unthinkable.

## What "send it in HTML" used to mean

Two years ago, asking a non-technical colleague for an HTML report was an act of hostility.

It meant: go learn a markup language, learn enough CSS to make it not look like 1998, install something to write it in, then debug the gap between what you meant and what the browser decided to show you. Nobody does that for a Tuesday report. They send a Word document, or a PDF exported from a Word document, and you accept it.

The format was never the hard part. The syntax tax was.

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

HTML is a good format for a report. One file, opens on any device without a license, prints to PDF, can hold a table that sorts itself or a chart that responds to a hover, and it will still open in forty years. The only reason it wasn't the default for internal documents is that writing it required a specialist.

That reason is gone.

## Then the same thing happened with LaTeX

The second half of this story surprised me more.

We have adopted LaTeX-style documents to produce perfectly typeset material: contracts, technical annexes, one-page summaries with real typography, mathematical notation that isn't a screenshot of an equation. Documents that look like they came out of a university press instead of a word processor.

And nobody on the team has opened TeXstudio. Not once. No TeX Live install, no package manager, no fifteen-minute detour to find out which of four incompatible ways to place a figure is the one that works this decade.

> LaTeX was never hard because of the typesetting. It was hard because of everything you had to survive before the typesetting started.

For forty years, LaTeX was effectively reserved for scientific and academic professionals, and mostly for the subset of them stubborn enough to push through the toolchain. The output was always worth it. The entry cost meant almost nobody outside academia ever found out.

Now the entry cost is a sentence.

## The evidence that this is happening everywhere

I wanted to check whether this was just my own bubble. It isn't.

**Documents are now the main thing people build.** Anthropic's Economic Index found that documents and reports are the largest category of work output, at 20% of work conversations, ahead of code. The default output of these tools is a document, not a program.

**The LaTeX platforms are selling relief from LaTeX.** In June 2025, Overleaf shipped AI writing tools to its 20 million-plus users, promising they would "spend less time wrestling with LaTeX code." When the largest LaTeX platform in the world describes its own syntax as the obstacle, the argument is over. Typst, a newer alternative with much friendlier markup, is meanwhile moving from curiosity to something journals accept.

**The language caught up too.** Collins named "vibe coding" its Word of the Year for 2025: describing what you want in plain language and letting the machine write the code. Dictionaries don't do that for niche practices.

The number I keep coming back to is the first one. Documents outrank code, which means the people driving this are not developers.

## Other formats that fell over

HTML and LaTeX are the two I noticed because they landed in my inbox. They are not the only ones.

| The format | What used to guard it |
| --- | --- |
| HTML & CSS | a front-end developer |
| LaTeX | TeX Live, TeXstudio, a 300-page manual |
| SVG | a designer and a licensed editor |
| Mermaid & Graphviz | a diagramming tool and its lock-in |

The formats haven't changed. The gatekeepers are optional now.

A few worth calling out:

1. **SVG.** People are producing vector graphics good enough to publish, including the two figures in this post, without touching a drawing tool. A diagram becomes text you can edit, diff, and version.
2. **Mermaid and Graphviz.** Diagrams-as-code went from a developer habit to a default output. There is now a published benchmark, MermaidSeqBench, built to measure how well models turn a description into a Mermaid sequence diagram. Nobody builds a benchmark for something nobody generates.
3. **Markdown.** It became the native tongue of these tools, so millions of people are writing structured documents with real headings and hierarchy while thinking they are just typing.
4. **Anything shaped like configuration.** YAML, JSON, TOML, iCal, GeoJSON, BibTeX. Formats where the concept is trivial and the punctuation is unforgiving, which is exactly the kind of problem a model handles well.

The formats that fell are the ones where the difficulty lived in the notation rather than in the thinking.

## What is actually being democratized

There is a version of this claim that is wrong, so let me be careful with it.

Nobody has been handed taste. The three reports I received last week were well formatted, and two of them were well argued, because the people who sent them are good at their jobs. The format came free. The thinking did not, and never will.

What has been democratized is access to the good format. For decades, choosing the right container for your work was a privilege of people who had already paid a technical toll. If you were not a developer, your options were the ones with a toolbar. Everything with better output, better longevity or better precision sat behind a wall of syntax.

> The wall was never protecting anything valuable. It was just there.

There is a real caveat. When someone produces a format they cannot read, they also cannot check it. A LaTeX document that compiles is not necessarily a document that says what you meant. An HTML report that renders is not necessarily accessible, or printable, or correct. Someone still has to know what good looks like. That job did not disappear, it moved from producing to judging, which is a better place for it to sit.

---

For forty years we told people that certain formats were not for them. We were describing a tooling problem, and they heard a statement about themselves.

Three reports in one week, from three people who would have politely refused the request a year ago. The format was the least interesting thing about any of them.

## References

- [Digital Science: AI writing tools for 20 million Overleaf users](https://www.digital-science.com/blog/2025/06/digital-science-launches-new-cutting-edge-ai-writing-tools-for-20-million-overleaf-users/)
- [Anthropic Economic Index](https://www.anthropic.com/research/economic-index-june-2026-report)
- [Collins Word of the Year 2025](https://blog.collinsdictionary.com/language-lovers/collins-word-of-the-year-2025-ai-meets-authenticity-as-society-shifts/)
- [MermaidSeqBench](https://arxiv.org/html/2511.14967v1)
- [Typst: a possible LaTeX replacement (LWN)](https://lwn.net/Articles/1037577/)
