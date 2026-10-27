import streamlit as st
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

credentials = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"])

SPREADSHEET_ID = "1WwBp8XhrDM7WA-emRpvhDfbbRYVX_nWQtPmrwTmxEhA"

@st.cache_data(ttl=60)
def load_data() :
    credentials.refresh(Request())
    service = build("sheets", "v4", credentials=credentials)
    sheet = service.spreadsheets()

    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=f"tabelWell!A1:ZZ"
    ).execute()

    values = result.get('values', [])

    if not values:
        return pd.DataFrame()

    df = pd.DataFrame(values[1:], columns=values[0])
    return df