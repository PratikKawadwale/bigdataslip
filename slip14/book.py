#2. Consider a book txt file. Write a Map Reduce program to display word count in sorted order.
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRSortedWordFrequency(MRJob):

    def mapper(self, _, line):
        for word in line.lower().split():
            yield word, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

    def mapper_sort(self, word, count):
        yield count, word

    def reducer_sort(self, count, words):
        for word in words:
            yield word, count

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(mapper=self.mapper_sort, reducer=self.reducer_sort)
        ]

if __name__ == "__main__":
    MRSortedWordFrequency.run()