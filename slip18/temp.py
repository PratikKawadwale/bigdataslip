#2. Considerthe Temperature Data set. Write a Map Reduce program to find minimum temperature for each weather station.
from mrjob.job import MRJob

class MRMinTemperature(MRJob):

    def mapper(self, _, line):
        data = line.split(',')
        station = data[0]
        temp_type = data[2]
        temp = int(data[3])

        if temp_type == "TMIN":
            yield station, temp

    def reducer(self, station, temperatures):
        yield station, min(temperatures)

if __name__ == "__main__":
    MRMinTemperature.run()