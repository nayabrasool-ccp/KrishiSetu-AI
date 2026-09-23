import streamlit as st
import random
import pandas as pd
from datetime import datetime, timedelta

# Set page layout to wide for a dual-column enterprise UI dashboard
st.set_page_config(page_title="KrishiSetu AI - Operations Hub", page_icon="🌾", layout="wide")

# Custom CSS styling injection to create a modern corporate glassmorphism layout
st.markdown("""
    <style>
    .main { background-color: #F8FAFC; }
    .stButton>button { background-color: #10B981 !important; color: white !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; border: none !important; }
    .stButton>button:hover { background-color: #059669 !important; }
    .mandi-card { padding: 15px; border-radius: 12px; background-color: white; border-left: 5px solid #10B981; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); margin-bottom: 10px; }
    .metric-box { text-align: center; padding: 15px; background: white; border-radius: 12px; box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1); }
    </style>
""", unsafe_allow_index=True)

# --- TOP BANNER ---
st.markdown("<div style='background-color:#1E293B; padding:20px; border-radius:12px; margin-bottom:25px;'><h1 style='color:white; margin:0;'>KrishiSetu AI 🌾</h1><p style='color:#94A3B8; margin:5px 0 0 0;'>Unified Agricultural Procurement, Quality Assurance & Transit Optimization Suite</p></div>", unsafe_allow_html=True)

# --- CORE INTERFACE SPLIT (Dual Column Layout) ---
col_left, col_right = st.columns([1, 1.2], gap="large")

# =========================================================================
# LEFT COLUMN: FARMER ENTRY PORTAL (FRONTEND INTERFACE)
# =========================================================================
with col_left:
    st.markdown("### 📱 Farmer Inbound Portal")
    st.caption("Mobile-optimized gateway for remote crop screening and scheduling registrations.")
    
    with st.container(border=True):
        farmer_name = st.text_input("👤 Farmer Registry Name:", value="Coco")
        
        c1, c2 = st.columns(2)
        with c1:
            crop_type = st.selectbox("🌱 Crop Category:", ["Chilli", "Tomato", "Potato", "Onion"])
        with c2:
            volume_kg = st.number_input("⚖️ Est. Weight (Quintals):", min_value=1.0, value=25.0, step=0.5)
            
        uploaded_file = st.file_uploader("📸 Capture/Upload Batch Sample Image:", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Inbound Batch Reference Capture", use_container_width=True)
            
            if st.button("PRODUCE ANALYSIS & ALLOCATE SLOT"):
                st.session_state['run_pipeline'] = True

# =========================================================================
# RIGHT COLUMN: MANDI OFFICER OPERATIONS ENGINE (BACKEND INTERFACE)
# =========================================================================
with col_right:
    st.markdown("### 🏢 Central Management Grid")
    st.caption("Live logistical load vectors, quality distribution metrics, and active procurement registers.")
    
    # Live Capacity Vector Row
    st.markdown("##### 📍 Active Mandi Yard Fill Capacities")
    mc1, mc2, mc3 = st.columns(3)
    with mc1:
        st.markdown("<div class='mandi-card'><b>Nellore Hub</b><br><span style='color:#10B981;'>● Stable</span><br><b>Load: 42%</b></div>", unsafe_allow_html=True)
    with mc2:
        st.markdown("<div class='mandi-card' style='border-left-color:#EF4444;'><b>Kavali Center</b><br><span style='color:#EF4444;'>⚠️ Congested</span><br><b>Load: 88%</b></div>", unsafe_allow_html=True)
    with mc3:
        st.markdown("<div class='mandi-card' style='border-left-color:#3B82F6;'><b>Gudur Yard</b><br><span style='color:#3B82F6;'>⚙️ Underutilized</span><br><b>Load: 15%</b></div>", unsafe_allow_html=True)

    st.markdown("---")

    # Dynamic pipeline output changes inside backend console window
    if st.session_state.get('run_pipeline', False):
        st.markdown("##### 📊 Evaluation Inferences & Generated Clearances")
        
        confidence = round(random.uniform(95.1, 98.9), 2)
        token_id = f"KSETU-2026-{random.randint(1000, 9999)}"
        eta_time = (datetime.now() + timedelta(hours=random.randint(2, 4))).strftime('%I:%M %p')
        
        # Metric data displays
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(label="AI Assigned Quality Grade", value="GRADE-A" if crop_type=="Chilli" else "GRADE-B")
        with m2:
            st.metric(label="Computer Vision Confidence", value=f"{confidence}%")
        with m3:
            st.metric(label="Optimized Routing Corridor", value="NH-16 Express")
            
        st.success(f"🎉 **Logistics Token Issued:** Secure clearance pass compiled for farmer code **{farmer_name}**.")
        
        # Render a clean receipt invoice layout block
        st.code(f"""
        ===========================================================
                    KRISHISETU LOGISTICS ROUTING PASSPORT          
        ===========================================================
        Pass Code       : {token_id}
        Target Facility : Gudur Agricultural Yard (Load Capacity Window Clear)
        Reporting Slot  : Today, {eta_time}
        Logistics Rule  : Priority access corridor cleared via NH-16.
        ===========================================================
        """, language="markdown")
        
        # Append mock records to an interactive transactional table matrix database
        st.markdown("##### 📋 Historical Logistics Ledger Registry")
        mock_table_records = pd.DataFrame({
            "Token ID": [token_id, "KSETU-2026-8812", "KSETU-2026-4190"],
            "Farmer": [farmer_name, "Anil Kumar", "V. Reddy"],
            "Crop Type": [crop_type, "Tomato", "Onion"],
            "Weight (Q)": [volume_kg, 45.0, 12.5],
            "Assigned Destination": ["Gudur Yard", "Nellore Hub", "Gudur Yard"],
            "Status": ["Dispatched", "Arrived", "Completed"]
        })
        st.dataframe(mock_table_records, use_container_width=True, hide_index=True)
        
    else:
        # Default placeholder layout vector displayed when the portal is resting idle
        st.info("⌛ **Awaiting Inbound Transmission:** Fill out the Farmer Inbound Portal parameter columns and select execute to run verification microservices.")
        
        st.markdown("##### 📋 Active Logistics Ledger Registry")
        default_table_records = pd.DataFrame({
            "Token ID": ["KSETU-2026-8812", "KSETU-2026-4190"],
            "Farmer": ["Anil Kumar", "V. Reddy"],
            "Crop Type": ["Tomato", "Onion"],
            "Weight (Q)": [45.0, 12.5],
            "Assigned Destination": ["Nellore Hub", "Gudur Yard"],
            "Status": ["Arrived", "Completed"]
        })
        st.dataframe(default_table_records, use_container_width=True, hide_index=True)
        
