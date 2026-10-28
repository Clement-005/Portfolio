import base64
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
        "video": "images/hospital_demo.mp4",  # screen recording (or a YouTube link)
        "screenshots": [  # save your images in the images/ folder with these names
            ("images/hospital_dashboard.png",
             "Operations dashboard: KPIs, conditions, admissions vs discharges, data quality, patient journey, insurers"),
            ("images/hospital_login.png",
             "Staff sign-in: each role sees different pages and fields"),
        ],
    },
    # To add another project, copy the block above, paste it here and edit it.
]
# =====================================================================
 
 
# Decorative illustration shown under the Projects list on the home page
WORKSPACE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" font-family="Segoe UI, Arial, sans-serif">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0C1745"/><stop offset="1" stop-color="#08102F"/>
  </linearGradient>
  <linearGradient id="desk" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1A2C6B"/><stop offset="1" stop-color="#101E50"/>
  </linearGradient>
  <linearGradient id="screen" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#14306F"/><stop offset="1" stop-color="#0B1C4C"/>
  </linearGradient>
  <linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1D4590"/><stop offset="1" stop-color="#163874"/>
  </linearGradient>
  <linearGradient id="base" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#D9E3F2"/><stop offset="1" stop-color="#AEBCD3"/>
  </linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.45" r="0.5">
    <stop offset="0" stop-color="#3D7BF0" stop-opacity=".35"/><stop offset="1" stop-color="#3D7BF0" stop-opacity="0"/>
  </radialGradient>
  <filter id="sh" x="-20%" y="-20%" width="140%" height="160%">
    <feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#000" flood-opacity=".35"/>
  </filter>
</defs>
 
<rect width="1200" height="560" rx="28" fill="url(#bg)"/>
<ellipse cx="600" cy="230" rx="430" ry="230" fill="url(#glow)"/>
<path d="M0 360 H1200 V532 a28 28 0 0 1 -28 28 H28 a28 28 0 0 1 -28 -28 Z" fill="url(#desk)"/>
 
<!-- left: chart printout -->
<g transform="translate(70 385) rotate(-8)" filter="url(#sh)">
  <rect width="250" height="150" rx="8" fill="#E8EFFA"/>
  <rect x="18" y="16" width="90" height="8" rx="4" fill="#9FB4D6"/>
  <g fill="#4C8DF6">
    <rect x="22" y="96" width="14" height="34"/><rect x="44" y="80" width="14" height="50"/>
    <rect x="66" y="88" width="14" height="42"/><rect x="88" y="62" width="14" height="68"/>
    <rect x="110" y="72" width="14" height="58"/><rect x="132" y="50" width="14" height="80"/>
  </g>
  <circle cx="205" cy="88" r="30" fill="none" stroke="#C7D5EC" stroke-width="12"/>
  <circle cx="205" cy="88" r="30" fill="none" stroke="#2CC4C9" stroke-width="12" stroke-dasharray="120 189" transform="rotate(-90 205 88)"/>
</g>
<!-- left: notebook and pen -->
<g transform="translate(40 300) rotate(4)" filter="url(#sh)">
  <rect width="150" height="70" rx="8" fill="#22366F"/>
  <rect x="8" y="0" width="6" height="70" fill="#2F4A8F"/>
  <rect x="40" y="58" width="150" height="7" rx="3.5" fill="#E6EDF7" transform="rotate(-18 40 58)"/>
</g>
<!-- sticky notes -->
<g filter="url(#sh)">
  <rect x="215" y="318" width="92" height="56" rx="4" fill="#7FB8FF" transform="rotate(-6 261 346)"/>
  <rect x="300" y="470" width="110" height="50" rx="4" fill="#F28BB0" transform="rotate(-4 355 495)"/>
  <rect x="845" y="470" width="110" height="52" rx="4" fill="#F4C542" transform="rotate(5 900 496)"/>
</g>
 
<!-- laptop screen -->
<g filter="url(#sh)">
  <rect x="345" y="58" width="510" height="320" rx="16" fill="#0A0F24"/>
  <rect x="361" y="74" width="478" height="288" rx="8" fill="url(#screen)"/>
</g>
<!-- panel 1: pie + bars -->
<rect x="377" y="90" width="200" height="120" rx="8" fill="url(#panel)"/>
<text x="389" y="110" fill="#A9C4F5" font-size="11" font-weight="600">Overview</text>
<circle cx="425" cy="160" r="30" fill="#D5E4FF"/>
<path d="M425 160 L425 130 A30 30 0 0 1 452 173 Z" fill="#4C8DF6"/>
<path d="M425 160 L452 173 A30 30 0 0 1 415 188 Z" fill="#2CC4C9"/>
<g fill="#7FB2FF"><rect x="478" y="168" width="10" height="24"/><rect x="494" y="152" width="10" height="40"/><rect x="510" y="160" width="10" height="32"/><rect x="526" y="140" width="10" height="52"/><rect x="542" y="148" width="10" height="44"/></g>
<!-- panel 2: network -->
<rect x="589" y="90" width="234" height="120" rx="8" fill="url(#panel)"/>
<text x="601" y="110" fill="#A9C4F5" font-size="11" font-weight="600">Relationships</text>
<g stroke="#7FB2FF" stroke-width="2" fill="none">
  <path d="M630 165 L680 135 L740 160 L790 130 M680 135 L700 190 L740 160 M740 160 L790 185"/>
</g>
<g fill="#0F2A63" stroke="#BFD6FF" stroke-width="2.5">
  <circle cx="630" cy="165" r="9"/><circle cx="680" cy="135" r="9"/><circle cx="740" cy="160" r="11"/>
  <circle cx="790" cy="130" r="8"/><circle cx="700" cy="190" r="8"/><circle cx="790" cy="185" r="8"/>
</g>
<!-- panel 3: bars -->
<rect x="377" y="222" width="150" height="124" rx="8" fill="url(#panel)"/>
<text x="389" y="242" fill="#A9C4F5" font-size="11" font-weight="600">Monthly</text>
<g fill="#9CC2FF"><rect x="390" y="300" width="9" height="34"/><rect x="404" y="286" width="9" height="48"/><rect x="418" y="294" width="9" height="40"/><rect x="432" y="276" width="9" height="58"/><rect x="446" y="290" width="9" height="44"/><rect x="460" y="268" width="9" height="66"/><rect x="474" y="280" width="9" height="54"/><rect x="488" y="258" width="9" height="76"/><rect x="502" y="266" width="9" height="68"/></g>
<!-- panel 4: KPI ring -->
<rect x="539" y="222" width="122" height="124" rx="8" fill="url(#panel)"/>
<circle cx="600" cy="288" r="36" fill="none" stroke="#24508F" stroke-width="10"/>
<circle cx="600" cy="288" r="36" fill="none" stroke="#2CC4C9" stroke-width="10" stroke-linecap="round" stroke-dasharray="68 226" transform="rotate(-90 600 288)"/>
<circle cx="600" cy="288" r="24" fill="none" stroke="#7FB2FF" stroke-width="2" opacity=".6"/>
<text x="600" y="294" fill="#FFFFFF" font-size="18" font-weight="700" text-anchor="middle">30%</text>
<!-- panel 5: trend bars + line -->
<rect x="673" y="222" width="150" height="124" rx="8" fill="url(#panel)"/>
<text x="685" y="242" fill="#A9C4F5" font-size="11" font-weight="600">Trend</text>
<g fill="#5B9BFF" opacity=".75"><rect x="688" y="306" width="8" height="28"/><rect x="701" y="296" width="8" height="38"/><rect x="714" y="300" width="8" height="34"/><rect x="727" y="284" width="8" height="50"/><rect x="740" y="290" width="8" height="44"/><rect x="753" y="272" width="8" height="62"/><rect x="766" y="278" width="8" height="56"/><rect x="779" y="258" width="8" height="76"/><rect x="792" y="262" width="8" height="72"/></g>
<polyline points="692,296 718,288 744,278 770,266 796,250" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
 
<!-- laptop base and keyboard -->
<g filter="url(#sh)">
  <path d="M300 378 H900 L948 452 Q950 462 938 462 H262 Q250 462 252 452 Z" fill="url(#base)"/>
  <rect x="540" y="378" width="120" height="7" rx="3" fill="#97A6C0"/>
</g>
<g fill="#1E2740">
  <path d="M338 394 H862 L872 410 H328 Z"/>
  <path d="M326 414 H874 L884 430 H316 Z"/>
  <path d="M520 434 H680 L684 446 H516 Z" fill="#C4CFE2"/>
</g>
<g stroke="#3A4566" stroke-width="2">
  <path d="M370 394 L366 410 M410 394 L406 410 M450 394 L447 410 M490 394 L488 410 M530 394 L529 410 M570 394 L570 410 M610 394 L611 410 M650 394 L652 410 M690 394 L693 410 M730 394 L734 410 M770 394 L775 410 M810 394 L816 410"/>
  <path d="M360 414 L356 430 M400 414 L397 430 M440 414 L438 430 M480 414 L479 430 M520 414 L520 430 M560 414 L560 430 M600 414 L601 430 M640 414 L642 430 M680 414 L683 430 M720 414 L724 430 M760 414 L765 430 M800 414 L806 430 M840 414 L847 430"/>
</g>
 
<!-- right: coffee cup -->
<g filter="url(#sh)">
  <path d="M960 250 H1040 L1030 360 H970 Z" fill="#EEF3FA"/>
  <path d="M964 290 H1036 L1032 325 H968 Z" fill="#B78C62"/>
  <rect x="952" y="236" width="96" height="18" rx="6" fill="#F7F9FC"/>
  <rect x="972" y="226" width="56" height="12" rx="5" fill="#E2E9F3"/>
</g>
<!-- right: line chart printout -->
<g transform="translate(905 385) rotate(6)" filter="url(#sh)">
  <rect width="240" height="140" rx="8" fill="#E8EFFA"/>
  <rect x="18" y="16" width="80" height="8" rx="4" fill="#9FB4D6"/>
  <polyline points="22,110 60,90 95,98 130,70 165,78 200,46 222,52" fill="none" stroke="#4C8DF6" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="22,120 60,112 95,114 130,100 165,104 200,88 222,90" fill="none" stroke="#2CC4C9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity=".8"/>
</g>
<!-- right: pen -->
<rect x="1000" y="372" width="160" height="7" rx="3.5" fill="#D6DEEA" transform="rotate(-12 1000 372)"/>
<!-- front: mug -->
<g filter="url(#sh)">
  <path d="M150 470 H240 V536 a14 14 0 0 1 -14 14 H164 a14 14 0 0 1 -14 -14 Z" fill="#ECF1F8"/>
  <ellipse cx="195" cy="470" rx="45" ry="11" fill="#2A3350"/>
  <path d="M240 488 q30 0 30 22 q0 22 -30 22" fill="none" stroke="#ECF1F8" stroke-width="9"/>
</g>
</svg>"""
 
 
def show_project(p):
    st.title(p["title"])
    st.write(p["tagline"])
    if p.get("demo"):
        st.link_button("Open live demo", p["demo"], type="primary")
 
    if p.get("kpis"):
        cols = st.columns(len(p["kpis"]))
        for col, (label, value) in zip(cols, p["kpis"]):
            col.metric(label, value)
 
    video = p.get("video")
    if video and (video.startswith("http") or os.path.exists(video)):
        st.subheader("Walkthrough")
        st.video(video)
 
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
 
    st.write("")
    img = base64.b64encode(WORKSPACE_SVG.encode()).decode()
    st.markdown(f'<img src="data:image/svg+xml;base64,{img}" alt="Laptop showing data dashboards on a desk" '
                f'style="width:100%;border-radius:16px;margin-top:8px;">', unsafe_allow_html=True)
 
 
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
