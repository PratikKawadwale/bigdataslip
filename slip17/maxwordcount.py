from mrjob.job import MRJob
from mrjob.step import MRStep

class MRMaxWord(MRJob):

    def mapper(self, _, line):
        for word in line.lower().split():
            yield word, 1

    def reducer(self, word, counts):
        yield None, (sum(counts), word)

    def mapper_max(self, _, data):
        count, word = data
        yield None, (count, word)

    def reducer_max(self, _, values):
        count, word = max(values)
        yield word, count

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(mapper=self.mapper_max, reducer=self.reducer_max)
        ]

if __name__ == "__main__":
    MRMaxWord.run()