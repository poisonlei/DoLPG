# 该函数将多句话的一行分割成多行
def split(file, save_file):
	with open(file, 'r') as f:
		data = [line.strip('\n').split('\t') for line in f.readlines()]
	with open(save_file, 'w') as f:
		for line in data:
			for seq in line:
				f.write(seq)
				f.write('\n')


def combine(file, save_file, cnt_max):
	with open(file, 'r', encoding='utf-8') as f:
		lines = [line for line in f.readlines()][:300000]
		print(len(lines))
		data = [line.strip('\n').strip() for line in lines]
	cnt = 0
	sent = []
	tmp = []
	for line in data:
		cnt += 1
		tmp.append(line)
		if cnt == cnt_max:
			cnt = 0
			sent.append('\t'.join(tmp))
			tmp = []
	with open(save_file, 'w', encoding='utf-8') as f:
		for line in sent:
			f.write(line)
			f.write('\n')


if __name__ == '__main__':
	train_source_file = './split/train.split'
	train_save_file = './comb/train.comb'

	pesu_source_file = './split/train.pesu.split'
	pesu_save_file = './comb/train.pesu.comb'

	test_source_file = './split/test.split'
	test_save_file = './comb/test.comb'

	combine(train_source_file, train_save_file, 10)
	combine(pesu_source_file, pesu_save_file, 10)
	combine(test_source_file, test_save_file, 10)
