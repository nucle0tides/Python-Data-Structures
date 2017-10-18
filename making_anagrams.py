import collections
def number_needed(a, b): 
	a_freq = dict(collections.Counter(a))
	b_freq = dict(collections.Counter(b))
	count(a_freq, b_freq)

def count(a, b):
	count = 0
	for k, v in a.items(): 
		if k in b: # everything in a & b
			count += abs(v - b[k])
		if k not in b: # everything in a
			count += v
	for k, v in b.items():
		if k not in a: # everything in b
			count += v
	return count

if __name__ == '__main__':
	number_needed('fsqoiaidfaukvngpsugszsnseskicpejjvytviya', 'ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget')