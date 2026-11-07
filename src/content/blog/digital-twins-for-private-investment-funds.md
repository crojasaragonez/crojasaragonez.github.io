---
title: "Digital Twins for Private Investment Funds"
description: "Engineers test engines and factories on virtual copies before touching the real thing. At Subaxa, we are applying the same idea to our private investment funds."
pubDate: 2026-11-07
draft: false
---

Before a pilot flies a new aircraft, they spend hours in a simulator. Before an engineer changes a production line, they can test the change on a virtual copy of the factory. Mistakes made there cost nothing.

Investors have their own versions of these tools. Scenario analysis, stress tests, and Monte Carlo simulations have been part of finance for decades. They are usually built for a specific decision, though, and left behind as the fund moves on.

At <a href="https://subaxa.com/en/?utm_source=crojasaragonez.github.io&utm_medium=blog&utm_campaign=digital-twins-for-private-investment-funds&referrer=https%3A%2F%2Fcrojasaragonez.github.io%2Fblog%2Fdigital-twins-for-private-investment-funds%2F" target="_blank" rel="noopener">Subaxa</a>, we are experimenting with the next step: building **digital twins** of our private investment funds. This post explains the concept, how digital twins work in the real world, and, at a high level, how we use one to explore decisions before we make them.

## What is a digital twin?

A digital twin is a software model of a real thing that stays connected to it. It has three parts:

1. **The real thing.** A jet engine, a factory, a building, a city, or, in our case, a fund.
2. **The model.** Software that represents how that thing behaves.
3. **The connection.** Data that keeps the model in sync with reality, and decisions that flow back from the model to the real world.

The connection is what separates a twin from an ordinary simulation or spreadsheet. A spreadsheet is usually built once, reflecting what we believed on the day we built it. A twin is updated as the real thing changes, so its picture of the present stays current and its forecasts start from where things actually are.

<figure class="fig">
<svg viewBox="0 0 700 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="dt1t dt1d">
<title id="dt1t">How a digital twin stays connected to the real thing</title>
<desc id="dt1d">On the left, the real asset: a jet engine, a factory line, a city, or an investment fund. On the right, the digital twin, a living model in software that simulates what-if scenarios. Data flows from the real asset into the twin, and decisions flow back from the twin to the real asset, in a continuous loop.</desc>
<defs><marker id="dtarrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="var(--accent)"/></marker></defs>
<text x="350" y="30" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text)">A model that stays connected to reality</text>
<rect x="30" y="65" width="210" height="230" rx="4" fill="var(--bg-elevated)" stroke="var(--border-strong)"/>
<text x="135" y="95" text-anchor="middle" font-size="11" font-weight="600" letter-spacing="1.5" fill="var(--accent-soft)">THE REAL THING</text>
<text x="135" y="119" text-anchor="middle" font-size="13" fill="var(--text)">A physical or financial asset</text>
<g font-size="12.5" fill="var(--text-muted)"><text x="62" y="160">• A jet engine</text><text x="62" y="186">• A factory line</text><text x="62" y="212">• A city</text><text x="62" y="238">• An investment fund</text></g>
<rect x="460" y="65" width="210" height="230" rx="4" fill="var(--bg-elevated)" stroke="var(--accent)"/>
<text x="565" y="95" text-anchor="middle" font-size="11" font-weight="600" letter-spacing="1.5" fill="var(--accent-soft)">THE DIGITAL TWIN</text>
<text x="565" y="119" text-anchor="middle" font-size="13" fill="var(--text)">A living model in software</text>
<g fill="none" stroke="var(--accent-soft)" stroke-width="2"><path d="M495 205 H535"/><path d="M535 205 C565 205 575 160 630 160"/><path d="M535 205 H630"/><path d="M535 205 C565 205 575 250 630 250"/></g>
<circle cx="495" cy="205" r="4" fill="var(--accent-soft)"/>
<g fill="var(--bg-elevated)" stroke="var(--accent-soft)" stroke-width="2"><circle cx="634" cy="160" r="5"/><circle cx="634" cy="205" r="5"/><circle cx="634" cy="250" r="5"/></g>
<text x="565" y="282" text-anchor="middle" font-size="11.5" fill="var(--text-muted)">Simulate “what if?”</text>
<line x1="248" y1="135" x2="452" y2="135" stroke="var(--accent)" stroke-width="2" marker-end="url(#dtarrow)"/>
<text x="350" y="123" text-anchor="middle" font-size="13" font-weight="600" fill="var(--text)">Data flows in</text>
<text x="350" y="155" text-anchor="middle" font-size="11" fill="var(--text-muted)">sensors · transactions · events</text>
<line x1="452" y1="230" x2="248" y2="230" stroke="var(--accent)" stroke-width="2" marker-end="url(#dtarrow)"/>
<text x="350" y="218" text-anchor="middle" font-size="13" font-weight="600" fill="var(--text)">Decisions flow back</text>
<text x="350" y="250" text-anchor="middle" font-size="11" fill="var(--text-muted)">maintain · adjust · invest</text>
<text x="350" y="190" text-anchor="middle" font-size="11" font-style="italic" fill="var(--text-muted)">a continuous loop</text>
</svg>
<figcaption><strong>Figure 1.</strong> The digital twin loop. Data from the real asset keeps the model current; the model is used to test options, and the chosen decisions are applied to the real asset.</figcaption>
</figure>

The idea is not new. Michael Grieves presented the concept in 2002, as a model for managing a product's lifecycle. The name "digital twin" is credited to John Vickers of NASA and appeared in NASA's 2010 technology roadmap. What changed in the last decade is cost: sensors, data storage, and computing power became cheap enough to build twins for far more than rockets.

## How a digital twin works in real life

Aircraft engines are a well-known example. Modern engines carry sensors that record temperatures, pressures, and vibration during flights. Manufacturers such as Rolls-Royce feed that data into models of each engine to monitor its health and estimate when it will need maintenance.

The process usually follows five steps:

1. **Connect.** Collect data from the real asset: sensor readings, transactions, events.
2. **Model.** Represent how the asset behaves. For an engine, how components wear under heat and stress.
3. **Calibrate.** Compare the model's predictions with what actually happens, and adjust it until they agree.
4. **Simulate.** Ask "what if?" What happens if this engine flies more routes in hot climates? What if maintenance is moved up a month?
5. **Act and learn.** Make the decision in the real world, then watch the new data to see whether the twin was right.

The value comes from step four. Instead of discovering a problem when a part fails, the airline can plan maintenance while the aircraft is already on the ground. The same pattern appears in factories that test layout changes before moving equipment, and in cities that model traffic or flooding before building new infrastructure.

## A fund is a system, too

An investment fund has no sensors or moving parts, but it has many of the same characteristics as an engine: components (the investments), processes that take time, money flowing in and out, and decisions that change how everything behaves.

Our funds invest in properties acquired through judicial auctions. Each property follows its own path: the auction, the legal process, taking possession, preparing the property, and eventually selling it. Every step has a range of possible durations and costs. A delay in one property ties up capital that could be working somewhere else, and small delays across many properties add up.

Following the money through a single sale makes this concrete. Every dollar a buyer pays for the property has to cover what the fund spent along the way before any of it becomes profit.

<figure class="fig data-figure">
<svg viewBox="0 0 700 480" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="dt5t dt5d">
<title id="dt5t">Where the money from one property sale goes</title>
<desc id="dt5d">Illustrative example, not Subaxa figures. A property sold for $150,000. Auction price: $90,000; Legal and court costs: $6,000; Repairs and preparation: $10,000; Holding costs: $6,000; Closing costs and taxes: $7,500. Costs total $119,500, leaving a net profit of $30,500, split Investors (80%) $24,400 and Fund manager (20%) $6,100.</desc>
<text x="350.0" y="30" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text)">Where the money from one property sale goes</text>
<path d="M54.0 114.0 C162.0 114.0 162.0 92.0 270.0 92.0 L270.0 331.0 C162.0 331.0 162.0 353.0 54.0 353.0 Z" fill="#fb7185" fill-opacity="0.32"/><path d="M54.0 353.0 C162.0 353.0 162.0 375.0 270.0 375.0 L270.0 436.0 C162.0 436.0 162.0 414.0 54.0 414.0 Z" fill="#34d399" fill-opacity="0.32"/><path d="M284.0 92.0 C377.0 92.0 377.0 78.0 470.0 78.0 L470.0 258.0 C377.0 258.0 377.0 272.0 284.0 272.0 Z" fill="#fb7185" fill-opacity="0.32"/><path d="M284.0 272.0 C377.0 272.0 377.0 270.0 470.0 270.0 L470.0 282.0 C377.0 282.0 377.0 284.0 284.0 284.0 Z" fill="#fb7185" fill-opacity="0.32"/><path d="M284.0 284.0 C377.0 284.0 377.0 294.0 470.0 294.0 L470.0 314.0 C377.0 314.0 377.0 304.0 284.0 304.0 Z" fill="#fb7185" fill-opacity="0.32"/><path d="M284.0 304.0 C377.0 304.0 377.0 326.0 470.0 326.0 L470.0 338.0 C377.0 338.0 377.0 316.0 284.0 316.0 Z" fill="#fb7185" fill-opacity="0.32"/><path d="M284.0 316.0 C377.0 316.0 377.0 350.0 470.0 350.0 L470.0 365.0 C377.0 365.0 377.0 331.0 284.0 331.0 Z" fill="#fb7185" fill-opacity="0.32"/><path d="M284.0 375.0 C377.0 375.0 377.0 377.0 470.0 377.0 L470.0 425.8 C377.0 425.8 377.0 423.8 284.0 423.8 Z" fill="#34d399" fill-opacity="0.32"/><path d="M284.0 423.8 C377.0 423.8 377.0 437.8 470.0 437.8 L470.0 450.0 C377.0 450.0 377.0 436.0 284.0 436.0 Z" fill="#34d399" fill-opacity="0.32"/><rect x="40" y="114.0" width="14" height="300.0" fill="var(--accent)"/><rect x="270" y="92.0" width="14" height="239.0" fill="#fb7185"/><rect x="270" y="375.0" width="14" height="61.0" fill="#34d399"/><rect x="470" y="78.0" width="14" height="180.0" fill="#fb7185"/><text x="494" y="172.0" font-size="12" fill="var(--text)">Auction price <tspan font-weight="600" fill="var(--text-muted)">$90,000</tspan></text><rect x="470" y="270.0" width="14" height="12.0" fill="#fb7185"/><text x="494" y="280.0" font-size="12" fill="var(--text)">Legal and court costs <tspan font-weight="600" fill="var(--text-muted)">$6,000</tspan></text><rect x="470" y="294.0" width="14" height="20.0" fill="#fb7185"/><text x="494" y="308.0" font-size="12" fill="var(--text)">Repairs and preparation <tspan font-weight="600" fill="var(--text-muted)">$10,000</tspan></text><rect x="470" y="326.0" width="14" height="12.0" fill="#fb7185"/><text x="494" y="336.0" font-size="12" fill="var(--text)">Holding costs <tspan font-weight="600" fill="var(--text-muted)">$6,000</tspan></text><rect x="470" y="350.0" width="14" height="15.0" fill="#fb7185"/><text x="494" y="361.5" font-size="12" fill="var(--text)">Closing costs and taxes <tspan font-weight="600" fill="var(--text-muted)">$7,500</tspan></text><rect x="470" y="377.0" width="14" height="48.8" fill="#34d399"/><text x="494" y="405.4" font-size="12" fill="var(--text)">Investors (80%) <tspan font-weight="600" fill="var(--text-muted)">$24,400</tspan></text><rect x="470" y="437.8" width="14" height="12.2" fill="#34d399"/><text x="494" y="447.9" font-size="12" fill="var(--text)">Fund manager (20%) <tspan font-weight="600" fill="var(--text-muted)">$6,100</tspan></text><text x="40" y="88.0" font-size="12.5" font-weight="600" fill="var(--text)">Sale price</text><text x="40" y="104.0" font-size="12" fill="var(--text-muted)">$150,000</text><text x="270" y="66.0" font-size="12.5" font-weight="600" fill="var(--text)">Costs</text><text x="270" y="82.0" font-size="12" fill="var(--text-muted)">$119,500</text><text x="270" y="454.0" font-size="12.5" font-weight="600" fill="var(--text)">Net profit</text><text x="270" y="470.0" font-size="12" fill="var(--text-muted)">$30,500</text>
</svg>
<figcaption><strong>Figure 2.</strong> Illustrative example, not Subaxa figures. Cash distribution for one hypothetical property sold for $150,000, with a simplified 80/20 profit split between investors and the fund manager. Real fund terms usually also include management fees and a preferred return for investors.</figcaption>
</figure>

In this example, about 80 cents of every dollar from the sale covers costs, and about 16 cents reaches investors as profit. A spreadsheet treats each of those flows as a fixed number. In reality, most of them move together: a longer legal process means more legal fees and more holding costs, and the sale price itself is uncertain. A twin varies every flow, for every property, in every simulated run.

A traditional financial model often reduces all of that to a single expected return. Reality delivers a range of outcomes, and two strategies with the same expected return can carry very different risks.

That is the gap our digital twin is meant to fill.

## What our fund twin looks like

We cannot share the details of our models, data, or assumptions: they are a core part of how Subaxa operates. At a high level, though, the structure is similar to any other digital twin.

<figure class="fig">
<svg viewBox="0 0 700 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="dt2t dt2d">
<title id="dt2t">A digital twin of an investment fund at a high level</title>
<desc id="dt2d">Four kinds of input (portfolio and pipeline, market assumptions, legal and operating timelines, cash flow rules) feed a simulation engine that models every asset, its timeline and its cash flows, running thousands of simulated futures per scenario. Scenario levers such as deal size, diversification, pace and timing change the inputs. The outputs are a range of returns, cash and liquidity over time, and the risk of loss and delays.</desc>
<defs><marker id="dtarrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="var(--accent)"/></marker></defs>
<text x="350" y="28" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text)">A fund twin, at a high level</text>
<g font-size="11" font-weight="600" letter-spacing="1.5" fill="var(--accent-soft)" text-anchor="middle"><text x="110" y="60">INPUTS</text><text x="350" y="60">ENGINE</text><text x="600" y="60">OUTPUTS</text></g>
<g fill="var(--bg-elevated)" stroke="var(--border-strong)"><rect x="20" y="75" width="180" height="48" rx="4"/><rect x="20" y="137" width="180" height="48" rx="4"/><rect x="20" y="199" width="180" height="48" rx="4"/><rect x="20" y="261" width="180" height="48" rx="4"/></g>
<g font-size="12.5" fill="var(--text)" text-anchor="middle"><text x="110" y="104">Portfolio and pipeline</text><text x="110" y="166">Market assumptions</text><text x="110" y="228">Legal and operating timelines</text><text x="110" y="290">Cash flow rules</text></g>
<g stroke="var(--accent)" stroke-width="1.5" fill="none" marker-end="url(#dtarrow2)"><path d="M200 99 C235 99 240 170 268 185"/><path d="M200 161 C235 161 240 185 268 190"/><path d="M200 223 C235 223 240 200 268 196"/><path d="M200 285 C235 285 240 210 268 201"/></g>
<rect x="270" y="85" width="160" height="210" rx="4" fill="var(--bg-elevated)" stroke="var(--accent)" stroke-width="1.5"/>
<text x="350" y="115" text-anchor="middle" font-size="14" font-weight="600" fill="var(--text)">The fund twin</text>
<g font-size="11.5" fill="var(--text-muted)" text-anchor="middle"><text x="350" y="138">Models every asset,</text><text x="350" y="154">its timeline and</text><text x="350" y="170">its cash flows</text></g>
<g fill="var(--accent-soft)" fill-opacity="0.75"><circle cx="305" cy="200" r="3"/><circle cx="320" cy="200" r="3"/><circle cx="335" cy="200" r="3"/><circle cx="350" cy="200" r="3"/><circle cx="365" cy="200" r="3"/><circle cx="380" cy="200" r="3"/><circle cx="395" cy="200" r="3"/><circle cx="305" cy="214" r="3"/><circle cx="320" cy="214" r="3"/><circle cx="335" cy="214" r="3"/><circle cx="350" cy="214" r="3"/><circle cx="365" cy="214" r="3"/><circle cx="380" cy="214" r="3"/><circle cx="395" cy="214" r="3"/><circle cx="305" cy="228" r="3"/><circle cx="320" cy="228" r="3"/><circle cx="335" cy="228" r="3"/><circle cx="350" cy="228" r="3"/><circle cx="365" cy="228" r="3"/><circle cx="380" cy="228" r="3"/><circle cx="395" cy="228" r="3"/></g>
<g font-size="11.5" fill="var(--text-muted)" text-anchor="middle"><text x="350" y="260">Thousands of simulated</text><text x="350" y="276">futures per scenario</text></g>
<rect x="225" y="340" width="250" height="56" rx="4" fill="var(--bg-elevated)" stroke="var(--accent-deep)"/>
<text x="350" y="362" text-anchor="middle" font-size="11" font-weight="600" letter-spacing="1.5" fill="var(--accent-deep)">SCENARIO LEVERS</text>
<text x="350" y="383" text-anchor="middle" font-size="12" fill="var(--text)">deal size · diversification · pace · timing</text>
<line x1="350" y1="340" x2="350" y2="298" stroke="var(--accent-deep)" stroke-width="1.5" marker-end="url(#dtarrow2)"/>
<g stroke="var(--accent)" stroke-width="1.5" fill="none" marker-end="url(#dtarrow2)"><path d="M430 185 C465 175 480 120 508 116"/><path d="M430 190 H508"/><path d="M430 195 C465 205 480 260 508 264"/></g>
<g fill="var(--bg-elevated)" stroke="var(--border-strong)"><rect x="510" y="92" width="180" height="48" rx="4"/><rect x="510" y="166" width="180" height="48" rx="4"/><rect x="510" y="240" width="180" height="48" rx="4"/></g>
<g font-size="12.5" fill="var(--text)" text-anchor="middle"><text x="600" y="121">A range of returns</text><text x="600" y="195">Cash and liquidity over time</text><text x="600" y="269">Risk of loss and delays</text></g>
</svg>
<figcaption><strong>Figure 3.</strong> A simplified view of a fund twin. The inputs describe the fund and its environment, the levers describe the decisions we want to test, and the outputs describe a range of outcomes rather than a single number.</figcaption>
</figure>

- **Inputs** describe the fund as it is today: the properties it holds, the opportunities in its pipeline, market assumptions, typical timelines for each stage, and the rules for how cash comes in and goes out.
- **The engine** models each asset individually and runs thousands of simulated futures. In each run, durations, costs, and sale prices vary within plausible ranges.
- **Levers** are the decisions we want to evaluate: how large each investment should be, how diversified the portfolio is, how quickly capital is deployed, or when to sell.
- **Outputs** are distributions, not single numbers: the range of possible returns, how cash and liquidity evolve over time, and the probability of losses or long delays.

As properties are bought and sold, real results feed back into the twin. That lets us check our assumptions against what actually happened and recalibrate the model.

## One plan, many futures

To illustrate the idea without revealing anything about Subaxa, I built a deliberately simple toy model: a fund that invests its capital in six properties over its first ten months and sells each one after a random legal and sales process. Some properties run into complications that add time and reduce their value. None of the numbers below are Subaxa's.

This toy model shows only the simulation part of a twin. It is not connected to any real fund. That connection, starting every simulation from the fund's actual state and recalibrating it as real results come in, is what turns a simulation into a twin.

Running that one plan 2,000 times produces the picture below.

<figure class="fig data-figure">
<svg viewBox="0 0 700 430" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="dt3t dt3d">
<title id="dt3t">Range of simulated fund value paths</title>
<desc id="dt3d">Illustrative simulation of 2000 paths for a toy property fund over 48 months, indexed to 100 at launch. The median path ends near 132; 80% of paths end between 111 and 157.</desc>
<text x="350.0" y="30" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text)">2,000 simulated futures for one illustrative fund</text>
<line x1="80" y1="340.0" x2="640" y2="340.0" stroke="var(--border)"/><text x="68" y="344.0" text-anchor="end" font-size="11" fill="var(--text-muted)">90</text><line x1="80" y1="306.2" x2="640" y2="306.2" stroke="var(--border)"/><text x="68" y="310.2" text-anchor="end" font-size="11" fill="var(--text-muted)">100</text><line x1="80" y1="272.5" x2="640" y2="272.5" stroke="var(--border)"/><text x="68" y="276.5" text-anchor="end" font-size="11" fill="var(--text-muted)">110</text><line x1="80" y1="238.8" x2="640" y2="238.8" stroke="var(--border)"/><text x="68" y="242.8" text-anchor="end" font-size="11" fill="var(--text-muted)">120</text><line x1="80" y1="205.0" x2="640" y2="205.0" stroke="var(--border)"/><text x="68" y="209.0" text-anchor="end" font-size="11" fill="var(--text-muted)">130</text><line x1="80" y1="171.2" x2="640" y2="171.2" stroke="var(--border)"/><text x="68" y="175.2" text-anchor="end" font-size="11" fill="var(--text-muted)">140</text><line x1="80" y1="137.5" x2="640" y2="137.5" stroke="var(--border)"/><text x="68" y="141.5" text-anchor="end" font-size="11" fill="var(--text-muted)">150</text><line x1="80" y1="103.8" x2="640" y2="103.8" stroke="var(--border)"/><text x="68" y="107.8" text-anchor="end" font-size="11" fill="var(--text-muted)">160</text><line x1="80" y1="70.0" x2="640" y2="70.0" stroke="var(--border)"/><text x="68" y="74.0" text-anchor="end" font-size="11" fill="var(--text-muted)">170</text><text x="80.0" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">0</text><text x="220.0" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">12</text><text x="360.0" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">24</text><text x="500.0" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">36</text><text x="640.0" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">48</text>
<line x1="80" y1="306.2" x2="640" y2="306.2" stroke="var(--border-strong)" stroke-dasharray="4 4"/>
<path d="M80.0 306.2 L91.7 306.2 L103.3 306.2 L115.0 306.2 L126.7 306.2 L138.3 306.2 L150.0 306.2 L161.7 306.2 L173.3 306.2 L185.0 306.2 L196.7 306.2 L208.3 306.2 L220.0 306.2 L231.7 287.9 L243.3 273.8 L255.0 263.5 L266.7 253.2 L278.3 244.1 L290.0 229.7 L301.7 218.3 L313.3 205.3 L325.0 191.5 L336.7 181.4 L348.3 172.9 L360.0 162.9 L371.7 153.3 L383.3 143.2 L395.0 135.5 L406.7 132.3 L418.3 125.6 L430.0 121.3 L441.7 119.7 L453.3 116.7 L465.0 115.3 L476.7 114.3 L488.3 114.2 L500.0 113.6 L511.7 113.6 L523.3 112.7 L535.0 112.7 L546.7 113.7 L558.3 113.7 L570.0 113.7 L581.7 113.7 L593.3 113.7 L605.0 113.7 L616.7 113.7 L628.3 113.7 L640.0 113.7 L640.0 269.4 L628.3 269.4 L616.7 269.4 L605.0 269.6 L593.3 269.6 L581.7 269.6 L570.0 269.4 L558.3 269.4 L546.7 269.0 L535.0 268.8 L523.3 268.7 L511.7 268.2 L500.0 268.1 L488.3 267.9 L476.7 267.6 L465.0 268.1 L453.3 268.3 L441.7 269.2 L430.0 271.8 L418.3 273.8 L406.7 277.1 L395.0 281.8 L383.3 284.8 L371.7 287.1 L360.0 293.0 L348.3 297.1 L336.7 304.3 L325.0 306.2 L313.3 306.2 L301.7 306.2 L290.0 306.2 L278.3 306.2 L266.7 306.2 L255.0 306.2 L243.3 306.2 L231.7 306.2 L220.0 306.2 L208.3 306.2 L196.7 306.2 L185.0 306.2 L173.3 306.2 L161.7 306.2 L150.0 306.2 L138.3 306.2 L126.7 306.2 L115.0 306.2 L103.3 306.2 L91.7 306.2 L80.0 306.2 Z" fill="var(--accent)" fill-opacity="0.2"/>
<path d="M80.0 306.2 L91.7 306.2 L103.3 306.2 L115.0 306.2 L126.7 306.2 L138.3 306.2 L150.0 306.2 L161.7 306.2 L173.3 306.2 L185.0 306.2 L196.7 306.2 L208.3 306.2 L220.0 306.2 L231.7 306.2 L243.3 306.2 L255.0 291.8 L266.7 279.2 L278.3 270.3 L290.0 259.3 L301.7 249.3 L313.3 235.7 L325.0 225.6 L336.7 216.1 L348.3 207.7 L360.0 196.8 L371.7 188.8 L383.3 180.9 L395.0 175.7 L406.7 169.5 L418.3 165.2 L430.0 160.4 L441.7 157.9 L453.3 155.1 L465.0 154.1 L476.7 154.0 L488.3 153.4 L500.0 152.6 L511.7 152.3 L523.3 152.7 L535.0 152.7 L546.7 153.2 L558.3 153.4 L570.0 153.5 L581.7 153.5 L593.3 153.5 L605.0 153.5 L616.7 153.5 L628.3 153.5 L640.0 153.5 L640.0 237.5 L628.3 237.5 L616.7 237.5 L605.0 237.5 L593.3 237.5 L581.7 237.6 L570.0 237.5 L558.3 237.5 L546.7 237.4 L535.0 237.2 L523.3 236.9 L511.7 237.0 L500.0 236.6 L488.3 236.8 L476.7 236.9 L465.0 237.6 L453.3 239.0 L441.7 240.7 L430.0 242.0 L418.3 245.2 L406.7 248.7 L395.0 252.5 L383.3 256.0 L371.7 261.4 L360.0 266.9 L348.3 272.7 L336.7 281.4 L325.0 290.4 L313.3 296.9 L301.7 305.5 L290.0 306.2 L278.3 306.2 L266.7 306.2 L255.0 306.2 L243.3 306.2 L231.7 306.2 L220.0 306.2 L208.3 306.2 L196.7 306.2 L185.0 306.2 L173.3 306.2 L161.7 306.2 L150.0 306.2 L138.3 306.2 L126.7 306.2 L115.0 306.2 L103.3 306.2 L91.7 306.2 L80.0 306.2 Z" fill="var(--accent)" fill-opacity="0.32"/>
<path d="M80.0 306.2 L91.7 306.2 L103.3 306.2 L115.0 306.2 L126.7 306.2 L138.3 306.2 L150.0 306.2 L161.7 306.2 L173.3 306.2 L185.0 306.2 L196.7 306.2 L208.3 306.2 L220.0 306.2 L231.7 306.2 L243.3 306.2 L255.0 306.2 L266.7 306.2 L278.3 298.2 L290.0 288.2 L301.7 279.0 L313.3 269.4 L325.0 260.8 L336.7 251.6 L348.3 242.3 L360.0 234.2 L371.7 227.9 L383.3 222.2 L395.0 217.3 L406.7 212.7 L418.3 209.1 L430.0 206.3 L441.7 202.9 L453.3 201.5 L465.0 200.1 L476.7 199.5 L488.3 199.3 L500.0 199.3 L511.7 199.6 L523.3 199.6 L535.0 199.6 L546.7 199.7 L558.3 199.7 L570.0 199.7 L581.7 199.7 L593.3 199.7 L605.0 199.7 L616.7 199.7 L628.3 199.7 L640.0 199.7" fill="none" stroke="var(--accent-soft)" stroke-width="2.5"/>
<text x="646" y="117.7" font-size="10.5" fill="var(--text-muted)">P90</text><text x="646" y="203.7" font-size="10.5" fill="var(--text)">Median</text><text x="646" y="273.4" font-size="10.5" fill="var(--text-muted)">P10</text>
<text x="360.0" y="384" text-anchor="middle" font-size="13" fill="var(--text-muted)">Months since launch →</text>
<text x="24" y="205.0" transform="rotate(-90 24 205.0)" text-anchor="middle" font-size="13" fill="var(--text-muted)">Fund value (100 = capital invested) →</text>
<g font-size="11" fill="var(--text-muted)"><rect x="150" y="402" width="18" height="10" fill="var(--accent)" fill-opacity="0.2"/><text x="174" y="411">80% of paths</text><rect x="270" y="402" width="18" height="10" fill="var(--accent)" fill-opacity="0.32"/><text x="294" y="411">50% of paths</text><line x1="390" y1="407" x2="408" y2="407" stroke="var(--accent-soft)" stroke-width="2.5"/><text x="414" y="411">Median path</text></g>
</svg>
<figcaption><strong>Figure 4.</strong> Illustrative toy model, not Subaxa data. Fund value for 2,000 simulated runs of the same plan, with unsold properties held at cost. The bands show where the middle 50% and 80% of paths fall each month. Values are before fees and taxes.</figcaption>
</figure>

A single-number model would show only something close to the median line, ending around 1.32 times the invested capital before fees and taxes. The twin shows the whole spread: in the weaker futures, the fund ends the period near 1.11, while the strongest ones exceed 1.57. It also shows *when* value appears. In this toy fund, very little happens in the first year, because properties are still moving through the legal process.

That timeline matters for planning cash, setting expectations with investors, and deciding when to open the next fund.

## Comparing different paths

The more interesting question is how outcomes change when we change a decision. Here is the same toy fund with one lever moved: instead of six larger properties, Path B spreads the same capital across 24 smaller ones.

<figure class="fig data-figure">
<svg viewBox="0 0 700 430" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="dt4t dt4d">
<title id="dt4t">Outcome distributions for two strategies</title>
<desc id="dt4d">Illustrative simulation. Fund value multiple after 48 months. Concentrated path (6 properties): median 1.32x, 3% of paths below 1.0x. Diversified path (24 properties): median 1.34x, 0.0% of paths below 1.0x.</desc>
<text x="350.0" y="30" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text)">Same capital, two paths, very different risk</text>
<line x1="80" y1="340.0" x2="640" y2="340.0" stroke="var(--border)"/><text x="68" y="344.0" text-anchor="end" font-size="11" fill="var(--text-muted)">0%</text><line x1="80" y1="306.2" x2="640" y2="306.2" stroke="var(--border)"/><text x="68" y="310.2" text-anchor="end" font-size="11" fill="var(--text-muted)">5%</text><line x1="80" y1="272.5" x2="640" y2="272.5" stroke="var(--border)"/><text x="68" y="276.5" text-anchor="end" font-size="11" fill="var(--text-muted)">10%</text><line x1="80" y1="238.8" x2="640" y2="238.8" stroke="var(--border)"/><text x="68" y="242.8" text-anchor="end" font-size="11" fill="var(--text-muted)">15%</text><line x1="80" y1="205.0" x2="640" y2="205.0" stroke="var(--border)"/><text x="68" y="209.0" text-anchor="end" font-size="11" fill="var(--text-muted)">20%</text><line x1="80" y1="171.2" x2="640" y2="171.2" stroke="var(--border)"/><text x="68" y="175.2" text-anchor="end" font-size="11" fill="var(--text-muted)">25%</text><line x1="80" y1="137.5" x2="640" y2="137.5" stroke="var(--border)"/><text x="68" y="141.5" text-anchor="end" font-size="11" fill="var(--text-muted)">30%</text><line x1="80" y1="103.8" x2="640" y2="103.8" stroke="var(--border)"/><text x="68" y="107.8" text-anchor="end" font-size="11" fill="var(--text-muted)">35%</text><line x1="80" y1="70.0" x2="640" y2="70.0" stroke="var(--border)"/><text x="68" y="74.0" text-anchor="end" font-size="11" fill="var(--text-muted)">40%</text><text x="80.0" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">0.8×</text><text x="173.3" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">1.0×</text><text x="266.7" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">1.2×</text><text x="360.0" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">1.4×</text><text x="453.3" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">1.6×</text><text x="546.7" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">1.8×</text><text x="640.0" y="360" text-anchor="middle" font-size="11" fill="var(--text-muted)">2.0×</text>
<rect x="80" y="70" width="93.3" height="270" fill="var(--text-muted)" fill-opacity="0.07"/>
<text x="126.7" y="86" text-anchor="middle" font-size="10.5" fill="var(--text-muted)">Lose money</text>
<rect x="81.0" y="337.0" width="22.3" height="3.0" fill="var(--accent-deep)"/><rect x="103.3" y="340.0" width="22.3" height="0.0" fill="var(--accent-soft)"/><rect x="127.7" y="325.1" width="22.3" height="14.9" fill="var(--accent-deep)"/><rect x="150.0" y="340.0" width="22.3" height="0.0" fill="var(--accent-soft)"/><rect x="174.3" y="297.1" width="22.3" height="42.9" fill="var(--accent-deep)"/><rect x="196.7" y="338.0" width="22.3" height="2.0" fill="var(--accent-soft)"/><rect x="221.0" y="236.1" width="22.3" height="103.9" fill="var(--accent-deep)"/><rect x="243.3" y="292.1" width="22.3" height="47.9" fill="var(--accent-soft)"/><rect x="267.7" y="192.5" width="22.3" height="147.5" fill="var(--accent-deep)"/><rect x="290.0" y="149.3" width="22.3" height="190.7" fill="var(--accent-soft)"/><rect x="314.3" y="204.0" width="22.3" height="136.0" fill="var(--accent-deep)"/><rect x="336.7" y="75.7" width="22.3" height="264.3" fill="var(--accent-soft)"/><rect x="361.0" y="234.4" width="22.3" height="105.6" fill="var(--accent-deep)"/><rect x="383.3" y="198.2" width="22.3" height="141.8" fill="var(--accent-soft)"/><rect x="407.7" y="272.8" width="22.3" height="67.2" fill="var(--accent-deep)"/><rect x="430.0" y="314.0" width="22.3" height="26.0" fill="var(--accent-soft)"/><rect x="454.3" y="304.6" width="22.3" height="35.4" fill="var(--accent-deep)"/><rect x="476.7" y="338.0" width="22.3" height="2.0" fill="var(--accent-soft)"/><rect x="501.0" y="326.5" width="22.3" height="13.5" fill="var(--accent-deep)"/><rect x="523.3" y="339.7" width="22.3" height="0.3" fill="var(--accent-soft)"/><rect x="547.7" y="336.6" width="22.3" height="3.4" fill="var(--accent-deep)"/><rect x="570.0" y="340.0" width="22.3" height="0.0" fill="var(--accent-soft)"/><rect x="594.3" y="338.3" width="22.3" height="1.7" fill="var(--accent-deep)"/><rect x="616.7" y="340.0" width="22.3" height="0.0" fill="var(--accent-soft)"/>
<line x1="173.3" y1="70" x2="173.3" y2="340" stroke="var(--border-strong)" stroke-dasharray="4 4"/>
<line x1="80" y1="340" x2="640" y2="340" stroke="var(--border-strong)"/>
<text x="360.0" y="384" text-anchor="middle" font-size="13" fill="var(--text-muted)">Fund value multiple after 48 months →</text>
<text x="24" y="205.0" transform="rotate(-90 24 205.0)" text-anchor="middle" font-size="13" fill="var(--text-muted)">Share of simulated paths →</text>
<g font-size="11" fill="var(--text-muted)"><rect x="160" y="402" width="12" height="12" fill="var(--accent-deep)"/><text x="178" y="412">Path A: 6 larger properties</text><rect x="390" y="402" width="12" height="12" fill="var(--accent-soft)"/><text x="408" y="412">Path B: 24 smaller properties</text></g>
</svg>
<figcaption><strong>Figure 5.</strong> Illustrative toy model, not Subaxa data. Distribution of fund value after 48 months across 2,000 simulated runs for each path. Both paths invest the same capital under the same assumptions. Values are before fees and taxes.</figcaption>
</figure>

Both paths have almost the same median outcome: about 1.32 times capital for Path A and 1.34 for Path B. Looking only at the expected return, they seem equivalent.

The distributions tell a different story. Path A is much wider. Its weakest 10% of runs end below 1.11, compared with 1.22 for Path B. About 2.7% of Path A's runs lose money; none of Path B's 2,000 runs do. One problematic property hurts a six-property fund far more than a 24-property one.

This is a textbook result about diversification, and nobody needs a twin to learn it. What the twin adds is the ability to put numbers on trade-offs that are not so obvious. Diversification has costs as well: more transactions, more legal processes to follow, and more work for the team. With a twin, we can ask questions such as:

- How does the picture change if legal processes take six months longer than expected?
- What happens if we deploy capital more slowly to wait for better opportunities?
- How much liquidity do we need to absorb a bad year without selling properties at a discount?
- At what point does adding more properties stop reducing risk enough to justify the extra work?

Each of those questions can be tested in minutes, in a simulated environment, before any real money moves.

## What a digital twin cannot do

A digital twin is not a crystal ball. Its answers are only as good as the assumptions and data behind it.

The toy model above is a good example of the limitations. It treats each property as independent, so a problem with one property says nothing about the others. In reality, a market downturn or a change in court procedures can affect many properties at once, and diversification protects less in that situation. A serious twin needs to model those shared shocks, and its results need to be checked continuously against real outcomes.

It also does not make decisions. It makes the consequences of a decision visible, so the people responsible can discuss them with better information. The judgment remains human.

## A safe place to make mistakes

The most useful thing about a digital twin is that it gives us a place to be wrong at no cost. We can try an aggressive strategy, a cautious one, and everything in between, see how each one behaves across thousands of possible futures, and discard the ones that fail before they touch real capital.

Engineers have worked this way for years. I believe private investment funds, especially those investing in less conventional assets, can benefit from the same discipline. We are still early in our experiments at Subaxa, but the way we discuss strategy has already changed: we spend less time debating a single forecast and more time understanding the range of outcomes we are signing up for.

## References

- National Academies of Sciences, Engineering, and Medicine (2023): [Foundational Research Gaps and Future Directions for Digital Twins](https://www.nationalacademies.org/read/26894/chapter/4). The definition of a digital twin used in this article, including the two-way link between the model and the real system.
- Michael Grieves (2014): [Digital Twin: Manufacturing Excellence through Virtual Factory Replication](https://theengineer.markallengroup.com/production/content/uploads/2014/12/Digital_Twin_White_Paper_Dr_Grieves.pdf), white paper. Grieves's account of the 2002 concept and of the name, which he attributes to John Vickers of NASA.
- Diginomica: [Grieves and Vickers on the history of digital twins](https://diginomica.com/grieves-and-vickers-history-digital-twins).
- Frontiers of Engineering Management (2022): [a review that questions the standard origin story of the digital twin](https://journal.hep.com.cn/fem/EN/PDF/10.1007/s42524-022-0216-2).
- Rolls-Royce (2018): [IntelligentEngine vision makes rapid progress](https://www.rolls-royce.com/media/press-releases/2018/16-07-2018-rr-intelligentengine-vision-makes-rapid-progress.aspx), press release.
- CIO: [Rolls-Royce turns to digital twins to improve jet engine efficiency](https://www.cio.com/article/3620993/rolls-royce-turns-to-digital-twins-to-improve-jet-engine-efficiency.html).
- [Simulation code and assumptions](https://github.com/crojasaragonez/crojasaragonez.github.io/tree/main/src/data/digital-twins) for the illustrative toy model behind Figures 2, 4 and 5.
