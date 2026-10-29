---
title: "Small Language Models Are Bringing AI to the Edge"
description: "Smaller models and simpler tools are making AI practical on laptops and phones. Liquid AI, Gemma, Ollama, AnythingLLM, and PocketPal show how close that future already is."
pubDate: 2026-10-29
draft: false
---

Put your phone in airplane mode. Open an AI assistant. Ask it to rewrite a paragraph.

If the answer still arrives, something important has changed: the device in your hand is doing the work.

That is becoming an increasingly accessible way to use AI. Small language models are making it possible to bring useful language capabilities onto ordinary computers and mobile devices. The software around them is making the experience easier to set up, too.

I think this will be one of the most consequential changes in how we use AI. More of the things we ask an assistant to do will become features our devices can provide directly.

## What “small” and “at the edge” actually mean

A small language model, or SLM, usually has a comparatively modest number of parameters: the learned numerical values that shape its responses. There is no universal cutoff. The useful question is whether a model can do the job within a device's memory, speed, and power limits.

The *edge* is where the work happens close to the person or equipment producing the data. That could be a laptop, a phone, a vehicle, or a computer on a factory floor. In this article, the focus is on models running directly on the device you are using.

A chat app installed on your phone may still send every prompt to a remote server. On-device AI means the model itself runs on the phone. Once the necessary files are downloaded, supported tasks can work without an internet connection.

That distinction changes what you can build.

## Why this keeps getting easier

Several improvements are arriving together.

Model developers are designing for constrained hardware from the beginning. Liquid AI explicitly targets processors outside data centers, with deployment options for phones, laptops, and other devices. Google's Gemma family also includes models built for local and mobile use. [Liquid AI](https://www.liquid.ai/), [Gemma overview](https://ai.google.dev/gemma/docs).

Quantization helps these models fit. It stores model values at lower numerical precision, reducing memory requirements, with a possible tradeoff in answer quality. Tools such as llama.cpp support several quantization levels and a range of CPU and GPU backends. That gives developers more ways to match a model to the hardware already available. [llama.cpp documentation](https://github.com/ggml-org/llama.cpp).

The experience is improving above that technical layer, too. Desktop apps can handle downloading, loading, and chatting with a model. Mobile apps bring the same basic workflow to a phone.

My expectation is that these improvements will reinforce one another: more useful small models give people a reason to install the tools, and better tools make those models accessible to more people.

## Two model families worth exploring

**Liquid AI** is an interesting place to start because efficiency is central to its approach. Its latest compact text model, **LFM3-1.7B**, has 1.73 billion parameters and is designed for local agents, tool calling, structured outputs, and specialized applications. It supports a 256K-token context window, although using that capacity requires additional memory. The wider LFM3 family also includes vision, audio, and multimodal models. [LFM3-1.7B model card](https://huggingface.co/LiquidAI/LFM3-1.7B).

The [Liquid playground](https://playground.liquid.ai) is a convenient first stop for trying the models before setting up a local runtime. Treat that as an online evaluation step; the separate local deployment is what lets you assess performance and offline behavior on your own hardware. LFM3-1.7B is available in GGUF format for local inference and in MLX format for Apple silicon. [LFM3 deployment options](https://huggingface.co/LiquidAI/LFM3-1.7B#inference).

**Google's Gemma** offers another route. Gemma 4 includes E2B and E4B variants designed for mobile and edge deployment. The “E” refers to effective parameters; it does not mean the complete model occupies the same memory as a conventional model with that parameter count. Google also publishes quantized versions for local and mobile runtimes. [Gemma 4 documentation](https://ai.google.dev/gemma/docs/core).

The practical lesson is to check the exact model, format, and runtime together. A model family's capabilities do not automatically carry over to every app that can load one of its versions. Text, image, audio, and tool support can differ.

## The tools are becoming ordinary software

You can approach local AI at several levels. Some tools provide the engine; others provide the application you interact with.

| Tool | What it provides | A useful starting point for |
| --- | --- | --- |
| [Ollama](https://docs.ollama.com/quickstart) | Model downloading, local inference, and an API | Running models from a terminal or connecting them to an application |
| [AnythingLLM](https://anythingllm.com/) | A desktop assistant with document knowledge and workflow features | Working with local documents through a graphical interface |
| [LM Studio](https://lmstudio.ai/docs/app/offline) | A desktop interface for model chat, document chat, and a local server | Trying local models without beginning with command-line tools |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | An inference engine with broad hardware and quantization support | Developers who want more control over execution |
| [MLX LM](https://github.com/ml-explore/mlx-lm) | Text generation and fine-tuning tools using MLX on Apple silicon | Developers building or experimenting on a Mac |

For example, after installing a current version of Ollama, you can run a small Gemma model with:

```bash
ollama run gemma4:e2b
```

For LFM3-1.7B, Liquid currently documents Ollama support on macOS with version 0.40.12 or newer:

```bash
ollama run lfm3:1.7b
```

These commands download the selected model if needed and start a local conversation. They follow the published [Gemma instructions](https://ollama.com/library/gemma4), [LFM3 Ollama listing](https://ollama.com/library/lfm3), and [Liquid's local runtime requirements](https://huggingface.co/LiquidAI/LFM3-1.7B-GGUF#how-to-run-lfm3-17b). Check the download size and available memory before choosing a model.

For a document assistant, AnythingLLM offers a more complete application around the model. LM Studio also supports offline document chat once the necessary model and runtime files are available. [AnythingLLM](https://anythingllm.com/), [LM Studio offline operation](https://lmstudio.ai/docs/app/offline).

The configuration still matters. Choose local inference and local document processing if your goal is to keep the workflow on the machine. Cloud providers, remote embeddings, and web tools can introduce network calls even when the main chat model runs locally.

## PocketPal makes the change easy to see

[PocketPal](https://pocketpal.dev/) brings language models directly to iOS and Android devices. It supports downloading compatible GGUF models, loading them on the phone, and chatting offline. Its built-in benchmarks can help compare speed and memory use on your particular device. [PocketPal's official repository](https://github.com/a-ghorbani/pocketpal-ai).

The simplest experiment is to install the app, choose a small supported model that fits your phone, download and load it, and then switch to airplane mode. Ask it to rewrite a short note or summarize a paragraph you supply.

That is a useful demonstration because the result is easy to inspect. You know the source text, you can judge whether the response preserved its meaning, and you can see whether the wait feels acceptable.

A phone still has limited memory and a battery to protect. Sustained generation can produce heat and reduce performance. A short exchange that works well is only the beginning of evaluating a mobile assistant.

## What becomes possible when the model is nearby

Consider a technician visiting a site with unreliable connectivity. A local assistant could help search a downloaded equipment manual and explain a relevant passage. A person traveling could draft messages or practice a language offline. A business could explore extracting fields from documents on an office computer.

These are candidate workflows to evaluate, each with a bounded task and an answer someone can check.

Local execution gives them several potential advantages:

- **Offline availability.** The core task can continue when connectivity disappears, provided its models and reference material are already on the device.
- **Control over data.** Prompts and documents can stay within the local workflow when all its components run locally.
- **Less dependence on network latency.** Responses avoid a round trip to a remote model, although a larger cloud model may still generate faster than a particular device.
- **A different cost structure.** Local inference removes the provider's per-token charge for that computation. Hardware, electricity, maintenance, and human review remain part of the bill.

That last point connects to [intelligence per dollar](/blog/the-real-llm-race-is-intelligence-per-dollar/). The useful measure is the cost of an accepted result. A local model earns its place when its answers are good enough and its operating costs make sense.

## The limits should shape the application

Memory is often the first constraint. The model file is only part of the requirement: the runtime and conversation context also need space. Long conversations can consume substantially more memory. Google's deployment guidance makes this distinction explicit. [Gemma memory planning](https://ai.google.dev/gemma/docs/core#key-considerations-for-memory-planning).

Quality is the next constraint. A model that rewrites a paragraph well may struggle with an unfamiliar question or a task requiring many dependent steps. Retrieval can supply relevant reference material, but the generated answer still needs checking.

I would begin with a small set of real examples. Give the model the same tasks you want it to perform in practice. Record whether each answer is acceptable, how long it takes, and how much correction it needs. On a phone, repeat the work long enough to notice battery use and heat. Include examples where the reference material does not contain an answer.

This also gives you a basis for deciding when to use a larger remote model. A hybrid application could handle bounded tasks locally and offer a deliberate cloud option for harder work. The user should understand when their data will leave the device. A small model's confidence alone is a poor routing rule; fluent mistakes can look convincing.

## AI as a device capability

I expect local AI to become easier to overlook as it becomes more useful. A writing feature, document search, or voice interface may quietly use a small model without asking the user to think about model hosting at all.

Liquid AI and Gemma provide models to build with. Ollama, AnythingLLM, LM Studio, llama.cpp, and MLX LM provide different paths to using them. PocketPal puts the experiment in your hand.

The opportunity is already concrete: choose one useful task, try a small model on hardware you own, and measure the result. Each task that works well expands what that device can do on its own.
