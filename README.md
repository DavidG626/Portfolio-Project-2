Holliston News
Holliston News is a Flask-based web application that provides users with the latest news articles in various categories, including general news, business, technology, science, health, sports, and entertainment. The app fetches news data from the NewsAPI and displays it in a user-friendly format.

Features
Landing Page: The home page where users can search for news articles using keywords.
News Categories: Users can browse news articles in different categories: General, Business, Technology, Science, Health, Sports, and Entertainment.
Search Functionality: Users can search for news articles by entering keywords.
Filtered Results: Articles without titles or descriptions are filtered out to ensure quality content.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/DavidG626/Portfolio-Project-2.git
cd Portfolio-Project-2
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Set up NewsAPI:

Obtain an API key from NewsAPI.
Replace 'your_api_key_here' in the source code with your actual API key.
Run the application:

bash
Copy code
flask run
Usage
Home Page:

Search for news articles using the search bar.
View the latest headlines in various categories.
Categories:

Click on any category from the navigation menu to view the latest news in that category.
Routes
/ : Landing page with a search bar and general news.
/search : Displays search results based on the user's query.
/headlines : Displays the top headlines in general news.
/business : Displays the top headlines in business news.
/technology : Displays the top headlines in technology news.
/science : Displays the top headlines in science news.
/health : Displays the top headlines in health news.
/sports : Displays the top headlines in sports news.
/entertainment : Displays the top headlines in entertainment news.
Code Overview
app.py: Main application file that defines the routes and logic for fetching and displaying news articles.
Templates:
home.html: Template for the landing page and search results.
headlines.html: Template for displaying general news headlines.
business.html: Template for displaying business news.
technology.html: Template for displaying technology news.
science.html: Template for displaying science news.
health.html: Template for displaying health news.
sports.html: Template for displaying sports news.
entertainment.html: Template for displaying entertainment news.
Dependencies
Flask
NewsAPI

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or suggestions, please contact David Gutierrez at davidguticodes@gmail.com

