from typing import Optional
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class DataPacket:
    """
    N: number of image cutouts
    H: height of image cutouts
    W: width of image cutouts
    P: number of point sources
    S: number of nearby stars
    Hp: height of PSF cutouts
    Wp: width of PSF cutouts
    Hs: height of nearby star cutouts
    Ws: width of nearby star cutouts
    """

    id: str

    data: np.ndarray  # (N, H, W)
    variance: np.ndarray  # (N, H, W)
    mask: np.ndarray  # (N, H, W)

    zeropoint: np.ndarray  # (N,)
    mjd: Optional[np.ndarray]  # (N,)

    crval: np.ndarray  # (2,)
    crpix: np.ndarray  # (N, 2)
    CD: np.ndarray  # (N, 2, 2)

    reference_image_flag: Optional[np.ndarray]  # (N,)

    point_source_flux: Optional[np.ndarray]  # (P, N)
    point_source_position: Optional[np.ndarray]  # (P, 2)

    psf: Optional[np.ndarray]  # (N, Hp, Wp)
    sky: Optional[np.ndarray]  # (N,)

    nearby_star_cutouts: Optional[np.ndarray]  # (S, Hs, Ws)
    nearby_star_positions: Optional[np.ndarray]  # (S, 2)
