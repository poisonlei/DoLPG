from utils import constants
import argparse
from collections import Counter
from math import inf
from utils.tools import save_vocab


def create_vocab(file_list, vocab_num):
	def create_corpus(file, num):
		with open(file, 'r', encoding='utf-8') as f:
			lines = [line for line in f.readlines()][:num]
			print(len(lines))
			corpus = [word.lower() for line in lines for word in line.strip('\n').split()]
		return corpus

	corpus = []
	print(file_list)
	for file in file_list:
		print(file)
		if file == './split/test.split':
			corpus.extend(create_corpus(file, 15000))
			# continue
		else:
			corpus.extend(create_corpus(file, 300000))

	word2index = {}
	index2word = {}
	word2index[constants.PAD_WORD] = constants.PAD_index
	index2word[constants.PAD_index] = constants.PAD_WORD
	word2index[constants.UNK_WORD] = constants.UNK_index
	index2word[constants.UNK_index] = constants.UNK_WORD
	word2index[constants.BOS_WORD] = constants.BOS_index
	index2word[constants.BOS_index] = constants.BOS_WORD
	word2index[constants.EOS_WORD] = constants.EOS_index
	index2word[constants.EOS_index] = constants.EOS_WORD

	if vocab_num != -1:
		w_count = [pair[0] for pair in Counter(corpus).most_common(vocab_num)]
	else:
		w_count = set(corpus)
	for word in w_count:
		word2index[word] = len(word2index)
		index2word[len(index2word)] = word
	return word2index, index2word


def main_vocab():
	parser = argparse.ArgumentParser(description='Create vocabulary.', prog='creat_vocab')

	parser.add_argument('--file', type=str, nargs='+',
						default={'./split/train.pesu.split', './split/train.split', './split/test.split'})
	parser.add_argument('--vocab_num', type=int, nargs='?', default=-1)
	parser.add_argument('--save_path', type=str, default='./vocab/vocab.share')

	args = parser.parse_args()
	word2index, index2word = create_vocab(file_list=args.file, vocab_num=args.vocab_num)
	print('Vocabulary Number: %d' % len(word2index))
	save_vocab(word2index, index2word, args.save_path)


if __name__ == '__main__':
	main_vocab()
