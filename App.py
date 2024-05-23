import streamlit as st
import cohere
import datetime
import pandas as pd

# Initialize Cohere client
cohere_client = cohere.Client('BFY1598ea13qck5eW1xLdRQ5vVOuDEPK6IrY6TDW')

# Function to generate study plan
def generate_study_plan(course_load, deadlines, preferences):
    prompt = f"Generate a study plan for the following courses: {course_load}. Deadlines are: {deadlines}. Preferences are: {preferences}."
    response = cohere_client.generate(prompt=prompt, max_tokens=300)
    return response.generations[0].text

# Function to parse deadlines
def parse_deadlines(deadlines):
    deadlines_list = [d.split(':') for d in deadlines.split(',')]
    return [{'course': d[0].strip(), 'date': d[1].strip()} for d in deadlines_list]

# Function to send notification
def send_notification(message):
    st.write(message)  # Placeholder for actual notification logic

# Streamlit app layout
st.title('Personalized Study Planner')
st.write('Generate a personalized study plan based on your course load, deadlines, and personal preferences.')

# Input fields
course_load = st.text_area('Course Load (e.g., Math, Physics, Chemistry)', '')
deadlines = st.text_area('Deadlines (e.g., Math: 2023-05-25, Physics: 2023-05-30)', '')
preferences = st.text_area('Personal Preferences (e.g., study in the morning, prefer short sessions)', '')

# Button to generate study plan
if st.button('Generate Study Plan'):
    if course_load and deadlines and preferences:
        study_plan = generate_study_plan(course_load, deadlines, preferences)
        st.subheader('Your Personalized Study Plan:')
        st.write(study_plan)
        
        # Show deadlines in a calendar
        deadlines_data = parse_deadlines(deadlines)
        df = pd.DataFrame(deadlines_data)
        st.subheader('Deadlines Calendar')
        st.write(df)
        
        # Notify the user of upcoming tasks
        for deadline in deadlines_data:
            days_left = (datetime.datetime.strptime(deadline['date'], '%Y-%m-%d') - datetime.datetime.now()).days
            if days_left <= 3:
                send_notification(f"Reminder: Only {days_left} days left for {deadline['course']} deadline!")
    else:
        st.error('Please fill in all the fields.')

# Running the app
if __name__ == '__main__':
    st.run()
