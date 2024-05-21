class GSP:
    def __init__(self, min_support):
        self.min_support = min_support
        self.database = None
        self.frequent_patterns = []

    def generate_candidates(self, patterns, length):
        """
        Generate candidate sequences of length 'length' by joining patterns of length 'length-1'.
        """
        candidates = []
        for i in range(len(patterns)):
            for j in range(i+1, len(patterns)):
                if patterns[i][:length-2] == patterns[j][:length-2]:
                    candidates.append(patterns[i] + [patterns[j][-1]])
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

        max_length = max(map(len, self.database))
        print(max_length)
        # Generate frequent 1-sequences
        unique_items = set(item for seq in self.database for item in seq)
        for item in unique_items:
            support_count = sum(1 for seq in self.database if item in seq)
            support = support_count / len(self.database)
            if support >= self.min_support:
                self.frequent_patterns.append(([item], support))

        # Generate frequent sequences of length > 1
        for length in range(2, depth + 1):
            print(length)
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


def helper_generate_database(database):
    """
    Helper function to generate the database from a list of sequences.
    """
    return [list(map(int, seq.split())) for seq in database]
# Example usage:
database = [[1, 2, 3, 4], [1, 2, 4], [1, 3, 4], [2, 3], [2, 4]]
# open database from file database.dup of format enter when end of cluster, space between elements
database = []
with open("smol.dup") as file:
    for line in file:
        database.append(list(map(int, line.strip().split())))
min_support = 0.01
print("data opened")

# save the database to a file in csv format
import csv
with open("smol.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(database)
print("data saved")

print(database)
gsp = GSP(min_support)
gsp.fit(database)
frequent_patterns = gsp.get_frequent_patterns()

print("Frequent Patterns:")
for pattern, support in frequent_patterns:
    print(pattern, "Support:", support)