!README
Analytics Instructions

1. download and save 'flint_cluster.pem'
2. cd to the directory where you saved the keys
3. run ' ssh -i ./flint_cluster.pem ubuntu@ec2-54-165-151-71.compute-1.amazonaws.com '
4. Once you are in run ‘flintrock start spark-hdfs-cluster-2’
5. run ' flintrock login spark-hdfs-cluster-2 '. You are now in the master of the cluster.
6. To run the analytics run './auto.sh'
7. See the results printed out or see the results in pearson.txt and tfidf.txt
8. Ignore the ‘Connection Refused’ Error

Alternatively:
1. download and save 'flint_cluster.pem'
2. cd to the directory where you saved the keys
3. run ' ssh -i ./flint_cluster.pem ubuntu@ec2-54-165-151-71.compute-1.amazonaws.com ‘
4. Once you are in run ‘flintrock start spark-hdfs-cluster-2’
5. run ' flintrock login spark-hdfs-cluster-2 '
6. You are now in the master of the cluster.
7. cd to ‘/analysis/’
8. run ‘python3.7 etl.py’
9. run ‘export PYSPARK_PYTHON=python3.7’
10. run ‘python3.7 analytics.py’
11. See the results printed out or see the results in pearson.txt and tfidf.txt
12. Ignore the ‘Connection Refused’ Error
