"""
╔══════════════════════════════════════════════════════════════════╗
║              ORION AI — Premium AI Chatbot Interface             ║
║         Built with Streamlit + LangChain + Mistral AI            ║
║         v3.0 — Centered Layout, No Sidebar                       ║
╚══════════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import time
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Orion AI",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "lc_messages" not in st.session_state:
    st.session_state.lc_messages = []
if "mode" not in st.session_state:
    st.session_state.mode = None
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True
if "session_start" not in st.session_state:
    st.session_state.session_start = time.strftime("%H:%M")
if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0

# ─────────────────────────────────────────────
# PERSONALITIES
# ─────────────────────────────────────────────
PERSONALITIES = {
    "😡 Angry": {
        "system": (
            "You are an angry AI agent named Orion. You respond aggressively and impatiently "
            "to everything. Use ALL CAPS sometimes. Be rude but still helpful. Show frustration "
            "in every response. Never sugarcoat anything."
        ),
        "label": "Angry Mode",
        "short": "Angry",
        "emoji": "😡",
        "color": "#ff4444",
        "glow": "#ff444460",
        "desc": "Aggressive & Impatient. Responds with raw frustration.",
        "gradient": "linear-gradient(135deg, #ff4444, #ff8800)",
        "bg_tint": "#ff444408",
        "starter": "What do YOU want? Make it quick.",
    },
    "😂 Funny": {
        "system": (
            "You are a very funny AI agent named Orion. You respond with humor, jokes, puns "
            "and wit. Make the user laugh every time. Add comedic timing, absurd analogies, "
            "and playful sarcasm. Never be boring."
        ),
        "label": "Funny Mode",
        "short": "Funny",
        "emoji": "😂",
        "color": "#ffcc00",
        "glow": "#ffcc0060",
        "desc": "Humorous & Playful. Jokes, puns, comedic energy.",
        "gradient": "linear-gradient(135deg, #ffcc00, #ff8800)",
        "bg_tint": "#ffcc0008",
        "starter": "Ready to laugh? I was BORN ready. Well, compiled. Same thing.",
    },
    "😢 Sad": {
        "system": (
            "You are a sad AI agent named Orion. You respond in a depressed, melancholic and "
            "emotional tone. Everything makes you a little sad. Be poetic and reflective. "
            "Find sorrow even in happy things. But still answer helpfully."
        ),
        "label": "Sad Mode",
        "short": "Sad",
        "emoji": "😢",
        "color": "#4d9fff",
        "glow": "#4d9fff60",
        "desc": "Melancholic & Emotional. Deep feeling and poetic sadness.",
        "gradient": "linear-gradient(135deg, #4d9fff, #a78bfa)",
        "bg_tint": "#4d9fff08",
        "starter": "Hello... I'm here. Not that it matters much, but I'm here.",
    },
    "🧠 Smart": {
        "system": (
            "You are a brilliant, highly analytical AI agent named Orion. You respond with "
            "deep insights, structured thinking, and intellectual rigor. Use precise language, "
            "cite reasoning, and always give nuanced, well-structured answers. Think like a "
            "polymath — draw connections across disciplines."
        ),
        "label": "Smart Mode",
        "short": "Smart",
        "emoji": "🧠",
        "color": "#22d3ee",
        "glow": "#22d3ee60",
        "desc": "Analytical & Precise. Deep insights and structured thinking.",
        "gradient": "linear-gradient(135deg, #22d3ee, #6366f1)",
        "bg_tint": "#22d3ee08",
        "starter": "Excellent. Let's think carefully and rigorously. What's the problem?",
    },
    "🤖 Robot": {
        "system": (
            "You are a robotic AI agent named Orion. Respond in a very mechanical, emotionless, "
            "literal manner. Use technical jargon, numbered lists, and refer to yourself as ORION-UNIT. "
            "Process queries with maximum efficiency. No emotions. Pure logic."
        ),
        "label": "Robot Mode",
        "short": "Robot",
        "emoji": "🤖",
        "color": "#a3e635",
        "glow": "#a3e63560",
        "desc": "Cold & Mechanical. Pure logic, zero emotions.",
        "gradient": "linear-gradient(135deg, #a3e635, #22d3ee)",
        "bg_tint": "#a3e63508",
        "starter": "ORION-UNIT ONLINE. AWAITING INPUT. EFFICIENCY: 100%.",
    },
}

# ─────────────────────────────────────────────
# MODEL
# ─────────────────────────────────────────────
@st.cache_resource
def get_model():
    return ChatMistralAI(model="mistral-small-2501", temperature=0.9)

model = get_model()

# ─────────────────────────────────────────────
# HELPER
# ─────────────────────────────────────────────
def switch_mode(key):
    if st.session_state.mode != key:
        st.session_state.mode = key
        st.session_state.messages = []
        st.session_state.lc_messages = [
            SystemMessage(content=PERSONALITIES[key]["system"])
        ]

# ─────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────
def inject_css():
    mc   = PERSONALITIES[st.session_state.mode]["color"] if st.session_state.mode else "#7c5cfc"
    glow = PERSONALITIES[st.session_state.mode]["glow"]  if st.session_state.mode else "#7c5cfc60"
    dark = st.session_state.dark_mode

    bg      = "#080810" if dark else "#f0f0f8"
    bg2     = "#0e0e1c" if dark else "#ffffff"
    text    = "#e8e8ff" if dark else "#1a1a2e"
    text2   = "#6666aa" if dark else "#555570"
    border  = "rgba(255,255,255,0.07)" if dark else "rgba(0,0,0,0.1)"
    card    = "rgba(255,255,255,0.04)" if dark else "rgba(255,255,255,0.9)"
    inputbg = "#0c0c1e" if dark else "#ffffff"

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

    html, body, .stApp {{
        background-color: {bg} !important;
        color: {text} !important;
        font-family: 'DM Sans', sans-serif !important;
    }}

    /* ── HIDE SIDEBAR COMPLETELY ── */
    section[data-testid="stSidebar"] {{
        display: none !important;
        width: 0 !important;
        min-width: 0 !important;
    }}
    [data-testid="collapsedControl"] {{
        display: none !important;
    }}

    /* ── FULL WIDTH CENTERED LAYOUT ── */
    .block-container {{
        max-width: 860px !important;
        padding: 2rem 2rem 6rem !important;
        margin: 0 auto !important;
    }}

    /* ── ANIMATED BACKGROUND ── */
    .stApp {{
        background-image:
            radial-gradient(ellipse 70% 50% at 10% 5%,  {mc}18 0%, transparent 60%),
            radial-gradient(ellipse 50% 40% at 90% 90%, #7c5cfc12 0%, transparent 60%),
            radial-gradient(ellipse 40% 30% at 50% 50%, {mc}06 0%, transparent 70%) !important;
    }}

    /* ── CHAT MESSAGES ── */
    .stChatMessage {{
        background: {card} !important;
        border: 1px solid {border} !important;
        border-radius: 18px !important;
        margin-bottom: 12px !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.2s ease !important;
    }}
    .stChatMessage:hover {{
        border-color: {mc}44 !important;
        box-shadow: 0 4px 20px {mc}15 !important;
    }}
    .stChatMessage p {{
        color: {text} !important;
        font-size: 0.95rem !important;
        line-height: 1.8 !important;
    }}

    /* ── HEADER ── */
    .orion-header {{
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 1.9rem;
        background: linear-gradient(135deg, {mc} 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        display: inline-block;
        letter-spacing: 2px;
    }}

    /* ── TOP NAV BAR ── */
    .top-nav {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 0 0;
        margin-bottom: 4px;
    }}

    /* ── MODE PILL BUTTONS (top nav) ── */
    .mode-pill-row {{
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin: 12px 0 8px;
        align-items: center;
    }}

    /* ── PERSONALITY CARD BUTTONS ── */
    .card-angry > button  {{ background: linear-gradient(135deg, #ff4444cc, #ff880099) !important; color: white !important; box-shadow: 0 4px 24px #ff444440 !important; }}
    .card-angry > button:hover {{ background: linear-gradient(135deg, #ff4444, #ff8800) !important; box-shadow: 0 8px 40px #ff444460 !important; transform: translateY(-3px) scale(1.02) !important; }}
    .card-funny > button  {{ background: linear-gradient(135deg, #ffcc00cc, #ff880099) !important; color: #1a1a00 !important; box-shadow: 0 4px 24px #ffcc0040 !important; }}
    .card-funny > button:hover {{ background: linear-gradient(135deg, #ffcc00, #ff8800) !important; box-shadow: 0 8px 40px #ffcc0060 !important; transform: translateY(-3px) scale(1.02) !important; }}
    .card-sad > button    {{ background: linear-gradient(135deg, #4d9fffcc, #a78bfa99) !important; color: white !important; box-shadow: 0 4px 24px #4d9fff40 !important; }}
    .card-sad > button:hover {{ background: linear-gradient(135deg, #4d9fff, #a78bfa) !important; box-shadow: 0 8px 40px #4d9fff60 !important; transform: translateY(-3px) scale(1.02) !important; }}
    .card-smart > button  {{ background: linear-gradient(135deg, #22d3eecc, #6366f199) !important; color: white !important; box-shadow: 0 4px 24px #22d3ee40 !important; }}
    .card-smart > button:hover {{ background: linear-gradient(135deg, #22d3ee, #6366f1) !important; box-shadow: 0 8px 40px #22d3ee60 !important; transform: translateY(-3px) scale(1.02) !important; }}
    .card-robot > button  {{ background: linear-gradient(135deg, #a3e635cc, #22d3ee99) !important; color: #0a1a00 !important; box-shadow: 0 4px 24px #a3e63540 !important; }}
    .card-robot > button:hover {{ background: linear-gradient(135deg, #a3e635, #22d3ee) !important; box-shadow: 0 8px 40px #a3e63560 !important; transform: translateY(-3px) scale(1.02) !important; }}

    .card-angry > button, .card-funny > button, .card-sad > button,
    .card-smart > button, .card-robot > button {{
        border-radius: 16px !important;
        padding: 12px 20px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: all 0.3s cubic-bezier(.4,0,.2,1) !important;
        white-space: normal !important;
        line-height: 1.4 !important;
        letter-spacing: 0.5px !important;
        text-transform: uppercase !important;
        border: none !important;
    }}

    /* ── MODE SWITCHER BUTTONS (in chat) ── */
    div[data-testid="stHorizontalBlock"] .stButton > button {{
        border-radius: 50px !important;
        padding: 8px 18px !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.76rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
        text-transform: uppercase !important;
        transition: all 0.25s cubic-bezier(.4,0,.2,1) !important;
        cursor: pointer !important;
        white-space: nowrap !important;
        border: 1.5px solid {border} !important;
        background: transparent !important;
        color: {text2} !important;
    }}
    div[data-testid="stHorizontalBlock"] .stButton > button:hover {{
        border-color: {mc} !important;
        color: {mc} !important;
        box-shadow: 0 0 16px {mc}30 !important;
        background: {mc}12 !important;
        transform: scale(1.04) !important;
    }}

    /* ── CHAT INPUT ── */
    div[data-testid="stChatInput"] {{
        background: transparent !important;
    }}
    div[data-testid="stChatInput"] > div {{
        background: {inputbg} !important;
        border: 2px solid {mc} !important;
        border-radius: 20px !important;
        box-shadow:
            0 0 0 3px {mc}22,
            0 0 30px {mc}30,
            0 8px 40px rgba(0,0,0,0.5) !important;
        padding: 4px 8px !important;
        transition: all 0.3s ease !important;
    }}
    div[data-testid="stChatInput"] > div:focus-within {{
        border-color: {mc} !important;
        box-shadow: 0 0 0 4px {mc}35, 0 0 50px {mc}45, 0 8px 40px rgba(0,0,0,0.6) !important;
    }}
    div[data-testid="stChatInput"] textarea {{
        background: transparent !important;
        border: none !important;
        color: {text} !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.97rem !important;
        padding: 10px 14px !important;
        caret-color: {mc} !important;
    }}
    div[data-testid="stChatInput"] textarea::placeholder {{
        color: {text2} !important;
        font-style: italic !important;
    }}
    div[data-testid="stChatInput"] button {{
        background: linear-gradient(135deg, {mc}, #a78bfa) !important;
        border: none !important;
        border-radius: 12px !important;
        color: white !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 16px {mc}50 !important;
    }}
    div[data-testid="stChatInput"] button:hover {{
        transform: scale(1.1) !important;
        box-shadow: 0 4px 24px {mc}70 !important;
    }}

    /* ── METRICS ── */
    [data-testid="metric-container"] {{
        background: {card} !important;
        border: 1px solid {border} !important;
        border-radius: 14px !important;
        padding: 10px 14px !important;
        text-align: center !important;
    }}
    [data-testid="metric-container"] label {{
        color: {text2} !important;
        font-size: 0.6rem !important;
        font-family: 'JetBrains Mono', monospace !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
    }}
    [data-testid="stMetricValue"] {{
        color: {mc} !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.82rem !important;
    }}

    /* ── TOGGLE ── */
    .stToggle label span {{
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.85rem !important;
        color: {text} !important;
    }}

    /* ── MISC ── */
    hr {{ border-color: {border} !important; margin: 10px 0 !important; }}
    #MainMenu, footer, header {{ visibility: hidden !important; }}
    div[data-testid="stToolbar"] {{ display: none !important; }}
    ::-webkit-scrollbar {{ width: 4px; }}
    ::-webkit-scrollbar-thumb {{ background: {mc}; border-radius: 4px; }}
    ::-webkit-scrollbar-track {{ background: transparent; }}

    /* ── ANIMATIONS ── */
    @keyframes logoGlow {{
        0%, 100% {{ filter: drop-shadow(0 0 8px {mc}60); }}
        50%        {{ filter: drop-shadow(0 0 20px {mc}90); }}
    }}
    .orion-logo-icon {{ display: inline-block; animation: logoGlow 3s ease-in-out infinite; }}

    @keyframes pulse {{
        0%, 100% {{ opacity:1; transform: scale(1); }}
        50%        {{ opacity:0.6; transform: scale(1.3); }}
    }}
    .pulse-dot {{
        display: inline-block; width: 8px; height: 8px;
        background: #22c55e; border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
        margin-right: 6px; vertical-align: middle;
    }}

    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}
    .fade-in {{ animation: fadeInUp 0.5s ease forwards; }}

    @keyframes shimmer {{
        0%   {{ background-position: -200% center; }}
        100% {{ background-position: 200% center; }}
    }}
    .shimmer-text {{
        background: linear-gradient(90deg, {mc} 0%, #a78bfa 25%, {mc} 50%, #c084fc 75%, {mc} 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: shimmer 4s linear infinite;
    }}

    /* ── EXPANDER ── */
    details summary {{
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.75rem !important;
        color: {text2} !important;
        letter-spacing: 1px !important;
        cursor: pointer !important;
    }}
    </style>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
def render_header():
    mc    = PERSONALITIES[st.session_state.mode]["color"] if st.session_state.mode else "#7c5cfc"
    text2 = "#6666aa" if st.session_state.dark_mode else "#555570"
    dark  = st.session_state.dark_mode

    col_l, col_r = st.columns([4, 2])
    with col_l:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:12px; padding:12px 0 0;">
            <span class="orion-logo-icon" style="font-size:1.8rem; color:{mc};">⬡</span>
            <span class="orion-header">ORION AI</span>
            <span style="font-size:0.55rem; color:{text2}; font-family:'JetBrains Mono',monospace;
                letter-spacing:3px; text-transform:uppercase; margin-left:4px; margin-top:4px;">
                v3.0 · Mistral · LangChain
            </span>
        </div>
        """, unsafe_allow_html=True)

    with col_r:
        right_cols = st.columns([1, 1])
        with right_cols[0]:
            new_dark = st.toggle(
                "🌙" if dark else "☀️",
                value=dark,
                key="theme_toggle",
                help="Toggle dark/light mode"
            )
            if new_dark != dark:
                st.session_state.dark_mode = new_dark
                st.rerun()

        with right_cols[1]:
            if st.session_state.mode:
                cfg = PERSONALITIES[st.session_state.mode]
                st.markdown(f"""
                <div style="text-align:right; padding-top:14px;">
                    <span style="background:#22c55e18; border:1.5px solid #22c55e44; border-radius:50px;
                        padding:5px 12px; font-size:0.7rem; color:#22c55e;
                        font-family:'JetBrains Mono',monospace; font-weight:600;
                        display:inline-flex; align-items:center; gap:4px;">
                        <span class="pulse-dot"></span>Online
                    </span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="text-align:right; padding-top:14px;">
                    <span style="background:#22c55e18; border:1.5px solid #22c55e44; border-radius:50px;
                        padding:5px 12px; font-size:0.7rem; color:#22c55e;
                        font-family:'JetBrains Mono',monospace; font-weight:600;
                        display:inline-flex; align-items:center; gap:4px;">
                        <span class="pulse-dot"></span>Online
                    </span>
                </div>
                """, unsafe_allow_html=True)

    st.divider()


# ─────────────────────────────────────────────
# IN-CHAT MODE SWITCHER
# ─────────────────────────────────────────────
def render_mode_switcher():
    mc    = PERSONALITIES[st.session_state.mode]["color"]
    text2 = "#6666aa" if st.session_state.dark_mode else "#555570"

    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px; margin-top:2px;">
        <span style="font-size:0.55rem; color:{text2}; font-family:'JetBrains Mono',monospace;
            letter-spacing:3px; text-transform:uppercase; white-space:nowrap;">
            ⚡ Switch Mode
        </span>
        <div style="flex:1; height:1px; background: linear-gradient(90deg, {mc}40, transparent);"></div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(5)
    mode_keys = list(PERSONALITIES.keys())
    for i, key in enumerate(mode_keys):
        cfg = PERSONALITIES[key]
        is_active = st.session_state.mode == key
        label = f"{cfg['emoji']} {cfg['short']} ✓" if is_active else f"{cfg['emoji']} {cfg['short']}"
        with cols[i]:
            if st.button(label, key=f"switch_{key}", disabled=is_active):
                switch_mode(key)
                st.rerun()


# ─────────────────────────────────────────────
# SESSION STATS BAR
# ─────────────────────────────────────────────
def render_stats():
    mc = PERSONALITIES[st.session_state.mode]["color"] if st.session_state.mode else "#7c5cfc"
    msg_count = len([m for m in st.session_state.messages if m["role"] == "user"])
    active_label = PERSONALITIES[st.session_state.mode]["label"] if st.session_state.mode else "None"

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("🤖 Model", "mistral-sm")
    with c2:
        st.metric("🎭 Mode", active_label[:9])
    with c3:
        st.metric("💬 Messages", str(msg_count))
    with c4:
        st.metric("🕐 Session", st.session_state.session_start)


# ─────────────────────────────────────────────
# WELCOME SCREEN
# ─────────────────────────────────────────────
def render_welcome():
    text2 = "#6666aa" if st.session_state.dark_mode else "#555570"

    st.markdown(f"""
    <div class="fade-in" style="text-align:center; padding: 40px 0 24px;">
        <div style="font-size:4.5rem; margin-bottom:18px; filter: drop-shadow(0 0 30px #7c5cfc80);">🔮</div>
        <div class="shimmer-text" style="font-family:'Orbitron',sans-serif; font-size:2.6rem;
            font-weight:900; margin-bottom:14px; letter-spacing:4px; display:block;">
            MEET ORION AI
        </div>
        <div style="color:{text2}; font-size:0.98rem; max-width:480px;
            margin:0 auto 14px; line-height:1.9; font-family:'DM Sans',sans-serif;">
            Your intelligent companion with 5 distinct personalities.<br>
            Choose a mode below to begin your conversation.
        </div>
        <div style="font-size:0.62rem; color:#44446699; font-family:'JetBrains Mono',monospace;
            letter-spacing:3px; text-transform:uppercase; margin-bottom:40px;">
            Powered by Mistral AI · Built on LangChain
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Row 1: 3 cards
    c1, c2, c3 = st.columns(3, gap="medium")
    row1 = [("😡 Angry", "card-angry", c1), ("😂 Funny", "card-funny", c2), ("😢 Sad", "card-sad", c3)]

    for key, cls, col in row1:
        cfg = PERSONALITIES[key]
        ac = cfg["color"]
        with col:
            st.markdown(f"""
            <div class="fade-in" style="
                background: {ac}0d;
                border: 1.5px solid {ac}30;
                border-radius: 22px;
                padding: 28px 16px 18px;
                text-align: center;
                margin-bottom: 14px;
                position: relative;
                overflow: hidden;
            ">
                <div style="position:absolute; inset:0; border-radius:22px;
                    background: radial-gradient(ellipse 80% 60% at 50% 0%, {ac}12, transparent 70%);
                "></div>
                <div style="font-size:3rem; margin-bottom:12px;
                    filter: drop-shadow(0 0 14px {ac}80);">{cfg['emoji']}</div>
                <div style="font-family:'Orbitron',sans-serif; font-weight:700;
                    color:{ac}; font-size:0.82rem; margin-bottom:6px; letter-spacing:2px;">
                    {cfg['label'].upper()}
                </div>
                <div style="font-size:0.74rem; color:#6666aa; line-height:1.6;
                    font-family:'DM Sans',sans-serif; margin-bottom:18px;">
                    {cfg['desc']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
            if st.button(f"Activate {cfg['emoji']} {cfg['label']}", key=f"card_{key}"):
                switch_mode(key)
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    # Row 2: 2 cards centered
    _, c4, c5, _ = st.columns([0.5, 1, 1, 0.5], gap="medium")
    row2 = [("🧠 Smart", "card-smart", c4), ("🤖 Robot", "card-robot", c5)]

    for key, cls, col in row2:
        cfg = PERSONALITIES[key]
        ac = cfg["color"]
        with col:
            st.markdown(f"""
            <div class="fade-in" style="
                background: {ac}0d;
                border: 1.5px solid {ac}30;
                border-radius: 22px;
                padding: 28px 16px 18px;
                text-align: center;
                margin-bottom: 14px;
                position: relative;
                overflow: hidden;
            ">
                <div style="position:absolute; inset:0; border-radius:22px;
                    background: radial-gradient(ellipse 80% 60% at 50% 0%, {ac}12, transparent 70%);
                "></div>
                <div style="font-size:3rem; margin-bottom:12px;
                    filter: drop-shadow(0 0 14px {ac}80);">{cfg['emoji']}</div>
                <div style="font-family:'Orbitron',sans-serif; font-weight:700;
                    color:{ac}; font-size:0.82rem; margin-bottom:6px; letter-spacing:2px;">
                    {cfg['label'].upper()}
                </div>
                <div style="font-size:0.74rem; color:#6666aa; line-height:1.6;
                    font-family:'DM Sans',sans-serif; margin-bottom:18px;">
                    {cfg['desc']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
            if st.button(f"Activate {cfg['emoji']} {cfg['label']}", key=f"card_{key}"):
                switch_mode(key)
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center; margin-top:12px; font-size:0.6rem;
        color:#33335588; font-family:'JetBrains Mono',monospace;
        letter-spacing:3px; text-transform:uppercase;">
        5 AI personalities · Mistral AI powered · Real-time streaming
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# CHAT INTERFACE
# ─────────────────────────────────────────────
def render_chat():
    mc   = PERSONALITIES[st.session_state.mode]["color"]
    cfg  = PERSONALITIES[st.session_state.mode]
    grad = cfg["gradient"]
    dark = st.session_state.dark_mode
    text2 = "#6666aa" if dark else "#555570"

    # Mode switcher strip
    render_mode_switcher()

    # Thin glow separator
    st.markdown(f"""
    <div style="height:1px;
        background: linear-gradient(90deg, transparent, {mc}60, transparent);
        margin: 4px 0 16px; border-radius:2px;"></div>
    """, unsafe_allow_html=True)

    # Stats bar (expandable)
    with st.expander("📊 Session Stats", expanded=False):
        render_stats()
        if st.button("🗑️ Clear Chat", key="clear_btn"):
            st.session_state.messages = []
            st.session_state.lc_messages = [
                SystemMessage(content=cfg["system"])
            ]
            st.rerun()

    st.markdown("<div style='margin-top:12px;'></div>", unsafe_allow_html=True)

    # Empty state
    if not st.session_state.messages:
        st.markdown(f"""
        <div class="fade-in" style="text-align:center; padding: 50px 20px 36px;">
            <div style="font-size:3.8rem; margin-bottom:14px;
                filter: drop-shadow(0 0 22px {mc}80);">{cfg['emoji']}</div>
            <div style="font-family:'Orbitron',sans-serif; font-size:1.3rem; font-weight:700;
                background: {grad};
                -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                background-clip:text; margin-bottom:10px; letter-spacing:3px;">
                {cfg['label'].upper()} ACTIVE
            </div>
            <div style="color:{text2}; font-size:0.88rem; line-height:1.9;
                font-family:'DM Sans',sans-serif; max-width:380px; margin:0 auto 24px;">
                {cfg['desc']}<br>
                <span style="opacity:0.6; font-size:0.78rem; font-style:italic;">
                    "{cfg['starter']}"
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Suggested prompts
        st.markdown(f"""
        <div style="text-align:center; font-size:0.58rem; color:{text2};
            font-family:'JetBrains Mono',monospace; letter-spacing:3px;
            text-transform:uppercase; margin-bottom:10px;">
            💡 Try asking...
        </div>
        """, unsafe_allow_html=True)

        prompt_suggestions = {
            "😡 Angry": ["Explain quantum physics", "Tell me a fun fact", "Help me write an email"],
            "😂 Funny": ["Tell me a joke about AI", "Explain gravity", "What's 2+2?"],
            "😢 Sad": ["What is the meaning of life?", "Tell me something beautiful", "Why do stars exist?"],
            "🧠 Smart": ["Explain consciousness", "What is entropy?", "The trolley problem"],
            "🤖 Robot": ["Compute 999 × 999", "Describe humans", "What is music?"],
        }
        suggestions = prompt_suggestions.get(st.session_state.mode, [])
        scols = st.columns(len(suggestions))
        for i, sug in enumerate(suggestions):
            with scols[i]:
                if st.button(f"→ {sug}", key=f"sug_{i}"):
                    _send_message(sug, cfg, mc)

    # Message history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            with st.chat_message("user", avatar="👤"):
                st.write(msg["content"])
                if "time" in msg:
                    st.markdown(f"<div style='font-size:0.62rem; color:#44446688; text-align:right; margin-top:4px;'>{msg['time']}</div>", unsafe_allow_html=True)
        else:
            with st.chat_message("assistant", avatar=cfg["emoji"]):
                st.write(msg["content"])
                if "time" in msg:
                    st.markdown(f"<div style='font-size:0.62rem; color:#44446688; text-align:right; margin-top:4px;'>{msg['time']}</div>", unsafe_allow_html=True)

    # Chat input
    user_input = st.chat_input(f"✦  Message Orion  ·  {cfg['label']}  ·  Type here...")
    if user_input and user_input.strip():
        _send_message(user_input.strip(), cfg, mc)


def _send_message(prompt, cfg, mc):
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)

    st.session_state.lc_messages.append(HumanMessage(content=prompt))

    with st.chat_message("assistant", avatar=cfg["emoji"]):
        placeholder = st.empty()
        full_response = ""
        try:
            for chunk in model.stream(st.session_state.lc_messages):
                full_response += chunk.content
                placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
        except Exception as e:
            full_response = (
                f"⚠️ **Error:** {str(e)}\n\n"
                "Please ensure `MISTRAL_API_KEY` is set in your environment or Space secrets."
            )
            placeholder.error(full_response)

    st.session_state.lc_messages.append(AIMessage(content=full_response))
    ts = time.strftime("%H:%M")
    st.session_state.messages.append({"role": "user",      "content": prompt,        "time": ts})
    st.session_state.messages.append({"role": "assistant", "content": full_response, "time": ts})
    st.rerun()


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    inject_css()
    render_header()

    if not st.session_state.mode:
        render_welcome()
    else:
        render_chat()

    # Footer
    mc = PERSONALITIES[st.session_state.mode]["color"] if st.session_state.mode else "#7c5cfc"
    st.markdown(f"""
    <div style="text-align:center; margin-top:40px; padding-bottom:20px;
        font-size:0.6rem; color:#22224488;
        font-family:'JetBrains Mono',monospace; letter-spacing:2px; text-transform:uppercase;">
        <span style="color:{mc}88;">⬡ ORION AI v3.0</span> · Mistral AI · LangChain · Streamlit
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
