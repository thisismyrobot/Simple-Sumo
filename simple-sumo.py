 """ Ultra simple Parrot Jumping Sumo drone control.
"""
import socket
import time


class Commander(object):
    """ Class to handle commanding a robot.
    """
    def __init__(self, ip='192.168.1.1', cmd_port=5556):
        self._ip = ip
        self._cmd_port = cmd_port
        self._seq = 1
        self._cmd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, cmd, *args):
        """ Send messages to the bot.
        """
        cmd_str = 'AT*{}={}'.format(cmd, self._seq)
        if len(args) > 0:
            cmd_str += ','.join(cmd_str + args)
        cmd_str = '{}\n'.format(cmd_str)

        print cmd_str

        self._cmd_sock.sendto(cmd_str, (self._ip, self._cmd_port))
        time.sleep(30) # 30ms


if __name__ == '__main__':

    c = Commander()
