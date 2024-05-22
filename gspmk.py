import csv
class GSPMK:
    def __init__(self, min_support, debug=False):
        self.min_support = min_support
        self.database = None
        self.frequent_patterns = []
        self.debug = debug
        if self.debug:
            print("GSPMK Algorithm")

    def generate_candidates(self, patterns, length):
        """
        Generate candidate sequences of length 'length' by joining patterns of length 'length-1'.
        Ensure no duplicate elements within a candidate sequence.
        """
        candidates = []
        for i in range(len(patterns)):
            for j in range(len(patterns)):
                if i != j and patterns[i][:length-2] == patterns[j][:length-2]:
                    candidate = patterns[i] + [patterns[j][-1]]
                    if len(set(candidate)) == length:
                        candidates.append(candidate)
        return candidates

    def scan_database(self, candidates):
        """
        Scan the database to count occurrences of each candidate sequence.
        """
        support_count = {}
        for seq in self.database:
            for candidate in candidates:
                if all(item in seq for item in candidate):
                    support_count[tuple(candidate)] = support_count.get(tuple(candidate), 0) + 1

        frequent_patterns = []
        for seq, count in support_count.items():
            support = count / len(self.database)
            if support >= self.min_support:
                frequent_patterns.append((list(seq), support))

        return frequent_patterns

    def fit(self, database, depth=5):
        """
        Fit the GSP model to the database to find frequent sequences.
        """
        self.database = database
        self.frequent_patterns = []
        
        # Generate frequent 1-sequences
        unique_items = set(item for seq in self.database for item in seq)
        for item in unique_items:
            support_count = sum(1 for seq in self.database if item in seq)
            support = support_count / len(self.database)
            if support >= self.min_support:
                self.frequent_patterns.append(([item], support))

        # Generate frequent sequences of length > 1
        for length in range(2, depth + 1):

            candidates = self.generate_candidates([pattern[0] for pattern in self.frequent_patterns], length)
            frequent_patterns = self.scan_database(candidates)
            if not frequent_patterns:  # Stop if no frequent patterns of this length
                break
            self.frequent_patterns.extend(frequent_patterns)

    def get_frequent_patterns(self):
        """
        Get the frequent sequences found by the GSP algorithm.
        """
        return self.frequent_patterns
    
    def export_frequent_patterns(self, filename):
        """
        Export the frequent sequences to a CSV file.
        """
        # create file with filename if not exists
        
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for pattern, support in self.frequent_patterns:
                writer.writerow([pattern, support])
