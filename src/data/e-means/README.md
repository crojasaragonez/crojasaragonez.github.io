# e-means versus Lloyd on MNIST

An actual CPU experiment run November 11, 2026, supporting the article
`src/content/blog/e-means-vs-k-means-on-mnist.md`.

## Reproduce

Open [benchmark.ipynb](benchmark.ipynb) in VS Code or Jupyter. It contains
the experiment code, methodology, validation, result tables, paired
comparisons, and inline charts. Python 3.11.15 was used for the original run.
Create an isolated environment from the repository root:

```sh
python3 -m venv /tmp/e-means-repro
/tmp/e-means-repro/bin/python -m pip install -r src/data/e-means/requirements.txt
```

Select `/tmp/e-means-repro/bin/python` as the notebook kernel. For Jupyter,
register it with:

```sh
/tmp/e-means-repro/bin/python -m ipykernel install --user --name e-means --display-name "Python (e-means)"
```

Restart the kernel and run all cells, starting from the repository root or
this notebook's directory. The saved notebook includes tables and charts
from the recorded measurements, so it can also be read without running it.

- **Explore recorded results:** keep `RUN_FRESH = False` (the default).
  This runs the analysis offline and leaves the original files unchanged.
- **Rerun the full experiment:** set `RUN_FRESH = True`. New measurements
  and summaries go to `/tmp/e-means-notebook-rerun/full` by default.
- **Check all four implementations quickly:** also set `SMOKE_TEST = True`.
  This uses small subsets and writes to `/tmp/e-means-notebook-rerun/smoke`.
  The notebook omits full-experiment plots and paired comparisons in this mode.
- **Export figures:** set `EXPORT_FIGURES = True`; edit `FIGURE_DIR` to
  choose the destination. It defaults to `/tmp/e-means-notebook-figures`.
  To refresh the article's assets deliberately, point it at
  `public/images/blog/e-means` in this checkout.

The notebook replaces the benchmark and plotting scripts. Its configuration
cell exposes cache and output paths; rerunning does not replace the article's
recorded measurements. Fresh runs replace prior files in their designated
rerun directory. Reviewing new results and updating article numbers is a
separate step.

Fresh-run mode downloads MNIST and three unmodified official e-means source
files to `/tmp/e-means-cache` by default. It verifies
SHA-256 checksums even for cached files. It loads those files as the Python
package `official_e_means` to avoid modifying the installed Faiss package.
Faiss 1.15.1 supplies the C++ CPU implementation but does not contain the new
Python e-means module. The official source is pinned to commit
`f777f7d82d30a444febaa29654296738d85b3f7a`; this is not a reimplementation of
the paper. The pinned code's constants and defaults differ in some details
from the paper. Dependencies and source pins capture what was actually run.

The validation cell verifies the complete run matrix, finite metrics, thread
settings, cluster occupancy bounds, and Lloyd iteration counts. Full mode
expects 120 configurations; smoke mode expects four. Recorded-results mode
needs only the files already in this repository, with no downloads or training.

## Protocol

- Dataset: [MNIST via Keras](https://keras.io/api/datasets/mnist/), 60,000
  training and 10,000 test images. The Keras-hosted `mnist.npz` archive has
  SHA-256 `731c5ac602752760c8e48fbffcf8c3b850d9dc2a2aedcf2cc48468fc17b673d1`.
  Credit: Yann LeCun, Corinna Cortes and Christopher J. C. Burges. Keras lists
  MNIST under CC BY-SA 3.0. Dataset files and image derivatives are not shipped
  in this repository.
- Flatten each 28×28 image to 784 contiguous float32 coordinates and divide
  by 255. No PCA, per-feature standardization, unit normalization, or embedding
  model. The same data is supplied to all implementations.
- Cluster counts 10 and 100; seeds 0–4. No tuning on the test set. The fixed
  budget grid is e-means at 1, 2.5, 5, 10, 25 passes; Faiss Lloyd at 1, 3, 5,
  10, 25 iterations; sklearn MiniBatchKMeans at 5 nominal epochs; sklearn
  KMeans with greedy k-means++ at 25 maximum iterations.
- For each `(k, seed)`, initial centers for e-means, Faiss Lloyd, and sklearn
  MiniBatchKMeans are exactly the same random training rows:
  `RandomState(seed).permutation(n)[:k]`. One initialization per run, no
  best-of-many selection. The k-means++ practical reference draws its own
  centers with the corresponding seed, using `n_init=1`; its initialization
  is included in fit time.
- Faiss Lloyd: exact L2 search, `nredo=1`, no spherical option, no GPU.
  `max_points_per_centroid=n` disables default training subsampling.
- e-means: official `NumpyEmeans`, default automatic batch law, step schedule,
  revival and closing means. Trains on every training row, including remainder
  batches; captures its default last-pass assignments. We **do not** score
  those moving-pass assignments or its logged objective. Batch size, initial
  step and update count are saved per run.
- MiniBatchKMeans: uses the corresponding 5-pass e-means batch size;
  `n_init=1`, `max_iter=5`, `tol=0`, `max_no_improvement=None`,
  `compute_labels=False`. Other defaults, including reassignment, remain.
  Its minibatches are sampled with replacement: five nominal epochs do not
  guarantee five full shuffled passes. This is a practical library reference,
  not an isolation of only the centroid update rule.
- sklearn KMeans: `algorithm='lloyd'`, `tol=0`, `max_iter=25`, `n_init=1`,
  greedy k-means++ initialization; exact label stability can still stop it.
- One CPU thread for Faiss, OpenMP and BLAS, enforced before imports and via
  `threadpoolctl`. A warmup runs each implementation once. The order of the
  12 configurations is shuffled deterministically within each `(k, seed)`.
  Models run sequentially; each configuration has one timed fit per seed.
- Fit time includes model construction, copies inside the wrapper, internal
  preparation and closing means. Shared random-row initialization, data
  download, loading, common preprocessing and metric computation are excluded.
  The MiniBatch wrapper also resolves the batch recipe within its fit timer.
  No claim is made about full application latency or memory/energy use.
- Reassign **all** train and test vectors to the final centroids with the
  same exact Faiss nearest-neighbor call. MSE is mean squared vector distance,
  `mean_i(sum_j((x_ij - c_assignment,j)**2))`; it is **not** per-pixel MSE.
  Also report ARI and arithmetic-normalized NMI against digit labels; labels
  never enter training. Record occupied clusters to expose collapse.

## Outputs and interpretation

- `runs.csv`: all 120 fits, train/test metrics, fit seconds, recipe details.
- `environment.json`: versions, hardware, timestamp, threadpool state, data
  and source provenance. This documents the original machine, not your rerun.
- `summary.csv`: medians and observed minima/maxima across the five seeds.
- `comparisons.json`: **paired** speedups and MSE changes against the same
  seed's 25-iteration Faiss Lloyd result. The median of ratios need not equal
  the ratio of medians. Win counts are strict lower test MSE; no tolerance or
  post-hoc margin is applied.
- `public/images/blog/e-means/{epochs,time}.{svg,png}`: generated figures.
  Bands show observed seed extrema, not confidence intervals. Each point is
  a separate fit with that requested budget, not a checkpoint in one run.
  Changing e-means' budget changes its automatic recipe. Figure error axes
  have different ranges for the two cluster counts and do not start at zero.

Fresh notebook runs save `runs.csv`, `environment.json`, `summary.csv` and
`paired-comparisons.csv` to their rerun directory. The notebook's `runs`,
`summary`, `paired` and `comparisons` DataFrames expose the measurements and
calculations for further exploration. The original `comparisons.json` is
retained as the article's recorded summary.

This small raw-pixel CPU benchmark is not a replication of the paper's
large embedding/GPU speed comparisons. Five seeds characterize some
initialization variability; timings have no independent repeated-run estimate
of system noise. Test-set comparisons are exploratory; no significance claim
or universal speedup follows. ARI is label agreement, not classification
accuracy, and increasing `k` changes the task.

Primary references:

- [Project](https://e-means.github.io/)
- [Paper, submitted November 6, 2026](https://arxiv.org/abs/2611.09501)
- [Pinned official code](https://github.com/facebookresearch/faiss/tree/f777f7d82d30a444febaa29654296738d85b3f7a/contrib/e_means), MIT licensed.
- [sklearn KMeans](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.KMeans.html)
- [sklearn MiniBatchKMeans](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.MiniBatchKMeans.html)
