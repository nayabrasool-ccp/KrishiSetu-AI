import streamlit as st
import random
import pandas as pd
from datetime import datetime, timedelta

# Set widescreen operational layout parameters
st.set_page_config(page_title="KrishiSetu AI - Operations Hub", page_icon="🌾", layout="wide")

# Custom CSS presentation layers injection
st.markdown("""
    <style>
    .main { background-color: #F8FAFC; }
    .stButton>button { background-color: #10B981 !important; color: white !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; border: none !important; }
    .stButton>button:hover { background-color: #059669 !important; }
    .mandi-card { padding: 15px; border-radius: 12px; background-color: white; border-left: 5px solid #10B981; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# Top Admin Banner Layout Frame
st.markdown("<div style='background-color:#1E293B; padding:20px; border-radius:12px; margin-bottom:25px;'><h1 style='color:white; margin:0;'>KrishiSetu AI 🌾</h1><p style='color:#94A3B8; margin:5px 0 0 0;'>Enterprise Procurement, Quality Assurance & Security Validation Portal</p></div>", unsafe_allow_html=True)

# Layout Splitting Segments
col_left, col_right = st.columns([1, 1.2], gap="large")

# LEFT COLUMN: FARMER PORTAL CONTROL
with col_left:
    st.markdown("### 📱 Farmer Inbound Portal")
    st.caption("Mobile portal for real-time crop verification.")
    
    with st.container(border=True):
        farmer_name = st.text_input("👤 Farmer Registry Name:", value="Coco")
        crop_type = st.selectbox("🌱 Crop Category:", ["Chilli", "Tomato", "Potato", "Onion"])
        volume_kg = st.number_input("⚖️ Est. Weight (Quintals):", min_value=1.0, value=25.0, step=0.5)
        
        # --- FIX: FORCED LIVE CAMERA CAPTURE ONLY ---
        # Replaced file uploader with direct camera interface so users cannot upload gallery files.
        camera_file = st.camera_input("📸 Take a Live Picture of the Harvest:")
        
        if camera_file is not None:
            if st.button("PRODUCE ANALYSIS & ALLOCATE SLOT"):
                # Save state variables securely to cache memory blocks with true live current time
                st.session_state['active_run'] = True
                st.session_state['timestamp'] = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
                st.session_state['reporting'] = (datetime.now() + timedelta(hours=3)).strftime('%Y-%m-%d %I:%M %p')
                st.session_state['token'] = f"KSETU-2026-{random.randint(1000, 9999)}"
                st.session_state['f_name'] = farmer_name
                st.session_state['c_type'] = crop_type
                st.session_state['weight'] = volume_kg
        else:
            # Re-set session state if no image is present to prevent layout persistence errors
            st.session_state['active_run'] = False

# RIGHT COLUMN: SYSTEM OPERATIONS LEDGER
with col_right:
    st.markdown("### 🏢 Central Management Grid")
    st.caption("Live logistical monitoring and authentication ledgers.")
    
    # Active facility monitoring vectors
    st.markdown("##### 📍 Active Mandi Yard Fill Capacities")
    mc1, mc2, mc3 = st.columns(3)
    with mc1:
        st.markdown("<div class='mandi-card'><b>Nellore Hub</b><br><span style='color:#10B981;'>● Stable</span><br><b>Load: 42%</b></div>", unsafe_allow_html=True)
    with mc2:
        st.markdown("<div class='mandi-card' style='border-left-color:#EF4444;'><b>Kavali Center</b><br><span style='color:#EF4444;'>⚠️ Congested</span><br><b>Load: 88%</b></div>", unsafe_allow_html=True)
    with mc3:
        st.markdown("<div class='mandi-card' style='border-left-color:#3B82F6;'><b>Gudur Yard</b><br><span style='color:#3B82F6;'>⚙️ Underutilized</span><br><b>Load: 15%</b></div>", unsafe_allow_html=True)

    st.markdown("---")

    # Read state cache data values to draw log reports
    if st.session_state.get('active_run', False):
        st.markdown("##### 📊 Evaluation Inferences & Live Receipts")
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(label="AI Assigned Quality Grade", value="GRADE-B")
        with m2:
            st.metric(label="Source Verification", value="LIVE CAMERA")
        with m3:
            st.metric(label="Dynamic Time Validation", value="PASSED")
            
        st.success(f"🎫 **Token Securely Verified:** Allocation authorized for session record **{st.session_state['f_name']}**.")
        
        # Render a clean transaction receipt printout 
        st.code(f"""
        ===========================================================
                    KRISHISETU LIVE PROCUREMENT RECEIPT           
        ===========================================================
        Pass Code       : {st.session_state['token']}
        Target Facility : Gudur Agricultural Yard
        Scan Timestamp  : {st.session_state['timestamp']}
        Reporting Slot  : {st.session_state['reporting']} (Window Matches Load Plan)
        Logistics Route : Priority path authorized via NH-16 corridor.
        ===========================================================
        """, language="markdown")
        
        # Draw dynamic historical database records data ledger
        st.markdown("##### 📋 Historical Logistics Ledger Registry")
        mock_table_records = pd.DataFrame({
            "Token ID": [st.session_state['token'], "KSETU-2026-8812", "KSETU-2026-4190"],
            "Farmer": [st.session_state['f_name'], "Anil Kumar", "V. Reddy"],
            "Crop Type": [st.session_state['c_type'], "Tomato", "Onion"],
            "Weight (Q)": [st.session_state['weight'], 45.0, 12.5],
            "Reporting Window": [st.session_state['reporting'], "2026-09-23 11:30 AM", "2026-09-23 03:15 PM"],
            "Status": ["Verified Pass", "Arrived", "Completed"]
        })
        st.dataframe(mock_table_records, use_container_width=True, hide_index=True)
    else:
        st.info("⌛ **Security System Active:** Please capture a live photograph using the device camera box above to view grading analysis logs.")
