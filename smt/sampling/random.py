"""
Author: Dr. John T. Hwang <hwangjt@umich.edu>

Random sampling.
"""
from __future__ import division
import numpy as np
from six.moves import range

from smt.sampling.sampling import Sampling


class Random(Sampling):

    def __call__(self, n):
        """
        Compute the requested number of sampling points.

        Arguments
        ---------
        n : int
            Number of points requested.

        Returns
        -------
        ndarray[n, nx]
            The sampling locations in the input space.
        """
        xlimits = self.options['xlimits']
        nx = xlimits.shape[0]

        x = np.random.rand(n, nx)
        for kx in range(nx):
            x[:, kx] = xlimits[kx, 0] + x[:, kx] * (xlimits[kx, 1] - xlimits[kx, 0])

        return x