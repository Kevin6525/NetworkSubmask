import ipaddress
from typing import List

def validateIPAddresses(ipAddresses: List[str]):
    """
    Helper function to determine if all the IP Addresses given are valid IP Addresses
    This could be validated more efficiently by using Regex expressions, but this is a more straightforward approach
    Due to the scope of the problem, we will assume any valid IP address will be of IPv4 form

    We can also use this to catch our case of an empty List being passed as an argument
    """
    if(len(ipAddresses) < 1):
        return False
    for ipAddr in ipAddresses:
        try:
            ip = ipaddress.ip_address(ipAddr)
        except ValueError:
            return False
    return True

def completeIPAddress(ipAddressPrefix: List[str]):
    """
    In our case since we compare the IP Address values after splitting by '.', we only need to fill out the rest of the IP Addresses w/ '.0' until it is a valid IP Address
    NOTE: We already validated our IP Addresses so we don't need to worry about invalid IP Address matching
    """
    if(len(ipAddressPrefix) < 1):
        return "0.0.0.0"
    multiplier = 4 - len(ipAddressPrefix)
    subnet = "."
    subnet = subnet.join(ipAddressPrefix) +  ".0" * multiplier
    return subnet


def findMinimalSpanningSubnet(ipAddresses: List[str]):
    # Begin by validating our IP Addresses
    if validateIPAddresses(ipAddresses):
        # Now we handle our edge case of having only one IP Address
        if len(ipAddresses) == 1:
            return ipAddresses[0]
        else:
            """
            Otherwise we can begin by sorting the IP Addresses and comparing the first and the last IP Addresses segments to locate the mismatch
            We will store our matches in the prefix list and join it/complete it for our result

            The brute force approach would be to loop through each IP Address and locate the mismatch, but sorting allows for optimization
            Python sorting time complexity is O(n * logn)
            """
            ipAddresses.sort()
            firstIP = ipAddresses[0].split('.')
            lastIP = ipAddresses[len(ipAddresses) - 1].split('.')
            prefix = []
            for index in range(0, 4):
                if(firstIP[index] != lastIP[index]):
                    return completeIPAddress(prefix)
                else:
                    prefix += [firstIP[index]]
            #In the event we have complete matches we need to create the IP Address with our helper function
            return completeIPAddress(prefix)
    else:
        #In the case that their is an invalid IP Address, then log the error message and return the message
        return "Invalid input"