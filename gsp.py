import logging
import multiprocessing as mp
from collections import Counter
from itertools import product, chain

class GSP:
    def __init__(self, raw_transactions):
        self.freq_patterns = []
        self.max_size = max(map(len, raw_transactions))
        self.raw_transactions = [tuple(transaction) for transaction in raw_transactions]
        counts = Counter(chain.from_iterable(raw_transactions))
        self.unique_candidates = [(item,) for item in counts]

    def _calc_frequency(self, item, minsup):
        frequency = sum(1 for transaction in self.raw_transactions if item in transaction)
        return (item, frequency) if frequency >= minsup else None

    def _support(self, items, minsup=0):
        results = mp.Manager().dict()
        pool = mp.Pool(processes=mp.cpu_count())

        for item in items:
            pool.apply_async(self._calc_frequency,
                             args=(results, item, minsup))
        pool.close()
        pool.join()

        return dict(results)
    def _print_status(self, run, candidates):
        logging.debug(f"Run {run}\nThere are {len(candidates)} candidates.\nThe candidates have been filtered down to {len(self.freq_patterns[run - 1])}.\n")

    def search(self, minsup=0.2):
        assert 0.0 < minsup <= 1.0
        minsup = int(len(self.raw_transactions) * minsup)
        candidates = self.unique_candidates
        self.freq_patterns.append(self._support(candidates, minsup))
        k_items = 1
        self._print_status(k_items, candidates)
        while len(self.freq_patterns[k_items - 1]) and (k_items + 1 <= self.max_size):
            k_items += 1
            items = sorted(set(pattern for pattern in self.freq_patterns[k_items - 2].keys()))
            candidates = list(product(items, repeat=k_items))
            self.freq_patterns.append(self._support(candidates, minsup))
            self._print_status(k_items, candidates)
        return self.freq_patterns[:-1]

if __name__ == "__main__":
    raw_transactions = [
        ['Bread', 'Milk'],
        ['Bread', 'Diaper', 'Beer', 'Eggs'],
        ['Milk', 'Diaper', 'Beer', 'Coke'],
        ['Bread', 'Milk', 'Diaper', 'Beer'],
        ['Bread', 'Milk', 'Diaper', 'Coke']
    ]
    logging.basicConfig(level=logging.DEBUG)
    gsp = GSP(raw_transactions)
    frequent_patterns = gsp.search(0.3)
    print("Frequent Patterns:")
    for patterns in frequent_patterns:
        print(patterns)