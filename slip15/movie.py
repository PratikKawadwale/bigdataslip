#2. Consider the Movie Data set. Write a Map Reduce program to find average rating per Movie.
from mrjob.job import MRJob

class MRAverageRating(MRJob):

    def mapper(self, _, line):
        userID, movieID, rating, timestamp = line.split('\t')
        yield movieID, float(rating)

    def reducer(self, movieID, ratings):
        total = 0
        count = 0

        for rating in ratings:
            total += rating
            count += 1

        yield movieID, total / count

if __name__ == "__main__":
    MRAverageRating.run()