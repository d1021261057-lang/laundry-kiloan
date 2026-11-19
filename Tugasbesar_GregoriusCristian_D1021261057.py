
import streamlit as st
import re

# =====================================================
# LAVE LAUNDRY STUDIO
# Smart Laundry Calculator
# =====================================================

st.set_page_config(
    page_title="LAVÉ | Laundry Studio",
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
    color-scheme: light;
    --navy: #142A46;
    --navy-light: #203D60;
    --gold: #C7A96B;
    --background: #F4F6F9;
    --white: #FFFFFF;
    --text: #26364D;
    --muted: #758195;
}

/* BACKGROUND DAN TEKS UTAMA */

.stApp,
[data-testid="stAppViewContainer"] {
    background: var(--background) !important;
    color: var(--text) !important;
}

[data-testid="stMain"] {
    background: var(--background) !important;
}

[data-testid="stMain"] p,
[data-testid="stMain"] label,
[data-testid="stMain"] li {
    color: var(--text);
}

[data-testid="stHeader"] {
    background: transparent;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: var(--navy) !important;
    border-right: 1px solid #263F5C;
}

[data-testid="stSidebar"] > div {
    background: var(--navy) !important;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF;
}

/* BRAND SIDEBAR */

.brand {
    padding: 25px 8px 20px;
    text-align: center;
}

.brand-logo {
    width: 90px;
    height: 90px;
    margin: 0 auto 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid rgba(199,169,107,0.55);
    border-radius: 22px;
    background: rgba(255,255,255,0.04);
}

.brand-name {
    font-size: 27px;
    font-weight: 800;
    letter-spacing: 5px;
    color: white;
}

.brand-subtitle {
    font-size: 10px;
    color: #C5D0DE;
    letter-spacing: 4px;
    margin-top: 5px;
}

.brand-line {
    width: 48px;
    height: 2px;
    background: var(--gold);
    margin: 18px auto;
}

.brand-description {
    color: #C5D0DE;
    font-size: 12px;
    line-height: 1.9;
}

/* MAIN HEADER */

.hero {
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 15px 0 8px;
}

.hero-logo {
    min-width: 65px;
    height: 65px;
    background: var(--navy);
    border-radius: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.main-heading {
    color: var(--navy) !important;
    font-size: 29px;
    font-weight: 800;
    margin: 0;
    line-height: 1.2;
}

.main-subheading {
    color: var(--muted) !important;
    font-size: 14px;
    line-height: 1.7;
    margin-bottom: 30px;
}

/* SECTION HEADING */

.section-heading {
    color: var(--navy) !important;
    font-size: 19px;
    font-weight: 800;
    margin: 20px 0 15px;
}

/* INPUT FORM */

div[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid #DCE2EA !important;
    border-radius: 15px !important;
    background: white !important;
}

[data-testid="stTextInput"] label {
    color: var(--navy) !important;
    font-weight: 650 !important;
}

[data-testid="stTextInput"] input {
    background: #FFFFFF !important;
    color: var(--text) !important;
    border: 1px solid #CCD5E1 !important;
    border-radius: 9px !important;
    min-height: 48px;
}

[data-testid="stTextInput"] input::placeholder {
    color: #929BA8 !important;
}

/* RESULT CARDS */

.info-card {
    background: #FFFFFF;
    border: 1px solid #E1E6ED;
    border-radius: 15px;
    padding: 20px;
    min-height: 150px;
    margin-bottom: 12px;
    box-shadow: 0 3px 12px rgba(20,42,70,0.04);
}

.card-icon {
    width: 44px;
    height: 44px;
    border-radius: 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 23px;
    font-weight: 700;
    margin-bottom: 14px;
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
    color: #758195 !important;
    font-size: 13px;
    margin-bottom: 8px;
}

.info-value {
    color: var(--navy) !important;
    font-size: 22px;
    font-weight: 800;
}

/* TOTAL PAYMENT */

.total-card {
    background: var(--navy);
    border-radius: 17px;
    padding: 27px;
    margin-top: 10px;
    margin-bottom: 18px;
    box-shadow: 0 6px 18px rgba(20,42,70,0.12);
    position: relative;
    overflow: hidden;
}

.total-label {
    color: #D8E0EA !important;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 700;
}

.total-value {
    color: #E7CC91 !important;
    font-size: 31px;
    font-weight: 850;
    margin-top: 12px;
}

.total-note {
    color: #C5D0DE !important;
    font-size: 13px;
    margin-top: 12px;
}

.total-decoration {
    position: absolute;
    right: 22px;
    top: 20px;
    font-size: 48px;
    color: rgba(231,204,145,0.22);
}

/* BUTTONS */

div.stButton > button {
    border-radius: 10px !important;
    min-height: 48px;
    font-weight: 650 !important;
    transition: 0.2s ease;
    background: #FFFFFF;
    color: var(--navy);
    border: 1px solid #DCE2EA;
}

div.stButton > button[kind="primary"] {
    background: var(--navy) !important;
    border-color: var(--navy) !important;
    color: white !important;
}

div.stButton > button[kind="primary"]:hover {
    background: var(--navy-light) !important;
    border-color: var(--navy-light) !important;
}

/* EXPANDER - FIX KONTRAS TULISAN */

[data-testid="stExpander"] {
    background: #FFFFFF !important;
    border: 1px solid #DCE2EA !important;
    border-radius: 12px !important;
    overflow: hidden;
    margin-top: 15px;
}

[data-testid="stExpander"] summary {
    background: #FFFFFF !important;
    color: var(--navy) !important;
}

[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span {
    color: var(--navy) !important;
    font-weight: 650 !important;
}

[data-testid="stExpanderDetails"] {
    background: #FFFFFF !important;
}

[data-testid="stExpanderDetails"] p,
[data-testid="stExpanderDetails"] span,
[data-testid="stExpanderDetails"] strong {
    color: var(--text) !important;
}

/* DETAIL ROW */

.detail-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    padding: 12px 2px;
    border-bottom: 1px solid #EDF0F4;
    color: var(--text) !important;
    font-size: 14px;
}

.detail-row strong {
    color: var(--navy) !important;
    text-align: right;
}

.detail-total {
    border-bottom: none;
    border-top: 2px solid var(--gold);
    margin-top: 8px;
    padding-top: 17px;
    font-weight: 800;
}

/* ALERT */

[data-testid="stAlert"] p {
    color: inherit !important;
}

/* FOOTER */

.footer {
    color: #8993A1 !important;
    text-align: center;
    font-size: 11px;
    padding: 30px 5px 15px;
    line-height: 1.9;
}

/* MOBILE */

@media (max-width: 600px) {
    .main-heading {
        font-size: 22px;
    }

    .main-subheading {
        font-size: 13px;
    }

    .hero-logo {
        min-width: 55px;
        height: 55px;
    }

    .info-card {
        padding: 15px;
        min-height: 135px;
    }

    .info-value {
        font-size: 18px;
    }

    .total-value {
        font-size: 26px;
    }

    .total-card {
        padding: 22px;
    }

    .brand-name {
        font-size: 23px;
    }

    .detail-row {
        font-size: 13px;
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


# =====================================================
# FUNGSI PERHITUNGAN
# =====================================================

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
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("""
    <div class="brand">

        <div class="brand-logo">
            <svg width="65" height="65"
                 viewBox="0 0 100 100"
                 fill="none"
                 xmlns="http://www.w3.org/2000/svg">

                <rect x="19" y="15" width="62" height="70"
                      rx="7" stroke="#C7A96B"
                      stroke-width="3"/>

                <line x1="20" y1="34" x2="80" y2="34"
                      stroke="#C7A96B" stroke-width="3"/>

                <circle cx="34" cy="25" r="3"
                        fill="#C7A96B"/>

                <circle cx="45" cy="25" r="3"
                        stroke="#C7A96B" stroke-width="2"/>

                <circle cx="62" cy="59" r="18"
                        stroke="#C7A96B" stroke-width="3"/>

                <path d="M54 64 L64 54 M60 68 L70 58"
                      stroke="#C7A96B"
                      stroke-width="3"
                      stroke-linecap="round"/>

            </svg>
        </div>

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
# HEADER UTAMA
# =====================================================

st.markdown("""
<div class="hero">

    <div class="hero-logo">
        <svg width="43" height="43"
             viewBox="0 0 100 100"
             fill="none"
             xmlns="http://www.w3.org/2000/svg">

            <rect x="17" y="12" width="66" height="76"
                  rx="8" stroke="#C7A96B"
                  stroke-width="4"/>

            <line x1="18" y1="32" x2="82" y2="32"
                  stroke="#C7A96B" stroke-width="4"/>

            <circle cx="34" cy="22" r="4"
                    fill="#C7A96B"/>

            <circle cx="47" cy="22" r="4"
                    stroke="#C7A96B" stroke-width="3"/>

            <circle cx="50" cy="60" r="20"
                    stroke="#C7A96B" stroke-width="4"/>

            <path d="M41 66 L53 54 M49 70 L61 58"
                  stroke="#C7A96B"
                  stroke-width="4"
                  stroke-linecap="round"/>

        </svg>
    </div>

    <div class="main-heading">
        Laundry Cost Calculator
    </div>

</div>

<div class="main-subheading">
    Perhitungan biaya laundry kiloan yang praktis,
    cepat, dan akurat.
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
            "Hitung Biaya",
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

    # DETAIL PELANGGAN

    with st.expander("⌄ Lihat Detail Data Pelanggan"):

        st.markdown(f"""
        <div class="detail-row">
            <span>NIM</span>
            <strong>{hasil['nim']}</strong>
        </div>

        <div class="detail-row">
            <span>Berat Cucian</span>
            <strong>{hasil['berat']} kg</strong>
        </div>

        <div class="detail-row">
            <span>Jumlah Digit Genap</span>
            <strong>{hasil['digit_genap']}</strong>
        </div>

        <div class="detail-row">
            <span>Tarif per kg</span>
            <strong>{format_rupiah(hasil['tarif'])}</strong>
        </div>

        <div class="detail-row">
            <span>Biaya Normal</span>
            <strong>{format_rupiah(hasil['normal'])}</strong>
        </div>

        <div class="detail-row">
            <span>Potongan Harga</span>
            <strong>{format_rupiah(hasil['potongan'])}</strong>
        </div>

        <div class="detail-row detail-total">
            <span>Total Bayar</span>
            <strong>{format_rupiah(hasil['total'])}</strong>
        </div>
        """, unsafe_allow_html=True)


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
