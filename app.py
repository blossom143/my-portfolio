from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample portfolio data - replace with your actual information
PORTFOLIO_DATA = {
    "about": {
        "name": "Tsomorlig Khishigbold",
        "title": "MLOps Engineer",
        "summary": "High-performing and self-driven MLOps Engineer with 5+ years of hands-on experience in the financial industry. Proven, demonstrable expertise in containerization, cloud computing, monitoring, automation, CI/CD pipelines and agile methodologies."
    },
    "education": [
        {
            "degree": "MSc in Engineering Science (Data Science)",
            "institution": "University at Buffalo",
            "year": "2025 - Present"
        },
        {
            "degree": "BE in Software Engineering",
            "institution": "National University of Mongolia",
            "year": "2016 - 2020"
        }
    ],
    "experience": [
        {
            "title": "Cloud Administrator",
            "company": "ESL FCU",
            "duration": "2025 - Present",
            "description": "Leading data science projects and developing machine learning models"
        },
        {
            "title": "Manager",
            "company": "Khan Bank",
            "duration": "2024 - 2024",
            "description": "Led cross-functional production teams to maintain 99.9% uptime for 300+ Java based microservices with over 2 million active users."
        },
        {
            "title": "Senior DevOps Engineer",
            "company": "Khan Bank",
            "duration": "2022 - 2024",
            "description": "Led cross-functional production teams to maintain 99.9% uptime for 300+ Java based microservices with over 2 million active users."
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
        "name": "Tsomorlig Khishigbold",
        "title": "MLOps Engineer",
        "summary": "High-performing and self-driven MLOps Engineer with 5+ years of hands-on experience in the financial industry. Proven, demonstrable expertise in containerization, cloud computing, monitoring, automation, CI/CD pipelines and agile methodologies."
    },
    "education": [
        {
            "degree": "MSc in Engineering Science (Data Science)",
            "institution": "University at Buffalo",
            "year": "2025 - Present"
        },
        {
            "degree": "BE in Software Engineering",
            "institution": "National University of Mongolia",
            "year": "2016 - 2020"
        }
    ],
    "experience": [
        {
            "title": "Cloud Administrator",
            "company": "ESL FCU",
            "duration": "2025 - Present",
            "description": "Leading data science projects and developing machine learning models"
        },
        {
            "title": "Manager",
            "company": "Khan Bank",
            "duration": "2024 - 2024",
            "description": "Led cross-functional production teams to maintain 99.9% uptime for 300+ Java based microservices with over 2 million active users."
        },
        {
            "title": "Senior DevOps Engineer",
            "company": "Khan Bank",
            "duration": "2022 - 2024",
            "description": "Led cross-functional production teams to maintain 99.9% uptime for 300+ Java based microservices with over 2 million active users."
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
