#from __future__ import with_statement
from fabric.api import *


def host_type():
    # run('cd voldemort-0.96')
    # run(' bin/voldemort-server.sh ../ycsb-0.1.4/voldemort-binding/conf/ > /tmp/voldemort.log &')
    # run('cd')
    # with cd('/home/ubuntu/ycsb-0.1.4'):
        #run('./ycsb load voldemort -p bootstrap_urls=tcp://10.110.235.32:6666 -p recordcount=1000 -P workloads/workloadb > wrklde.test')
      run('cd ycsb-0.1.4/ && bin/ycsb load voldemort -p bootstrap_urls=tcp://10.151.3.175:6666 -p recordcount=1000 -P workloads/workloadb > test.448.res')




def ycsb(workload):
  # cmd='cd /home/ubuntu/ycsb-0.1.4/ && bin/ycsb load voldemort -p bootstrap_urls=tcp://10.151.3.175:6666 -p recordcount=1000 -P workloads/'+ workload + '> test.448.res'
  cmd= 'cd /home/ubuntu/ycsb-0.1.4/ && bin/ycsb run mongodb -s -P workloads/'+ workload + ' -p mongodb.url=mongodb://10.152.163.208:27017 -p mongodb.database=ycsb -p mongodb.writeConcern=normal >mongo.1054.res'
  local(cmd)
