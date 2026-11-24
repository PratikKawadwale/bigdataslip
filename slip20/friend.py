#2. Consider the Friends data set. Write a MapReduce program to find the person having maximun number of friends.
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRMaxFriends(MRJob):

    def mapper(self, _, line):
        data = line.strip().split(',')
        person = data[0]
        friends = data[1:]
        yield person, len(friends)

    def reducer(self, person, counts):
        yield None, (sum(counts), person)

    def reducer_max(self, _, values):
        count, person = max(values)
        yield person, count

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_max)
        ]

if __name__ == '__main__':
    MRMaxFriends.run()