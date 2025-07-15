from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Sample Data Science glossary
glossary_data = {
    'regression': {
        'term': 'Regression',
        'definition': 'A supervised learning technique used to predict continuous values.'
    },
    'clustering': {
        'term': 'Clustering',
        'definition': 'An unsupervised learning technique used to group similar data points.'
    },
    'pca': {
        'term': 'PCA (Principal Component Analysis)',
        'definition': 'A dimensionality reduction technique that transforms variables into a smaller set of uncorrelated components.'
    },
    'feature_engineering': {
        'term': 'Feature Engineering',
        'definition': 'The process of creating new features or transforming existing ones to improve model performance.'
    }
}

@app.route('/')
def index():
    terms = glossary_data.keys()
    return render_template('index.html', terms=terms)

@app.route('/glossary')
def glossary_prompt():
    terms = glossary_data.keys()
    return render_template('glossary_prompt.html', terms=terms)

@app.route('/glossary/<term_name>')
def glossary_detail(term_name):
    term = glossary_data.get(term_name.lower())
    if term:
        return render_template('glossary_detail.html', term=term)
    else:
        # -----------------------------------------
        # If term name is invalid (not found),
        # redirect user back to /glossary prompt page
        # using redirect and url_for functions
        # -----------------------------------------
        return redirect(url_for('glossary_prompt'))

# Handle wrong URLs gracefully
@app.errorhandler(404)
def page_not_found(e):
    # -----------------------------------------
    # If user visits a completely wrong URL (404),
    # automatically redirect them to homepage (/)
    # using redirect and url_for functions
    # -----------------------------------------
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5555)
