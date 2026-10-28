import os
import streamlit as st
 
st.set_page_config(page_title="Clement's Data Portfolio", page_icon="📊", layout="wide")
 
# =====================================================================
# EDIT THIS SECTION: your name, intro, links and projects
# =====================================================================
ABOUT = {
    "name": "Clement Kabenla Amenlemah",
    "headline": "Data Analyst",
    "intro": "I build dashboards that turn raw data into decisions. "
             "Pick a project from the sidebar to explore it.",
    "linkedin": "https://www.linkedin.com/in/clement-amenlemah-088b00243",
    "github": "https://github.com/Clement-005",
}
 
PROJECTS = [
    {
        "title": "Book Launch Analytics Dashboard",
        "tagline": "Live Power BI dashboard for a book launch, fed by attendee details captured through a QR code and Google Sheets.",
        "problem": "The launch team needed a live view of who was attending and how much was being pledged and given during the event.",
        "approach": "Created a QR code that attendees scanned at the launch to fill in their details, "
                    "which were collected in a Google Sheet. "
                    "I first built a sample dashboard on synthetic data, then used it to define the data quality rules: "
                    "amounts set to currency (Ghana Cedis, GH₵), all text fields in capitalised initials (title case), "
                    "and the first row promoted to column headers. "
                    "For the live event I deleted the synthetic rows, so each attendee's submission flows from the "
                    "Google Sheet into the Power BI dashboard and can be tracked live. "
                    "The dashboard has two pages. Demographics covers attendees, members vs visitors, gender, preferred mode of payment, "
                    "pledged vs given, and members by branch. Financials covers amount raised, pledged and given, "
                    "amount given by attendee, amount raised by mode of payment, and members vs visitors.",
        "results": "The dashboard tracked 63 attendees (32 Oasis members and 31 visitors) and GH₵230.70K raised in total: "
                   "GH₵205.25K pledged and GH₵25.45K given. Visitors were 49% of attendees but accounted for about "
                   "GH₵151K of the amount raised, against about GH₵79K from members. Of the amount given, "
                   "GH₵25,200 came in as cash and GH₵250 through MTN Mobile Money.",
        "kpis": [
            ("Attendees", "63"),
            ("Oasis Members", "32"),
            ("Visitors", "31"),
            ("Amount Raised", "GH₵230.70K"),
            ("Pledged", "GH₵205.25K"),
            ("Given", "GH₵25.45K"),
        ],
        "tools": ["Google Sheets", "QR code", "Power BI"],
        "github": "https://github.com/Clement-005/portfolio",
        "screenshots": [  # save your images in the images/ folder with these names
            ("images/book_demographics.png", "Demographics page: attendees, members vs visitors, gender, payment mode, pledged vs given"),
            ("images/book_financials.png", "Financials page: amount raised, pledged and given, by payment mode and by members vs visitors"),
        ],
    },
    {
        "title": "Hospital Management System and Operations Dashboard",
        "tagline": "Role-based hospital records system with a live operations dashboard, staff login, audit logging and data quality checks.",
        "problem": "Hospital records are often spread across spreadsheets and paper files. Front desk staff, doctors, billing officers "
                   "and managers each need different information, but rarely in one place, and there is usually no record of who "
                   "looked at which patient file.",
        "approach": "Cleaned the healthcare dataset in Python (Jupyter): removed duplicates, fixed data types and name formatting, "
                    "and checked outliers. Designed a MySQL database with three linked tables (patients, admissions, billings) "
                    "using primary and foreign keys, and added CHECK constraints so the database rejects negative bills, "
                    "discharge dates before admission and impossible ages. "
                    "Built a Streamlit web app on top of it with four parts: an operations dashboard (KPIs against the previous "
                    "period, admissions by condition, admissions vs discharges, admission type, test results, patient journey, "
                    "billing by insurer and recent activity), Find Patient, Register Patient with validation and dropdowns, and an "
                    "Audit Log. Staff sign in with bcrypt-hashed passwords, and each role (front desk, doctor, billing, admin) "
                    "sees only the pages and fields it needs. The app connects through a least-privilege MySQL account that "
                    "can read and add records but cannot change, delete or erase the audit log.",
        "results": "A working system that gives management a live view of admissions, conditions, billing and insurer mix, "
                   "while keeping clinical and financial details limited to the staff who need them. Data checks found 106 "
                   "negative billing amounts, which were backed up and set to empty so they no longer distort totals. "
                   "The public demo runs on made-up patients so anyone can try every role without real data.",
        "kpis": [
            ("Database tables", "5"),
            ("Staff roles", "4"),
            ("App pages", "4"),
            ("Data quality checks", "5"),
        ],
        "tools": ["Python", "pandas", "Jupyter", "MySQL", "SQLAlchemy", "Streamlit", "Plotly", "bcrypt"],
        "github": "https://github.com/Clement-005/Hospital_Dahboard",
        "demo": "PASTE-YOUR-APP-LINK-HERE",   # your hospital app link, e.g. https://clement-hospital-dashboard.streamlit.app
        "screenshots": [  # loaded straight from the hospital repository
            ("https://raw.githubusercontent.com/Clement-005/Hospital_Dahboard/main/docs/dashboard.png",
             "Operations dashboard: KPIs, conditions, admissions vs discharges, data quality, patient journey, insurers"),
            ("https://raw.githubusercontent.com/Clement-005/Hospital_Dahboard/main/docs/login.png",
             "Staff sign-in: each role sees different pages and fields"),
        ],
    },
    # To add another project, copy the block above, paste it here and edit it.
]
# =====================================================================
 
 
def show_project(p):
    st.title(p["title"])
    st.write(p["tagline"])
    if p.get("demo"):
        st.link_button("Open live demo", p["demo"], type="primary")
 
    if p.get("kpis"):
        cols = st.columns(len(p["kpis"]))
        for col, (label, value) in zip(cols, p["kpis"]):
            col.metric(label, value)
 
    tab_shots, tab_story, tab_tech = st.tabs(["Screenshots", "Problem → Result", "Tools & Code"])
 
    with tab_shots:
        for path, caption in p["screenshots"]:
            if path.startswith("http") or os.path.exists(path):
                st.image(path, caption=caption, use_container_width=True)
            else:
                st.info(f"Add `{path}` to show: {caption}")
 
    with tab_story:
        st.subheader("The problem")
        st.write(p["problem"])
        st.subheader("The approach")
        st.write(p["approach"])
        st.subheader("The result")
        st.write(p["results"])
 
    with tab_tech:
        st.write("**Built with:** " + ", ".join(p["tools"]))
        if p.get("demo"):
            st.link_button("Open live demo", p["demo"])
        st.link_button("View code on GitHub", p["github"])
 
 
def show_home():
    st.title(ABOUT["name"])
    st.subheader(ABOUT["headline"])
    st.write(ABOUT["intro"])
    c1, c2 = st.columns(2)
    c1.link_button("LinkedIn", ABOUT["linkedin"])
    c2.link_button("GitHub", ABOUT["github"])
 
    st.divider()
    st.subheader("Projects")
    for p in PROJECTS:
        st.markdown(f"**{p['title']}**  \n{p['tagline']}")
        if p.get("demo"):
            st.link_button("Live demo", p["demo"])
 
 
# ---------- Sidebar navigation ----------
st.sidebar.title("Portfolio")
pages = ["Home"] + [p["title"] for p in PROJECTS]
choice = st.sidebar.radio("Go to", pages)
st.sidebar.divider()
st.sidebar.caption("Personal details are blurred, removed or replaced with made-up data.")
 
if choice == "Home":
    show_home()
else:
    show_project(next(p for p in PROJECTS if p["title"] == choice))
