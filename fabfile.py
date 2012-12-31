#from __future__ import with_statement
from fabric.api import *
from time import strftime


def host_type():
    # run('cd voldemort-0.96')
    # run(' bin/voldemort-server.sh ../ycsb-0.1.4/voldemort-binding/conf/ > /tmp/voldemort.log &')
    # run('cd')
    # with cd('/home/ubuntu/ycsb-0.1.4'):
        #run('./ycsb load voldemort -p bootstrap_urls=tcp://10.110.235.32:6666 -p recordcount=1000 -P workloads/workloadb > wrklde.test')
      run('cd ycsb-0.1.4/ && bin/ycsb load voldemort -p bootstrap_urls=tcp://10.151.3.175:6666 -p recordcount=1000 -P workloads/workloadb > test.448.res')




def ycsb(voldemort,workload,recordcount):
  stime=strftime("%H%M%S")[1:4];
  #Voldemort
  if len(voldemort)>0 :
    cmd='cd /home/ubuntu/ycsb-0.1.4/ && bin/ycsb load voldemort -p bootstrap_urls=tcp://10.151.3.175:6666 -p recordcount='+recordcount+' -P workloads/'+ workload
    cmd='cd /home/ubuntu/ycsb-0.1.4/ && bin/ycsb run voldemort -p bootstrap_urls=tcp://10.151.3.175:6666 -p recordcount='+recordcount+' -P workloads/'+ workload + ' > res/voldemort.'+stime+'.res'
    local(cmd)
  #MongoDB
  # cmd= 'cd /home/ubuntu/ycsb-0.1.4/ && bin/ycsb run mongodb -s -p workloads/'+ workload + ' -p mongodb.url=mongodb://10.152.163.208:27017 -p mongodb.database=ycsb -p mongodb.writeConcern=normal > mongo.'+stime+'.res'
  #Cassandra
  # cmd='cd /home/ubuntu/ycsb-0.1.4/ && bin/ycsb load cassandra-10 -P workloads/'+ workload + ' -p recordcount=10000  -p hosts=10.152.150.205 -threads 10 -s > filepath'+stime+'.res'
# bin/ycsb run cassandra-10 -P workloads/workloada -p recordcount=10000 -p operationcount=10000 -threads 10 -s > filepath
  
