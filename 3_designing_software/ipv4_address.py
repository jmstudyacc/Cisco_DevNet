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
