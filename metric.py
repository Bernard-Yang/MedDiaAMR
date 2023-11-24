import os
import torch
import random
# from apex import amp

random.seed(0)
torch.manual_seed(0)
torch.cuda.manual_seed(0)
import torch.nn as nn
import numpy as np
from rouge import Rouge
import codecs
np.random.seed(0)
torch.backends.cudnn.deterministic = True
import tqdm
import argparse
import config_utils
from dataset_utils import (
    load_vocab_new,
    tokenize,
    bpe_tokenize,
)
from nltk.translate import bleu
from nltk.translate.bleu_score import SmoothingFunction
from nltk.translate.bleu_score import sentence_bleu
from model_adapter import DualTransformer
from torch.utils import data
from torch import optim
from bpemb import BPEmb
import math
import time
import utils as nlg_eval_utils
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def id2words(path, vocab_size=-1):
    words = []
    with codecs.open(path, "r", "utf-8") as fr:
        for line in fr:
            line = line.strip().replace("\1", " ").split()
            words.append(line[0])
    return words


def cal_ROUGE2(refer, candidate):
    if not candidate:
        candidate = '<unk>'
    rouge = Rouge()
    scores = rouge.get_scores(' '.join(candidate), ' '.join(refer))
    return scores[0]['rouge-2']['f']
    
def cal_ROUGE1(refer, candidate):
    if not candidate:
        candidate = '<unk>'
    rouge = Rouge()
    scores = rouge.get_scores(' '.join(candidate), ' '.join(refer))
    print(scores)
    return scores[0]['rouge-1']['f']

def cal_ROUGEL(refer, candidate):
    if not candidate:
        candidate = '<unk>'
    rouge = Rouge()
    scores = rouge.get_scores(' '.join(candidate), ' '.join(refer))
    return scores[0]['rouge-l']['f']

def cal_BLEU(refer, candidate, ngram=1):
    smoothie = SmoothingFunction().method4
    if ngram == 1:
        weight = (1, 0, 0, 0)
    elif ngram == 2:
        weight = (0.5, 0.5, 0, 0)
    elif ngram == 3:
        weight = (0.33, 0.33, 0.33, 0)
    elif ngram == 4:
        weight = (0.25, 0.25, 0.25, 0.25)
    return sentence_bleu(refer, candidate, weights=weight, smoothing_function=smoothie)

with open('output.txt', 'r') as outs:
    with open('target.txt', 'r') as tgts:
        candidates = outs.readlines()
        refers = tgts.readlines()

metric = {'rouge1':[], 'rouge2':[], 'rougel':[], 'bleu1':[], 'bleu2':[], 'bleu3':[], 'bleu4':[],
    'distinct-1':[], 'distinct-2':[], 'distinct-3':[], 'distinct-4':[]}

index = 0
for candidate, refer in zip(candidates, refers):
    index += 1
    candidate = candidate.strip()
    refer = refer.strip()
    metric['rouge1'].append(cal_ROUGE1(candidate, refer))
    metric['rouge2'].append(cal_ROUGE2(candidate, refer))
    metric['rougel'].append(cal_ROUGEL(candidate, refer))
    metric['bleu1'].append(cal_BLEU(refer, candidate, ngram=1))
    metric['bleu2'].append(cal_BLEU(refer, candidate, ngram=2))
    metric['bleu3'].append(cal_BLEU(refer, candidate, ngram=3))
    metric['bleu4'].append(cal_BLEU(refer, candidate, ngram=4))
    print(index)
    # metrics = nlg_eval_utils.repetition_distinct_metric(candidate, metrics={}, repetition_times=2)
    # metric['distinct-1'].append(metrics['distinct-1'])
    # metric['distinct-2'].append(metrics['distinct-2'])
    # metric['distinct-3'].append(metrics['distinct-3'])
    # metric['distinct-4'].append(metrics['distinct-4'])



key = sorted(metric.keys())
for k in key:
    print(k, metric[k])
print("=" * 10)
