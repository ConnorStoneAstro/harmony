from typing import Optional

import numpy as np

from harmony import Packet


class ResultPacket(Packet):
    """
    P: number of point sources
    N: number of image cutouts
    S: number of nearby stars
    B: number of posterior samples
    """

    id: str
    packet_key: str = "result_packet"
    point_source_flux: np.ndarray  # (P, N)
    point_source_flux_uncertainty: np.ndarray  # (P, N)
    point_source_position: np.ndarray  # (P, 2) ra dec

    point_source_flux_posterior_samples: Optional[np.ndarray] = None  # (P, N, B)
    nearby_star_flux: Optional[np.ndarray] = None  # (S, N)
    nearby_star_flux_uncertainty: Optional[np.ndarray] = None  # (S, N)
    zeropoint: Optional[np.ndarray] = None  # (N,)
    zeropoint_uncertainty: Optional[np.ndarray] = None  # (N,)

    fitter_flags: Optional[dict[str, bool | int]] = None
    chi_squared: Optional[float] = None  # ()
    per_cutout_chi_squared: Optional[np.ndarray] = None  # (N,)
