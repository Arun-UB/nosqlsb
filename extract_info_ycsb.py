import re
import os
temp = "mongodb.dat" #for now
def extract_data(file_loc):
	if not os.path.exists(file_loc):
		print "failed to find file"
		return
	f = open(file_loc)
	f = f.readlines()
	for line in f:
		if re.search("AverageLatency",line):
			data = line.split(',')
			avg_latency = data[2].lstrip().rstrip()
		elif re.search("Throughput",line):
		 	data = line.split(',')
			throughput = data[2].lstrip().rstrip()
	 
		elif re.search("RunTime",line):
			data = line.split(',')
			run_time = data[2].lstrip().rstrip()
	
	return [avg_latency, throughput, run_time]

if __name__ == '__main__':
	print extract_data(temp)
	print extract_data("voldemort.dat")
