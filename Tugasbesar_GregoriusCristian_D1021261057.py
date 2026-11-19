
import streamlit as st
import re

# =====================================================
# LAVE LAUNDRY STUDIO
# Aplikasi Perhitungan Biaya Laundry Kiloan
# =====================================================

st.set_page_config(
    page_title="LAVE | Laundry Studio",
    page_icon="🫧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CSS - LAVE SIGNATURE DESIGN
# =====================================================

st.markdown("""
<style>
    :root {
        --navy: #142A46;
        --navy-light: #203D60;
        --gold: #C7A96B;
        --background: #F5F6F8;
        --muted: #758195;
    }

    .stApp {
        background: var(--background);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    /* SIDEBAR */

    [data-testid="stSidebar"] {
        background: var(--navy);
        border-right: 1px solid #263F5C;
    }

    [data-testid="stSidebar"] > div {
        background: var(--navy);
    }

    [data-testid="stSidebar"] * {
        color: #FFFFFF;
    }

    /* BRAND */

    .brand {
        padding: 22px 8px 16px;
        text-align: center;
    }

    .brand-symbol {
        font-size: 48px;
        color: var(--gold);
        font-weight: 300;
        letter-spacing: 4px;
    }

    .brand-name {
        font-size: 25px;
        font-weight: 800;
        letter-spacing: 4px;
        color: white;
        margin-top: 5px;
    }

    .brand-subtitle {
        font-size: 10px;
        color: #C5D0DE;
        letter-spacing: 3px;
        margin-top: 5px;
    }

    .brand-line {
        width: 45px;
        height: 2px;
        background: var(--gold);
        margin: 17px auto;
    }

    .brand-description {
        color: #C5D0DE;
        font-size: 12px;
        line-height: 1.8;
    }

    /* MAIN HEADER */

    .hero {
        text-align: center;
        padding: 15px 5px 25px;
    }

    .washer-logo {
        width: 82px;
        height: 82px;
        background: var(--navy);
        border: 1px solid rgba(199,169,107,0.5);
        border-radius: 23px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 17px;
        box-shadow: 0 5px 16px rgba(20,42,70,0.10);
    }

    .washer-logo svg {
        width: 54px;
        height: 54px;
    }

    .main-heading {
        color: var(--navy);
        font-size: 30px;
        font-weight: 800;
        margin-bottom: 5px;
        letter-spacing: -0.5px;
    }

    .main-subheading {
        color: var(--muted);
        font-size: 14px;
        margin-bottom: 12px;
        line-height: 1.7;
    }

    .section-heading {
        color: var(--navy);
        font-size: 19px;
        font-weight: 750;
        margin: 12px 0 15px;
    }

    /* INPUT FORM */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 15px;
        border-color: #DCE2EA;
    }

    div[data-testid="stTextInput"] label {
        color: var(--navy) !important;
        font-weight: 600;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 9px;
        min-height: 45px;
        background: #FFFFFF !important;
        color: var(--navy) !important;
        border: 1px solid #DCE2EA;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: #9AA4B2 !important;
    }

    /* RESULT CARDS */

    .info-card {
        background: white;
        border: 1px solid #E4E8EE;
        border-radius: 15px;
        padding: 19px;
        min-height: 145px;
        margin-bottom: 12px;
        box-shadow: 0 3px 12px rgba(20,42,70,0.035);
    }

    .card-icon {
        width: 48px;
        height: 48px;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 25px;
        font-weight: 700;
        margin-bottom: 15px;
    }

    .icon-blue {
        background: #E5EFFB;
        color: #244D79;
    }

    .icon-purple {
        background: #EEE8F7;
        color: #70568F;
    }

    .icon-green {
        background: #E3F1E9;
        color: #367C59;
    }

    .icon-gold {
        background: #F7EEDC;
        color: #A17B3E;
    }

    .info-label {
        color: #7B8797;
        font-size: 13px;
        margin-bottom: 9px;
    }

    .info-value {
        color: var(--navy);
        font-size: 21px;
        font-weight: 800;
    }

    /* TOTAL PAYMENT */

    .total-card {
        background: var(--navy);
        border-radius: 16px;
        padding: 25px;
        margin-top: 10px;
        box-shadow: 0 6px 18px rgba(20,42,70,0.12);
        position: relative;
        overflow: hidden;
    }

    .total-label {
        color: #D8E0EA;
        font-size: 12px;
        letter-spacing: 2px;
        font-weight: 600;
    }

    .total-value {
        color: #E7CC91;
        font-size: 30px;
        font-weight: 850;
        margin-top: 10px;
    }

    .total-note {
        color: #C5D0DE;
        font-size: 13px;
        margin-top: 9px;
    }

    .total-decoration {
        position: absolute;
        right: 20px;
        top: 20px;
        font-size: 48px;
        color: rgba(231,204,145,0.18);
    }

    /* BUTTONS */

    div.stButton > button {
        border-radius: 10px;
        min-height: 45px;
        font-weight: 650;
        transition: 0.2s ease;
    }

    div.stButton > button[kind="primary"] {
        background: var(--navy);
        border-color: var(--navy);
        color: white;
    }

    div.stButton > button[kind="primary"]:hover {
        background: var(--navy-light);
        border-color: var(--navy-light);
        color: white;
    }

    div.stButton > button[kind="secondary"] {
        background: #FFFFFF;
        border: 1px solid #DCE2EA;
        color: var(--navy);
    }

    div.stButton > button[kind="secondary"]:hover {
        background: #EAF0F6;
        border-color: var(--navy);
        color: var(--navy);
    }

    /* EXPANDER / CUSTOMER DETAILS */

    [data-testid="stExpander"] {
        border: 1px solid #DCE2EA;
        border-radius: 11px;
        background: white;
        margin-top: 12px;
    }

    [data-testid="stExpander"] summary {
        color: var(--navy) !important;
        background: #FFFFFF;
        font-weight: 650;
    }

    [data-testid="stExpander"] summary p {
        color: var(--navy) !important;
    }

    [data-testid="stExpander"] [data-testid="stExpanderDetails"] {
        background: #FFFFFF;
        color: var(--navy) !important;
        padding: 15px;
    }

    [data-testid="stExpander"] [data-testid="stExpanderDetails"] p {
        color: #34445A !important;
        font-size: 14px;
    }

    /* FOOTER */

    .footer {
        color: #8993A1;
        text-align: center;
        font-size: 11px;
        padding: 25px 5px 10px;
        line-height: 1.8;
    }

    .footer b {
        color: #667387;
        letter-spacing: 0.5px;
    }

    /* MOBILE */

    @media (max-width: 600px) {
        .hero {
            padding-top: 10px;
        }

        .washer-logo {
            width: 72px;
            height: 72px;
            border-radius: 20px;
        }

        .washer-logo svg {
            width: 48px;
            height: 48px;
        }

        .main-heading {
            font-size: 24px;
        }

        .main-subheading {
            font-size: 13px;
        }

        .info-value {
            font-size: 18px;
        }

        .total-value {
            font-size: 25px;
        }

        .brand-name {
            font-size: 22px;
        }

        .info-card {
            padding: 15px;
            min-height: 135px;
        }
    }
</style>
""", unsafe_allow_html=True)


# =====================================================
# FUNGSI BANTU
# =====================================================

def format_rupiah(nilai):
    return "Rp " + f"{nilai:,.0f}".replace(",", ".")


def reset_data():
    st.session_state["nim"] = ""
    st.session_state["berat"] = ""
    st.session_state["hasil"] = None
    st.session_state["error"] = None


def hitung_laundry(nim, berat):

    if not re.fullmatch(r"[0-9]{10}", nim):
        raise ValueError(
            "NIM tidak valid! Masukkan tepat 10 digit angka."
        )

    if not re.fullmatch(r"[0-9]+", berat):
        raise ValueError(
            "Berat cucian harus berupa bilangan bulat positif."
        )

    berat_kg = int(berat)

    if berat_kg <= 0:
        raise ValueError(
            "Berat cucian harus lebih dari 0 kg."
        )

    digit_terakhir = int(nim[-1])

    jumlah_digit_genap = sum(
        1 for digit in nim
        if int(digit) % 2 == 0
    )

    tarif = 5000 + (digit_terakhir * 500)

    persen_diskon = jumlah_digit_genap

    biaya_normal = berat_kg * tarif

    potongan = biaya_normal * persen_diskon / 100

    total_bayar = biaya_normal - potongan

    return {
        "nim": nim,
        "berat": berat_kg,
        "tarif": tarif,
        "digit_genap": jumlah_digit_genap,
        "diskon": persen_diskon,
        "normal": biaya_normal,
        "potongan": potongan,
        "total": total_bayar
    }


# =====================================================
# SESSION STATE
# =====================================================

if "nim" not in st.session_state:
    st.session_state["nim"] = ""

if "berat" not in st.session_state:
    st.session_state["berat"] = ""

if "hasil" not in st.session_state:
    st.session_state["hasil"] = None

if "error" not in st.session_state:
    st.session_state["error"] = None


# =====================================================
# SIDEBAR / IDENTITAS APLIKASI
# =====================================================

with st.sidebar:

    st.markdown("""
    <div class="brand">
        <div class="brand-symbol">〰</div>
        <div class="brand-name">LAVÉ</div>
        <div class="brand-subtitle">LAUNDRY STUDIO</div>
        <div class="brand-line"></div>
        <div class="brand-description">
            Smart Laundry Calculator<br>
            Aplikasi Perhitungan<br>
            Biaya Laundry Kiloan
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### Tentang Aplikasi")
    st.markdown("**Kategori:** Laundry Calculator")
    st.markdown("**Bahasa:** Python")
    st.markdown("**Framework:** Streamlit")
    st.markdown("**Versi:** 1.0")

    st.divider()

    st.markdown("### Panduan")
    st.markdown("""
    1. Masukkan NIM 10 digit.
    2. Masukkan berat cucian.
    3. Tekan tombol Hitung.
    4. Lihat rincian pembayaran.
    """)

    st.divider()

    st.caption("LAVÉ LAUNDRY STUDIO")
    st.caption("Clean. Simple. Reliable.")


# =====================================================
# HEADER UTAMA + LOGO MESIN CUCI
# =====================================================

st.markdown("""
<div class="hero">

    <div class="washer-logo">
        <svg viewBox="0 0 100 100"
             xmlns="http://www.w3.org/2000/svg"
             fill="none">

            <!-- BODY MESIN CUCI -->
            <rect x="13" y="10" width="74" height="80"
                  rx="8"
                  stroke="#C7A96B"
                  stroke-width="3"/>

            <!-- PANEL ATAS -->
            <path d="M13 31 H87"
                  stroke="#C7A96B"
                  stroke-width="3"/>

            <!-- TOMBOL KONTROL -->
            <circle cx="68" cy="21" r="3.5"
                    stroke="#C7A96B"
                    stroke-width="2.5"/>

            <circle cx="79" cy="21" r="3.5"
                    stroke="#C7A96B"
                    stroke-width="2.5"/>

            <!-- LAYAR KECIL -->
            <rect x="21" y="17" width="24" height="8"
                  rx="3"
                  stroke="#C7A96B"
                  stroke-width="2.5"/>

            <!-- PINTU MESIN CUCI -->
            <circle cx="50" cy="59" r="22"
                    stroke="#C7A96B"
                    stroke-width="3"/>

            <!-- GARIS AIR -->
            <path d="M40 62 Q45 53 50 62 T60 62"
                  stroke="#C7A96B"
                  stroke-width="2.5"
                  stroke-linecap="round"/>

        </svg>
    </div>

    <div class="main-heading">
        Laundry Cost Calculator
    </div>

    <div class="main-subheading">
        Perhitungan biaya laundry kiloan yang praktis,
        cepat, dan akurat.
    </div>

</div>
""", unsafe_allow_html=True)


# =====================================================
# FORM INPUT
# =====================================================

st.markdown(
    '<div class="section-heading">01 / DATA PELANGGAN</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    nim = st.text_input(
        "Nomor Induk Mahasiswa (NIM)",
        placeholder="Masukkan 10 digit angka",
        max_chars=20,
        key="nim"
    )

    berat = st.text_input(
        "Berat Cucian (kg)",
        placeholder="Masukkan berat dalam kilogram",
        max_chars=20,
        key="berat"
    )

    col_hitung, col_reset = st.columns(2)

    with col_hitung:
        tombol_hitung = st.button(
            "🧺 Hitung Biaya",
            type="primary",
            use_container_width=True
        )

    with col_reset:
        st.button(
            "↻ Reset",
            on_click=reset_data,
            use_container_width=True
        )


# =====================================================
# PROSES HITUNG
# =====================================================

if tombol_hitung:

    st.session_state["hasil"] = None
    st.session_state["error"] = None

    try:
        st.session_state["hasil"] = hitung_laundry(
            nim.strip(),
            berat.strip()
        )

    except ValueError as error:
        st.session_state["error"] = str(error)


# =====================================================
# PESAN VALIDASI
# =====================================================

if st.session_state["error"]:
    st.error(st.session_state["error"])


# =====================================================
# HASIL PERHITUNGAN
# =====================================================

hasil = st.session_state["hasil"]

if hasil is not None:

    st.markdown("---")

    st.markdown("""
    <div class="section-heading">
        02 / RINCIAN PERHITUNGAN
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-icon icon-blue">◇</div>
            <div class="info-label">Tarif per Kilogram</div>
            <div class="info-value">
                {format_rupiah(hasil['tarif'])}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-icon icon-purple">%</div>
            <div class="info-label">Persentase Diskon</div>
            <div class="info-value">
                {hasil['diskon']}%
            </div>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-icon icon-green">▤</div>
            <div class="info-label">Biaya Normal</div>
            <div class="info-value">
                {format_rupiah(hasil['normal'])}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-icon icon-gold">−</div>
            <div class="info-label">Potongan Harga</div>
            <div class="info-value">
                {format_rupiah(hasil['potongan'])}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # TOTAL PEMBAYARAN

    st.markdown(f"""
    <div class="total-card">
        <div class="total-decoration">✦</div>

        <div class="total-label">
            TOTAL PEMBAYARAN
        </div>

        <div class="total-value">
            {format_rupiah(hasil['total'])}
        </div>

        <div class="total-note">
            Berat {hasil['berat']} kg
            &nbsp; | &nbsp;
            Diskon {hasil['diskon']}%
        </div>
    </div>
    """, unsafe_allow_html=True)

    # DETAIL DATA PELANGGAN

    with st.expander("⌄ Lihat Detail Data Pelanggan"):

        st.write("**NIM:**", hasil["nim"])

        st.write(
            "**Berat Cucian:**",
            hasil["berat"],
            "kg"
        )

        st.write(
            "**Jumlah Digit Genap:**",
            hasil["digit_genap"]
        )

        st.write(
            "**Tarif per kg:**",
            format_rupiah(hasil["tarif"])
        )

        st.write(
            "**Biaya Normal:**",
            format_rupiah(hasil["normal"])
        )

        st.write(
            "**Potongan:**",
            format_rupiah(hasil["potongan"])
        )

        st.write(
            "**Total Bayar:**",
            format_rupiah(hasil["total"])
        )


# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">
    <b>LAVÉ LAUNDRY STUDIO</b><br>
    Smart Laundry Calculator<br>
    © 2026 · All Rights Reserved
</div>
""", unsafe_allow_html=True)
