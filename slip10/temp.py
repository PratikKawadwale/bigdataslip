#2. Considerthe Temperature Data set. Write a Map Reduce program to find maximum temperature for each weather station.
from mrjob.job import MRJob

class MRMaxTemperature(MRJob):

    def mapper(self, _, line):
        data = line.split(',')
        station = data[0]
        temp_type = data[2]
        temp = int(data[3])

        if temp_type == "TMAX":
            yield station, temp

    def reducer(self, station, temperatures):
        yield station, max(temperatures)

if __name__ == "__main__":
    MRMaxTemperature.run()