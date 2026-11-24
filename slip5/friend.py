#2. Consider the Friends Data set. Write a Map Reduce program to find average number friends for each age value.
from mrjob.job import MRJob

class MRFriendsAverage(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        age = fields[2]
        friends = int(fields[3])

        yield age, friends

    def reducer(self, age, friends):
        total = 0
        count = 0

        for friend in friends:
            total += friend
            count += 1

        yield age, total / count

if __name__ == "__main__":
    MRFriendsAverage.run()