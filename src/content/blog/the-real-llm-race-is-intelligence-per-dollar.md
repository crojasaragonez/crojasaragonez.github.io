---
title: "The Real LLM Race Is Intelligence per Dollar"
description: "Benchmark scores tell us what a model can do. Cost, reliability, and time tell us whether it is worth using."
pubDate: 2026-09-10
draft: false
---

<div class="paper-kicker">Analysis · September 2026</div>

A model release can make headlines for beating a benchmark by a few points. For a team building with AI, the more useful question is often simpler: **what does it cost to get a result we can actually use?**

Imagine a coding assistant that produces a patch for a few cents, but leaves a developer with twenty minutes of cleanup. A more expensive model could be the better deal if its patch takes two minutes to review. The API bill captures only part of the cost.

That is what I mean by *intelligence per dollar*: useful work delivered within a budget, with an acceptable error rate and waiting time. A benchmark score helps us assess capability. It takes a workflow evaluation to establish value.

The evidence below brings together a September 2026 comparison and an older price series. I also propose a way to think about reliability, cost, and time together. The price data supports a specific claim: reaching some benchmark thresholds became much cheaper. It does not establish how quickly the total cost of reliable work has fallen.

## What the price tag leaves out

Per-token pricing is easy to compare. The cost of finishing a task is harder.

Models can use different numbers of tokens, spend different amounts of time reasoning, or need several attempts. Tool calls and human review add costs of their own. A cheap response can become an expensive result if someone has to keep fixing it.

For a real deployment, I would track total spending across the workload and divide it by the number of accepted results. Failed attempts belong in that bill too. I would also measure completion time through validation, including how often tasks miss their deadline or never finish.

Artificial Analysis provides a useful starting point: a weighted average token cost per benchmark task, based on actual token consumption. This is still an evaluation cost, rather than a full production bill. [Methodology and measurements](https://artificialanalysis.ai/models/).

<figure class="fig data-figure">
<svg viewBox="0 0 700 430" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="f1t f1d">
<title id="f1t">Quality versus cost for eleven selected models</title>
<desc id="f1d">Eleven selected models plotted by Artificial Analysis Intelligence Index and token cost per benchmark task. Six observations lie on this sample's cost–quality frontier, including Claude Fable 5.1. Calculations use unrounded source values.</desc>
<text x="350" y="28" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text)">Quality–cost frontier, September 2026</text>
<g stroke="var(--border)" stroke-width="1"><line x1="95" y1="325" x2="640" y2="325"/><line x1="95" y1="263" x2="640" y2="263"/><line x1="95" y1="200" x2="640" y2="200"/><line x1="95" y1="138" x2="640" y2="138"/><line x1="95" y1="75" x2="640" y2="75"/><line x1="95" y1="325" x2="95" y2="75"/><line x1="368" y1="325" x2="368" y2="75"/><line x1="640" y1="325" x2="640" y2="75"/></g>
<g fill="var(--text-muted)" font-size="11"><text x="82" y="329" text-anchor="end">35</text><text x="82" y="267" text-anchor="end">40</text><text x="82" y="204" text-anchor="end">45</text><text x="82" y="142" text-anchor="end">50</text><text x="82" y="79" text-anchor="end">55</text><text x="95" y="346" text-anchor="middle">$0.10</text><text x="368" y="346" text-anchor="middle">$1</text><text x="640" y="346" text-anchor="middle">$10</text></g>
<line x1="95" y1="325" x2="640" y2="325" stroke="var(--border-strong)"/><line x1="95" y1="325" x2="95" y2="75" stroke="var(--border-strong)"/>
<text x="368" y="397" text-anchor="middle" font-size="13" fill="var(--text-muted)">Cost per Intelligence Index task, USD (logarithmic scale) →</text>
<text x="24" y="200" transform="rotate(-90 24 200)" text-anchor="middle" font-size="13" fill="var(--text-muted)">Artificial Analysis Intelligence Index →</text>
<path d="M163.44 293.69 L210.44 268.18 L393.22 247.67 L423.48 160.39 L507.26 102.32 L607.98 95.33" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
<circle cx="607.98" cy="95.33" r="6" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>
<text x="615.98" y="110.33" text-anchor="start" fill="var(--text-muted)" font-size="10.5">Fable</text>
<circle cx="507.26" cy="102.32" r="6" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>
<text x="507.26" y="87.32" text-anchor="middle" fill="var(--text-muted)" font-size="10.5">GPT-6</text>
<circle cx="576.72" cy="128.75" r="5" fill="var(--bg-elevated)" stroke="var(--text-muted)" stroke-width="1.5"/>
<text x="576.72" y="146.75" text-anchor="middle" fill="var(--text-muted)" font-size="10.5">Opus</text>
<circle cx="423.48" cy="160.39" r="6" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>
<text x="423.48" y="145.39" text-anchor="middle" fill="var(--text-muted)" font-size="10.5">Muse</text>
<circle cx="449.86" cy="201.80" r="5" fill="var(--bg-elevated)" stroke="var(--text-muted)" stroke-width="1.5"/>
<text x="463.86" y="193.80" text-anchor="start" fill="var(--text-muted)" font-size="10.5">GLM</text>
<circle cx="440.87" cy="207.44" r="5" fill="var(--bg-elevated)" stroke="var(--text-muted)" stroke-width="1.5"/>
<text x="422.87" y="229.44" text-anchor="end" fill="var(--text-muted)" font-size="10.5">Grok</text>
<circle cx="449.54" cy="215.20" r="5" fill="var(--bg-elevated)" stroke="var(--text-muted)" stroke-width="1.5"/>
<text x="458.54" y="237.20" text-anchor="start" fill="var(--text-muted)" font-size="10.5">Kimi</text>
<circle cx="393.22" cy="247.67" r="6" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>
<text x="393.22" y="267.67" text-anchor="middle" fill="var(--text-muted)" font-size="10.5">Gemini</text>
<circle cx="210.44" cy="268.18" r="6" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>
<text x="210.44" y="253.18" text-anchor="middle" fill="var(--text-muted)" font-size="10.5">DS Flash</text>
<circle cx="163.44" cy="293.69" r="6" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>
<text x="163.44" y="313.69" text-anchor="middle" fill="var(--text-muted)" font-size="10.5">Luna</text>
<circle cx="320.81" cy="308.96" r="5" fill="var(--bg-elevated)" stroke="var(--text-muted)" stroke-width="1.5"/>
<text x="320.81" y="328.96" text-anchor="middle" fill="var(--text-muted)" font-size="10.5">DS Pro</text>
<g font-size="11"><line x1="460" y1="375" x2="486" y2="375" stroke="var(--accent)" stroke-width="2.5"/><circle cx="473" cy="375" r="4" fill="var(--accent-soft)"/><text x="493" y="379" fill="var(--text-muted)">frontier within this sample</text></g>
</svg>
<figcaption><strong>Figure 1.</strong> Quality and token cost per benchmark task for eleven selected models, using unrounded values. The line connects the six observations on this sample's frontier; it does not describe the full market. Source: <a href="https://artificialanalysis.ai/models/">Artificial Analysis</a>, Intelligence Index v4.3, retrieved September 10, 2026.</figcaption>
</figure>

The highlighted line shows the **cost–quality frontier**: among these eleven observations, each highlighted model offers a score that no cheaper option matches. This helps narrow a shortlist. It does not establish the best model for every application.

The distinction matters at the top. Claude Fable 5.1 and GPT-6 Astra both display a rounded score of 53, but their underlying scores are about 53.37 and 52.81. Both belong on this sample's frontier. That small gap alone does not establish a meaningful performance difference.

This is a selected comparison at the effort settings recorded in the data. Adding other models or changing how much reasoning they use can change the frontier. Artificial Analysis's [broader v4.3 comparison](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3) includes other models and effort settings.

## What became cheaper over time?

To compare across years, it helps to hold the target steady: how much did it cost to reach a given benchmark score?

Epoch AI's historical dataset gives two examples on GPQA Diamond, a benchmark of difficult science questions:

- At the **33% threshold**, matching GPT-4-0314's recorded score, the lowest listed price fell from **$37.50 to $0.1225 per million tokens** between March 2023 and December 2024. That is roughly **306× cheaper**.
- At the **56% threshold**, matching the June 2024 Claude 3.5 Sonnet score, the price fell from **$6.00 to $0.175** between June 2024 and February 2025: roughly **34× cheaper**.

These calculations use Epoch's [published dataset](https://epoch.ai/data/charts/llm-inference-price-trends/lowest_price_models_data.csv) and its blended token-price convention. Matching one score does not mean matching the original model's capabilities across all tasks.

<figure class="fig data-figure">
<svg viewBox="0 0 700 430" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="f2t f2d">
<title id="f2t">Historical minimum inference price at fixed GPQA Diamond capability</title>
<desc id="f2d">Among models meeting a GPQA Diamond score of 33%, the lowest listed token price fell from $37.50 per million tokens in March 2023 to $0.1225 in December 2024. At a 56% threshold, it fell from $6 in June 2024 to $0.175 in February 2025. These are the last improvements in each selected series; the source dataset ends February 5, 2025.</desc>
<text x="350" y="28" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text)">Lowest listed price at fixed GPQA scores</text>
<g stroke="var(--border)" stroke-width="1"><line x1="95" y1="75" x2="640" y2="75"/><line x1="95" y1="151" x2="640" y2="151"/><line x1="95" y1="226" x2="640" y2="226"/><line x1="95" y1="302" x2="640" y2="302"/><line x1="95" y1="325" x2="95" y2="75"/><line x1="328" y1="325" x2="328" y2="75"/><line x1="598" y1="325" x2="598" y2="75"/></g>
<g fill="var(--text-muted)" font-size="11"><text x="82" y="79" text-anchor="end">$100</text><text x="82" y="155" text-anchor="end">$10</text><text x="82" y="230" text-anchor="end">$1</text><text x="82" y="306" text-anchor="end">$0.10</text><text x="82" y="329" text-anchor="end">$0.05</text><text x="112" y="346" text-anchor="middle">Mar 2023</text><text x="328" y="346" text-anchor="middle">Jan 2024</text><text x="598" y="346" text-anchor="middle">Jan 2025</text></g>
<line x1="95" y1="325" x2="640" y2="325" stroke="var(--border-strong)"/><line x1="95" y1="325" x2="95" y2="75" stroke="var(--border-strong)"/>
<text x="368" y="397" text-anchor="middle" font-size="13" fill="var(--text-muted)">Model release date →</text>
<text x="24" y="200" transform="rotate(-90 24 200)" text-anchor="middle" font-size="13" fill="var(--text-muted)">USD per 1M tokens (logarithmic scale) →</text>
<path d="M112 107.3 H368 V167.5 H374 V249.3 H424 V293.6 H584 V295.5" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
<path d="M454 167.5 H524 V200.7 H594 V250.7 H623 V283.8" fill="none" stroke="var(--accent-soft)" stroke-width="2.5"/>
<g fill="var(--accent)" stroke="var(--bg)" stroke-width="1.5"><circle cx="112" cy="107.3" r="5"/><circle cx="368" cy="167.5" r="5"/><circle cx="374" cy="249.3" r="5"/><circle cx="424" cy="293.6" r="5"/><circle cx="584" cy="295.5" r="5"/></g>
<g fill="var(--accent-soft)" stroke="var(--bg)" stroke-width="1.5"><circle cx="454" cy="167.5" r="5"/><circle cx="524" cy="200.7" r="5"/><circle cx="594" cy="250.7" r="5"/><circle cx="623" cy="283.8" r="5"/></g>
<g fill="var(--text-muted)" font-size="10.5"><text x="120" y="103">GPT-4</text><text x="358" y="164" text-anchor="end">Mistral Large</text><text x="364" y="246" text-anchor="end">Claude 3 Haiku</text><text x="424" y="311" text-anchor="middle">Gemini 1.5 Flash</text><text x="578" y="308" text-anchor="end">Phi-4</text><text x="464" y="164">Claude 3.5 Sonnet</text><text x="524" y="218" text-anchor="middle">Gemini 1.5 Pro</text><text x="584" y="247" text-anchor="end">DeepSeek V3</text><text x="613" y="277" text-anchor="end">Gemini 2.0 Flash</text></g>
<g font-size="11"><line x1="114" y1="375" x2="140" y2="375" stroke="var(--accent)" stroke-width="2.5"/><text x="147" y="379" fill="var(--text-muted)">GPQA ≥ 33%</text><line x1="390" y1="375" x2="416" y2="375" stroke="var(--accent-soft)" stroke-width="2.5"/><text x="423" y="379" fill="var(--text-muted)">GPQA ≥ 56%</text></g>
</svg>
<figcaption><strong>Figure 2.</strong> Lowest listed token prices at two GPQA Diamond thresholds. Prices use a 3:1 input-to-output blend. Points mark recorded improvements, with dates as listed by Epoch; the two series' last improvements occur in December 2024 and February 2025. Source: <a href="https://epoch.ai/data-insights/llm-inference-price-trends">Epoch AI</a>, <a href="https://epoch.ai/data/charts/llm-inference-price-trends/lowest_price_models_data.csv">dataset</a> (CC BY 4.0), retrieved September 10, 2026.</figcaption>
</figure>

These are substantial declines, but their scope matters. They measure **price per token at a benchmark threshold**, without accounting for tokens consumed per completed task, retries, review, or latency. The source dataset ends in February 2025; this chart supplies no evidence about the subsequent nineteen months. See [Epoch's methodology](https://epoch.ai/data-insights/llm-inference-price-trends).

For a product team, the useful implication is to revisit model choices. An option that was too expensive when a product was designed may become affordable later. Whether that saves money depends on how it performs in the product's own workflow.

## A proposed way to compare useful work

Price is only one part of the decision. I use **Reliable Intelligence Yield (RIY)** as a proposed framework for bringing quality, serious errors, cost, and time into the same discussion:

<div class="equation" role="math" aria-label="Reliable Intelligence Yield equals quality times one minus the serious-error penalty, divided by cost times time">
  <span class="equation-name">RIY</span>
  <span class="equation-symbol">=</span>
  <span class="equation-fraction"><span>Q × (1 − E)</span><span>C × T</span></span>
</div>

| Term | What it represents |
| --- | --- |
| **Q: Quality** | A score from 0 to 1 on tasks representative of the workload |
| **E: Serious-error penalty** | A severity-weighted penalty from 0 to 1, measured on those tasks |
| **C: Cost** | Average total cost per evaluated task, including retries, tools, and verification |
| **T: Time** | Average elapsed time per evaluated task, through validation or a fixed timeout |

All four terms need the same task set and a fixed evaluation protocol. Unfinished tasks stay in the evaluation and receive the quality score and error penalty specified in advance. Keeping cost and time on a per-evaluated-task basis avoids counting only successful attempts.

A visible failure and a convincing mistake can have very different consequences. A broken code snippet may be caught immediately; a plausible but incorrect calculation may survive review. The error penalty expresses that difference. It needs a published severity scale, and any overlap with the quality score needs to be explicit so the same failure is not penalized twice by accident.

**RIY is a proposal, not an established benchmark or a direct measurement of intelligence.** Its ranking depends on how each term is defined. Multiplying cost by time also penalizes longer reasoning through both terms. That can be appropriate when both resources matter, but it is a choice rather than a law.

For many teams, a simpler rule will be easier to defend: set minimum quality and reliability requirements, set a deadline, then compare total cost per accepted result among the systems that qualify.

## What happens when we try the idea on public data?

The next chart is an exploratory calculation, **RIY-AA**. It combines the Artificial Analysis index divided by 100, its AA-Omniscience non-hallucination measure, cost per task, and decode time in minutes. Dividing the index by 100 rescales it; it does not turn it into a probability of success.

<figure class="fig data-figure">
<svg viewBox="0 0 700 430" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="f3t f3d">
<title id="f3t">Exploratory RIY-AA calculation for selected models</title>
<desc id="f3d">A dot plot of a current RIY proxy for eleven models. Muse Spark 1.3 has the highest value, followed by Gemini 3.8 Flash and GPT-5.6 Luna.</desc>
<text x="350" y="25" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text)">Exploratory yield score: sensitive to assumptions</text>
<text x="350" y="45" text-anchor="middle" font-size="11" fill="var(--text-muted)">RIY-AA = (index / 100) × (1 − hallucination rate) ÷ (cost × decode minutes)</text>
<g stroke="var(--border)" stroke-width="1"><line x1="160" y1="58" x2="160" y2="355"/><line x1="400" y1="58" x2="400" y2="355"/><line x1="640" y1="58" x2="640" y2="355"/></g>
<line x1="160" y1="72" x2="543.83" y2="72" stroke="var(--border)" stroke-width="1.5"/>
<circle cx="543.83" cy="72" r="5" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="148" y="76" fill="var(--text-muted)" font-size="10.5" text-anchor="end">Muse Spark 1.3</text>
<text x="551.83" y="76" fill="var(--text)" font-size="9.5">0.0397</text>
<line x1="160" y1="99" x2="527.85" y2="99" stroke="var(--border)" stroke-width="1.5"/>
<circle cx="527.85" cy="99" r="5" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="148" y="103" fill="var(--text-muted)" font-size="10.5" text-anchor="end">Gemini 3.8 Flash</text>
<text x="535.85" y="103" fill="var(--text)" font-size="9.5">0.0341</text>
<line x1="160" y1="126" x2="491.52" y2="126" stroke="var(--border)" stroke-width="1.5"/>
<circle cx="491.52" cy="126" r="5" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="148" y="130" fill="var(--text-muted)" font-size="10.5" text-anchor="end">GPT-5.6 Luna</text>
<text x="499.52" y="130" fill="var(--text)" font-size="9.5">0.0241</text>
<line x1="160" y1="153" x2="435.62" y2="153" stroke="var(--border)" stroke-width="1.5"/>
<circle cx="435.62" cy="153" r="5" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="148" y="157" fill="var(--text-muted)" font-size="10.5" text-anchor="end">Grok 4.6</text>
<text x="443.62" y="157" fill="var(--text)" font-size="9.5">0.0141</text>
<line x1="160" y1="180" x2="399.80" y2="180" stroke="var(--border)" stroke-width="1.5"/>
<circle cx="399.80" cy="180" r="5" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="148" y="184" fill="var(--text-muted)" font-size="10.5" text-anchor="end">GLM-5.3</text>
<text x="407.80" y="184" fill="var(--text)" font-size="9.5">0.0100</text>
<line x1="160" y1="207" x2="393.70" y2="207" stroke="var(--border)" stroke-width="1.5"/>
<circle cx="393.70" cy="207" r="5" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="148" y="211" fill="var(--text-muted)" font-size="10.5" text-anchor="end">GPT-6 Astra</text>
<text x="401.70" y="211" fill="var(--text)" font-size="9.5">0.0094</text>
<line x1="160" y1="234" x2="387.74" y2="234" stroke="var(--border)" stroke-width="1.5"/>
<circle cx="387.74" cy="234" r="5" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="148" y="238" fill="var(--text-muted)" font-size="10.5" text-anchor="end">DeepSeek V4.1 Flash</text>
<text x="395.74" y="238" fill="var(--text)" font-size="9.5">0.0089</text>
<line x1="160" y1="261" x2="338.53" y2="261" stroke="var(--border)" stroke-width="1.5"/>
<circle cx="338.53" cy="261" r="5" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="148" y="265" fill="var(--text-muted)" font-size="10.5" text-anchor="end">Kimi K3</text>
<text x="346.53" y="265" fill="var(--text)" font-size="9.5">0.0055</text>
<line x1="160" y1="288" x2="254.04" y2="288" stroke="var(--border)" stroke-width="1.5"/>
<circle cx="254.04" cy="288" r="5" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="148" y="292" fill="var(--text-muted)" font-size="10.5" text-anchor="end">DeepSeek V4 Pro</text>
<text x="262.04" y="292" fill="var(--text)" font-size="9.5">0.0025</text>
<line x1="160" y1="315" x2="250.87" y2="315" stroke="var(--border)" stroke-width="1.5"/>
<circle cx="250.87" cy="315" r="5" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="148" y="319" fill="var(--text-muted)" font-size="10.5" text-anchor="end">Claude Opus 5</text>
<text x="258.87" y="319" fill="var(--text)" font-size="9.5">0.0024</text>
<line x1="160" y1="342" x2="206.86" y2="342" stroke="var(--border)" stroke-width="1.5"/>
<circle cx="206.86" cy="342" r="5" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="148" y="346" fill="var(--text-muted)" font-size="10.5" text-anchor="end">Claude Fable 5.1</text>
<text x="214.86" y="346" fill="var(--text)" font-size="9.5">0.0016</text>
<line x1="160" y1="355" x2="640" y2="355" stroke="var(--border-strong)"/>
<g fill="var(--text-muted)" font-size="11"><text x="160" y="375" text-anchor="middle">0.001</text><text x="400" y="375" text-anchor="middle">0.01</text><text x="640" y="375" text-anchor="middle">0.1</text><text x="400" y="407" text-anchor="middle" font-size="13">RIY-AA (1 / USD-minute; logarithmic scale) →</text></g>
</svg>
<figcaption><strong>Figure 3.</strong> An experimental score for the same eleven models. Calculated from unrounded source inputs, with values rounded for display. This combines a broad capability index with a factual-question error measure and decode time; it is not a validated production-reliability ranking. Source inputs: <a href="https://artificialanalysis.ai/models/">Artificial Analysis</a>, retrieved September 10, 2026.</figcaption>
</figure>

The assumptions behind this chart matter more than the winner:

- **The error measure is narrower than production reliability.** AA-Omniscience defines hallucination rate as incorrect answers divided by incorrect, partially correct, and unanswered questions. Correct answers are excluded from that denominator. It measures guessing when a model fails to answer correctly, rather than the share of all tasks with serious errors. [Benchmark paper](https://arxiv.org/html/2511.13029v1#S2.SS4.SSS3).
- **The inputs cover different tasks.** The index combines ten evaluations; AA-Omniscience is one of them. Applying its error measure across the index adds a separate weight to one kind of behavior. [Index composition](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3).
- **Decode time leaves out part of the wait.** It excludes time to first token and overhead, so it is shorter than a complete workflow measurement. [Time-per-task definition](https://artificialanalysis.ai/models/).

The calculation is also sensitive to values near 100% hallucination. A rate of 96% leaves a multiplier of 0.04; at 97%, it falls to 0.03, a 25% reduction. That is why the chart uses the underlying source values and rounds only the displayed results.

I would treat this as an illustration of how assumptions affect a ranking. I would not select a production model from this score alone. A useful next test would measure quality, serious errors, cost, and complete task time on the same workload, then check whether the ordering survives changes in weights and reasoning effort.

## How I would use this when choosing a model

The practical decision starts with the work:

1. **Define an acceptable result.** Use representative tasks and acceptance criteria that a reviewer can apply consistently.
2. **Set the limits.** Decide how much delay and what kinds of errors the application can tolerate.
3. **Measure the whole bill.** Include failed attempts, retries, tools, and human verification. Report the completion rate alongside cost per accepted result.
4. **Compare the qualifying options.** A low price is useful only if the system meets the requirements.
5. **Recheck when something changes.** Model versions, prices, reasoning settings, and the workload can all affect the decision.

There is no universal exchange rate between benchmark points and business value. An extra point may matter greatly if it lets a system pass a necessary acceptance test. Elsewhere, the same gain may make no practical difference.

That is why intelligence per dollar deserves attention alongside the leaderboard. Better models expand what we can attempt. Lower costs, fewer consequential mistakes, and shorter waits determine how much of that work we can afford to do.

<div class="paper-status"><strong>Data and scope.</strong> Figures 1 and 3 use selected Artificial Analysis observations retrieved September 10, 2026. Figure 2 uses Epoch AI's archival dataset, ending February 5, 2025. I have not run an independent model evaluation or established a historical RIY trend. The <a href="https://github.com/crojasaragonez/crojasaragonez.github.io/tree/main/src/data/riy">supporting CSV files</a> contain the data behind the figures.</div>

## Sources

- [Artificial Analysis: model measurements](https://artificialanalysis.ai/models/) and [Intelligence Index v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3).
- [AA-Omniscience: benchmark paper](https://arxiv.org/abs/2511.13029) and [benchmark introduction](https://artificialanalysis.ai/articles/aa-omniscience-knowledge-hallucination-benchmark).
- [Epoch AI: LLM inference price trends](https://epoch.ai/data-insights/llm-inference-price-trends) and [underlying dataset](https://epoch.ai/data/charts/llm-inference-price-trends/lowest_price_models_data.csv), licensed under CC BY 4.0.
