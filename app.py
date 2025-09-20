#World Clock Dashboard

import streamlit as st
from datetime import datetime
import pytz
from rich.console import Console
from rich.table import Table

console = Console(record=True)

st.set_page_config(page_title="World Clock", page_icon="🌎", layout="wide")
st.title("🌎 World Clock")
st.caption("App loaded ✅")


cities = [
    "America/New_York",
    "America/Chicago",
    "America/Detroit",
    "America/Phoenix",
    "America/Los_Angeles",
    "America/Anchorage",
    "America/Denver",
    "America/Boise",
    "America/Phoenix",
    "America/Los_Angeles",
    "Europe/London",
    "Europe/Paris",
    "Asia/Tokyo",
    "Europe/Moscow",
    "Asia/Shanghai",
    "Asia/Seoul",
    "Asia/Singapore",
    "Australia/Sydney",
    "Europe/Berlin",
    "Europe/Rome",
    "Europe/Warsaw",
    "Europe/Lisbon",
    "Europe/Madrid",
    "Europe/Stockholm",
    "Europe/Oslo",
    "Europe/Helsinki",
    "Europe/Copenhagen",
    "Asia/Jakarta",
    "Asia/Kolkata",
    "Asia/Kathmandu",
    "Asia/Dhaka",
]

table = Table(title=" 🌎World Clock", style="cyan", show_header=True, header_style="bold magenta", expand=True)
table.add_column("City_Name", style="cyan", no_wrap=True)
table.add_column("Current Time", justify="right", style="magenta")

try:
    for c in cities:
        tz = pytz.timezone(c)
        city_name = c.split("/")[-1].replace("_", " ")
        dt = datetime.now(tz)
        current_time = dt.strftime("%H:%M:%S")
        table.add_row(city_name, current_time)
except Exception as e:
    st.error(f"Error building table: {e}")

console.print(table)                               # render to console buffer
html = console.export_html(inline_styles=True)     # export styled HTML
st.components.v1.html(html, height=600, width=1000, scrolling=True)  # table size in Streamlit
