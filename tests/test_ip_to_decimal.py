import pytest

from leetcode.ip_to_decimal import Solution


@pytest.mark.parametrize('ip', [
  '210.193.151.238',
  '10.9.8.7',
])
def test_ip_to_decimal(ip):
  assert Solution.toInt(ip) == Solution.toInt2(ip)
