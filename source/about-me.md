(about-me-main)=

# About Me

This is an overview of my open source [models](#models), [datasets](#datasets),
[projects](#projects) and [contributions](#pull-requests).

## Models

:::{card} [german-nlp-group/electra-base-german-uncased](https://huggingface.co/german-nlp-group/electra-base-german-uncased)
German [Electra](https://arxiv.org/abs/2003.10555) NLP model,
joined work with [Philipp Reißel](https://www.linkedin.com/in/philipp-reissel/)
([ambeRoad](https://amberoad.de/))

Talk about this model:\
[BEYOND BERT – Challenges and Potentials in the Training of German Language Models](https://www.youtube.com/watch?v=cxgrTd2AQis)
:::

:::{card} German T5 models in 3 different sizes

- [GermanT5/t5-efficient-gc4-all-german-large-nl36](https://huggingface.co/GermanT5/t5-efficient-gc4-all-german-large-nl36)
- [GermanT5/t5-efficient-gc4-german-base-nl36](https://huggingface.co/GermanT5/t5-efficient-gc4-german-base-nl36)
- [GermanT5/t5-efficient-gc4-all-german-small-el32](https://huggingface.co/GermanT5/t5-efficient-gc4-all-german-small-el32)

These models are trained on our [GC4 corpus](https://german-nlp-group.github.io/projects/gc4-corpus.html).

Joined work with [Stefan Schweter](https://github.com/stefan-it) ([schweter.ml](https://schweter.ml)) and [Philipp Schmid ](https://www.philschmid.de/) ([Hugging Face](https://huggingface.co/)).
:::

:::{card} [T-Systems-onsite/cross-en-de-roberta-sentence-transformer](https://huggingface.co/T-Systems-onsite/cross-en-de-roberta-sentence-transformer)
This model is intended to [compute sentence (text) embeddings](https://www.sbert.net/examples/applications/computing-embeddings/README.html)
for English and German text. These embeddings can then be compared with [cosine-similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
to find sentences with a similar semantic meaning.
:::

:::{card} [T-Systems-onsite/mt5-small-sum-de-en-v2](https://huggingface.co/T-Systems-onsite/mt5-small-sum-de-en-v2)
A bilingual summarization model for English and German.
It is based on the multilingual T5 model [google/mt5-small](https://huggingface.co/google/mt5-small).
:::

:::{card} [German ELMo Model](https://github.com/t-systems-on-site-services-gmbh/german-elmo-model)
This is a German [ELMo deep contextualized word representation](https://allennlp.org/elmo).
It is trained on a special [German Wikipedia Text Corpus](https://github.com/t-systems-on-site-services-gmbh/german-wikipedia-text-corpus).
:::

## Datasets

:::{card} [Ger-RAG-eval](https://huggingface.co/datasets/deutsche-telekom/Ger-RAG-eval)
This dataset is intended for the evaluation of German RAG (retrieval augmented generation) capabilities of LLM models.
It is based on the test set of the [deutsche-telekom/wikipedia-22-12-de-dpr](https://huggingface.co/datasets/deutsche-telekom/wikipedia-22-12-de-dpr)
data set (also see [wikipedia-22-12-de-dpr on GitHub](https://github.com/telekom/wikipedia-22-12-de-dpr)) and
consists of 4 subsets or tasks.

Ger-RAG-eval is also implemented in [LightEval](https://github.com/huggingface/lighteval):

- [community_tasks/german_rag_evals.py](https://github.com/huggingface/lighteval/blob/main/community_tasks/german_rag_evals.py)
- [tasks/all_german_rag_evals.txt](https://github.com/huggingface/lighteval/blob/main/examples/tasks/all_german_rag_evals.txt)
:::

:::{card} [wikipedia-22-12-de-dpr](https://huggingface.co/datasets/deutsche-telekom/wikipedia-22-12-de-dpr)
This dataset provides a German dataset for DPR model training.
DPR (Dense Passage Retrieval) is one of the most important components of RAG applications.
Based on this dataset, German document retrieval models can be trained.

The unique feature of this data set is that it contains not only training data for questions,
but also imperative questions.
An imperative question is a type of question that is phrased as a command or an instruction.
Since there is a formal and informal form of address in German, both cases are included in the case of imperative questions.
:::

:::{card} [The German colossal, cleaned Common Crawl corpus (GC4 corpus)](https://german-nlp-group.github.io/projects/gc4-corpus.html)
This is a German text corpus which is based on [Common Crawl](https://commoncrawl.org/).
The text corpus has the size of 454 GB packed. Unpacked it is more than 1 TB.
It has been cleaned up and preprocessed and can be used for various tasks in the NLP field.
The dataset is joined work with [Philipp Reißel](https://twitter.com/phil_ipp_)
([ambeRoad](https://amberoad.de/)).
:::

:::{card} STSb Multi MT
Machine translated multilingual translations and
the English original of the [STSbenchmark dataset](https://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark).
Translation has been done with [deepl.com](https://www.deepl.com/).\
This dataset is available on [GitHub](https://github.com/PhilipMay/stsb-multi-mt) and
as a [Hugging Face Dataset](https://huggingface.co/datasets/stsb_multi_mt).
:::

:::{card} [German Backtranslated Paraphrase Dataset](https://huggingface.co/datasets/deutsche-telekom/ger-backtrans-paraphrase)
This is a dataset of more than 21 million German paraphrases.
These are text pairs that have the same meaning but are expressed with different words.
This dataset can be used for example to train semantic text embeddings.
To do this, for example, [SentenceTransformers](https://www.sbert.net/)
and the [MultipleNegativesRankingLoss](https://www.sbert.net/docs/package_reference/losses.html#multiplenegativesrankingloss)
can be used.
:::

:::{card} [Wikipedia 2 Corpus](https://github.com/GermanT5/wikipedia2corpus)
Tools to extract and clean the Wikipedia texts to transform them into a text corpus for self-supervised NLP model training.
Includes also a prepared corpus for English and German language.
:::

:::{card}  [NLU Evaluation Data - German and English + Similarity](https://github.com/t-systems-on-site-services-gmbh/NLU-Evaluation-Data-de-en)
This repository contains two datasets:

1. A labeled multi-domain (21 domains) German and
   English dataset with 25K user utterances for human-robot interaction.
   It is also available as a Hugging Face dataset:
   [deutsche-telekom/NLU-Evaluation-Data-en-de](https://huggingface.co/datasets/deutsche-telekom/NLU-Evaluation-Data-en-de)
2. A dataset with 1,127 German sentence pairs with a similarity score. The sentences originate from the first data set.

:::

:::{card} [deutsche-telekom/NLU-few-shot-benchmark-en-de](https://huggingface.co/datasets/deutsche-telekom/NLU-few-shot-benchmark-en-de)
This is a few-shot training dataset from the domain of human-robot interaction.
It contains texts in German and English language with 64 different utterances (classes).
Each utterance (class) has exactly 20 samples in the training set.
This leads to a total of 1280 different training samples.

The dataset is intended to benchmark the intent classifiers of chat bots in English and especially in German language.
We are building on our
[deutsche-telekom/NLU-Evaluation-Data-en-de](https://huggingface.co/datasets/deutsche-telekom/NLU-Evaluation-Data-en-de)
data set.
:::

## Projects

:::{card} [Machine Learning Tool Box 2](https://github.com/telekom/mltb2) ([Documentation Page](https://telekom.github.io/mltb2/))
A box of different machine learning tools. It contains tools for:\
data loading,
[fastText](https://fasttext.cc/), files, Markdown,
Markdown,
[OpenAI](https://github.com/openai/openai-python),
[Optuna](https://optuna.readthedocs.io/), plot,
[SoMaJo](https://github.com/tsproisl/SoMaJo),
text cleaning,
[Transformers](https://huggingface.co/docs/transformers/index)
:::

:::{card} [XLSR – Cross-Lingual Sentence Representations](https://github.com/German-NLP-Group/xlsr)
Models and training code for cross-lingual sentence representations like
[T-Systems-onsite/cross-en-de-roberta-sentence-transformer](https://huggingface.co/T-Systems-onsite/cross-en-de-roberta-sentence-transformer)
:::

:::{card} [LightGBM Tools](https://github.com/telekom/lightgbm-tools)
This Python package implements tools for [LightGBM](https://lightgbm.readthedocs.io/).
In the current version lightgbm-tools focuses on binary classification metrics.
:::

:::{card} [ML-Cloud-Tools](https://github.com/telekom/ml-cloud-tools)
Tools for machine learning in cloud environments.
At the moment it is only a tool to easily handle [Amazon S3](https://aws.amazon.com/s3/).
:::

:::{card} [Census-Income with LightGBM and Optuna](https://github.com/telekom/census-income-lightgbm)
This project uses the [census income data](https://archive-beta.ics.uci.edu/ml/datasets/census+income) and
fits [LightGBM](https://lightgbm.readthedocs.io/) models on it.
It is not intended to bring super good results, but rather as a demo to show the interaction between
[LightGBM](https://lightgbm.readthedocs.io/), [Optuna](https://optuna.readthedocs.io/en/stable/index.html) and
[HPOflow](https://github.com/telekom/HPOflow). The usage of HPOflow is optional and can be removed if wanted.
We also calculare the feature importances
with [SHAP (SHapley Additive exPlanations)](https://github.com/slundberg/shap).
:::

:::{card} [S.M.A.R.T. Prometheus Metrics Exporter](https://github.com/PhilipMay/smart-prom-next)
smart-prom-next is a [Prometheus](https://prometheus.io/docs/introduction/overview/) metric exporter for
[S.M.A.R.T.](https://en.wikipedia.org/wiki/S.M.A.R.T.) values of hard disks.
:::

:::{card} [MLflow Image](https://github.com/PhilipMay/mlflow-image)
The MLflow Docker image.\
MLflow does not provide an official Docker image. This project fills that gap.
:::

:::{card} [Style-Doc](https://github.com/telekom/style-doc)
This is Black for Python docstrings and reStructuredText (rst). It can be used to format
docstrings ([Google docstring format](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings))
in Python files or [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html).
:::

:::{card} [conda-forge/hyperopt-feedstock](https://github.com/conda-forge/hyperopt-feedstock)
[conda-forge](https://conda-forge.org/) release of [Hyperopt](https://github.com/hyperopt/hyperopt)
:::

## Pull Requests

:::{card} [Hugging Face / Transformers](https://github.com/huggingface/transformers)

- add classifier_dropout to classification heads: [#12794](https://github.com/huggingface/transformers/pull/12794)
- add option for subword regularization in sentencepiece tokenizer: [#11149](https://github.com/huggingface/transformers/pull/11149),
  [#11417](https://github.com/huggingface/transformers/pull/11417)
- add strip_accents to basic BertTokenizer: [#6280](https://github.com/huggingface/transformers/pull/6280)
- refactor slow sentencepiece tokenizers and add tests: [#11716](https://github.com/huggingface/transformers/pull/11716),
  [#11737](https://github.com/huggingface/transformers/pull/11737)
- [more fixes and improvements](https://github.com/huggingface/transformers/pulls?q=is%3Apr+author%3APhilipMay)

:::

:::{card} [Optuna](https://github.com/optuna/optuna)

- add MLflow integration callback: [#1028](https://github.com/optuna/optuna/pull/1028)
- trial level suggest for same variable with different parameters give warning: [#908](https://github.com/optuna/optuna/pull/908)
- [more fixes and improvements](https://github.com/optuna/optuna/pulls?q=is%3Apr+author%3APhilipMay)

:::

:::{card} [Sentence Transformers](https://github.com/UKPLab/sentence-transformers)

- add callback so we can do pruning and check for nan values: [#327](https://github.com/UKPLab/sentence-transformers/pull/327)
- add option to pass params to tokenizer: [#342](https://github.com/UKPLab/sentence-transformers/pull/342)
- always store best_score: [#439](https://github.com/UKPLab/sentence-transformers/pull/439)
- fix for OOM problems on GPU with large datasets: [#525](https://github.com/UKPLab/sentence-transformers/pull/525)
- [more fixes and improvements](https://github.com/UKPLab/sentence-transformers/pulls?q=is%3Apr+author%3APhilipMay)

:::

:::{card} [SetFit - Efficient Few-shot Learning with Sentence Transformers](https://github.com/huggingface/setfit)

- add option to normalize embeddings [#177](https://github.com/huggingface/setfit/pull/177)
- add option to set `samples_per_label` [#196](https://github.com/huggingface/setfit/pull/196)
- add warmup_proportion param - make warmup_steps configurable [#140](https://github.com/huggingface/setfit/pull/140)
- add option to use amp / FP16 [#134](https://github.com/huggingface/setfit/pull/134)
- add num_epochs to train_step calculation [#139](https://github.com/huggingface/setfit/pull/134)
- add more loss function options [#159](https://github.com/huggingface/setfit/pull/159)
- [more fixes and improvements](https://github.com/huggingface/setfit/pulls?q=is%3Apr+author%3APhilipMay)

:::

:::{card} Other Fixes and Improvements

- [google-research/electra](https://github.com/google-research/electra): add toggle to turn off `strip_accents` [#88](https://github.com/google-research/electra/pull/88)
- [opensearch-project/opensearch-py](https://github.com/opensearch-project/opensearch-py):
  add Sphinx to generate Code Documentation [#112](https://github.com/opensearch-project/opensearch-py/pull/112) -
  also see [API Reference](https://opensearch-project.github.io/opensearch-py/api-ref.html)
- [deepset-ai/FARM](https://github.com/deepset-ai/FARM): [various fixes and improvements](https://github.com/deepset-ai/FARM/pulls?q=is%3Apr+author%3APhilipMay)
- [hyperopt/hyperopt](https://github.com/hyperopt/hyperopt): add progressbar with tqdm [#455](https://github.com/hyperopt/hyperopt/pull/455)
- [mlflow/mlflow](https://github.com/mlflow/mlflow): add possibility to use client cert. with tracking API [#2843](https://github.com/mlflow/mlflow/pull/2843)

:::

## Archived Projects

:::{card} [Lazy-Imports](https://github.com/telekom/lazy-imports)
Python tool to support lazy imports
:::

:::{card} [Machine Learning Tool Box](https://github.com/PhilipMay/mltb)
This is the machine learning tool box.
A collection of userful machine learning tools intended for reuse and extension.
The toolbox contains the following modules:
hyperopt, keras, lightgbm, shap, metrics, plot, tools

The main functionality is now available in
[MLTB2](https://github.com/telekom/mltb2).
:::

:::{card} [HPOflow](https://github.com/telekom/HPOflow)
Tools for [Optuna](https://optuna.readthedocs.io/),
[MLflow](https://www.mlflow.org/docs/latest/index.html) and
the integration of both
:::

:::{card} [Transformer-Tools](https://github.com/telekom/transformer-tools)
Tools for [Hugging Face / Transformers](https://github.com/huggingface/transformers)
:::

:::{card} [PyCharm Community Edition IDE for Python with bundled JRE](https://aur.archlinux.org/packages/pycharm-community-jre)
An [Arch Linux](https://archlinux.org/) package ([AUR](https://wiki.archlinux.org/title/Arch_User_Repository))
:::

%# Indices and tables
%
%- {ref}`genindex`
%- {ref}`modindex`
%- {ref}`search`
