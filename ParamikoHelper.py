import paramiko
'''
Basic wrapper for Paramiko
'''
# For paramiko debugging
# paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)

class ConnectToDevice():

    def __init__(self):
        self.hosts = []
        self.connections = []

    def add_host(self, args):
        """
        add hosts to the connection list
        """
        if args:
            self.hosts.append(args.split(','))
        else:
            print 'usage: host'

    def connect(self):
        """Connect to hosts in host list"""
        for host in self.hosts:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(host[0],username=host[1],password=host[2], look_for_keys=False, allow_agent=False)
            self.connections.append(self.client)
    # Rewrite this to use the transport class instead of SSHClient.
    def command(self,command):
        """Execute this command on all hosts in the list and return output as string"""
        if command:
            for host, conn in zip(self.hosts, self.connections):
                stdin, stdout, stderr = conn.exec_command(command)
                stdin.close()
                output = ''
                for line in stdout.read().splitlines():
                    output += "%s\n" % (line)
                return output

        else:
            return 'No command entered.'

    def close(self):
        for conn in self.connections:
            conn.close()
