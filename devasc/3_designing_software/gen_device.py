# as this is declared outside of the function the value is assigned APJ
datacenter = 'APJ'


def generate_device_name(device, description):
    """ This function generates a name
    of a VNF running in RTP data center
    """
    datacenter = 'RTP'
    devices = {'firewall': 'Cisco_ASAv', 'router': 'Cisco_Cat-8k'}

    device_type = devices[device]
    name = f"{device_type}--{description}__{datacenter}"

    return name

# once outside of the function the value for datacenter will again be APJ
