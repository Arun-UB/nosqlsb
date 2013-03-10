from fabric.api import *
from time import strftime


def ycsb(workload,recordcount,target):
  voldemort_ip='10.204.115.205'
  mongo_ip='10.195.206.102'
  #stime=strftime("%H%M%S")[1:4]
  #Voldemort
#   if len(voldemort)>0 :
  cmd='cd /home/ubuntu/YCSB/ && bin/ycsb load voldemort -p bootstrap_urls=tcp://'+voldemort_ip+':6666  -target '+target+' -p recordcount='+recordcount+' -P workloads/'+ workload
  local(cmd)
  cmd='cd /home/ubuntu/YCSB/ && bin/ycsb run voldemort -p bootstrap_urls=tcp://'+voldemort_ip+':6666 -target '+target+' -p operationcount='+recordcount+' -P workloads/'+ workload + ' > voldemort.res'
  local(cmd)

  #MongoDB
  # if len(mongo)>0 : 
  cmd= 'cd /home/ubuntu/YCSB/ && bin/ycsb load mongodb -s -P workloads/'+ workload + ' -p mongodb.url=mongodb://'+mongo_ip+':27017 -threads 10 -p recordcount='+recordcount+' -p mongodb.database=ycsb -target '+target+' -p mongodb.writeConcern=normal'
  local(cmd) 
  cmd= 'cd /home/ubuntu/YCSB/ && bin/ycsb run mongodb -s -P workloads/'+ workload + ' -p mongodb.url=mongodb://'+mongo_ip+':27017 -threads 10 -p operationcount='+recordcount+' -p mongodb.database=ycsb -target '+target+' -p mongodb.writeConcern=normal > mongo.res'
  local(cmd)
 
  #Cassandra
  # if len(cassandra)>0 : 
  cmd='cd /home/ubuntu/YCSB/ && bin/ycsb load cassandra-10 -s -P workloads/'+ workload + ' -p recordcount='+recordcount+' -p hosts=10.80.77.61 -target '+target+' -threads 10 -p recordcount='+recordcount
  local(cmd)
#  cmd='cd /home/ubuntu/YCSB/ && bin/ycsb run cassandra-10 -s -P workloads/'+ workload + ' -p recordcount='+recordcount+'  -p hosts=10.80.77.61 -threads 10 -target '+target+' -p recordcount='+recordcount+' > res/cassandra.res'
#  local(cmd)
# bin/ycsb run cassandra-10 -P workloads/workloada -p recordcount=10000 -p operationcount=10000 -threads 10 -s > filepath
 # ./bin/ycsb load cassandra-10 -s -P workloads/workloada -p hosts=10.80.77.61 -target 8000 -threads 16 -p recordcount=100000 > testcasa.dat
  
  #DynamoDB
#  cmd='cd /home/ubuntu/YCSB/ && bin/ycsb load dynamodb -P workloads/'+ workload + ' -target '+target+' -p recordcount='+recordcount+' -P dynamodb/conf/dynamodb.properties'
#  local(cmd)
#  cmd='cd /home/ubuntu/YCSB/ && bin/ycsb run dynamodb -P workloads/'+ workload + ' -target '+target+' -p recordcount='+recordcount+' -P dynamodb/conf/dynamodb.properties > dynamodb.res'
#  local(cmd)


  cmd = 'python /home/ubuntu/project/extract_info_ycsb.py'
  local(cmd)
  cmd = 'sh /home/ubuntu/project/plot.sh'
  local(cmd)
