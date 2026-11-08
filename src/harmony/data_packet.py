from typing import Optional
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class DataPacket:
    """
    N: number of image cutouts
    H: height of image cutouts (pix)
    W: width of image cutouts (pix)
    P: number of point sources
    S: number of nearby stars
    Hp: height of PSF cutouts (pix, always odd)
    Wp: width of PSF cutouts (pix, always odd)
    Hs: height of nearby star cutouts (pix)
    Ws: width of nearby star cutouts (pix)
    """

    id: str

    data: np.ndarray  # (N, H, W)
    variance: np.ndarray  # (N, H, W)
    mask: np.ndarray  # (N, H, W)

    zeropoint: np.ndarray  # (N,)
    mjd: np.ndarray  # (N,)
    reference_image_flag: np.ndarray  # (N,) bool, True = no transient

    crval: np.ndarray  # (2,) ra dec
    crpix: np.ndarray  # (N, 2) 0 indexing, pixel loc of crval
    CD: np.ndarray  # (N, 2, 2)

    point_source_flux: Optional[np.ndarray] = None  # (P, N)
    point_source_position: Optional[np.ndarray] = None  # (P, 2) ra dec

    psf: Optional[np.ndarray] = None  # (N, Hp, Wp)
    sky: Optional[np.ndarray] = None  # (N,)
    sky_uncertainty: Optional[np.ndarray] = None  # (N,)

    nearby_star_cutouts: Optional[np.ndarray] = None  # (S, Hs, Ws)
    nearby_star_positions: Optional[np.ndarray] = None  # (S, 2) ra dec
