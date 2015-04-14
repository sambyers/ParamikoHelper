# ParamikoHelper
Simple Paramiko wrapper for basic connect and command type situations.

Requires <a href="https://github.com/paramiko/paramiko">Paramiko</a>.

example:

  import ParamikoHelper
  
  ip = '10.0.0.1' <br />
  username = 'uname' <br />
  password = 'pword' <br />
  <br />
  conn_string = "%s,%s,%s" % (ip,username,password) <br />
  ssh = ParamikoHelper.ConnectToDevice() <br />
  ssh.add_host(conn_string) <br />
  ssh.connect() <br />
  output = ssh.command("show version") <br />
  print output <br />
  ssh.close()
