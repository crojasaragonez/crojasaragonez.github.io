---
title: "Faster Clustering: What e-means Could Save Companies"
description: "A faster algorithm could cut compute time, release capacity, and reduce energy use. An e-means experiment shows the opportunity and what a business still needs to validate."
pubDate: 2026-11-11
draft: false
---

<div class="paper-kicker">Technology strategy · November 2026</div>

When a company wants to make its AI systems faster, the conversation often turns to buying more compute. A better algorithm offers another possibility: **get useful results from the infrastructure we already have, with less work.**

That is why e-means caught my attention. Clustering groups similar data points together. It can help organize large collections of documents and images, build search infrastructure, and select data for further processing. When that work runs repeatedly or at large scale, a faster way to reach comparable quality could change its operating cost. The [e-means paper](https://arxiv.org/abs/2611.09501) explores this opportunity through a new optimization procedure for the familiar k-means objective.

I tried the official implementation on MNIST, the handwritten-digit dataset. In this small CPU experiment, five-pass e-means was approximately **3.2–3.5× faster** than 25-pass Lloyd k-means, with slightly lower distance error in the median paired comparison. It did not win every seed or every quality metric.

For a business, the implication is worth investigating: less compute for an acceptable result could mean a lower bill, shorter processing windows, or more work from the same capacity. Turning that possibility into savings requires measuring the complete workflow.

## Where companies could benefit

The first place I would look is a recurring job that already uses k-means and consumes a meaningful share of resources. A company starting from a different clustering method may have a different objective; e-means would need a broader evaluation.

Consider a retailer grouping product-image vectors before rebuilding a search index. Finishing the clustering stage sooner could make room for more frequent catalog updates. A team organizing a growing document collection could process more data within its overnight window. A data team testing different representations could complete more experiments before its next decision.

These are possible applications, rather than outcomes established by my MNIST test. Their value comes through three routes:

- **Time:** a shorter processing stage can reduce waiting when it sits on the workflow's critical path.
- **Money and capacity:** fewer billed machine-hours can reduce variable spending; on existing infrastructure, the benefit may instead be capacity released for other jobs.
- **Energy:** performing the same useful work with less electricity can reduce operating energy and associated emissions. Runtime alone does not establish the size of that reduction.

Management has a choice about how to use an efficiency gain. It can spend less on the same workload, or process more data and refresh results more often. The latter may create more value, while leaving total spending and electricity use unchanged or even increasing them.

## What e-means changes

Lloyd's algorithm repeatedly assigns every point to its closest centroid, then moves each centroid to the mean of its assigned points. One complete pass produces one centroid update.

e-means still seeks compact groups under squared Euclidean distance. It changes how the centroids get there: mini-batches update exponentially weighted counts and vector sums. New assignments can therefore change centroids several times during a pass. The recipe also includes a decreasing step size, revival of underused clusters, and a final centroid calculation. [Official project explanation](https://e-means.github.io/).

The distinction matters: **e-means optimizes the same clustering objective with a different procedure.** It does not automatically discover the right number of clusters, or turn spherical distance-based clusters into arbitrary shapes.

The [paper by Bessa and colleagues](https://arxiv.org/abs/2611.09501), submitted November 6, reports reaching Lloyd's 25-pass error in roughly 1.4–2.6 passes on large embedding datasets, with substantial GPU speedups. It also notes that its fitted parameter rules are less suited to tiny or very low-dimensional datasets. This experiment uses raw image pixels and a CPU, so it tests a different workload.

## What the experiment actually showed

MNIST has **60,000 training images and 10,000 test images**, each 28 × 28 pixels. I flattened each image into 784 coordinates and divided pixel values by 255. There is no PCA, learned embedding, or per-pixel standardization. The digit labels are used only for evaluation. [Dataset documentation](https://keras.io/api/datasets/mnist/).

I used **ten clusters**, matching the number of digit classes, and **100 clusters**, allowing several groups to represent different writing styles. Each setting had five random seeds. e-means and Faiss Lloyd received identical starting centroids and every training image; Faiss's default subsampling was disabled.

The code comes from a [pinned Faiss source commit](https://github.com/facebookresearch/faiss/tree/f777f7d82d30a444febaa29654296738d85b3f7a/contrib/e_means), using the authors' NumPy implementation and automatic settings. All training ran sequentially on an **AMD Ryzen AI 7 PRO 350**, with numerical libraries limited to **one CPU thread**. Warmups and shuffled configuration order helped make the comparison consistent.

Across several training budgets and two additional scikit-learn references, I ran **120 timed fits**. The notebook preserves the complete results and configuration details, including the comparison with MiniBatchKMeans and k-means++ initialization.

The main quality measure is **mean squared vector distance**: how far images lie from their nearest final centroid, using all 784 coordinates. Lower is better. I recomputed this measure consistently for every model, rather than comparing their internal training logs.

The following comparison matches five-pass e-means to 25-pass Faiss Lloyd for the same seed. Speedups and error changes are medians of those paired comparisons.

| Cluster count | Fit-time speedup | Test distance-error change | Seeds with lower error |
| --- | ---: | ---: | ---: |
| 10 | 3.53× | −0.14% | 3 of 5 |
| 100 | 3.19× | −0.36% | 5 of 5 |

The practical finding is a substantial reduction in fitting time with small improvements in the median distance objective. At 100 clusters, the advantage was consistent across the five seeds. At ten, two seeds still favored Lloyd on distance error.

There is also an important quality distinction. At ten clusters, Lloyd had better agreement with the digit labels: median adjusted Rand index was **0.392**, compared with **0.371** for five-pass e-means. A tighter group of pixels is not necessarily a better group of digits. A company needs a quality measure tied to its actual use: for example, search relevance or the usefulness of document groups.

## What that could mean in time and money

Here is an **illustrative scenario, not a forecast from MNIST**. Suppose a company's recurring clustering work consumes 1,000 machine-hours per month. Assume a metered price of $2 per machine-hour, the same machine configuration and data volume, acceptable output quality, and a 3.2× reduction in compute time that holds at production scale.

| Monthly resource | Before | At 3.2× speedup | Potential reduction |
| --- | ---: | ---: | ---: |
| Clustering machine-hours | 1,000 | 312.5 | 687.5 hours |
| Compute spend at $2/hour | $2,000 | $625 | $1,375 |
| IT electricity at 200 W/machine | 200 kWh | 62.5 kWh | 137.5 kWh |

All three rows assume the same workload and unchanged resource rates. The dollar rate and power draw are chosen assumptions, not a cloud quote or a measurement of the benchmark machine. The electricity row also assumes unchanged average power while running and excludes cooling and other facility overhead. These conditions produce **68.75% less time, variable compute spending, and IT electricity for the clustering work**.

The accounting changes on prepaid or owned infrastructure. A faster job releases capacity immediately, but cash savings may require shutting down resources, reducing a future commitment, or delaying an expansion. Storage, data transfer, and other fixed costs may remain. Integration, validation, and maintenance also belong in the adoption decision.

The complete processing window matters too. If clustering accounts for **20% of a workflow's elapsed time**, accelerating that stage by 3.2× reduces total elapsed time by only **13.75%**, assuming the other stages stay unchanged. Loading data, generating vectors, rebuilding indexes, and validation can still dominate the schedule. Parallel workloads need their critical path measured directly.

This is why I would estimate the opportunity from a company's current resource use and pipeline profile, then measure a pilot. Multiplying the entire AI budget by a benchmark speedup would greatly overstate the case.

## Energy savings need their own measurement

The experiment measured fitting time. **It did not measure electricity or carbon emissions.** The energy row above is conditional: electricity depends on average power as well as duration. A faster implementation could draw more power while it runs; a shared server could remain powered on after the job ends.

For a production evaluation, I would measure energy over a defined workload, use the same system boundary for both methods, and report electricity per accepted result. If a company uses the released capacity to run more jobs, it should track total electricity alongside that efficiency measure.

Carbon adds another variable: the emissions intensity of the electricity supply. Hardware manufacturing and facility overhead also need a consistent accounting boundary. The [Green Software Foundation's Software Carbon Intensity specification](https://sci.greensoftware.foundation/) provides a framework that distinguishes energy consumption, electricity carbon intensity, and embodied hardware emissions. A runtime improvement alone cannot establish a carbon reduction.

## Why the time budget matters

<figure class="fig chart-figure">
<img src="/images/blog/e-means/epochs.svg" alt="Median test error versus training passes for e-means and Faiss Lloyd, at 10 and 100 clusters. e-means reduces error much earlier in both settings. Bands show the observed range across five seeds." loading="lazy" />
<figcaption><strong>Figure 1.</strong> Independent fits at each requested budget; lines connect medians and bands show observed seed minima and maxima, not confidence intervals. Each panel has its own error scale. Changing the e-means budget also changes its automatic recipe.</figcaption>
</figure>

At 100 clusters, five-pass e-means uses batches of 4,096 images and makes 75 updates. Lloyd makes 25 updates in 25 full passes. More frequent adaptation helps e-means reach low error earlier, but assembling batches and updating statistics costs time too.

<figure class="fig chart-figure">
<img src="/images/blog/e-means/time.svg" alt="Median test error versus CPU fit time on logarithmic time axes. e-means reaches low error sooner than Faiss Lloyd. MiniBatchKMeans provides a quick higher-error reference, while k-means++ has a larger fit cost at 100 clusters." loading="lazy" />
<figcaption><strong>Figure 2.</strong> The same measurements plotted against fit time, with the two scikit-learn references added. The time axis is logarithmic. Bands show error variability; timing variability is recorded in the supporting CSV. Lower and farther left is preferable.</figcaption>
</figure>

At the aggressive **2.5-pass** budget, the median paired speedup over 25-pass Lloyd is **7.01× at 10 clusters and 8.83× at 100**. However, it beats the paired test error in only three and four seeds, respectively. Calling those numbers an unconditional speedup at equal quality would hide the misses.

Running e-means for all 25 passes is also revealing: it takes longer than 25-pass Lloyd on this CPU. Its advantage comes from reaching useful quality earlier. Giving both algorithms the same pass count does not give them the same computation time.

## How I would make the adoption decision

I would start with a bounded pilot on one expensive recurring clustering job:

1. **Set the acceptable result.** Define both the clustering objective and a downstream quality threshold. Agree on how much variation is acceptable before comparing algorithms.
2. **Measure the current workflow.** Record clustering time, total elapsed time, billed resources, and energy where available. Find out whether clustering is a meaningful bottleneck.
3. **Compare realistic alternatives.** Test e-means against the deployed configuration and a practical mini-batch baseline, including initialization, data movement, and repeated runs on representative data.
4. **Calculate the net benefit.** Account for integration and validation effort, then distinguish cash savings, capacity released, and shorter delivery windows. Do not count the same released capacity as both reduced spending and extra output.
5. **Choose how to use the gain.** Reduce resource consumption, increase update frequency, or process a larger workload. Measure whether that choice delivers the intended value.

My experiment is a reason to run that pilot. It is one raw-pixel dataset, one CPU, one thread setting, and five seeds, with one timing per configuration per seed. The small error differences do not establish statistical significance, and neither the speedup nor the quality result is guaranteed to transfer to production.

Still, the opportunity is meaningful. Companies can improve the economics of AI through the algorithms underneath their systems as well as through the hardware they buy. When a faster method meets the required quality, it gives the business more room to choose how much to spend, how soon to deliver, and how much energy to consume.

## Reproduce the experiment

The [experiment notebook](https://github.com/crojasaragonez/crojasaragonez.github.io/blob/main/src/data/e-means/benchmark.ipynb) contains the complete benchmark code, explanations, validation, result tables, and inline charts. Its saved outputs show the recorded experiment. Training and test metrics, including normalized mutual information, are preserved even where they are omitted from the article's tables.

```sh
python3 -m venv /tmp/e-means-repro
/tmp/e-means-repro/bin/python -m pip install -r src/data/e-means/requirements.txt
```

Open `src/data/e-means/benchmark.ipynb` in VS Code or Jupyter, select that environment as the kernel, and run all cells. The default mode analyzes the recorded measurements without downloading data or retraining. Set `RUN_FRESH = True` to rerun the experiment, or also enable `SMOKE_TEST` for a quick check of all four implementations. Fresh measurements go to a separate directory outside the checkout.

The [supporting directory and README](https://github.com/crojasaragonez/crojasaragonez.github.io/tree/main/src/data/e-means) include pinned dependencies, checksums, the environment record, all 120 runs, and the exact library settings. The notebook verifies the source and dataset before a fresh run and can export the article's charts.

<div class="paper-status"><strong>Scope.</strong> Measurements were collected November 11, 2026, using the official e-means CPU implementation. Reported speedups are medians of paired seed-level fit-time ratios against Faiss Lloyd at 25 passes. This is an exploratory comparison on MNIST, not a replication of the paper's large-scale GPU benchmarks.</div>
