import torch
from utils.tools import load_vocab, show_info
from utils.trainer import trainer
from utils.args import get_train_parser
from math import inf
from os import environ
import importlib
from preprocess import data_loader
import random
import warnings

warnings.filterwarnings("ignore")


def train():
	# cuda 的随机数种子
	torch.backends.cudnn.deterministic = True
	# gpu 加速
	torch.backends.cudnn.benchmark = True
	# 加载配置文件
	args = get_train_parser()
	# args.vocab  默认是./
	_, tgt_index2word = load_vocab(args.vocab)
	# vocab_size 词汇长度
	vocab_size = len(tgt_index2word)

	# 给args实例化对象添加’vocab_size‘属性并且赋值位vocab_size
	setattr(args, 'vocab_size', vocab_size)
	# 设置gpu
	args.cuda_num = str(torch.cuda.current_device())
	environ['CUDA_VISIBLE_DEVICES'] = args.cuda_num

	show_info(epoch=args.epoch, vocab_size=vocab_size, CUDA_NUM=args.cuda_num)

	environ['MASTER_ADDR'] = 'localhost'
	environ['MASTER_PORT'] = '8878'
	# 动态导入cuda共享模块torch.multiprocessing
	mp = importlib.import_module('torch.multiprocessing')
	seed = random.randint(0, 2048)
	setattr(args, 'world_size', len(args.cuda_num))
	# mp.spawn相对于torch.multiprocessing.spawn(function,args=(),nprocs=1)  nprocs进程数
	mp.spawn(trainer, nprocs=args.world_size, args=(args, seed))


if __name__ == '__main__':
	train()
