from flask import Flask, render_template, request
from datetime import datetime, timedelta
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='a8c8eeba0d99436196dfaecbc47b52c1')


app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def landing_page():
     return render_template('home.html')


@app.route('/search')
def home():
    query = request.args.get('q')
    if query:
        search_results = newsapi.get_everything(q=query, language='en', sort_by='relevancy')
        if 'articles' in search_results:
            # Filter out articles without title or description
            filtered_articles = [article for article in search_results['articles']
                                 if 'title' in article and 'description' in article]
            return render_template('home.html', search_results=filtered_articles, query=query)
        else:
            error_message = "No articles found."
            return render_template('home.html', error_message=error_message)
    return render_template('home.html')

@app.route('/headlines')
def headlines():
    category = "general"  # Category for business news
    search_results = newsapi.get_top_headlines(category=category, language='en')

    if 'articles' in search_results:
        # Filter out articles without title or description
        filtered_headlines = [article for article in search_results['articles']
                             if 'title' in article and 'description' in article]
        return render_template("headlines.html", search_results=filtered_headlines, category=category)
    else:
        error_message = "No articles found"
        return render_template('headlines.html', error_message=error_message)

@app.route('/business')
def business():
    category = "business"  # Category for business news
    search_results = newsapi.get_top_headlines(category=category, language='en')

    if 'articles' in search_results:
        # Filter out articles without title or description
        filtered_business = [article for article in search_results['articles']
                             if 'title' in article and 'description' in article]
        return render_template("business.html", search_results=filtered_business, category=category)
    else:
        error_message = "No articles found"
        return render_template('business.html', error_message=error_message)

@app.route('/technology')
def technology():
    category = "technology"  # Category for business news
    search_results = newsapi.get_top_headlines(category=category, language='en')

    if 'articles' in search_results:
        # Filter out articles without title or description
        filtered_technology = [article for article in search_results['articles']
                             if 'title' in article and 'description' in article]
        return render_template("technology.html", search_results=filtered_technology, category=category)
    else:
        error_message = "No articles found"
        return render_template('technology.html', error_message=error_message)


@app.route('/science')
def science():
    category = "science"  # Category for business news
    search_results = newsapi.get_top_headlines(category=category, language='en')

    if 'articles' in search_results:
        # Filter out articles without title or description
        filtered_science = [article for article in search_results['articles']
                             if 'title' in article and 'description' in article]
        return render_template("science.html", search_results=filtered_science, category=category)
    else:
        error_message = "No articles found"
        return render_template('science.html', error_message=error_message)
    
@app.route('/health')
def health():
    category = "health"  # Category for business news
    search_results = newsapi.get_top_headlines(category=category, language='en')

    if 'articles' in search_results:
        # Filter out articles without title or description
        filtered_health = [article for article in search_results['articles']
                             if 'title' in article and 'description' in article]
        return render_template("health.html", search_results=filtered_health, category=category)
    else:
        error_message = "No articles found"
        return render_template('health.html', error_message=error_message)
    
@app.route('/sports')
def sports():
    category = "sports"  # Category for business news
    search_results = newsapi.get_top_headlines(category=category, language='en')

    if 'articles' in search_results:
        # Filter out articles without title or description
        filtered_sports = [article for article in search_results['articles']
                             if 'title' in article and 'description' in article]
        return render_template("sports.html", search_results=filtered_sports, category=category)
    else:
        error_message = "No articles found"
        return render_template('sports.html', error_message=error_message)
    

@app.route('/entertainment')
def entertainment():
    category = "entertainment"  # Category for business news
    search_results = newsapi.get_top_headlines(category=category, language='en')

    if 'articles' in search_results:
        # Filter out articles without title or description
        filtered_entertainment = [article for article in search_results['articles']
                             if 'title' in article and 'description' in article]
        return render_template("entertainment.html", search_results=filtered_entertainment, category=category)
    else:
        error_message = "No articles found"
        return render_template('entertainment.html', error_message=error_message)
    



    
    
if __name__ == '__main__':
    app.run(debug=True, port=5024)
