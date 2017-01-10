from __future__ import print_function
from builtins import str
from builtins import range
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o


def h2oconnection():
    """
    h2o.connection()

    Testing the h2o.connection() command here.

    :return: none if test passes or error message otherwise
    """
    # call with no arguments
    try:
        temp = h2o.connection()
        assert temp.requests_count==7, "h2o.connection() command not working."
    except Exception as e:  # some errors are okay like version mismatch
        assert False, "h2o.connection() command not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oconnection)
else:
    h2oconnection()
