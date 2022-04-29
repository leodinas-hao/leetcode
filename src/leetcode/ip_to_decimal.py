'''
convert ipv4 address to decimal
consider IPv4 as 'a.b.c.d' then the decimal number can be calculated as below:

'a.b.c.d' = a * 256^3 + b * 256^2 + c * 256^1 + d * 256^0

Example:
210.193.151.238 is equal to 3535902702
'''

import ipaddress


class Solution:

  @staticmethod
  def toInt(ip: str) -> int:

    octets = [int(i) for i in ip.split('.')]
    return octets[0] * 256 * 256 * 256 + octets[1] * 256 * 256 + octets[2] * 256 + octets[3]

  @staticmethod
  def toInt2(ip: str) -> int:
    '''https://docs.python.org/3/library/ipaddress.html#conversion-to-strings-and-integers'''

    return int(ipaddress.IPv4Address(ip))
