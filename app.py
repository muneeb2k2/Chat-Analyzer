import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.facecolor'] = '#0f1117'
matplotlib.rcParams['axes.facecolor'] = '#1a1d27'
matplotlib.rcParams['axes.edgecolor'] = '#2e3347'
matplotlib.rcParams['text.color'] = '#e2e8f0'
matplotlib.rcParams['axes.labelcolor'] = '#94a3b8'
matplotlib.rcParams['xtick.color'] = '#94a3b8'
matplotlib.rcParams['ytick.color'] = '#94a3b8'
matplotlib.rcParams['grid.color'] = '#2e3347'

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Chat Analysis",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* ── Dark background ── */
.stApp {
    background-color: #0a0c13;
    color: #e2e8f0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1117 0%, #12151f 100%);
    border-right: 1px solid #1e2235;
}

[data-testid="stSidebar"] .stMarkdown h1 {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #ffffff;
    padding: 1.2rem 0 0.5rem;
}

/* ── File uploader ── */
[data-testid="stFileUploader"] {
    background: #13161f;
    border: 1.5px dashed #2a2f45;
    border-radius: 12px;
    padding: 0.5rem;
    transition: border-color 0.2s;
}
[data-testid="stFileUploader"]:hover {
    border-color: #4f8ef7;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
    background: #13161f;
    border: 1px solid #2a2f45;
    border-radius: 10px;
    color: #e2e8f0;
}

/* ── Primary button ── */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #4f8ef7 0%, #7c3aed 100%);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1.2rem;
    font-family: 'Syne', sans-serif;
    font-weight: 600;
    font-size: 0.9rem;
    letter-spacing: 0.03em;
    transition: opacity 0.2s, transform 0.15s;
    cursor: pointer;
}
.stButton > button:hover {
    opacity: 0.88;
    transform: translateY(-1px);
}
.stButton > button:active {
    transform: translateY(0);
}

/* ── Metric cards ── */
.metric-card {
    background: #13161f;
    border: 1px solid #1e2235;
    border-radius: 16px;
    padding: 1.5rem 1.75rem;
    text-align: center;
    transition: border-color 0.2s, transform 0.2s;
}
.metric-card:hover {
    border-color: #4f8ef7;
    transform: translateY(-2px);
}
.metric-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #64748b;
    margin-bottom: 0.6rem;
}
.metric-value {
    font-family: 'Syne', sans-serif;
    font-size: 2.4rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1;
}
.metric-accent {
    border-top: 3px solid transparent;
}
.metric-accent-blue  { border-top-color: #4f8ef7; }
.metric-accent-purple{ border-top-color: #7c3aed; }
.metric-accent-teal  { border-top-color: #14b8a6; }
.metric-accent-rose  { border-top-color: #f43f5e; }

/* ── Section headers ── */
.section-header {
    font-family: 'Syne', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.01em;
    margin: 2rem 0 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #1e2235;
}

/* ── Divider ── */
hr { border-color: #1e2235; }

/* ── DataFrame ── */
[data-testid="stDataFrame"] {
    background: #13161f;
    border: 1px solid #1e2235;
    border-radius: 12px;
    overflow: hidden;
}

/* ── Hero banner ── */
.hero-banner {
    background: linear-gradient(135deg, #0f1117 0%, #0d1229 50%, #130a24 100%);
    border: 1px solid #1e2235;
    border-radius: 20px;
    padding: 2.5rem 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 180px; height: 180px;
    background: radial-gradient(circle, rgba(79,142,247,0.12) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.03em;
    margin-bottom: 0.4rem;
}
.hero-sub {
    font-size: 1rem;
    color: #64748b;
    font-weight: 300;
}

/* ── Plot container ── */
.plot-container {
    background: #13161f;
    border: 1px solid #1e2235;
    border-radius: 16px;
    padding: 1.25rem;
}

/* ── Upload prompt ── */
.upload-prompt {
    background: #13161f;
    border: 1px solid #1e2235;
    border-radius: 16px;
    padding: 3rem 2rem;
    text-align: center;
    color: #475569;
}
.upload-prompt-icon { font-size: 3rem; margin-bottom: 1rem; }
.upload-prompt-text {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    color: #64748b;
}

/* ── Hide default streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("# 💬 Chat Analysis")
    st.markdown("<p style='color:#475569; font-size:0.82rem; margin-top:-0.6rem; margin-bottom:1.5rem;'>WhatsApp conversation insights</p>", unsafe_allow_html=True)
    st.divider()

    uploaded_file = st.file_uploader("Upload exported chat (.txt)", type=["txt"])

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        data = bytes_data.decode("utf-8")
        df = preprocessor.preprocess(data)

        user_list = df['user'].unique().tolist()
        if "group_notification" in user_list:
            user_list.remove("group_notification")
        user_list.sort()
        user_list.insert(0, "Overall")

        st.markdown("<p style='color:#64748b; font-size:0.8rem; font-weight:500; text-transform:uppercase; letter-spacing:0.06em; margin-top:1.2rem; margin-bottom:0.4rem;'>Participant</p>", unsafe_allow_html=True)
        selected_user = st.selectbox("", user_list, label_visibility="collapsed")

        st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
        analyze_btn = st.button("→  Run Analysis")

        st.divider()
        st.markdown(f"<p style='color:#334155; font-size:0.75rem;'>📁 {uploaded_file.name}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#334155; font-size:0.75rem;'>📊 {len(df)} messages loaded</p>", unsafe_allow_html=True)


# ── Main area ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <div class="hero-title">Chat Analyzer</div>
  <div class="hero-sub">Uncover patterns &amp; insights hidden in your conversations</div>
</div>
""", unsafe_allow_html=True)

if uploaded_file is None:
    st.markdown("""
    <div class="upload-prompt">
      <div class="upload-prompt-icon">📂</div>
      <div class="upload-prompt-text">Upload a WhatsApp export to get started</div>
      <p style="color:#334155; font-size:0.85rem; margin-top:0.5rem;">
        Export via WhatsApp → Chat → More → Export Chat (without media)
      </p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# Raw data preview (collapsed by default)
with st.expander("🗒️  Raw data preview"):
    st.dataframe(df, use_container_width=True)

# Only run after button click
if uploaded_file is not None and 'analyze_btn' in dir() and analyze_btn:

    # ── Stats ──────────────────────────────────────────────────────────────
    num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

    st.markdown("<div class='section-header'>📈 Overview</div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    cards = [
        (c1, "Total Messages",  num_messages, "blue"),
        (c2, "Total Words",     words,         "purple"),
        (c3, "Media Shared",    num_media_messages, "teal"),
        (c4, "Links Shared",    num_links,     "rose"),
    ]
    for col, label, value, accent in cards:
        with col:
            st.markdown(f"""
            <div class="metric-card metric-accent metric-accent-{accent}">
              <div class="metric-label">{label}</div>
              <div class="metric-value">{value:,}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Most busy users ────────────────────────────────────────────────────
    if selected_user == 'Overall':
        st.markdown("<div class='section-header'>🏆 Most Active Participants</div>", unsafe_allow_html=True)

        x, new_df = helper.most_busy_user(df)
        col_chart, col_table = st.columns([3, 2], gap="large")

        with col_chart:
            fig, ax = plt.subplots(figsize=(7, 4))
            fig.patch.set_facecolor('#13161f')
            ax.set_facecolor('#13161f')

            colors = ['#4f8ef7', '#7c3aed', '#14b8a6', '#f43f5e', '#f59e0b',
                      '#10b981', '#6366f1', '#ec4899']
            bar_colors = [colors[i % len(colors)] for i in range(len(x))]

            bars = ax.bar(x.index, x.values, color=bar_colors,
                          width=0.6, zorder=3, edgecolor='none')

            ax.spines[:].set_visible(False)
            ax.yaxis.grid(True, linestyle='--', alpha=0.3, zorder=0)
            ax.set_xticklabels(x.index, rotation=40, ha='right', fontsize=9)
            ax.set_ylabel("Messages", fontsize=9, color='#64748b')

            for bar in bars:
                h = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2, h + max(x.values)*0.01,
                        f'{int(h):,}', ha='center', va='bottom',
                        fontsize=8, color='#94a3b8')

            plt.tight_layout(pad=0.5)
            st.pyplot(fig)

        with col_table:
            st.markdown("<p style='color:#64748b; font-size:0.8rem; font-weight:500; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.5rem;'>Breakdown</p>", unsafe_allow_html=True)
            st.dataframe(new_df, use_container_width=True, height=260)

    # ── Word cloud ─────────────────────────────────────────────────────────
    st.markdown("<div class='section-header'>☁️ Word Cloud</div>", unsafe_allow_html=True)

    df_wc = helper.create_word_cloud(selected_user, df)
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor('#13161f')
    ax.set_facecolor('#13161f')
    ax.imshow(df_wc, interpolation='bilinear')
    ax.axis('off')
    plt.tight_layout(pad=0)
    st.pyplot(fig)