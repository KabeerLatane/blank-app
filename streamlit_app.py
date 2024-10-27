import streamlit as st

st.title("Disaster Preparedness Chatbot")

# Basic Information
st.header("Basic Information")
location = st.text_input("What is your location (city, state)?")
household_size = st.number_input("How many people are in your household?", min_value=1, value=1)
has_pets = st.checkbox("Do you have pets?")
if has_pets:
    pet_count = st.number_input("How many pets do you have?", min_value=1, value=1)
    pet_types = st.multiselect("What types of pets?", ["Dogs", "Cats", "Birds", "Fish", "Other"])

# Disaster Type and Risk Assessment
st.header("Disaster Risk Assessment")
disaster_type = st.selectbox(
    "Select the primary type of disaster you're preparing for:",
    ["Hurricane", "Earthquake", "Flood", "Wildfire", "Tornado", "Winter Storm", 
     "Tsunami", "Volcanic Eruption", "Drought", "Heat Wave", "Pandemic"]
)

secondary_disasters = st.multiselect(
    "Select any secondary disasters that commonly occur in your area:",
    ["Power Outages", "Landslides", "Storm Surge", "Flash Floods", "High Winds"]
)

# Vulnerability Assessment
st.header("Vulnerability Assessment")
vulnerable_members = st.multiselect(
    "Are there any vulnerable individuals in your household?",
    ["Elderly (65+)", "Young children (under 5)", "Pregnant women", 
     "People with disabilities", "People with chronic medical conditions"]
)

medical_needs = st.multiselect(
    "Select any specific medical needs in your household:",
    ["Prescription medications", "Medical devices requiring power", 
     "Mobility assistance", "Vision/hearing aids", "Special dietary requirements"]
)

# Home Assessment
st.header("Home Assessment")
home_type = st.selectbox(
    "What type of home do you live in?",
    ["Single-family house", "Apartment", "Mobile home", "Townhouse", "Other"]
)

floor_level = st.number_input("If in a multi-story building, what floor do you live on?", min_value=1, value=1)

home_features = st.multiselect(
    "Select the features of your home:",
    ["Basement", "Generator", "Solar panels", "Storm shutters", "Safe room/shelter",
     "Elevated foundation", "Fire-resistant materials", "Emergency exit routes"]
)

# Resources and Preparedness
st.header("Current Resources")
emergency_supplies = st.multiselect(
    "Which emergency supplies do you currently have?",
    ["First aid kit", "Non-perishable food", "Water supply", "Emergency contact list",
     "Battery-powered radio", "Flashlights", "Extra batteries", "Manual can opener",
     "Matches in waterproof container", "Cell phone backup battery", "Emergency blankets",
     "Multi-tool", "Dust masks", "Moist towelettes", "Garbage bags", "Basic tools",
     "Extra clothing and sturdy shoes", "Important documents in waterproof container",
     "Cash and change", "Fire extinguisher", "Paper maps of your area"]
)

water_supply = st.number_input("How many gallons of emergency water do you have stored?", min_value=0.0, value=0.0)
food_supply = st.number_input("How many days of non-perishable food do you have?", min_value=0, value=0)

# Communication and Planning
st.header("Emergency Planning")
has_plan = st.checkbox("Do you have a written emergency plan?")

communication_methods = st.multiselect(
    "What methods of emergency communication do you have access to?",
    ["Cell phone", "Landline", "Two-way radio", "Emergency radio", "Satellite phone",
     "Social media", "Email", "Local emergency alert system"]
)

evacuation = st.multiselect(
    "Select your evacuation preparations:",
    ["Identified primary and secondary evacuation routes",
     "Designated meeting points for family",
     "Emergency contact cards for all family members",
     "Go-bags packed and ready",
     "Fuel kept in vehicles above half tank",
     "Access to reliable transportation",
     "Identified emergency shelter locations",
     "Plan for pet evacuation"]
)

# Insurance and Documentation
st.header("Insurance and Documentation")
insurance_coverage = st.multiselect(
    "What types of insurance coverage do you have?",
    ["Homeowner's/Renter's insurance", "Flood insurance", "Earthquake insurance",
     "Wind damage coverage", "Vehicle insurance", "Life insurance", "Medical insurance"]
)

documents_ready = st.multiselect(
    "Which important documents do you have readily accessible?",
    ["Insurance policies", "Identification documents", "Medical records",
     "Banking information", "Property deeds/leases", "Birth certificates",
     "Social security cards", "Immunization records", "Pet documentation"]
)

# Training and Skills
st.header("Skills and Training")
emergency_skills = st.multiselect(
    "Select any emergency response skills you or household members have:",
    ["CPR certification", "First aid training", "CERT training",
     "Fire safety", "Basic survival skills", "Ham radio license",
     "Swimming", "Basic mechanical/repair skills", "Medical training"]
)

# Local Resources
st.header("Community Resources")
local_resources = st.multiselect(
    "Are you aware of these local emergency resources?",
    ["Emergency shelters", "Evacuation routes", "Emergency alert systems",
     "Local emergency services", "Community emergency response team",
     "Local aid organizations", "Medical facilities", "Emergency supply stores"]
)

# Special Considerations
st.header("Special Considerations")
specific_needs = st.text_area(
    "Please describe any other specific needs or concerns regarding disaster preparedness:",
    height=100
)

# Preparedness Level Assessment
st.header("Self-Assessment")
preparedness_level = st.select_slider(
    "How prepared do you feel for a disaster?",
    options=["Not at all prepared", "Slightly prepared", "Somewhat prepared", 
             "Well prepared", "Very well prepared"]
)

# Send user inputs to IBM Granit and display response
if st.button("Get Personalized Recommendations"):
    # Example function to format question for IBM Granit
    def ask_granit(inputs):
        # Format all inputs into a comprehensive question
        # This is a placeholder for the actual IBM Granit integration
        return f"[Detailed IBM Granit Response based on all inputs]"
    
    response = ask_granit(locals())
    st.write("Chatbot Response:", response)