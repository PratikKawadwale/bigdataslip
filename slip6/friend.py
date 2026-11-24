#Consider the Friends Data set. Write a Map Reduce program to find agewise number of friends sorted on age.
from mrjob.job import MRJob

class MRFriendsByAge(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        age = int(fields[2])
        friends = int(fields[3])

        yield age, friends

    def reducer(self, age, friends):
        yield age, sum(friends)

if __name__ == "__main__":
    MRFriendsByAge.run()