import streamlit as st
from transform import filtered_month

st.set_page_config(
    page_title="Well Performance PEP Bunyu",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Monthly Well Performance Pertamina EP Bunyu Field")
st.divider()


colA, colB = st.columns(2)
with colA :
    bulan = st.selectbox("Pilih Bulan", ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"], key="bulan")

tabelWell = filtered_month(bulan)
listWell = tabelWell["Well"].unique().tolist()

with colB :
    well = st.multiselect("Pilih Well", listWell, default=listWell, key="well")

for a in range(0, len(well), 3) :
    col1, col2, col3 = st.columns(3)

    with col1 :
        namaWell = well[a]
        df = tabelWell[tabelWell["Well"] == namaWell][["Date", "Prod Act Gross", "Prod Act Oil", "Gas Own (Mscfd)" ]].copy()
        st.subheader(f"Well : {namaWell}")
        st.line_chart(x="Date", x_label="Date",
                        y=["Prod Act Gross"] + ["Prod Act Oil"] + ["Gas Own (Mscfd)"],
                        y_label="Daily Production",
                        data=df,
                        width="stretch")

    if a + 1 < len(well) :
        with col2 :
            namaWell = well[a+1]
            df = tabelWell[tabelWell["Well"] == namaWell][["Date", "Prod Act Gross", "Prod Act Oil", "Gas Own (Mscfd)" ]].copy()
            st.subheader(f"Well : {namaWell}")
            st.line_chart(x="Date", x_label="Date",
                            y=["Prod Act Gross"] + ["Prod Act Oil"] + ["Gas Own (Mscfd)"],
                            y_label="Daily Production",
                            data=df,
                            width="stretch")

    if a + 2 < len(well) :
            with col3 :
                namaWell = well[a+2]
                df = tabelWell[tabelWell["Well"] == namaWell][["Date", "Prod Act Gross", "Prod Act Oil", "Gas Own (Mscfd)" ]].copy()
                st.subheader(f"Well : {namaWell}")
                st.line_chart(x="Date", x_label="Date",
                                y=["Prod Act Gross"] + ["Prod Act Oil"] + ["Gas Own (Mscfd)"],
                                y_label="Daily Production",
                                data=df,
                                width="stretch")
    