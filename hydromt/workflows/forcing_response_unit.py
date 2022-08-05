import pandas as pd
import numpy as np
import re
import logging
from typing import Tuple, Union, Optional

logger = logging.getLogger(__name__)

def setup_forcing_from_constant(
    self,
    ts_in: pd.DataFrame,
    key: str,
    interp_method: Optional[str] = 'none'
) -> pd.DataFrame:
    """Workflow for temporal interpolation of one or multiple time series. Used for precipitation and evaporation time series.

    Parameters
    ----------
    ts_in: pandas.DataFrame
        Imported DataFrame time series containing precipitation and/or evaporation.
    key: str
        Name of key containing forcing data to be interpolated.
    interp_method: str, optional
        Method for temporal interpolation of time series. Options: none (default), zeros (inserting zeros), ffill, bfill, linear (linear interpolation between previous and next value)

    Returns
    ----------
    p_out: pandas.DataFrame
        interpolated precipitation and evaporation time series
    """
    logger.info(f"Interpolating {key} using {interp_method}.")
    
    ### step 1: remove all non-int and non-float vlaues and replace with NaN
    ts_in[key] = pd.to_numeric(ts_in[key], errors='coerce')
    
    ### step 2: Interpolate with provided method
    if interp_method == 'none':
        ts_out = ts_in
    elif interp_method == 'linear':
        ts_in[key] = ts_in[key].interpolate(method='linear')
        ts_out = ts_in
    elif interp_method == 'zeros':
        ts_out = ts_in.fillna(0)
    else:
        ts_out = ts_in.fillna(method=interp_method)
    
    return ts_out

