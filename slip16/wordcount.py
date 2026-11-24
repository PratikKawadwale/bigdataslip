#2. Consider a book txt file. Write a Map Reduce program to display word count in sorted order.

from mrjob.job import MRJob

class MRWordCount(MRJob):

    def mapper(self, _, line):
        for word in line.lower().split():
            yield word, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == "__main__":
    MRWordCount.run()
#python3 wordcount.py book.txt | sort