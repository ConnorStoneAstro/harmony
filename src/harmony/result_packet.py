from typing import Optional
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ResultPacket:
    """
    P: number of point sources
    N: number of image cutouts
    S: number of nearby stars
    B: number of posterior samples
    """

    id: str
    point_source_flux: np.ndarray  # (P, N)
    point_source_flux_uncertainty: np.ndarray  # (P, N)
    point_source_position: np.ndarray  # (P, 2)

    point_source_flux_posterior_samples: Optional[np.ndarray]  # (P, N, B)
    nearby_star_flux: Optional[np.ndarray]  # (S, N)
    nearby_star_flux_uncertainty: Optional[np.ndarray]  # (S, N)
    zeropoint: Optional[np.ndarray]  # (N,)
    zeropoint_uncertainty: Optional[np.ndarray]  # (N,)
