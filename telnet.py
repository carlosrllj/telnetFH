import sys,pexpect
import getpass
import time
import arrow

HOST = sys.argv[1]

#configure here all variables following you system 
#=======================================================================
user = 'GEPON'
password = 'GEPON'
#FTPSERVER = '200.200.200.200'
#ftpuser = 'user'
#ftppassword = '123456'
#ftpdirectory = '/backups'
#=======================================================================


child = pexpect.spawn ('telnet '+HOST) #option needs to be a list
child.timeout = 150
child.logfile = sys.stdout #display progress on screen

#logging in OLT IP
time.sleep(0.25)
child.expect ('Login:')  #waiting for login
child.sendline (user) #sending login name
child.expect('Password:') #waiting for password
child.sendline (password) #sending password
child.expect('>')

time.sleep(0.5)

#go up enable configuration
child.sendline ('EN'+'\r') #going to ENABLE configuration
child.expect('Password:') #waiting enable password
child.sendline (password) #sending enable password 
time.sleep(0.5)
child.expect('#')


#defining the actual date to be add to the filename
#mydate = arrow.now().format('YYYY-MM-DD')


#sending commando to copy configuration file to remote FTP server
child.sendline('cd gpononu')
#teste = child.sendline('show unauth_discovery')
teste = pexpect.spawn('show unauth_discovery')

#child.sendline ('upload ftp config '+FTPSERVER+' '+ftpuser+' '+ftppassword+' '+ftpdirectory+'/bk-olt-'+HOST+'-'+mydate+'.cfg')
time.sleep(1)

#exiting connection
child.expect('#')
child.sendline ('exit \r')
child.sendline ('exit \r')
print teste.read()