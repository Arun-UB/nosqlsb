import sh
msg=sh.fab("-H","ubuntu@ec2-174-129-80-204.compute-1.amazonaws.com","-i","/home/arun/nosqlsb.pem","host_type");
print msg