# Mood-Analysis-SW-CMPSC463-REPORT

### **1\. Project Goals**

Objective: To develop a software application that not only predicts mood based on user activities and sentiment analysis but it also offeres suggestions based on the mood of the user.

Goals: Enhance well-being by providing mood insights and suggestions for individuals. The suggestion is always intended to enhance the mood of the user. It can be achieved by suggesting various activities that are known to enhance the mood of the user.

### **2\. Significance of the Project**

Meaningfulness: Aims to contribute to mental well-being by analyzing activities and suggesting mood-enhancing actions.

Contribution to Safe Space: Promotes a positive environment by aiding users in understanding and managing their moods. The journey to achieving peace begins when an individual is aware of his/her own emotions and can understand them better.

## Installation Instructions: 

### Clone the repository to your machine:
```bash 
https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-.git
```

### Install the required dependencies using the following command:
```bash 
pip install -r requirements.txt 
```

### File paths of Database file, NLP API .json file, and images in the code
Place this files in the same directory as your main Python script or within a designated folder within the project directory. This way the paths in the code will be relative and it will easier to access the files in your environment. Place the 'sun.png', 'rain.png', 'clouds.png', and 'mood_data.db' files within the same directory as the main Python script.

### Supporting Python Files
Make sure you have supporting python files in the same directory. Supporting files are: 'Data.py' and 'data_processing.py'. 

## Usage Instructions (Main file: 'app.py'): 

### 1. Launching the Application:

**Navigate to Project Directory:**

Open a terminal or command prompt window on your system. Execute the python script you want to run. The main application script in this project is 'app.py'.
```bash
python app.py
```

**Open the project directory in an IDE, like PYCharm or IntelliJ IDEA.**

Load all the project  files in tabs and you will have easy access to the 'app.py' which will run the main application as well as 'Data.py' which you can use to access the database of your application. 

### 2. Adding Users
**Create User Profile:**
- On the application's interface, locate the "Add User" section.
- Enter a unique username in the provided text entry box.  
- Click the "Add User" button to create a new user profile.

### 3. Submitting User Activities
**Enter Activities:**
- Choose the user from the displayed list of users in the application interface.
- Input the activities performed by the user into the "User Activities" text box.
  
**Submit Activities:**
- Click the "Submit Activities" button to save the entered activities for the selected user.

### 4. Analyze Sentiment
**Input Sentiment Text:**
- In the "Sentiment Analysis" section of the application, type the text for sentiment analysis.

**Analyze Sentiment:**
- Click the "Analyze Sentiment" button to trigger sentiment analysis using Google's Natural Language API.
  
**Interpreting Results:**
- The application will display a sentiment analysis result in a message box.
- Based on the sentiment score, it will suggest mood-based activities related to the analyzed text.
- Additionally, the GUI will showcase the mood and suggested activities alongside an associated image.

### 5. Exiting the Application
**Exit Application:**
- To close the application, click the "Exit" button or use the application window's close button.

## Usage Instructions ('Data.py') for managing User Data:
**1. Run the Python Script:**
- Execute the Python script containing this code in your preferred Python environment or IDE.

**2. GUI for Displaying User Activities:**
- Upon running the script, a graphical user interface (GUI) window titled "User Activities" will appear.
  
**3. Displaying User Activities:**
-The interface will initially display all user activities stored in the specified SQLite database file (mood_data.db).

**4. Sorting the Displayed Data:**
- To sort the displayed activities, use the drop-down menu labeled "Sort by" to select either "Username" or "Activities."
- The displayed data will be sorted based on the chosen option.

**5. Filtering User Activities:**
- Use the drop-down menu labeled "Filter by" to select either "Username" or "Activities."
- Enter a filter term in the corresponding entry field to filter the displayed activities based on the chosen filter criteria.

**6. Search Functionality:**
- The search bar located at the top allows users to search for specific terms across all user activities displayed.
- As you type into the search bar, the displayed activities will dynamically update to match the search term.

**7. Interpreting Displayed Data:**
- The main listbox in the interface presents the formatted user activities.
- Each entry includes the username and their corresponding activities, separated by an empty line for better readability.

**8. Exiting the Interface:**
- To close the interface, simply close the GUI window or use the standard window close function of your operating system.

## Code Structure
### 1. Main Functional Blocks:
- **User Interface (GUI):**
  -  Window setup (root = tk.Tk(), geometry, and title).
  -  Interface layout design using labels, entries, buttons, and list boxes.
  -  Background image display.
- **Database Handling:**
  - Functions to create and manage SQLite database operations (create_table, write_user_activities_to_db, read_user_activities_from_db).
  - Handling user data, including adding users, collecting user activities, and performing sentiment analysis.
- **Sentiment Analysis:**
   - Sentiment analysis functions using Google's Natural Language API (analyze_sentiment, get_mood_suggestion, show_mood_and_suggestion).
 
### 2. External Libraries and Modules:
- Imported libraries such as tkinter, sqlite3, PIL, google.cloud, requests, and others.

### 3. Graphical User Interface (GUI) Components:
- Labels, entries, buttons, and list boxes for user interaction.
- Styling elements (colors, fonts) and image display within the interface.

### 4. User Interaction Functions:
- Functions triggered by user actions such as adding users, submitting activities, analyzing sentiment, deleting users, and exiting the program.

### Diagrammatic Representation:

├── User Interface (GUI)

│   ├── Window Setup

│   ├── Interface Design

│   ├── Background Image Display

│   └── Event Handling Functions

│

├── Database Handling

│   ├── SQLite Operations

│   └── User Data Management

│

├── Sentiment Analysis

│   ├── Google's Natural Language API Integration

│   ├── Sentiment Analysis Functions

│   └── Display Functions

│

├── External Libraries and Modules

│   ├── tkinter

│   ├── sqlite3

│   ├── PIL

│   ├── google.cloud

│   ├── requests

│   └── ...

│

└── User Interaction Functions

    ├── Add User

    ├── Collect User Activities

    ├── Analyze Sentiment

    ├── Delete User

    └── Exit Program

## Functionalities and Testing

### 1. User Interface (GUI)
- Window Setup: Creates the main window for the application using tkinter.
- Interface Design: Constructs the layout with labels, entries, buttons, and list boxes for user interaction.
- Background Image Display: Sets up a background image for the GUI.
- Event Handling Functions: Defines functions triggered by user actions like button clicks.
### 2. Database Handling
**SQLite Operations:**
- create_table: Creates a table in the SQLite database if it doesn't exist.
- write_user_activities_to_db: Writes user activities to the database.
- read_user_activities_from_db: Reads user activities from the database.
### 3. Sentiment Analysis
**Google's Natural Language API Integration:**
- analyze_sentiment: Uses Google's API to perform sentiment analysis on user-entered text.
- get_mood_suggestion: Determines mood based on sentiment score.
- show_mood_and_suggestion: Displays analysis results and mood suggestions to the user.
### 4. External Libraries and Modules
- Imports necessary libraries such as tkinter, sqlite3, PIL (Pillow), Google Cloud's language_v1, requests, and more.
### 5. User Interaction Functions
**Add User (add_user):**
- Adds a new user to the system, updating the active user and database.

**Collect User Activities (collect_user_activities):**
- Collects user-entered activities, handles missing values, and performs data processing:
   - Adds temporal features, calculates activity frequency, and sentiment scores.
   - Aggregates similar activities and adds weather conditions.
   - Updates user activities in the database.
     
**Analyze Sentiment (analyze_sentiment):**
- Utilizes Google's Natural Language API to analyze sentiment from user-entered text.
- Displays analysis results, mood, and suggested activities to the user.

**Delete User (delete_user):**
- Removes a user and their activities from the system and updates the UI.
  
**Exit Program (exit_program):**
- Closes the application window and terminates the program.

### Test Results

![Screenshot (498)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/ea4a2a27-3284-429e-bc61-2d150a89f364)
![Screenshot (499)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/83cd42de-db77-4ef9-89f1-164bd9b22fab)
![Screenshot (500)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/8071d164-217b-4faa-ac5e-e3d8c58ba333)

**Check to see if Data is being transferred correctly after each use:**

![Screenshot (501)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/3d59f3bc-cf98-4b9a-88f0-19424e912e96)
![Screenshot (504)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/85392070-69ae-4f5a-a683-87f614c04ae9)
![Screenshot (505)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/0fbcff57-d0f1-4f42-be87-4b5223b7122e)
![Screenshot (511)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/e00643e2-ccfb-4753-8d22-75f973fb5910)
![Screenshot (512)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/e8250943-80df-4909-90d1-af6f70003fad)
![Screenshot (513)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/bf24c0cd-e319-4f4b-9340-7ec41fec217b)
![Screenshot (514)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/d4672354-9e36-40ee-a22c-9ac4a0b57eef)
![Screenshot (515)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/1dd6e572-c950-419e-b39c-b1f5fbdce403)


**Deleting Users:**
![Screenshot (518)](https://github.com/dravyaaa/Mood-Analysis-SW-CMPSC463-/assets/107662465/72cf23be-09cd-469a-bc11-cc9ea4eebf05)


## Discussion & Conclusion
### 1. Project Issues and Challenges:
**Integration and API Handling:**
- Google's Natural Language API was unable to load in my environment which prevented the application from being a web application. To overcome this challenge, we implemented an alternative way to integrate API into our program. We created a key on our service account on GCP and provided that account with admin access to our API which we obtained in our GCP account. After that we downloaded the API key in .json file. Throught this process, we could integrate API call in our code in a similar way we would call any file on our machine. However, connecting API to our environment would have still been a better and more efficient option if it had worked properly.

**Data Processing Complexity:**
- Because the data entered is raw and our program is not pre-trained on various models, it was important to implement functions in a way that would process data with more accuracy. To avoid inconsistencies with the data, we implemented a double analysis of data, one in main application and the other in 'data_processing.py' file which we also import into our main file. By doing this, we get two sentiment analysis from two different NLPs (the other is textblob) which will help user understand their emotion analysis better.
- Another problem was integrating database to our program which was similar to API call. To overcome, this issue, we decided to connect the database directly to our program and access the database using the python script. Accessing the database using external source such DB Browser was yielding expected results as database was returning empty almost everytime. By creating 'Data.py' file which will show us the databased by executing python script, we can solve this issue to some extent.

### 2. Project Limitations: 
**API Dependency:**
- Our app's sentiment analysis capabilities are bound by the API usage limits imposed by Google. These limits might restrict the number of analyses we can perform in a given timeframe or the volume of text that can be processed, affecting the app's real-time analysis and responsiveness.

**Data Accuracy:**
- Interpreting Context and Nuances:
  - Sentiment analysis, although sophisticated, might stumble when interpreting contextual nuances, sarcasm, or cultural subtleties present in user-inputted text. This limitation might result in occasional misinterpretations or a lack of contextual depth in the analysis.

- Evolutionary Nature of Sentiment:
  - Human emotions are intricate and ever-evolving, posing a challenge for any automated sentiment analysis tool. The app's reliance on predefined sentiment models will struggle to adapt to changes in emotional expression over time.
 
### 3. Course Learnings:
**Algorithmic Thinking and Problem Solving:**
- Data Processing Algorithms: We utilized various algorithms to process user-entered activities, aggregate similar activities, and calculate sentiment scores. Concepts like sorting algorithms (for activity aggregation) and sentiment analysis algorithms formed the backbone of these functionalities.

- Optimization Techniques: Learnings about algorithmic optimization were instrumental in streamlining data processing. We applied optimization strategies to enhance the app's efficiency when handling large volumes of user data.

**Data Structure and Management:**
- Database Management: Leveraging SQLite, a lightweight database system, aligned with the course's teachings on database management. We structured our data storage model to ensure seamless data retrieval and management of user activities.

- Text Processing Structures: Concepts of text processing data structures, such as arrays or linked lists, were adapted to handle and manipulate user-entered text for sentiment analysis and activity aggregation.

**Design Patterns and Modularity:**
- Modular Code Structure: We compartmentalized functionalities into separate modules and functions, adhering to the principles of modularity and reusability. Each module catered to a specific task, promoting code readability and ease of maintenance.

- GUI Design Patterns: Concepts of GUI design patterns guided the layout and organization of the user interface elements, ensuring a user-friendly and intuitive design for data entry and result visualization.

**Complexity Analysis:**
- Efficiency and Performance: We continuously evaluated algorithms and data processing techniques to minimize time complexity and optimize resource utilization, aligning with the course's focus on efficiency and performance analysis.

### Conclusion
In conclusion, the development of the mood analysis application exemplifies a fusion of practical implementation and theoretical concepts taught in the Designs and Algorithms course. This project's foundation lies in algorithmic thinking, data structure management, and modular design, which seamlessly converged to create an intuitive user interface for activity input and sentiment analysis. Leveraging SQLite for data storage and Google's sentiment analysis API underscored the reliance on external services, emphasizing the need for robust error handling and mitigation strategies. Despite built-in limitations in API dependencies, data accuracy, and scalability, our project embodies the amalgamation of academic learnings with real-world challenges. By navigating through these limitations and applying course teachings, we've tried to create a application that not only provides mood insights to the user but also attempts to enhance the mood by suggesting various activities. 
