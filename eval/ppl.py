from tqdm import tqdm
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import argparse
import os
import torch


@torch.no_grad()
def cal_ppl(file, model_file):
	with open(file, 'r', encoding='utf-8') as f:
		sents = [line.strip('\n').strip().lower() for line in f.readlines()]
	model = GPT2LMHeadModel.from_pretrained(model_file).cuda()
	tokenizer = GPT2TokenizerFast.from_pretrained(model_file)
	model.eval()
	ppl = torch.FloatTensor(len(sents)).cuda()
	max_length = model.config.n_positions
	for index, sent in tqdm(enumerate(sents)):
		encodings = tokenizer(sent, return_tensors='pt')
		input_ids = encodings.input_ids[:, :max_length].cuda()
		target_ids = input_ids.clone()
		outputs = model(input_ids, labels=target_ids)
		ppl[index] = torch.exp(outputs[0]).tolist()
	print('perplexity: %f' % ppl.mean())


def get_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--model_file', type=str, default='gpt2')
	parser.add_argument('--cuda_num', type=str, default='0')
	parser.add_argument('--file', type=str, default='../data/generate/result.txt')
	return parser.parse_args()


if __name__ == '__main__':
	args = get_parser()
	os.environ['CUDA_VISIBLE_DEVICES'] = args.cuda_num
	cal_ppl(args.file, args.model_file)
