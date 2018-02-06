from pytest import raises
from populus.contracts.exceptions import NoKnownAddress
from nkms_eth.token import NuCypherKMSToken


def test_get_token_before_creation(testerchain):
    with raises(NoKnownAddress):
        NuCypherKMSToken.get(blockchain=testerchain)

