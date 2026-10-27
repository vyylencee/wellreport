import pandas as pd
from load import load_data

bulan_map = {
    "Januari" : 1,
    "Februari" : 2,
    "Maret" : 3,
    "April" : 4,
    "Mei" : 5,
    "Juni" : 6,
    "Juli" : 7,
    "Agustus" : 8,
    "September" : 9,
    "Oktober" : 10,
    "November" : 11,
    "Desember" : 12
}

def transform_data () :
    tabelWell = load_data()

    tabelWell["Date"] = pd.to_datetime(tabelWell["Date"],format="%Y-%m-%d")

    tabelWell["Prev Day Oil"] = pd.to_numeric(tabelWell["Prev Day Oil"].str.replace(",", "."), errors="coerce")
    tabelWell["Prev Day Gross"] = pd.to_numeric(tabelWell["Prev Day Gross"].str.replace(",", "."), errors="coerce")

    tabelWell["Prod Act Oil"] = pd.to_numeric(tabelWell["Prod Act Oil"].str.replace(",", "."), errors="coerce")
    tabelWell["Prod Act Gross"] = pd.to_numeric(tabelWell["Prod Act Gross"].str.replace(",", "."), errors="coerce")
    tabelWell["Gas Own (Mscfd)"] = pd.to_numeric(tabelWell["Gas Own (Mscfd)"].str.replace(",", "."), errors="coerce")
    tabelWell["Gas Inj (Mscfd)"] = pd.to_numeric(tabelWell["Gas Inj (Mscfd)"].str.replace(",", "."), errors="coerce")
    tabelWell["Prod Act WC"] = pd.to_numeric(tabelWell["Prod Act WC"].str.replace(",", "."), errors="coerce")

    return tabelWell

def filtered_month (month) :
    tabelWell = load_data()
    
    tabelWell["Date"] = pd.to_datetime(tabelWell["Date"],format="%Y-%m-%d")

    tabelWell["Prev Day Oil"] = pd.to_numeric(tabelWell["Prev Day Oil"].str.replace(",", "."), errors="coerce")
    tabelWell["Prev Day Gross"] = pd.to_numeric(tabelWell["Prev Day Gross"].str.replace(",", "."), errors="coerce")

    tabelWell["Prod Act Oil"] = pd.to_numeric(tabelWell["Prod Act Oil"].str.replace(",", "."), errors="coerce")
    tabelWell["Prod Act Gross"] = pd.to_numeric(tabelWell["Prod Act Gross"].str.replace(",", "."), errors="coerce")
    tabelWell["Gas Own (Mscfd)"] = pd.to_numeric(tabelWell["Gas Own (Mscfd)"].str.replace(",", "."), errors="coerce")
    tabelWell["Gas Inj (Mscfd)"] = pd.to_numeric(tabelWell["Gas Inj (Mscfd)"].str.replace(",", "."), errors="coerce")
    tabelWell["Prod Act WC"] = pd.to_numeric(tabelWell["Prod Act WC"].str.replace(",", "."), errors="coerce")

    tabelWell = tabelWell[tabelWell["Date"].dt.month == bulan_map[month]]
    return tabelWell