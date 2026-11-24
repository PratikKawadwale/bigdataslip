#2. Consider a Book text file. Write a Map Reduce program to find word count.
from mrjob.job import MRJob

class MRWordCount(MRJob):

    def mapper(self, _, line):
        words = line.split()

        for word in words:
            yield word, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == "__main__":
    MRWordCount.run()