import streamlit as st
import plotly.express as px
from backend import get_data

st.title("previsão do tempo para os próximos dias")
place = st.text_input("place: ")
days = st.slider("Previsões", min_value=1, max_value=5,
                 help="Selecione o numero de previsões desejadas")
option = st.selectbox("selecione o tipo de previsão", ("Temperatura", "Clima"))
st.subheader(f"{option} para os proximos {days} dias na localização {place}")

if place:

    try:
        filtered_data = get_data(place, days)

        if option == "Temperatura":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Clima":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=110)
    except KeyError:
        st.write("esse lugar não existe")

