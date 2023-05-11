import paramiko
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():

    # create a new SSH client
    ssh = paramiko.SSHClient()

    # automatically add the server's host key
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # connect to the Ubuntu server
    ssh.connect('server_ip_address', username='username', password='password')

    # execute the command to get the contents of the file you want
    stdin, stdout, stderr = ssh.exec_command('cat /path/to/file')

    # read the output of the command
    output = stdout.read().decode()

    # close the SSH connection
    ssh.close()

    # write the output to an HTML file
    with open('output.html', 'w') as f:
        f.write('<html><body><pre>')
        f.write(output)
        f.write('</pre></body></html>')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
