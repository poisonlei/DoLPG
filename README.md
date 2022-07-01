# DoLPG

Code for paper  [Document-level Paraphrase Generation Base on Attention Enhanced Graph LSTM]  by Dong Qiu,
Lei Chen and Yang Yv.

<img src="https://github.com/poisonlei/DoLPG/blob/main/img/PG.png?raw=true" width = "800" alt="overview" align=center />

## Datasets

We leverage [ParaNMT](https://www.cs.cmu.edu/~jwieting/) to train a sentence-level paraphrasing model. We
select [News-Commentary](http://www.statmt.org/wmt20/translation-task.html) as document corpora, and we employ sentence-level paraphrasing
model to generate a pseudo document-level paraphrase and use ALBERT to generate its coherence relationship graph.

## Dependencies

> PyTorch >= 1.4
> 
>Transformers == 4.1.1
> 
>nltk == 3.5
> 
>tqdm
> 
>torch_optimizer == 0.1.0

## Train a Document-Level Paraphrase Model

### Step1: Prepare dataset

We release the dataset we used in [data folder](https://github.com/L-Zhe/CoRPG/releases/download/model/news-commentary.zip)

### Step2: Process dataset

Create Vocabulary:

```shell
data/createVocab.py 
```

Processing Training Dataset and Test Dataset:

```shell
preprocess.py 
```

### Step3: Train a document-level paraphrase model

```shell
train.py
```

### Step4: Generate document-level paraphrase

```shell
generator.py
```

## Pre-trained Models

```shell
albert
```

## Evaluation Matrics

We evaluate our model in three aspects: relevancy, diversity, coherence.

### Relevancy

We leverage BERTScore (in Transformer/bert_score) to evaluate the semantic relevancy between paraphrase and original sentence.

### Diversity

We employ self-[TER](https://github.com/jhclark/multeval) and self-[WER](https://github.com/belambert/asr-evaluation) to evaluate the
diversity of our model.

### Coherence

```shell
eval/coherence.py
```
