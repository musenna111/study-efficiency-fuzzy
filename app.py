import streamlit as st

from fuzzy_system import calculate_efficiency
from plots import plot_memberships, plot_defuzzification


st.set_page_config(
    page_title="Akıllı Ders Çalışma Verimlilik Sistemi",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 0.8rem;
    padding-bottom: 0.8rem;
    max-width: 1180px;
}

.main-title {
    font-size: 24px;
    font-weight: 800;
    color: #1f2937;
    margin-bottom: 0px;
}

.sub-text {
    font-size: 12px;
    color: #6b7280;
    margin-bottom: 10px;
}

.card {
    background: #f8fafc;
    padding: 6px 10px;
    border-radius: 8px;
    border: 1px solid #e5e7eb;
    min-height: 55px;
}

.card h4 {
    margin: 0;
    font-size: 11px;
    color: #374151;
}

.card h2 {
    margin-top: 4px;
    font-size: 16px;
    color: #111827;
}

.rule-box {
    background-color: #f8fafc;
    padding: 8px;
    border-radius: 7px;
    margin-bottom: 6px;
    border-left: 4px solid #2563eb;
    font-size: 12px;
}

div[data-testid="stImage"] img {
    max-width: 100%;
    height: auto;
}
</style>
""", unsafe_allow_html=True)


# =========================
# SIDEBAR
# =========================

st.sidebar.header("Giriş Değerleri")

study_hours = st.sidebar.slider(
    "Çalışma Süresi (Saat)",
    0.0,
    8.0,
    4.0,
    0.1
)

phone_hours = st.sidebar.slider(
    "Telefon Kullanımı (Saat)",
    0.0,
    6.0,
    2.0,
    0.1
)

sleep_quality = st.sidebar.slider(
    "Uyku Kalitesi",
    0.0,
    10.0,
    5.0,
    0.1
)

break_quality = st.sidebar.slider(
    "Mola Düzeni",
    0.0,
    10.0,
    5.0,
    0.1
)

st.sidebar.button("Hesapla")


# =========================
# CALCULATE
# =========================

result = calculate_efficiency(
    study_hours,
    phone_hours,
    sleep_quality,
    break_quality
)

score = result["score"]
level = result["level"]


# =========================
# TITLE
# =========================

st.markdown(
    '<div class="main-title">📚 Akıllı Ders Çalışma Verimlilik Sistemi</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-text">Bulanık Mantık Tabanlı Ders Çalışma Verimlilik Analizi</div>',
    unsafe_allow_html=True
)


# =========================
# RESULT CARDS
# =========================

st.markdown("##### 🎯 Verimlilik Sonucu")

col1, col2 = st.columns([1, 1], gap="small")

with col1:
    st.markdown(
        f"""
        <div class="card">
            <h4>Verimlilik Skoru</h4>
            <h2>{score}/100</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="card">
            <h4>Verimlilik Seviyesi</h4>
            <h2>{level}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()


# =========================
# TABS
# =========================

tab1, tab2, tab3 = st.tabs([
    "Üyelik Fonksiyonları",
    "Durulaştırma Grafiği",
    "Aktif Kurallar"
])


# =========================
# MEMBERSHIP TAB
# =========================

with tab1:

    st.markdown("##### 📊 Üyelik Fonksiyonları")

    fig1 = plot_memberships(result)

    fig1.savefig(
        "membership_plot.png",
        bbox_inches="tight",
        dpi=130
    )

    st.image(
        "membership_plot.png",
        use_container_width=True
    )


# =========================
# DEFUZZIFICATION TAB
# =========================

with tab2:

    st.markdown("##### 📈 Durulaştırma Grafiği")

    fig2 = plot_defuzzification(result)

    fig2.savefig(
        "defuzzification_plot.png",
        bbox_inches="tight",
        dpi=130
    )

    st.image(
        "defuzzification_plot.png",
        use_container_width=True
    )


# =========================
# RULES TAB
# =========================

with tab3:

    st.markdown("##### ⚙️ Aktif Kurallar")

    if result["active_rules"]:

        for rule in result["active_rules"]:

            st.markdown(
                f"""
                <div class="rule-box">
                    <b>Kural:</b> {rule['rule']} <br>
                    <b>Aktivasyon:</b> {rule['activation']} <br>
                    <b>Çıkış:</b> {rule['output']}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:
        st.warning("Aktif kural bulunamadı.")