from __future__ import print_function
from builtins import str
from builtins import range
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o


def h2oconnect():
    """
    h2o.connect(server=None, url=None, ip=None, port=None, https=None, verify_ssl_certificates=None, auth=None,
    proxy=None, cluster_id=None, cookies=None, verbose=True)

    Testing the h2o.connect() command here.  I will call this command in the most popular way.  Goal here is not
    to extensively test this command here but rather to make sure it has not changed in a way that it will fail with
    old code version.

    :return: none if test passes or error message otherwise
    """
    ipA = "127.0.0.1"
    portN = "54321"
    urlS = "http://127.0.0.1:54321"

    try:
        h2o.connect(ip = ipA, port = portN, verbose = True)     # pass if no connection issue
    except Exception as e:  # port number may not match.  Make sure the right error message is returned
        assert "Could not establish link to H2O cloud" in e.args[0], "h2o.connect command is not working."

    try:
        h2o.connect(url=urlS, https=True, verbose = True)     # pass if no connection issue
    except Exception as e:  # port number may not match.  Make sure the right error message is returned
        assert "Could not establish link to H2O cloud" in e.args[0], "h2o.connect command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oconnect)
else:
    h2oconnect()
