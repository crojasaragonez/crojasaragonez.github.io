---
title: "Open Source Matters More When Software Moves This Fast"
description: "Recent Linux kernel releases, hundreds of Firefox security fixes, and downloadable AI models show what happens when more people can improve the software they depend on."
pubDate: 2026-11-24T12:00:00Z
draft: true
---

On October 18, 2026, Linux 7.3 shipped after a nine-week development cycle. In that time, a record 3,021 developers contributed 18,765 non-merge commits. Of those developers, 807 had never contributed to the kernel before. [LWN’s Linux 7.3 development statistics](https://lwn.net/Articles/1100241/)

That’s what makes open source so relevant right now. AI can make it easier to explore an unfamiliar codebase or try a fix. The Linux numbers show what happens at the other end of that process, when thousands of people’s changes make it into software everyone can use.

## What five Linux releases tell us

Compared with Linux 6.19 in February, Linux 7.3 took in 31% more non-merge commits and more than twice as many first-time contributors. The charts cover five completed mainline releases. Linux 7.4 reached its fourth release candidate on November 22. [Linux Kernel Archives](https://www.kernel.org/doc/html/)

<style>
.content .kernel-activity table {
  margin: 0;
}
.kernel-activity caption {
  padding-bottom: 0.45rem;
  color: var(--text);
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 650;
  text-align: left;
}
.content .kernel-activity th,
.content .kernel-activity td {
  padding: 0.5rem 0.35rem;
  vertical-align: middle;
}
.kernel-activity tbody th {
  border-color: var(--border);
}
.kernel-activity tbody tr:last-child th {
  border-bottom: 0;
}
.kernel-activity .kernel-count {
  font-variant-numeric: tabular-nums;
  text-align: right;
  white-space: nowrap;
}
.kernel-activity .kernel-plot {
  width: 100%;
}
.kernel-activity .kernel-bar {
  display: block;
  height: 0.65rem;
  border-radius: 0.15rem;
  background: linear-gradient(to right,
    var(--accent-soft) 0 var(--first),
    var(--accent) var(--first) var(--total),
    var(--bg-elevated) var(--total) 100%);
}
</style>

<figure class="fig kernel-activity">
<table>
<caption>Non-merge commits in each Linux release</caption>
<thead><tr><th scope="col">Release</th><th class="kernel-plot" aria-hidden="true"></th><th class="kernel-count" scope="col">Commits</th></tr></thead>
<tbody>
<tr><th scope="row">6.19</th><td aria-hidden="true"><span class="kernel-bar" style="--first: 71.72%; --total: 71.72%"></span></td><td class="kernel-count">14,344</td></tr>
<tr><th scope="row">7.0</th><td aria-hidden="true"><span class="kernel-bar" style="--first: 71.25%; --total: 71.25%"></span></td><td class="kernel-count">14,251</td></tr>
<tr><th scope="row">7.1</th><td aria-hidden="true"><span class="kernel-bar" style="--first: 79.25%; --total: 79.25%"></span></td><td class="kernel-count">15,849</td></tr>
<tr><th scope="row">7.2</th><td aria-hidden="true"><span class="kernel-bar" style="--first: 82.09%; --total: 82.09%"></span></td><td class="kernel-count">16,418</td></tr>
<tr><th scope="row">7.3</th><td aria-hidden="true"><span class="kernel-bar" style="--first: 93.83%; --total: 93.83%"></span></td><td class="kernel-count">18,765</td></tr>
</tbody>
</table>
<figcaption>Bars start at zero and share a scale of 20,000 commits.</figcaption>
</figure>

<figure class="fig kernel-activity">
<table>
<caption>Contributors in each Linux release</caption>
<thead><tr><th scope="col">Release</th><th class="kernel-plot" aria-hidden="true"></th><th class="kernel-count" scope="col">First-time</th><th class="kernel-count" scope="col">Total</th></tr></thead>
<tbody>
<tr><th scope="row">6.19</th><td aria-hidden="true"><span class="kernel-bar" style="--first: 10.41%; --total: 66.91%"></span></td><td class="kernel-count">333</td><td class="kernel-count">2,141</td></tr>
<tr><th scope="row">7.0</th><td aria-hidden="true"><span class="kernel-bar" style="--first: 15.28%; --total: 73.81%"></span></td><td class="kernel-count">489</td><td class="kernel-count">2,362</td></tr>
<tr><th scope="row">7.1</th><td aria-hidden="true"><span class="kernel-bar" style="--first: 16.56%; --total: 77.47%"></span></td><td class="kernel-count">530</td><td class="kernel-count">2,479</td></tr>
<tr><th scope="row">7.2</th><td aria-hidden="true"><span class="kernel-bar" style="--first: 19.16%; --total: 82.88%"></span></td><td class="kernel-count">613</td><td class="kernel-count">2,652</td></tr>
<tr><th scope="row">7.3</th><td aria-hidden="true"><span class="kernel-bar" style="--first: 25.22%; --total: 94.41%"></span></td><td class="kernel-count">807</td><td class="kernel-count">3,021</td></tr>
</tbody>
</table>
<figcaption>Cyan marks first-time contributors and blue marks returning contributors. The full bar shows the total on a scale of 0 to 3,200.</figcaption>
</figure>

The charts use Jonathan Corbet’s release-by-release Git analysis for LWN. [6.19](https://lwn.net/Articles/1057302/), [7.0](https://lwn.net/Articles/1066723/), [7.1](https://lwn.net/Articles/1077425/), [7.2](https://lwn.net/Articles/1088776/), [7.3](https://lwn.net/Articles/1100241/)

A driver patch can start with somebody who has the hardware and sees a problem. The relevant subsystem maintainers review changes in their area, and the kernel’s integration tree brings changes from different subsystems together for testing before the next release. The contribution counts tell us how many people got changes through that process. How much AI contributed to the increase is an open question. The kernel’s guidance asks contributors using tools to understand their entire submission and be ready to answer reviewers’ questions. [Linux kernel development process](https://www.kernel.org/doc/html/latest/process/2.Process.html), [kernel guidelines for tool-generated contributions](https://docs.kernel.org/7.2/process/generated-content.html)

## Old bugs are getting a fresh look

In April 2026, Firefox 150 shipped fixes for 271 previously undiscovered security bugs identified in Mozilla’s initial evaluation of Claude Mythos Preview. Mozilla later said it rated 180 of those bugs high severity. The Firefox team had already been finding bugs through fuzzing and manual inspection. AI-assisted review gave it another way to find problems that had survived those efforts. [Mozilla’s Firefox 150 announcement](https://blog.mozilla.org/en/firefox/privacy-security/ai-security-zero-day-vulnerabilities/), [Mozilla’s severity breakdown](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)

A bug report is one step toward a safer browser. Someone still has to confirm the finding, write and review a fix, get it into a release, and get that release onto people’s machines. Faster discovery makes the people and processes behind those steps more valuable.

## Your first contribution can start with something you use

Say you use a library every week and spot a quick-start example that fails on a fresh install. You can read the contribution guide, reproduce the problem, and send the maintainer the exact command, version, and expected result. If the fix is small, you can open a pull request. An AI assistant can help you find where the example lives or explain how the documentation tests run. You can verify the change by following the updated example from a clean environment. [GitHub’s guide to contributing to open source](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source)

That first contribution is easier when you already care about the result. You know what the project does for you and can tell whether your change makes it better. A short, verified fix saves the maintainer time and saves the next user from hitting the same problem.

## Open weights let you run the model yourself

Model weights are the numerical parameters learned during training. When a developer releases them, you can download a copy and run it on hardware you control, subject to the license and the model’s hardware requirements. OpenAI’s `gpt-oss-20b` and `gpt-oss-120b` are examples released under Apache 2.0. A team evaluating a model for document search can run a specific version on its own infrastructure and keep the documents and queries there. [OpenAI’s gpt-oss release](https://openai.com/index/introducing-gpt-oss/)

The Open Source Initiative’s definition of open source AI asks for the code used to train and run the model and enough information about its training data to build a substantially equivalent system, alongside the weights. Ai2’s Olmo 3 shows what sharing more can enable. It publishes training data, code, and intermediate checkpoints so researchers can compare what the model could do at different stages of training. [Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition), [Ai2’s Olmo 3 release](https://allenai.org/blog/olmo3)

The next time a dependency wastes an hour of your day, think about what would have saved you that hour. It might be a package someone could build once, a test that catches the bug you found, or two lines in the docs. Open source gives you a way to leave that fix where the next person can find it.
