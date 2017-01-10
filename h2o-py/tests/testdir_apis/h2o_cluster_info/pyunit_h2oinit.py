from __future__ import print_function
from builtins import str
from builtins import range
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o


def h2oinit():
    """
    h2o.init(url=None, ip=None, port=None, https=None, insecure=None, username=None, password=None, cluster_id=None,
    cookies=None, proxy=None, start_h2o=True, nthreads=-1, ice_root=None, enable_assertions=True, max_mem_size=None,
    min_mem_size=None, strict_version_check=None, **kwargs)

    Testing the h2o.init() command here.

    :return: none if test passes or error message otherwise
    """
    # call with no arguments
    try:
        h2o.init(strict_version_check=False)
    except Exception as e:  # some errors are okay like version mismatch
        print("In exception mode")
        assert "Version mismatch." in e.args[0], "Wrong exception messages found.  h2o.init() command not working"

    # try to start a cluster and test out various commands
    ipS = "127.0.0.1"
    portS = "54321"
    nthread = 2
    max_mem_size=10
    min_mem_size=3
    strict_version_check = False
    start_h2o = False

    try:
        h2o.init(ip=ipS, port=portS, nthreads=nthread, max_mem_size=max_mem_size, min_mem_size=min_mem_size,
                 start_h2o=start_h2o, strict_version_check=strict_version_check)
    except Exception as e:  # some errors are okay like version mismatch
        assert "H2OConnectionError: Unexpected HTTP error:" in e.args[0], "Wrong exception messages found.  " \
                                                                          "h2o.init() command not working"


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oinit)
else:
    h2oinit()
