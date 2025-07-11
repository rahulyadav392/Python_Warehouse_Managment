import streamlit as st
from supabase_config import supabase

# Streamlit page config
st.set_page_config(page_title="Inventory Management System", layout="centered")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""

# --- Login UI ---
def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = supabase.table("users").select("*").eq("username", username).execute()
	st.write("DEBUG - Supabase response:", response.data)

        if response.data and len(response.data) == 1:
            user = response.data[0]
            if user["password_hash"] == password:  # ❗ Replace with proper hash validation in production
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = user["role"]
                st.success(f"Welcome, {username} ({user['role']})")
                st.experimental_rerun()
            else:
                st.error("❌ Incorrect password")
        else:
            st.error("❌ User not found")

# --- Admin Dashboard Placeholder ---
def admin_dashboard():
    st.title("🛠 Admin Dashboard")
    st.info("You are logged in as Admin.")
    st.write("✅ Access to all features like:")
    st.markdown("""
    - Add/Edit SKUs  
    - Approve stock in/out/returns  
    - View full inventory reports
    """)

# --- Staff Dashboard Placeholder ---
def staff_dashboard():
    st.title("📦 Staff Dashboard")
    st.info("You are logged in as Staff.")
    st.write("✅ Access to:")
    st.markdown("""
    - Add Stock In  
    - Add Stock Out  
    - Add Returns  
    """)

# --- Main Routing Logic ---
if not st.session_state.logged_in:
    login()
else:
    st.sidebar.success(f"Logged in as: {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.experimental_rerun()

    # Role-based dashboards
    if st.session_state.role == "admin":
        admin_dashboard()
    elif st.session_state.role == "staff":
        staff_dashboard()
    else:
        st.error("Unknown role. Please contact admin.")
