import re
import os
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
	mongodb =  extract_data('/home/akarsh/mongodb.dat')
	cassandra =  extract_data("/home/akarsh/cassandra.dat")
	voldemort = extract_data('/home/akarsh/voldemort.dat')
	f = open("avg_latency.dat","w")
	f.write('MongoDB  '+ mongodb[0] +'\n')
	f.write('Cassandra  ' + cassandra[0] +'\n')
	f.write('Voldemort  ' + voldemort[0] + '\n')
	
	f = open("throughput.dat","w")
	f.write('MongoDB  '+ mongodb[1] +'\n')
	f.write('Cassandra  ' + cassandra[1] +'\n')
	f.write('Voldemort  ' + voldemort[1] + '\n')
	
	f = open("runtime.dat","w")
	f.write('MongoDB  '+ mongodb[2] +'\n')
	f.write('Cassandra  ' + cassandra[2] +'\n')
	f.write('Voldemort  ' + voldemort[2] + '\n')
