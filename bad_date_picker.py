import streamlit as st
import random
from datetime import datetime, timedelta

st.title("🎲 Losowanie terminu, który nikomu nie pasuje")

# Losowe lata do wyboru
rok = random.choice([2025, 2026])

# Dni specjalnie "niepasujące"
dni_specjalne = [
    datetime(rok, 1, 1),       # Nowy Rok
    datetime(rok, 12, 24),     # Wigilia
    datetime(rok, 5, 1),       # Majówka
    datetime(rok, 11, 1),      # Wszystkich Świętych
]

def losuj_poniedzialek():
    start = datetime(rok, 1, 1)
    end = datetime(rok, 12, 31)
    while True:
        delta = end - start
        losowy_dzien = start + timedelta(days=random.randint(0, delta.days))
        if losowy_dzien.weekday() == 0:
            return losowy_dzien

if st.button("Losuj termin, który nikomu nie pasuje"):
    if random.random() < 0.5:
        wybrana_data = losuj_poniedzialek()
    else:
        wybrana_data = random.choice(dni_specjalne)

    godzina = random.randint(7, 7)
    minuta = random.randint(0, 59)

    finalna_data = wybrana_data.replace(hour=godzina, minute=minuta)

    st.success(f"Wylosowano termin: **{finalna_data.strftime('%A, %d %B %Y, %H:%M')}**")
    st.write("💀 Idealnie, żeby nikomu nie pasowało.")
else:
    st.info("Kliknij przycisk powyżej, aby wylosować termin.")
