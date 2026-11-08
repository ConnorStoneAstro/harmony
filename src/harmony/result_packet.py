from typing import Optional
from dataclasses import dataclass
from pathlib import Path

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
    point_source_position: np.ndarray  # (P, 2) ra dec

    point_source_flux_posterior_samples: Optional[np.ndarray] = None  # (P, N, B)
    nearby_star_flux: Optional[np.ndarray] = None  # (S, N)
    nearby_star_flux_uncertainty: Optional[np.ndarray] = None  # (S, N)
    zeropoint: Optional[np.ndarray] = None  # (N,)
    zeropoint_uncertainty: Optional[np.ndarray] = None  # (N,)

    fitter_flags: Optional[dict[str, bool | int]] = None

    def save(self, filepath: Path):
        # FIXME
        pass

    @classmethod
    def load(cls, filepath: Path) -> "ResultPacket":
        # FIXME
        pass
