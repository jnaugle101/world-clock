#World Clock Dashboard

import streamlit as st
from datetime import datetime
import pytz
#from rich.console import Console
from rich.table import Table

st.set_page_config(page_title="World Clock", page_icon="🌎", layout="centered")
st.title("🌎 World Clock")
st.caption("App loaded ✅")


cities = [
    "America/New_York",
    "Europe/London",
    "Europe/Paris",
    "Asia/Tokyo",
    "Europe/Moscow",
    "Asia/Shanghai",
    "Asia/Seoul",
    "Asia/Singapore",
    "Australia/Sydney",
]

table = Table(title=" 🌎World Clock", style="cyan", show_header=True, header_style="bold magenta")
table.add_column("City_Name", style="cyan", no_wrap=True)
table.add_column("Current Time", justify="right", style="magenta")

try:
    for c in cities:
     tz = pytz.timezone(c)
     city_name = c.split("/")[-1].replace("_", " ")
     dt = datetime.now(tz)
     current_time = dt.strftime("%H:%M:%S")
     table.add_row(city_name, current_time)


    st.write(table)

except Exception as e:
    st.error(f"Error building table: {e}")
