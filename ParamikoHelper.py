__author__ = 'https://github.com/swabyears'
import paramiko
from time import sleep

class ConnectToDevice():
    def __init__(self):
        self.hosts = []
        self.connections = []

    def add_host(self, args):
        """
        :param args: IPs or domain names
        :return: nothing
        """
        if args:
            self.hosts.append(args.split(','))
        else:
            print 'usage: add_host("x.x.x.x,x.x.x.x")'

    def connect(self):
        """
        :return: nothing
        """
        for host in self.hosts:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(host[0],username=host[1],password=host[2], look_for_keys=False, allow_agent=False)
            self.connections.append(self.client)

    def command(self,command):
        '''
        :param command: IOS command to execute on the connected hosts
        :return: the text output from the devices
        '''
        if command:
            for host, conn in zip(self.hosts, self.connections):
                shell = conn.invoke_shell()
                shell.send("terminal length 0\n")
                sleep(2)
                shell.send(command)
                sleep(2)
                output = shell.recv(10000)
                return output

        else:
            return 'No command entered.'

    def close(self):
        for conn in self.connections:
            conn.close()