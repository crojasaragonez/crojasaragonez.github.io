---
title: "How to Switch LLM Models Without Breaking Your Agents"
description: "Build an internal benchmark, measure Intelligence per Dollar, and make every model upgrade a decision you can test and reverse."
pubDate: 2026-09-30
draft: false
---

This has been a great week for geeks.

Three major model announcements in three days:

- **September 28:** [Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5).
- **September 29:** [OpenAI GPT-6.1 Sol](https://developers.openai.com/api/docs/changelog).
- **September 30:** [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/), announced with an initial rollout to trusted cyber defenders ahead of broader availability.

For those of us building agentic systems, the excitement comes with a very practical question:

**How do I switch models safely without breaking the system I already have?**

A new model might reason better, cost less, or finish tasks faster. It can also interpret an instruction differently, choose a different tool, or produce an output your application does not expect. A stronger model on a leaderboard can still be a regression in your product.

At Subaxa, our answer has been to build our own internal benchmark. It has cost us peanuts compared with the improvements we have seen from major LLM upgrades. Having a repeatable way to evaluate those upgrades lets us make better decisions about which ones to adopt.

## Public benchmarks help you build a shortlist

Public benchmarks are a good reference. They tell us where capabilities are moving and which models deserve a closer look.

But your customers are not sending you benchmark questions. They are sending you incomplete requests, documents with inconsistent formatting, and problems that depend on your business rules. Your agents have to work with your tools, your data, and your definition of a correct result.

A public score cannot tell you whether a model will follow your escalation policy or stop before making an unauthorized change.

Use public results to decide what to investigate. Use your own evaluation to decide what to deploy.

## Build a benchmark from the work you actually do

You do not need a research lab to start. You need a small, representative collection of tasks and a clear definition of success.

Start with real examples, with sensitive information removed or handled appropriately. Include routine tasks, difficult cases, and failures you have already encountered. Keep some cases aside so that prompt tuning does not turn the entire benchmark into a practice set.

For each task, write down what an acceptable result looks like. That might be an exact extracted value, a valid database query, a correctly completed workflow, or a decision to ask for missing information. When several answers could be correct, define a rubric rather than expecting one exact response.

An agent evaluation should check the path to the result as well as the final answer:

| What to measure | What it tells you |
| --- | --- |
| Task completion | Did the agent deliver a result you can use? |
| Tool use | Did it choose the right tools and supply valid arguments? |
| Output validity | Did the result satisfy your schema and business rules? |
| Boundaries and escalation | Did it respect permissions and ask for help when needed? |
| Total cost | What did the run cost, including retries, tools, and review? |
| Completion time | How long did it take to reach a validated result or timeout? |

Run the current system and the candidate on the same cases, with equivalent starting data and permissions. First establish a baseline with the current prompts. If the candidate needs different prompts or settings, evaluate that configuration separately and record what changed.

Repeat cases where results vary. One successful run is encouraging; it is weak evidence that a workflow will remain reliable.

Use deterministic checks where you can. For subjective results, review against the same rubric, ideally without showing the reviewer which model produced the answer. If you use another LLM to grade outputs, check its judgments against human review before trusting its scores.

## Choose a figure of merit you can measure objectively

Before comparing models, decide what you are trying to improve.

At Subaxa, we use **Intelligence per Dollar**. I explain the idea in [The Real LLM Race Is Intelligence per Dollar](/blog/the-real-llm-race-is-intelligence-per-dollar/): useful work delivered within a budget, with an acceptable error rate and waiting time.

A practical starting measure is:

**Accepted results per dollar = number of accepted results ÷ total evaluation cost.**

Count the cost of failed attempts too. Include retries, tool calls, and human verification using a consistent accounting method. Define acceptance before running the comparison.

For an illustrative example, suppose one configuration costs $10 across 100 tasks and produces 80 accepted results. Another costs $8 and produces 90. That is 8 versus 11.25 accepted results per dollar. These are hypothetical numbers, but they show why the price per token alone does not settle the decision.

The ratio also needs constraints. A cheaper system that occasionally takes an unauthorized action should fail the evaluation, even if its average score looks excellent. Set your minimum quality, reliability, and latency requirements first. Compare value among the configurations that meet them.

Look at results by task type too. An overall improvement can hide a regression in the one workflow that matters most to your customers.

## Evaluate the whole agent, then roll it out gradually

Switching a model changes one part of a larger system. Prompts, retrieval, memory, tool definitions, validation, and retry logic all affect the outcome.

Test the candidate inside that system. A model that answers beautifully in a chat window may behave differently after several tool calls and a long conversation.

I would use this release process:

1. **Record the baseline.** Save the model version, prompts, tool schemas, settings, and evaluation results for the system you already trust.
2. **Run the candidate in isolation.** Replay representative tasks in a sandbox. Simulate or intercept actions that would change production data.
3. **Apply the acceptance criteria.** Check individual regressions, critical failures, cost, and time. Decide what passes before seeing the scores.
4. **Move a small share of eligible traffic.** Monitor actual outcomes, intervention rates, cost, and latency. Keep existing approval and permission checks in place.
5. **Expand or roll back.** Increase traffic when the evidence supports it. Keep the previous configuration available and define the conditions that trigger a rollback.

If you compare models on live requests in shadow mode, only the active system should execute real actions. The candidate can propose actions for inspection; it should not send a second email or make a second database write.

Rollback needs some thought as well. Returning to the old configuration does not undo actions already taken. Start new sessions on the candidate where possible, and test compatibility before moving conversations with existing state between models.

Every production failure you discover should become another evaluation case. Over time, your benchmark becomes a record of what your system needs to get right.

## Stay open to different providers

Do not tie your organization's model strategy to a single provider.

Use what works best for your workload today, and keep trying alternatives as they become available. The best choice can differ by task: document extraction, planning, and final review may benefit from different configurations.

Keep provider-specific details behind an adapter where practical, and make the model choice configurable. That lowers the effort required to run the next comparison. Still test each integration: a common interface does not make providers' tool calling, context handling, or failure behavior identical.

The same principle applies to specialized models. [Jev, TypeSafe's first System One model](https://typesafe.ai/blog/introducing-system-one-models-and-jev), produces typed decisions with probabilities rather than generating free-form text. TypeSafe positions it for tasks such as classification, routing, scoring, and verification.

Jev was not a good fit for us because the problems we are solving leave little or no room for it to improve the outcome. I have seen it work well in other organizations. Fit depends on the work.

Your internal benchmark gives you a way to test that fit, whether you are changing the provider, the model, or the approach around it.

## Make the next release easier to evaluate

This week's announcements will not be the last ones worth exploring.

If every release forces your team to rely on a few impressive demos and a nervous production switch, upgrades will remain expensive decisions. A modest internal benchmark gives you a repeatable process: run the candidate, inspect the failures, measure the value, and release it gradually when it qualifies.

At Subaxa, that investment has been small relative to the improvements we have seen. It also gives us the confidence to keep exploring.

Enjoy the new releases. Then make them earn their place in your system.
