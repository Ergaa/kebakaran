import streamlit as st

from web_functions import predict

def app(df, x, y):

    st.title("Prediksi Kebakaran")

    col1, col2, col3 = st.columns(3)

    with col1:
        Temperature = st.text_input ('input nilai suhu dalam (°C)')
    with col1:
        Humidity = st.text_input ('input nilai tingkat kelembaban udara dalam (%)')
    with col1:
        TVOC = st.text_input ('input nilai konsentrasi senyawa organik dalam (ppb)')
    with col1:
        eCO2 = st.text_input ('input nilai konsentrasi karbon dioksida dalam (ppm)')
    with col2:
        Raw_H2 = st.text_input ('input nilai konsentrasi hidrogen (H2)')
    with col2:
        Raw_Ethanol = st.text_input ('input nilai konsentrasi gas etanol')
    with col2:
        Pressure = st.text_input ('input nilai tekanan atmosfer dalam (hPa)')
    with col2:
        PM1 = st.text_input ('input nilai konsentrasi partikel dengan ukuran 1.0 mikrometer')
    with col3:
        PM2 = st.text_input ('input nilai konsentrasi partikel dengan ukuran 2.5 mikrometer')
    with col3:
        NC0 = st.text_input ('input nilai jumlah partikel per unit volume ukuran 0.5 mikrometer')
    with col3:
        NC1 = st.text_input ('input nilai jumlah partikel per unit volume ukuran 1.0 mikrometer')
    with col3:
        NC2 = st.text_input ('input nilai jumlah partikel per unit volume ukuran 2.5 mikrometer')
    with col3:
        CNT = st.text_input ('input nilai total jumlah partikel terhitung')
    
    features = [Temperature,Humidity,TVOC,eCO2,Raw_H2,Raw_Ethanol,Pressure,PM1,PM2,NC0,NC1,NC2,CNT]

    #tombol
    if st.button("prediksikan kebakaran"):
        prediction, score =  predict(x,y,features)
        score = score
        st.info("prediksi sukses✨")

        if (prediction[0]==0):
            st.warning("Tidak Terjadi Kebakaran🧯")
        else:
            st.success("Telah Terjadi Kebakaran🔥")
        
        st.write("model akurasi", (score*100), "%")