import streamlit as st
import random
from datetime import datetime, timedelta

# Set up page configurations
st.set_page_config(page_title="KrishiSetu AI Portal", page_icon="🌾", layout="centered")

# --- UI Header Section ---
st.title("KrishiSetu AI 🌾🚚")
st.subheader("Smart Farm-to-Market Supply Chain Portal")
st.write("Welcome to the unified portal for automated crop grading and procurement scheduling.")

st.divider()

# --- Tab 1: Farmer Dashboard ---
st.header("📸 Phase 1: AI Harvest Quality Scanner")

# User Inputs
farmer_name = st.text_input("Enter Farmer Name:", placeholder="e.g., Ramesh Kumar")
crop_type = st.selectbox("Select Crop Category:", ["Tomato", "Potato", "Onion", "Chilli"])

# Image upload widget simulation
uploaded_file = st.file_uploader("Upload or Capture Crop Image:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Harvest Batch Sample", use_container_width=True)
    
    # Process Button
    if st.button("RUN AI QUALITY GRADING"):
        with st.spinner("Analyzing structural data arrays offline..."):
            # Simulate real-time classification parameters
            confidence = round(random.uniform(91.2, 99.6), 2)
            quality_grade = random.choice(["GRADE-A (Premium Price)", "GRADE-B (Standard Price)", "REJECTED (Spoiled)"])
            
            st.success("Analysis Complete!")
            
            # Display outputs in clean metrics blocks
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Assigned Quality Tier", value=quality_grade.split(" ")[0])
            with col2:
                st.metric(label="Model Confidence Score", value=f"{confidence}%")
                
            st.info(f"💡 **Market Action Suggestion:** {quality_grade}")

            # --- Automatically move to Phase 2: Mandi Slot Booking ---
            st.divider()
            st.header("🎫 Phase 2: Automated Mandi Entry Token Engine")
            st.write("Checking dynamic capacities across regional government markets...")
            
            # Select mock market locations
            mandi_options = ["Nellore Main Mandi Hub", "Kavali Procurement Center", "Gudur Agricultural Yard"]
            selected_mandi = random.choice(mandi_options)
            reporting_time = datetime.now() + timedelta(hours=random.randint(2, 5))
            token_id = f"TOKEN-SIH-{random.randint(1000, 9999)}"
            
            # Display generated digital token
            st.balloons()
            st.subheader("🎉 Entry Slot Secured Successfully!")
            st.code(f"""
            ==============================================
                    KRISHISETU AI PROCUREMENT TOKEN       
            ==============================================
            Token ID       : {token_id}
            Farmer Name    : {farmer_name if farmer_name else 'Registered Farmer'}
            Crop Category  : {crop_type}
            Assigned Yard  : {selected_mandi}
            Reporting Time : {reporting_time.strftime('%Y-%m-%d %I:%M %p')}
            Logistics Note : Take NH-16 corridor for minimum transit delays.
            ==============================================
            """, language="markdown")
          
