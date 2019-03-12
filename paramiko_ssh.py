#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import paramiko
import threading

def remote_command(host, ssh_port, user, password, command):

    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host,ssh_port,user,password)
        std_in, std_out, std_err = ssh_client.exec_command(command)
        print("--------------------%s command exec result-------------------- \n" % host)
        for line in std_out:
            print("\t %s " % line.strip("\n"))
    except Exception as e:

        print("error: %s " % e)

if __name__ == '__main__':

    if len(sys.argv) != 6:
        print("usage: %s hosts_file ssh_port username password command" % sys.argv[0])
    else:
        hosts_file = sys.argv[1]
        ssh_port = sys.argv[2]
        username = sys.argv[3]
        password = sys.argv[4]
        command = sys.argv[5]

        try:

            with open(hosts_file, 'r') as f:

                for host in f:

                    t = threading.Thread(target=remote_command, args=[host.strip(), ssh_port, username, password, command])
                    t.start()

        except Exception as e:

            print(e)
