import pytest
from macinfo import get_vendor

@pytest.mark.parametrize("mac_address, expected_result", [
    ('54:26:96:d2:11:0f', 'Apple, Inc'),
    ('', 'Invalid input - please double-check the mac-address.'),
    ('hjklsdfk', 'Invalid input - please double-check the mac-address.')
])
def test_get_vendor_positive(mac_address, expected_result):
    assert get_vendor(mac_address) == expected_result
