import os
from urllib.request import urlretrieve
import pandas as pd

Fremont_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename="Fremont.csv",url=Fremont_URL
                     ,force_download=False):
    """
    Download and cache the fremont data
    
    Parameters
    ----------
    filename: string(optinal)
        location to save the data
    url: string(oprinal)
        web location of the data
    force_download: bool (optinal)
        if True, force redownload of the data
        
    Returns
    -------
    data: pandas.DataFrame
        The fremont bridge data
    """                 
    
    
    if force_download or not os.path.exists(filename):
        urlretrieve(url,filename)
    data = pd.read_csv("Fremont.csv",index_col = "Date", parse_dates=True).drop("Fremont Bridge Total",axis=1)
    data.columns = ["West","East"]
    data["Total"] = data["West"] + data["East"]
    return data