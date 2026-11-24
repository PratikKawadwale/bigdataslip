#2. Consider the Movie Data set. Write a Map Reduce program to find number of ratings per rating value.

from mrjob.job import MRJob

class MRRatingFrequency(MRJob): 
    def mapper(self, _, line): 
        line = line.strip() 
        userID, movieID, rating, timestamp = line.split('\t') 
        yield rating, 1 
    def reducer(self, rating, counts): 
        yield rating, sum(counts) 
if __name__ == "__main__": 
    MRRatingFrequency.run() 