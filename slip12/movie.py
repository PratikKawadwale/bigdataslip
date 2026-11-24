#2. Consider the Movie Data set. Write a Map Reduce program to find average rating per user.

from mrjob.job import MRJob

class MRRatingAverage(MRJob):

    def mapper(self, _, line):
        userID, movieID, rating, timestamp = line.strip().split('\t')
        yield userID, float(rating)

    def reducer(self, userID, ratings):
        total = 0
        count = 0

        for rating in ratings:
            total += rating
            count += 1

        yield userID, total / count

if __name__ == '__main__':
    MRRatingAverage.run()
 