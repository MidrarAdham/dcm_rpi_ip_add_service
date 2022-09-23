import os
import time
import paramiko

print('Hey, welcome!')
os.system('hostname -I >> ip_.txt')
ssh = paramiko.SSHClient() 
ssh.connect('10.218.219.90', username='deras', password='powerlab1111')
sftp = ssh.open_sftp()
# Localpath is a string containing the path of the local file, remotepath is where the file should be copied on the raspberry pi
local_file = ''
remote_host = ''
sftp.put(local_file, remote_host)
sftp.close()
ssh.close()
