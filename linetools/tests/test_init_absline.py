# Module to run tests on initializing AbsLine

# TEST_UNICODE_LITERALS

import numpy as np
import os, pdb
import pytest
from astropy import units as u

from linetools.spectralline import AbsLine

'''
def data_path(filename):
    data_dir = os.path.join(os.path.dirname(__file__), 'files')
    return os.path.join(data_dir, filename)
'''

def test_mk_absline():
	# Init HI Lya
    abslin = AbsLine(1215.6700*u.AA)
    np.testing.assert_allclose(abslin.data['f'], 0.4164)

	# Init CII 1334 with LineList
    abslin2 = AbsLine(1334.5323*u.AA, linelist='Strong')
    np.testing.assert_allclose(abslin2.data['Ek'], 74932.62 / u.cm)
