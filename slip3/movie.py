#2. Consider the Movie Data set. Write a Map Reduce program to find number of movies watched by each user.
from mrjob.job import MRJob

class MRMovieCounter(MRJob):

    def mapper(self, _, line):
        line = line.strip()
        userID, movieID, rating, timestamp = line.split('\t')
        yield userID, movieID

    def reducer(self, userID, movies):
        total = 0

        for movieID in movies:
            total += 1

        yield userID, total

if __name__ == "__main__":
    MRMovieCounter.run()