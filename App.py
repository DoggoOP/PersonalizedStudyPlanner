import streamlit as st
import cohere
import datetime
import pandas as pd

# Fetch API key from Streamlit secrets
try:
    cohere_api_key = st.secrets["cohere"]["api_key"]
except KeyError as e:
    st.error(f"Missing secret: {e}. Please make sure your Streamlit secrets are configured correctly.")
    st.stop()

# Initialize Cohere client
cohere_client = cohere.Client(cohere_api_key)

# Function to generate study plan
def generate_study_plan(course_load, deadlines, preferences):
    prompt = f"Generate a study plan for the following courses: {course_load}. Deadlines are: {deadlines}. Preferences are: {preferences}."
    response = cohere_client.generate(prompt=prompt, max_tokens=300)
    return response.generations[0].text

# Function to parse deadlines
def parse_deadlines(deadlines):
    deadlines_list = [d.split(':') for d in deadlines.split(',')]
    parsed_deadlines = []
    for d in deadlines_list:
        if len(d) == 2:
            parsed_deadlines.append({'course': d[0].strip(), 'date': d[1].strip()})
        else:
            st.warning(f"Invalid deadline format: {d}. Expected format: 'Course: YYYY-MM-DD'")
    return parsed_deadlines

# Function to send notification
def send_notification(message):
    st.write(message)  # Placeholder for actual notification logic

# Layout 1: Dashboard
def dashboard_view(course_load, deadlines, preferences, study_plan, deadlines_data):
    st.subheader('📅 Weekly Calendar View')
    df = pd.DataFrame(deadlines_data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')
    st.write(df)

    st.subheader('📋 Upcoming Deadlines List')
    st.write(df.sort_index())

    st.subheader('📝 Study Plan Summary')
    st.write(study_plan)

# Layout 3: Combined View
def combined_view(course_load, deadlines, preferences, study_plan, deadlines_data):
    st.subheader('🔄 Visual Timeline and Checklist')

    st.write('## Timeline')
    for deadline in deadlines_data:
        course = deadline['course']
        date = deadline['date']
        days_left = (datetime.datetime.strptime(date, '%Y-%m-%d') - datetime.datetime.now()).days
        st.write(f"{course}: {date} ({days_left} days left)")
    
    st.write('## Checklist')
    for deadline in deadlines_data:
        st.checkbox(f"{deadline['course']}: {deadline['date']}")

# Main app layout
st.title('📚 Personalized Study Planner')
st.write('Generate a personalized study plan based on your course load, deadlines, and personal preferences.')

# User selects the view
view = st.sidebar.selectbox('Select View', ['Dashboard', 'Combined'])

# Input fields
st.header('📝 Input Your Information')
course_load = st.text_area('Course Load (e.g., Math, Physics, Chemistry)', placeholder='Enter your courses separated by commas')
deadlines = st.text_area('Deadlines (e.g., Math: 2023-05-25, Physics: 2023-05-30)', placeholder='Enter your deadlines in the format Course: YYYY-MM-DD')
preferences = st.text_area('Personal Preferences (e.g., study in the morning, prefer short sessions)', placeholder='Enter any study preferences')

if st.button('Generate Study Plan'):
    if course_load and deadlines and preferences:
        study_plan = generate_study_plan(course_load, deadlines, preferences)
        deadlines_data = parse_deadlines(deadlines)
        
        if view == 'Dashboard':
            dashboard_view(course_load, deadlines, preferences, study_plan, deadlines_data)
        elif view == 'Combined':
            combined_view(course_load, deadlines, preferences, study_plan, deadlines_data)
    else:
        st.error('Please fill in all the fields.')

