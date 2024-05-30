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

# Streamlit app layout
st.title('📚 Personalized Study Planner')
st.write('Generate a personalized study plan based on your course load, deadlines, and personal preferences.')

# Input fields with enhanced UI
st.header('📝 Input Your Information')
course_load = st.text_area('Course Load (e.g., Math, Physics, Chemistry)', placeholder='Enter your courses separated by commas')
deadlines = st.text_area('Deadlines (e.g., Math: 2023-05-25, Physics: 2023-05-30)', placeholder='Enter your deadlines in the format Course: YYYY-MM-DD')
preferences = st.text_area('Personal Preferences (e.g., study in the morning, prefer short sessions)', placeholder='Enter any study preferences')

# Button to generate study plan
if st.button('Generate Study Plan'):
    if course_load and deadlines and preferences:
        study_plan = generate_study_plan(course_load, deadlines, preferences)
        st.subheader('Your Personalized Study Plan:')
        st.write(study_plan)
        
        # Show deadlines in a calendar
        deadlines_data = parse_deadlines(deadlines)
        if deadlines_data:
            df = pd.DataFrame(deadlines_data)
            st.subheader('📅 Deadlines Calendar')
            st.dataframe(df)
        
            # Notify the user of upcoming tasks
            for deadline in deadlines_data:
                days_left = (datetime.datetime.strptime(deadline['date'], '%Y-%m-%d') - datetime.datetime.now()).days
                if days_left <= 3:
                    send_notification(f"🔔 Reminder: Only {days_left} days left for {deadline['course']} deadline!")
    else:
        st.error('Please fill in all the fields.')

# Section for feedback
st.header('🔍 Provide Feedback')
st.write('Help us improve by providing your feedback!')
feedback = st.text_area('Your feedback', placeholder='Enter your feedback here')
if st.button('Submit Feedback'):
    if feedback:
        st.success('Thank you for your feedback!')
    else:
        st.error('Please enter your feedback before submitting.')

# Footer with more info
st.markdown('---')
st.write('Built with ❤️ by [Your Name]. For more information, visit [Your GitHub](https://github.com/your-username).')
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

# Streamlit app layout
st.title('📚 Personalized Study Planner')
st.write('Generate a personalized study plan based on your course load, deadlines, and personal preferences.')

# Input fields with enhanced UI
st.header('📝 Input Your Information')
course_load = st.text_area('Course Load (e.g., Math, Physics, Chemistry)', placeholder='Enter your courses separated by commas')
deadlines = st.text_area('Deadlines (e.g., Math: 2023-05-25, Physics: 2023-05-30)', placeholder='Enter your deadlines in the format Course: YYYY-MM-DD')
preferences = st.text_area('Personal Preferences (e.g., study in the morning, prefer short sessions)', placeholder='Enter any study preferences')

# Button to generate study plan
if st.button('Generate Study Plan'):
    if course_load and deadlines and preferences:
        study_plan = generate_study_plan(course_load, deadlines, preferences)
        st.subheader('Your Personalized Study Plan:')
        st.write(study_plan)
        
        # Show deadlines in a calendar
        deadlines_data = parse_deadlines(deadlines)
        if deadlines_data:
            df = pd.DataFrame(deadlines_data)
            st.subheader('📅 Deadlines Calendar')
            st.dataframe(df)
        
            # Notify the user of upcoming tasks
            for deadline in deadlines_data:
                days_left = (datetime.datetime.strptime(deadline['date'], '%Y-%m-%d') - datetime.datetime.now()).days
                if days_left <= 3:
                    send_notification(f"🔔 Reminder: Only {days_left} days left for {deadline['course']} deadline!")
    else:
        st.error('Please fill in all the fields.')


# Footer with more info
st.markdown('---')
