
import streamlit as st
import re

# =====================================================
# LAVE LAUNDRY STUDIO
# =====================================================

st.set_page_config(
    page_title="LAVE | Laundry Studio",
    page_icon="🫧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# DESAIN / CSS
# =====================================================

st.markdown("""
<style>
:root {
    --navy: #142A46;
    --navy2: #203D60;
    --gold: #C7A96B;
    --bg: #F4F6F9;
    --muted: #778397;
}

.stApp {
    background: var(--bg);
}

[data-testid="stSidebar"] {
    background: var(--navy);
}

[data-testid="stSidebar"] * {
    color: white;
}

.brand {
    text-align: center;
    padding: 25px 8px;
}

.brand-symbol {
    font-size: 48px;
    color: var(--gold);
}

.brand-name {
    font-size: 29px;
    font-weight: 800;
    letter-spacing: 5px;
}

.brand-subtitle {
    color: #C5D0DE;
    letter-spacing: 4px;
    font-size: 11px;
}

.brand-line {
    width: 65px;
    height: 3px;
    background: var(--gold);
    margin: 20px auto;
}

.main-heading {
    color: var(--navy);
    font-size: 31px;
    font-weight: 850;
}

.main-subheading {
    color: var(--muted);
    font-size: 15px;
    margin-bottom: 28px;
}

.section-heading {
    color: var(--navy);
    font-size: 20px;
    font-weight: 800;
    margin: 16px 0;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 15px;
}

.info-card {
    background: white;
    border: 1px solid #E1E6ED;
    border-radius: 15px;
    padding: 17px;
    min-height: 125px;
    margin-bottom: 12px;
    box-shadow: 0 3px 12px rgba(20,42,70,.04);
}

.info-top {
    display: flex;
    align-items: center;
    gap: 11px;
    margin-bottom: 14px;
}

.info-icon {
    width: 37px;
    height: 37px;
    border-radius: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 19px;
    background: #EDF3FA;
}

.info-label {
    color: #78869A;
    font-size: 12px;
    font-weight: 600;
}

.info-value {
    color: var(--navy);
    font-size: 22px;
    font-weight: 850;
}

.total-card {
    background: var(--navy);
    border-radius: 17px;
    padding: 23px;
    margin-top: 8px;
    box-shadow: 0 6px 18px rgba(20,42,70,.12);
}

.total-top {
    display: flex;
    align-items: center;
    gap: 12px;
}

.total-icon {
    background: #294361;
    border-radius: 12px;
    padding: 10px;
    font-size: 22px;
}

.total-label {
    color: #D8E0EA;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.total-value {
    color: #E7CC91;
    font-size: 32px;
    font-weight: 900;
    margin-top: 15px;
}

.total-note {
    color: #C5D0DE;
    font-size: 13px;
    margin-top: 8px;
}

div.stButton > button {
    border-radius: 10px;
    min-height: 45px;
    font-weight: 700;
}

div.stButton > button[kind="primary"] {
    background: var(--navy);
    border-color: var(--navy);
    color: white;
}

div.stButton > button[kind="primary"]:hover {
    background: var(--navy2);
    color: white;
}

div[data-testid="stTextInput"] input {
    border-radius: 9px;
}

.footer {
    text-align: center;
    color: #8993A1;
    font-size: 12px;
    padding: 30px 5px 15px;
    line-height: 1.9;
}

@media (max-width: 600px) {
    .main-heading { font-size: 25px; }
    .info-value { font-size: 18px; }
    .total-value { font-size: 27px; }
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# FUNGSI PERHITUNGAN
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
    diskon = jumlah_digit_genap
    biaya_normal = berat_kg * tarif
    potongan = biaya_normal * diskon / 100
    total = biaya_normal - potongan

    return {
        "nim": nim,
        "berat": berat_kg,
        "tarif": tarif,
        "digit_genap": jumlah_digit_genap,
        "diskon": diskon,
        "normal": biaya_normal,
        "potongan": potongan,
        "total": total
    }


# =====================================================
# SESSION STATE
# =====================================================

for key, value in {
    "nim": "",
    "berat": "",
    "hasil": None,
    "error": None
}.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =====================================================
# SIDEBAR / IDENTITAS LAVE
# =====================================================

with st.sidebar:

    st.markdown("""
    <div class="brand">
        <div class="brand-symbol">〰</div>
        <div class="brand-name">LAVÉ</div>
        <div class="brand-subtitle">LAUNDRY STUDIO</div>
        <div class="brand-line"></div>
        <p style="color:#C5D0DE;line-height:1.9">
        Smart Laundry Calculator<br>
        Aplikasi Perhitungan<br>
        Biaya Laundry Kiloan
        </p>
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
    3. Tekan Hitung Biaya.
    4. Lihat hasil perhitungan.
    """)

    st.divider()
    st.caption("LAVÉ LAUNDRY STUDIO")
    st.caption("Clean. Simple. Reliable.")


# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="main-heading">
    LAVÉ Laundry Calculator
</div>
<div class="main-subheading">
    Perhitungan biaya laundry kiloan yang praktis,
    cepat, dan akurat.
</div>
""", unsafe_allow_html=True)


# =====================================================
# INPUT PELANGGAN
# =====================================================

st.markdown(
    '<div class="section-heading">01 / DATA PELANGGAN</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    nim = st.text_input(
        "Nomor Induk Mahasiswa (NIM)",
        placeholder="Masukkan 10 digit angka",
        key="nim"
    )

    berat = st.text_input(
        "Berat Cucian (kg)",
        placeholder="Masukkan berat dalam kilogram",
        key="berat"
    )

    col_hitung, col_reset = st.columns(2)

    with col_hitung:
        tombol_hitung = st.button(
            "✦  Hitung Biaya",
            type="primary",
            use_container_width=True
        )

    with col_reset:
        st.button(
            "↻  Reset",
            on_click=reset_data,
            use_container_width=True
        )


# =====================================================
# PROSES PERHITUNGAN
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
# VALIDASI
# =====================================================

if st.session_state["error"]:
    st.error(st.session_state["error"])


# =====================================================
# RINCIAN HASIL
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

    cards = [
        ("🏷️", "Tarif per Kilogram",
         format_rupiah(hasil["tarif"])),
        ("％", "Persentase Diskon",
         str(hasil["diskon"]) + "%"),
        ("🧺", "Biaya Normal",
         format_rupiah(hasil["normal"])),
        ("✧", "Potongan Harga",
         format_rupiah(hasil["potongan"]))
    ]

    for index, (icon, label, value) in enumerate(cards):

        column = col1 if index % 2 == 0 else col2

        with column:
            st.markdown(f"""
            <div class="info-card">
                <div class="info-top">
                    <div class="info-icon">{icon}</div>
                    <div class="info-label">{label}</div>
                </div>
                <div class="info-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="total-card">
        <div class="total-top">
            <div class="total-icon">🧾</div>
            <div class="total-label">
                TOTAL PEMBAYARAN
            </div>
        </div>
        <div class="total-value">
            {format_rupiah(hasil["total"])}
        </div>
        <div class="total-note">
            Berat {hasil["berat"]} kg
            &nbsp; | &nbsp;
            Diskon {hasil["diskon"]}%
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("Lihat Detail Data Pelanggan"):

        st.write("**NIM:**", hasil["nim"])
        st.write("**Berat Cucian:**", hasil["berat"], "kg")
        st.write("**Jumlah Digit Genap:**", hasil["digit_genap"])
        st.write("**Tarif per kg:**", format_rupiah(hasil["tarif"]))
        st.write("**Biaya Normal:**", format_rupiah(hasil["normal"]))
        st.write("**Potongan:**", format_rupiah(hasil["potongan"]))
        st.write("**Total Bayar:**", format_rupiah(hasil["total"]))


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
