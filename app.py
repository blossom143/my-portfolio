from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample portfolio data - replace with your actual information
PORTFOLIO_DATA = {
    "about": {
        "name": "Your Name",
        "title": "Data Scientist",
        "summary": "A passionate data scientist with expertise in machine learning, data analysis, and AI applications."
    },
    "education": [
        {
            "degree": "Master of Science in Data Science",
            "institution": "University of Example",
            "year": "2022 - Present"
        },
        {
            "degree": "Bachelor of Science in Computer Science",
            "institution": "Example University",
            "year": "2018 - 2022"
        }
    ],
    "experience": [
        {
            "title": "Data Scientist",
            "company": "Tech Company Inc.",
            "duration": "2023 - Present",
            "description": "Leading data science projects and developing machine learning models"
        },
        {
            "title": "Data Analyst Intern",
            "company": "Data Co.",
            "duration": "2022 - 2023",
            "description": "Analyzed large datasets and provided insights for business decisions"
        }
    ],
    "projects": [
        {
            "title": "AI Project 1",
            "description": "Description of your AI project",
            "technologies": ["Python", "TensorFlow", "Keras"]
        },
        {
            "title": "Data Analysis Project",
            "description": "Description of your data analysis project",
            "technologies": ["Pandas", "NumPy", "Matplotlib"]
        }
    ],
    "skills": [
        "Python", "Machine Learning", "Data Analysis", "TensorFlow", "SQL", "Git"
    ],
    "certifications": [
        "Certified Data Scientist",
        "Machine Learning Engineer",
        "Python Developer"
    ]
}

@app.route('/api/portfolio')
def get_portfolio():
    return jsonify(PORTFOLIO_DATA)

from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample portfolio data - replace with your actual information
PORTFOLIO_DATA = {
    "about": {
        "name": "Your Name",
        "title": "Data Scientist",
        "summary": "A passionate data scientist with expertise in machine learning, data analysis, and AI applications."
    },
    "education": [
        {
            "degree": "Master of Science in Data Science",
            "institution": "University of Example",
            "year": "2022 - Present"
        },
        {
            "degree": "Bachelor of Science in Computer Science",
            "institution": "Example University",
            "year": "2018 - 2022"
        }
    ],
    "experience": [
        {
            "title": "Data Scientist",
            "company": "Tech Company Inc.",
            "duration": "2023 - Present",
            "description": "Leading data science projects and developing machine learning models"
        },
        {
            "title": "Data Analyst Intern",
            "company": "Data Co.",
            "duration": "2022 - 2023",
            "description": "Analyzed large datasets and provided insights for business decisions"
        }
    ],
    "projects": [
        {
            "title": "AI Project 1",
            "description": "Description of your AI project",
            "technologies": ["Python", "TensorFlow", "Keras"]
        },
        {
            "title": "Data Analysis Project",
            "description": "Description of your data analysis project",
            "technologies": ["Pandas", "NumPy", "Matplotlib"]
        }
    ],
    "skills": [
        "Python", "Machine Learning", "Data Analysis", "TensorFlow", "SQL", "Git"
    ],
    "certifications": [
        "Certified Data Scientist",
        "Machine Learning Engineer",
        "Python Developer"
    ]
}

@app.route('/')
def index():
    return render_template('portfolio.html', data=PORTFOLIO_DATA)

@app.route('/api/portfolio')
def get_portfolio():
    return jsonify(PORTFOLIO_DATA)

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    # TODO: Implement actual contact form handling
    return jsonify({"success": True, "message": "Message received!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    lat = data.get('latitude')
    lng = data.get('longitude')
    print(f"User location: Latitude={lat}, Longitude={lng}")
    return jsonify({"status": "received", "latitude": lat, "longitude": lng})

if __name__ == '__main__':
    app.run(debug=True)
