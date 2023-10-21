# Big-Data
Big data exercises and solutions

How to run:
1. Set up hadoop multi clusters on your devices
2. Make folder for the data:

   2.1 hadoop fs -mkdir /{YOUR DIR NAME}

   2.2 hadoop fs -mkdir /{YOUR DIR NAME}/input
   
4. Move the data from local to HDFS: hadoop fs -put {PATH TO DATA IN LOCAL} {PATH TO DIRECTORY IN HDFS CREATED ABOVE}
5. Use Hadoop Streaming to run the Map reduce code:

   Example:

   hadoop jar hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -file {PATH TO mapper.py IN LOCAL} -mapper "python3 mapper.py" -file {PATH TO reducer.py IN LOCAL} -reducer "python3 reducer.py" -input {PATH TO INPUT DIR (STEP 2)} -output {PATH TO OUTPUT DIR (YOUR CHOICE)} -cmdenv n=10

   -cmdev is used to set environment variable, which is used in some code. It's the total number of lines in your data.

   If there is many map-reduce phases, just replace the input dir of next step by output dir of last step

7. Download the output from HDFS to local: hadoop fs -get {PATH TO OUTPUT DIR} {PATH TO DESIRED DIR IN LOCAL}
