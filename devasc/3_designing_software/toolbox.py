"""
Module containing the functions to generate device name and check if an input is an ipv4 address.

To test the module try out the following in a terminal:

>>> name = toolbox.generate_device_name('firewall', 'test')
>>> print(name)

>>> toolbox.is_ipv4_address('192.168.4.52')

>>> toolbox.is_ipv4_address('192.168.256.52')
"""


def generate_device_name(device, description):
    """ This function generates a name
    of a VNF running in RTP data center
    """
    datacenter = 'RTP'
    devices = {'firewall': 'Cisco_ASAv', 'router': 'Cisco_Cat-8k'}

    device_type = devices[device]
    name = f"{device_type}--{description}__{datacenter}"

    return name


def is_ipv4_address(ip):
    """ Return true if ipv4 address,
    False if not
    """
    octets = ip.split('.')

    if len(octets) != 4:
        return False

    # if anything in the octet variable is not a digit, return False
    elif any(not octet.isdigit() for octet in octets):
        return False

    # if any int in the octet variable is less than 0, return False
    elif any(int(octet) < 0 for octet in octets):
        return False

    # if any int in the octet is bigger than 0, return False
    elif any(int(octet) > 255 for octet in octets):
        return False

    return True


"""
Although this module does not need to run directly it can with the below configuration

import random
import string

# using __name__ == '__main__' aka the dunder allows this module to also be run directly
if __name__ == '__main__':
    # characters variables is assigned as a string of lowercase ascii characters
    characters = string.ascii_lowercase

    # with an empty string, join it with a random selection of ascii lowercase characters (above) in a 1 to 10 loop
    description = ''.join(random.choice(characters) for i in range(10))

    # the device object then could either be a router or a firewall as per the 'router' or 'firewall' with randrange
    device = ['router', 'firewall'][random.randrange(0, 2)]

    # print an instance of the generate_device_name method using device & description variables from above
    print(generate_device_name(device, description))"""