#2. Consider the Friends Data set. Write a Map Reduce program to find number of friends per user.
from mrjob.job import MRJob

class MRFriendsPerUser(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        name = fields[1]
        friends = int(fields[3])

        yield name, friends

    def reducer(self, name, friends):
        yield name, sum(friends)

if __name__ == "__main__":
    MRFriendsPerUser.run()