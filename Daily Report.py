import streamlit as st
import datetime as dt
from transform import transform_data
from datetime import date, timedelta

st.set_page_config(
    page_title="Well Performance PEP Bunyu",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Daily Well Performance Pertamina EP Bunyu Field")
st.divider()

tabelWell = transform_data()
try :
    listWell = tabelWell["Well"].unique().tolist()

    hariIni = date.today()
    h_1 = hariIni - timedelta(days=28)
    tanggal = st.date_input("Tanggal Hari Ini", value=h_1, key="tanggal", disabled=True)

    listWell = tabelWell[tabelWell["Date"].dt.date == h_1]["Well"].unique().tolist()
    listGS = tabelWell[tabelWell["Date"].dt.date == h_1]["GS"].unique().tolist()

    col1, col2 = st.columns(2)

    with col1 :
        gs = st.multiselect("Pilih GS", listGS, default=listGS, key="gs")
    with col2 :
        sumur = st.multiselect("Pilih Well", listWell, default=listWell, key="well")


    nilai = tabelWell[(tabelWell["Date"].dt.date == h_1) & (tabelWell["Well"].isin(sumur)) & (tabelWell["GS"].isin(gs))].copy()
    nilai2 = tabelWell[(tabelWell["Date"].dt.date == h_1) & (tabelWell["GS"].isin(gs))].copy()

    df = nilai.groupby(["Well", "GS"])[["Prod Act Gross", "Prod Act Oil", "Gas Own (Mscfd)"]].sum().reset_index()

    st.line_chart(x="Well", x_label="Well",
                    y=["Prod Act Gross", "Prod Act Oil", "Gas Own (Mscfd)"],
                    y_label="Daily Production",
                    data=df,
                    width="stretch")

    col1, col2, col3 = st.columns(3)

    with col1 :
        df = nilai.groupby("Well")["Prod Act Gross"].sum().reset_index()

        st.subheader("Production Oil - Gross")
        st.line_chart(x="Well", x_label="Well",
                    y="Prod Act Gross", y_label="Gross",
                    data=df,
                    width="stretch")

    with col2 :
        df = nilai.groupby("Well")["Prod Act Oil"].sum().reset_index()

        st.subheader("Production Oil - Nett")
        st.line_chart(x="Well", x_label="Well",
                    y="Prod Act Oil", y_label="Nett",
                    data=df,
                    width="stretch")   

    with col3 :
        df = nilai.groupby("Well")["Gas Own (Mscfd)"].sum().reset_index()

        st.subheader("Production Gas Own")
        st.line_chart(x="Well", x_label="Well",
                    y="Gas Own (Mscfd)", y_label="Gas Own",
                    data=df,
                    width="stretch")


    # st.subheader("Test of Date")

    # hariIni = date.today()
    # h_1 = hariIni - timedelta(days=1)
    # tanggal = tabelWell["Date"].dt.date == h_1
    # st.write("Tanggal : ", h_1)
    # st.dataframe(tabelWell.loc[tanggal, ["Well", "Date of Test", "Status/Lifting"]], hide_index=True)

    st.divider()
    col5, col6, col7 = st.columns(3)

    with col5 :
        st.subheader("Top 10 Production Oil - Gross")

        df = nilai2.groupby(["Well", "GS"])["Prod Act Gross"].sum().reset_index().sort_values("Prod Act Gross", ascending=False).head(10)
        st.dataframe(df.style.format({"Prod Act Gross" : "{:,.0f}"}), hide_index=True)

    with col6 :
        st.subheader("Top 10 Production Oil - Nett")

        df = nilai2.groupby(["Well", "GS"])["Prod Act Oil"].sum().reset_index().sort_values("Prod Act Oil", ascending=False).head(10)
        st.dataframe(df.style.format({"Prod Act Oil" : "{:,.0f}"}), hide_index=True)

    with col7 :
        st.subheader("Top 10 Production Gas Own")

        df = nilai2.groupby(["Well", "GS"])["Gas Own (Mscfd)"].sum().reset_index().sort_values("Gas Own (Mscfd)", ascending=False).head(10)
        st.dataframe(df.style.format({"Gas Own (Mscfd)" : "{:,.4f}"}), hide_index=True)
except UserWarning :
    days = date.today()
    yesterday = days - timedelta(days=1)
    st.error(f"Data pada tanggal {yesterday} belum tersedia.")