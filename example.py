import ParamikoHelper

ip1 = '10.0.0.1'
ip2 = '10.0.0.2'
username = 'uname'
password = 'pword' 

host1 = "%s,%s,%s" % (ip1,username,password)
host2 = "%s,%s,%s" % (ip2,username,password)

ssh = ParamikoHelper.ConnectToDevice() 
ssh.add_host(host1)
ssh.add_host(host2)
ssh.connect()
output = ssh.command("show version") 
print output 
ssh.close()