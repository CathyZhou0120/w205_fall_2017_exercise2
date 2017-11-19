This is for W205 2017 Fall Exercise 2

How to run this application 

1. Launch an EC2 instance from AWS console 
   EC2 name: UCB MIDS W205 EX2-FULL
   AMI id: ami-d4dd4ec3

2. Mount /data volume from previous project to EC2 instance.
   hint: use the snapshot to mount

3. Once logged into the instance, install psycopg2 and  tweepy as root user

4. Switch to an alternative user w205 and clone git repo from student's github

5. run psycopg-sample.py to create the database table

6. Navigate to extweetwordcount folder

7. execute sparse run - and you should see live streaming Twitter data with
wordcounts coming through

8. While the command is running, either duplicate a new session, or enter
Control + C to stop execution to check results

9. Execute finalresults.py to check specific word count

10. Execute histogram.py to check words  from specific count range

11. safely shut down EC2 instance 


