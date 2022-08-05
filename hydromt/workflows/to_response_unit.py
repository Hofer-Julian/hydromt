import pandas as pd
import numpy as np
import re
import logging
from typing import Tuple, Union, Optional
import geopandas as gpd


#TODO: add self, 
#TODO: add column if it doesn't exist?


def setup_constant_pars(
    self,
    response_unit: gpd.GeoDataFrame,
    value_name: str,
    value: int or float,
    name: Optional[str] = None
) -> gpd.GeoDataFrame:
    """Adding a constant value to a response unit.
    
    Parameters
    ----------
    response_unit: pd.GeoDataFrame
        Response unit geometry
    value_name: str
        Name of the attribute that is changed.
    value: float or int
        Value of the attribute that is changed.
    name: str, optional
        Name of new map layer, this is used to overwrite the name of a DataFrame
        or to select a variable from a Dataset.
    
    Returns
    ----------
    response_unit: pd.GeoDataFrame
        Response unit geometry
    """
    ### type checks, copied from set_staticgeoms.
    gtypes = [gpd.GeoDataFrame, gpd.GeoSeries]
    if not np.any([isinstance(response_unit, t) for t in gtypes]):
        raise ValueError("First parameter map(s) should be geopandas.GeoDataFrame or geopandas.GeoSeries")
    
    ### setting single value:    
    if value_name not in response_unit:
        raise ValueError(f"Attribute '{value_name}' not found in GeoDataFrame")
    
    if not (isinstance(value, int) or isinstance(value, float)):
        raise ValueError(f"The assigned value for '{value_name}' must be an integer or float")
    else: 
        response_unit[value_name] = value
    
    return response_unit
    
