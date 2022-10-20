#!/sur/bin/python3
import os
import time
import paramiko

print('Hey, welcome!')# Welcome message. Not important. I was bored.
os.system('hostname -I >> ip_.txt') # os command to get ip address
ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.218.219.90', username='deras', password='powerlab1111') # fill in credentials for the remote host.
sftp = ssh.open_sftp()
local_file = 'ip_.txt' # name of the file you want to send over to the remote host.
remote_host = '/home/deras/Desktop/trial.txt' #Directory is not enough. Need to specify a file name!
sftp.put(local_file, remote_host)
sftp.close()
ssh.close()
