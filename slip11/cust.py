#2. Consider the Customer order Data set. Write a Map Reduce program to find the amount spent by each customer.
from mrjob.job import MRJob

class MRCustomerAmount(MRJob):

    def mapper(self, _, line):
        customer, item, amount = line.split(',')
        yield customer, float(amount)

    def reducer(self, customer, amounts):
        yield customer, sum(amounts)

if __name__ == "__main__":
    MRCustomerAmount.run()