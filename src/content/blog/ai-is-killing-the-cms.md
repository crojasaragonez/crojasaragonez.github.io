---
title: AI Is Killing the CMS
description: "The content management system was sold as a way for non-technical people to run their own websites. That promise was never kept. AI assistants finally deliver it, and they do it without the CMS."
pubDate: 2026-08-08
---

Every content management system has been sold with the same promise: *you will not need a developer.*

Log in, click around, change your text, hit publish. No HTML, no JavaScript, no engineer standing between you and your own website.

Let's be honest. That promise was never kept.

## The loop that never closed

I have watched the same scene play out in dozens of small companies. A business owner needs to change a price, swap a photo, or add a page. They log in to the CMS, and within a few minutes they run into something the interface cannot explain: a template that doesn't match, a plugin that needs configuring, a block that refuses to sit where they want it.

So they do what they always did. They call the person who knows.

<figure class="fig">
<svg viewBox="0 0 600 370" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="f1t f1d">
<title id="f1t">The editing loop a CMS was supposed to break</title>
<desc id="f1d">A four step cycle. The owner wants a small change, they open the CMS and start clicking, a template or plugin blocks them, so they call the IT person and wait, which sends them back to the beginning.</desc>
<defs><marker id="a1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#94a3b8"/></marker></defs>
<rect x="20" y="40" width="260" height="120" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/>
<text x="44" y="72" font-size="12" font-weight="600" letter-spacing="1.6" fill="var(--accent-soft)">01</text>
<text x="44" y="104" font-size="16" font-weight="600" fill="var(--text)">The owner wants a</text>
<text x="44" y="127" font-size="16" font-weight="600" fill="var(--text)">small change</text>
<rect x="320" y="40" width="260" height="120" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/>
<text x="344" y="72" font-size="12" font-weight="600" letter-spacing="1.6" fill="var(--accent-soft)">02</text>
<text x="344" y="104" font-size="16" font-weight="600" fill="var(--text)">They open the CMS</text>
<text x="344" y="127" font-size="16" font-weight="600" fill="var(--text)">and start clicking</text>
<rect x="320" y="200" width="260" height="120" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/>
<text x="344" y="232" font-size="12" font-weight="600" letter-spacing="1.6" fill="var(--accent-soft)">03</text>
<text x="344" y="264" font-size="16" font-weight="600" fill="var(--text)">A template or plugin</text>
<text x="344" y="287" font-size="16" font-weight="600" fill="var(--text)">gets in the way</text>
<rect x="20" y="200" width="260" height="120" rx="2" fill="var(--bg-elevated)" stroke="var(--accent-deep)"/>
<text x="44" y="232" font-size="12" font-weight="600" letter-spacing="1.6" fill="var(--accent-soft)">04</text>
<text x="44" y="264" font-size="16" font-weight="600" fill="var(--text)">They call the IT</text>
<text x="44" y="287" font-size="16" font-weight="600" fill="var(--text)">person, and wait</text>
<path d="M288 100 H312" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#a1)"/>
<path d="M450 168 V192" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#a1)"/>
<path d="M312 260 H288" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#a1)"/>
<path d="M150 192 V168" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#a1)"/>
<text x="300" y="352" text-anchor="middle" font-size="13" fill="var(--text-muted)">Every &#8220;simple&#8221; change ends up back on someone else&#8217;s to-do list.</text>
</svg>
<figcaption>The loop the CMS was supposed to break, and never did.</figcaption>
</figure>

The CMS did not remove the technical person from the process. It moved them one step further away and gave everyone a login screen to feel good about.

> The CMS never made websites easy to edit. It only made them easy to log in to.

## What actually changed

Tools like Claude, Cursor, Codex, and Google Antigravity changed the shape of the problem.

A person can now write, in plain language, *"add a page about our new summer menu, use the same style as the others, and put it in the top navigation"*, and get exactly that. Not a form to fill in. Not a block to drag. The actual change, made in the actual files, ready to publish.

The difference is subtle but decisive:

1. **A CMS gave people a restricted interface** to a system they still did not understand. Anything the interface did not anticipate was out of reach.
2. **An AI assistant gives people plain language** over the whole thing. Nothing is out of reach, because nothing has to be anticipated in advance.

For twenty years we tried to solve a language problem with a user interface. The answer turned out to be language.

## This blog is the proof

There is no backend behind this site. No WordPress. No headless CMS, no admin panel, no API, no database. Just text files that get turned into plain, static HTML pages and served as-is.

When I want a new post, I describe it. When I want to change the layout, I describe that too. If I handed this repository tomorrow to someone who has never written a line of code, they could keep it running with any of the tools above, and the site would never notice the difference.

That is not a clever trick. It is what most small websites should have looked like all along.

## Far fewer moving parts

The hidden cost of a CMS was never the license. It was everything the CMS dragged along with it.

<figure class="fig">
<svg viewBox="0 0 600 350" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="f3t f3d">
<title id="f3t">Moving parts behind a CMS page versus a static page</title>
<desc id="f3d">A CMS-backed page has seven moving parts: browser request, CDN or cache, PHP runtime, CMS core, plugins and themes, database, and backups and security patches. A static page has two: browser request and an HTML file on a CDN.</desc>
<text x="20" y="30" font-size="16" font-weight="600" fill="var(--text)">A CMS-backed page</text>
<text x="20" y="50" font-size="12.5" fill="var(--text-muted)">7 moving parts</text>
<rect x="20" y="68" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="68" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="88" font-size="14" fill="var(--text)">Browser request</text>
<rect x="20" y="105" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="105" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="125" font-size="14" fill="var(--text)">CDN / cache</text>
<rect x="20" y="142" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="142" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="162" font-size="14" fill="var(--text)">Application runtime</text>
<rect x="20" y="179" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="179" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="199" font-size="14" fill="var(--text)">CMS core</text>
<rect x="20" y="216" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="216" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="236" font-size="14" fill="var(--text)">Plugins &amp; themes</text>
<rect x="20" y="253" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="253" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="273" font-size="14" fill="var(--text)">Database</text>
<rect x="20" y="290" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="20" y="290" width="3" height="30" fill="var(--accent-deep)"/><text x="38" y="310" font-size="14" fill="var(--text)">Backups &amp; security patches</text>
<text x="310" y="30" font-size="16" font-weight="600" fill="var(--text)">A static page</text>
<text x="310" y="50" font-size="12.5" fill="var(--text-muted)">2 moving parts</text>
<rect x="310" y="68" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="310" y="68" width="3" height="30" fill="var(--accent-soft)"/><text x="328" y="88" font-size="14" fill="var(--text)">Browser request</text>
<rect x="310" y="105" width="270" height="30" rx="2" fill="var(--bg-elevated)" stroke="var(--border)"/><rect x="310" y="105" width="3" height="30" fill="var(--accent-soft)"/><text x="328" y="125" font-size="14" fill="var(--text)">An HTML file on a CDN</text>
<rect x="310" y="142" width="270" height="178" rx="2" fill="none" stroke="var(--border)" stroke-dasharray="4 5"/>
<text x="445" y="218" text-anchor="middle" font-size="14" fill="var(--text-muted)">No server. No database.</text>
<text x="445" y="242" text-anchor="middle" font-size="14" fill="var(--text-muted)">Nothing to patch at 2 a.m.</text>
</svg>
<figcaption>Every box on the left is something that can break, expire, or need updating. The right side has almost nothing to go wrong.</figcaption>
</figure>

A static site cannot be hacked through a plugin it does not have. It cannot go down because a database ran out of connections. It does not need an urgent security update on a Friday afternoon.

## What this does to the bill

I have helped a few friends migrate old websites, the kind that needed a technical person permanently on call. None of them are technical people, and none of them have needed me since.

The clearest change was the invoice.

<figure class="fig">
<svg viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="f2t f2d">
<title id="f2t">Monthly cost of a small business website, before and after</title>
<desc id="f2d">A traditional CMS stack costs roughly 100 dollars a month: 25 for managed hosting, 15 for plugins and themes, and 60 amortized for someone technical on call. A static site with an AI assistant costs roughly 21 dollars a month: nothing for hosting, 1.25 for the domain, and 20 for the assistant.</desc>
<text x="20" y="44" font-size="16" font-weight="600" fill="var(--text)">Traditional CMS stack</text>
<rect x="20" y="56" width="112.5" height="40" fill="#7c5cff"/>
<rect x="132.5" y="56" width="67.5" height="40" fill="#4f8cff"/>
<rect x="200" y="56" width="270" height="40" fill="#35d6ff"/>
<text x="76" y="81" text-anchor="middle" font-size="13" font-weight="600" fill="#f8fafc">$25</text>
<text x="166" y="81" text-anchor="middle" font-size="13" font-weight="600" fill="#f8fafc">$15</text>
<text x="335" y="81" text-anchor="middle" font-size="13" font-weight="600" fill="#0b0f19">$60</text>
<text x="486" y="82" font-size="17" font-weight="700" fill="var(--text)">&#8776; $100 / mo</text>
<text x="20" y="124" font-size="12.5" fill="var(--text-muted)">Managed hosting $25 &#183; Plugins &amp; themes $15 &#183; Someone technical on call $60</text>
<text x="20" y="180" font-size="16" font-weight="600" fill="var(--text)">Static site + AI assistant</text>
<rect x="20" y="192" width="5.6" height="40" fill="#7c5cff"/>
<rect x="25.6" y="192" width="90" height="40" fill="#4f8cff"/>
<text x="70" y="217" text-anchor="middle" font-size="13" font-weight="600" fill="#f8fafc">$20</text>
<rect x="115.6" y="192" width="354.4" height="40" fill="none" stroke="var(--border)" stroke-dasharray="4 5"/>
<text x="293" y="217" text-anchor="middle" font-size="12.5" fill="var(--text-muted)">no longer on the bill</text>
<text x="486" y="218" font-size="17" font-weight="700" fill="var(--text)">&#8776; $21 / mo</text>
<text x="20" y="260" font-size="12.5" fill="var(--text-muted)">Static hosting $0 &#183; Domain $1.25 &#183; AI assistant $20, already paid for other work</text>
</svg>
<figcaption>Illustrative monthly costs for a small business site, based on the migrations I have helped with. The exact numbers vary. The shape of the comparison does not.</figcaption>
</figure>

Hosting a small website used to be a recurring expense with a recurring dependency attached. Now the hosting is free, the domain costs about as much as a coffee, and the only real subscription is a tool that most people already pay for and use for a dozen other things.

## To be fair, the CMS is not dead everywhere

A newsroom with two hundred authors needs editorial workflows, scheduled publishing, per-role permissions, and review queues. A large retailer needs a product catalog in nine languages with inventory behind it. In those places a CMS is genuine infrastructure, and it earns every dollar it costs.

But that was never the market that made the CMS universal.

The universal market was the restaurant, the law firm, the clinic, the consultancy, the small agency: sites of five to thirty pages that change a handful of times a year. For all of them, the CMS was always too much machine for too little content, and now there is something better suited to the job.

---

## What this really means

The CMS is not dying because it is bad software. Much of it is excellent software, built by people who were solving a real problem with the best tools available at the time.

It is dying because the problem it was built to solve, *letting non-technical people change a website*, has finally been solved properly.

> And the solution did not look like a CMS at all. It looked like a conversation.
