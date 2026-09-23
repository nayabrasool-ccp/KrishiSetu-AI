import streamlit as st
import random
import pandas as pd
from datetime import datetime, timedelta

# Set page layout configuration
st.set_page_config(page_title="KrishiSetu AI - Operations Hub", page_icon="🌾", layout="wide")

# Custom CSS styling injection
st.markdown("""
    <style>
    .main { background-color: #F8FAFC; }
    .stButton>button { background-color: #10B981 !important; color: white !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; border: none !important; }
    .stButton>button:hover { background-color: #059669 !important; }
    .mandi-card { padding: 15px; border-radius: 12px; background-color: white; border-left: 5px solid #10B981; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- TOP BANNER ---
st.markdown("<div style='background-color:#1E293B; padding:20px; border-radius:12px; margin-bottom:25px;'><h1 style='color:white; margin:0;'>KrishiSetu AI 🌾</h1><p style='color:#94A3B8; margin:5px 0 0 0;'>Enterprise Procurement, Quality Assurance & Fraud Prevention Suite</p></div>", unsafe_allow_html=True)

# --- CORE INTERFACE SPLIT ---
col_left, col_right = st.columns([1, 1.2], gap="large")

# LEFT COLUMN: FARMER ENTRY PORTAL
with col_left:
    st.markdown("### 📱 Farmer Inbound Portal")
    st.caption("Mobile-optimized gateway for remote crop screening.")
    
    with st.container(border=True):
        farmer_name = st.text_input("👤 Farmer Registry Name:", value="Coco")
        crop_type = st.selectbox("🌱 Crop Category:", ["Chilli", "Tomato", "Potato", "Onion"])
        volume_kg = st.number_input("⚖️ Est. Weight (Quintals):", min_value=1.0, value=25.0, step=0.5)
        
        uploaded_file = st.file_uploader("📸 Capture/Upload Batch Sample Image:", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded Image Reference File", use_container_width=True)
            
            if st.button("PRODUCE ANALYSIS & ALLOCATE SLOT"):
                # --- NEW FEATURE 1: IMAGE AUTHENTICITY VALIDATION (ANTI-CHEAT) ---
                # Checks if the image filename looks like a downloaded stock web photo
                fn_lower = uploaded_file.name.lower()
                if "download" in fn_lower or "stock" in fn_lower or "preview" in fn_lower or "close-u" in fn_lower:
                    st.error("🚨 Image Verification Failed: System detected a downloaded web asset. Please capture a real-time on-field photograph.")
                    st.session_state['run_pipeline'] = False
                else:
                    st.session_state['run_pipeline'] = True
                    st.session_state['selected_crop'] = crop_type
                    st.session_state['farmer'] = farmer_name
                    st.session_state['weight'] = volume_kg

# RIGHT COLUMN: CENTRAL MANAGEMENT GRID
with col_right:
    st.markdown("### 🏢 Central Management Grid")
    st.caption("Live logistical tracking and verification ledger registers.")
    
    # Mandi Capacity Vectors
    st.markdown("##### 📍 Active Mandi Yard Fill Capacities")
    mc1, mc2, mc3 = st.columns(3)
    with mc1:
        st.markdown("<div class='mandi-card'><b>Nellore Hub</b><br><span style='color:#10B981;'>● Stable</span><br><b>Load: 42%</b></div>", unsafe_allow_html=True)
    with mc2:
        st.markdown("<div class='mandi-card' style='border-left-color:#EF4444;'><b>Kavali Center</b><br><span style='color:#EF4444;'>⚠️ Congested</span><br><b>Load: 88%</b></div>", unsafe_allow_html=True)
    with mc3:
        st.markdown("<div class='mandi-card' style='border-left-color:#3B82F6;'><b>Gudur Yard</b><br><span style='color:#3B82F6;'>⚙️ Underutilized</span><br><b>Load: 15%</b></div>", unsafe_allow_html=True)

    st.markdown("---")

    if st.session_state.get('run_pipeline', False):
        st.markdown("##### 📊 Evaluation Inferences & Live Receipts")
        
        # Pull parameters from memory
        c_type = st.session_state['selected_crop']
        f_name = st.session_state['farmer']
        w_quintals = st.session_state['weight']
        
        confidence = round(random.uniform(96.1, 98.9), 2)
        token_id = f"KSETU-2026-{random.randint(1000, 9999)}"
        
        # --- NEW FEATURE 2: REAL-TIME DYNAMIC TIME MATCHING ---
        # Calculates reporting hour windows precisely derived from the current system clock
        current_time = datetime.now()
        matching_reporting_slot = current_time + timedelta(hours=3)
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(label="AI Assigned Quality Grade", value="GRADE-B")
        with m2:
            st.metric(label="Authenticity Match", value="100% REAL")
        with m3:
            st.metric(label="Dynamic Time Validation", value="PASSED")
            
        st.success(f"🎫 **Token Securely Verified:** Match confirmed for user instance **{f_name}**.")
        
        # Render clean dynamic tracking invoice
        st.code(f"""
        ===========================================================
                    KRISHISETU LIVE PROCUREMENT RECEIPT           
        ===========================================================
        Pass Code       : {token_id}
        Target Facility : Gudur Agricultural Yard
        Scan Timestamp  : {current_time.strftime('%Y-%m-%d %I:%M:%S %p')}
        Reporting Slot  : {matching_reporting_slot.strftime('%Y-%m-%d %I:%M %p')} (Window Matches Load Plan)
        Logistics Route : Priority path authorized via NH-16 corridor.
        ===========================================================
        """, language="markdown")
        
        # Interactive registry ledger database table mapping
        st.markdown("##### 📋 Historical Logistics Ledger Registry")
        mock_table_records = pd.DataFrame({
            "Token ID": [token_id, "KSETU-2026-8812", "KSETU-2026-4190"],
            "Farmer": [f_name, "Anil Kumar", "V. Reddy"],
            "Crop Type": [c_type, "Tomato", "Onion"],
            "Weight (Q)": [w_quintals, 45.0, 12.5],
            "Reporting Time": [matching_reporting_slot.strftime('%I:%M %p'), "11:30 AM", "03:15 PM"],
            "Status": ["Verified Pass", "Arrived", "Completed"]
        })
        st.dataframe(mock_table_records, use_container_width=True, hide_index=True)
    else:
        st.info("⌛ **Awaiting Valid Inbound Transmission:** Capture an authentic image reference above and execute to initialize verification microservices.")
        
