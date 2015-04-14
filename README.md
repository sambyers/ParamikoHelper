# ParamikoHelper
Simple Paramiko wrapper for basic connect and command type situations.

Requires <a href="https://github.com/paramiko/paramiko">Paramiko</a>.

example:

  import ParamikoHelper
  
  ip = '10.0.0.1' 
  
  username = 'uname' 
  
  password = 'pword' 
  
  
  
  conn_string = "%s,%s,%s" % (ip,username,password) 
  
  ssh = ParamikoHelper.ConnectToDevice() 
  
  ssh.add_host(conn_string) 
  
  ssh.connect() 
  
  output = ssh.command("show version") 
  
  print output 
  
  ssh.close()
