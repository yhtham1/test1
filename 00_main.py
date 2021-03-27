import re
import zenhan


def printb(b):
	for it in b:
		print(it)
	print('len:{}'.format(len(b)))


def main():
	b = ''
	with open('data.txt', 'rt', encoding='utf8') as f:
		b = f.readlines()
	b1 = []
	for it in b:
		it = it.strip()
		# print(it)
		m = re.split(r'[_]', it)
		for it2 in m:
			if re.match(r'\d{6}', it2):
				pass
			else:
				b1.append(it2)
			pass
	b1 = sorted(b1)
	for it in b1:
		print(it)
	print('len:{}'.format(len(b1)))
	return

	b1 = []
	p = re.compile(r".*～(.*)")
	for it in b:
		a = it.strip()
		# a = zenhan.z2h(a)
		m = p.search(a)
		if m:
			# print(m.group(1))
			b1.append(m.group(1))
	b = []
	for it in b1:
		k = re.split(r'[・、]', it)
		for k1 in k:
			if len(k1):
				b.append(k1)
	b1 = []
	for it in b:
		k = it.split('、')
		for k1 in k:
			b1.append(k1)
	b = []
	for it in b1:
		if len(it):
			# print(it)
			b.append(it)
	b1 = sorted(b)
	print('total:{}名'.format(len(b1)))
	k = ''
	for it in b1:
		if k == it:
			print(k, ' - ', end='')
		else:
			if len(k):
				print(k)
		k = it
	print(it)


if __name__ == '__main__':
	main()
