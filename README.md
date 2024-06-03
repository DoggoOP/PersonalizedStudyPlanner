# Personalized Study Planner

This is a web application that generates personalized study plans based on user inputs such as courses, deadlines, and study preferences. The app utilizes Cohere's large language model (LLM) to create a detailed and effective study schedule.

## Features

- **Dynamic Input Management**: Add and manage multiple courses and deadlines dynamically.
- **Personalized Study Plan**: Receive a study plan tailored to your specific courses, deadlines, and study preferences.
- **Interactive UI**: User-friendly interface with expandable sections for each course and deadline, and a checklist for managing tasks.
- **Error Handling**: Comprehensive error handling to ensure a smooth user experience.

## Tech Stack

- **Streamlit**: For building the web application.
- **Cohere**: For generating the study plan using an LLM.
- **Pandas**: For data manipulation and display.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/personalized-study-planner.git
   cd personalized-study-planner
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Cohere API key:
   - Create a file named `.streamlit/secrets.toml`.
   - Add your API key in the following format:
     ```toml
     [cohere]
     api_key = "YOUR_COHERE_API_KEY"
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Add Courses and Deadlines**: Use the "Add Course" button to dynamically add new courses and their respective deadlines.
2. **Input Study Preferences**: Enter your study preferences in the provided text area.
3. **Generate Study Plan**: Click the "Generate Study Plan" button to receive a detailed study schedule based on your inputs.
4. **View and Manage**: Choose between the "Dashboard" and "Combined" views to visualize your study plan and manage your tasks.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

