from fabric.api import *
from time import strftime


def ycsb(voldemort,workload,recordcount):
  voldemort_ip='10.72.189.226'
  #stime=strftime("%H%M%S")[1:4]
  #Voldemort
  if len(voldemort)>0 :
    cmd='cd /home/ubuntu/ycsb-0.1.4/ && bin/ycsb load voldemort -p bootstrap_urls=tcp://'+voldemort_ip+':6666 -p recordcount='+recordcount+' -P workloads/'+ workload
    cmd='cd /home/ubuntu/ycsb-0.1.4/ && bin/ycsb run voldemort -p bootstrap_urls=tcp://'+voldemort_ip+':6666 -target 1000 -p recordcount='+recordcount+' -P workloads/'+ workload + ' > res/voldemort.res'
    local(cmd)
  #MongoDB
  # if len(mongo)>0 : 
  #   cmd= 'cd /home/ubuntu/ycsb-0.1.4/ && bin/ycsb run mongodb -s -p workloads/'+ workload + ' -p mongodb.url=mongodb://10.152.163.208:27017 -p mongodb.database=ycsb -p mongodb.writeConcern=normal > mongo.'+stime+'.res'
  #Cassandra
  # if len(cassandra)>0 : 
  #   cmd='cd /home/ubuntu/ycsb-0.1.4/ && bin/ycsb load cassandra-10 -P workloads/'+ workload + ' -p recordcount=10000  -p hosts=10.152.150.205 -threads 10 -s > filepath'+stime+'.res'
# bin/ycsb run cassandra-10 -P workloads/workloada -p recordcount=10000 -p operationcount=10000 -threads 10 -s > filepath
  
