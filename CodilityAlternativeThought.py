from collections import defaultdict, deque

class SlidingWindowLimiter:
	def __init__(self, N: int, T: int):
		self.N = int(N)
		self.T = int(T)
		self._history = defaultdict(deque)

	def process(self, timestamps, client_ids):
		result = []
		for ts, cid in zip(timestamps, client_ids):
			q = self._history[cid]
			cutoff = ts - self.T
			while q and q[0] <= cutoff:
				q.popleft()
			if len(q) < self.N:
				q.append(ts)
				result.append(True)
			else:
				result.append(False)
		return result


class FixedWindowLimiter:
	def __init__(self, N: int, T: int):
		self.N = int(N)
		self.T = int(T)
		self._counts = {}

	def process(self, timestamps, client_ids):
		result = []
		for ts, cid in zip(timestamps, client_ids):
			win = int(ts // self.T)  # floor(ts / T)
			key = (cid, win)
			count = self._counts.get(key, 0)
			if count < self.N:
				self._counts[key] = count + 1
				result.append(True)
			else:
				result.append(False)
		return result
