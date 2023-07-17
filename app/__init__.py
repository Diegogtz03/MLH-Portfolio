import os
import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', email_address='diego_gtz_t@hotmail.com', github_username = 'diegogtz03', linkedin_username = 'diegogtzt')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/projects')
def projects():
    projects = [
        {
            "id": "1",
            "title": "GT Dent",
            "image": "../static/projects/GT_Dent.png",
            "description": "Java desk application designed for the registry and management of dental patient records and prescription creation in a dental office. This greatly reduced friction in the office with 1000+ records registered while saving up to 90% of the time looking for and updating the records. Database information exchanges handled with MySQL. Created also using dropbox API, java PDF creator and Figma.",
        },
        {
            "id": "2",
            "title": "MediFAST",
            "image": "../static/projects/Medifast.png",
            "description": "Web application combined with a physical pill dispenser that provides a safe way for doctors and families to give out prescriptions for patients with disabilities. This system also helped in the generation and validation of medical prescriptions to reduce medication robbery around the world. It was built using a combination of Arduino, NodeMCU, C++, Python, Flask and HTML. Worked in a team of 4, personally helped in putting together the website and programmed the logic for the pill dispenser using a NodeMCU. We were ranked at the top 10 places in the hackathon!",
            "link": "https://devpost.com/software/medifast-bzme2h" 
        },
        {
            "id": "3",
            "title": "Trainees Managment System",
            "image": "../static/projects/traineeSystem.png",
            "description": "A full-stack web application built for a company to help guide their traineers in their learning process while helping the admins take better administration of the program. This website included a game made specifically to motivate the trainees to continue the program. The system was built using React, Next, SQL, .NET, and Unity. Personally worked on the whole front-end and part of the back-end of the website.",
        },
        {
            "id": "4",
            "title": "Med-Link",
            "image": "../static/projects/MedLink.jpeg",
            "description": "Website designed for the global registry and availability of medical records and insurance in emergency situations using facial recognition as a tool for a quick recognition of patients. Built using OpenCV, Python, Flask, HTML, CSS and JS. Personally worked on building the website and setting up the facial recognition.",
            "link": "https://devpost.com/software/med-link"
        },
        {
            "id": "5",
            "title": "Y2-Hub",
            "image": "../static/projects/pyhub.png",
            "description": "Small and simple Python desktop app designed to download videos and audios from Youtube. Made as a learning experience and not as a final product.",
        },
        {
            "id": "6",
            "title": "Kronos - Music Bot",
            "image": "../static/projects/Kronos.png",
            "description": "A personal musical discord bot made using discord's API, Python, Youtube_dl and spotifybot. It allows to play music from youtube and spotify, some of the features include playing a specific song, skipping songs, stopping songs and queueing songs/playlists. It was a fun challenge to get the audio compression, threading and async functions right in order to get the best quality and experience out of the bot!",
        },
        {
            "id": "7",
            "title": "Portfolio Website",
            "image": "../static/projects/Portfolio.png",
            "description": "This very website currently built using Flask, MySQL, HTML, CSS and JS. In the process of migrating the website to React, Next and Three.js.",
        },
        {
            "id": "8",
            "title": "Code Syntax Highlighter",
            "image": "../static/projects/Resaltador.png",
            "description": "A simple console application made using C++ and Regex that allows to highlight the syntax of a code file written in C++. The program is able to create an HTML file highlighting the syntax of the code file with different colors.",
        },
        {
            "id": "9",
            "title": "Calendar Reminder System",
            "image": "../static/projects/Calendar_reminder.png",
            "description": "A web app built to reduce work in a dental office by reminding patients directly in their emails using Google's Calendar API instead of having to call them. Built using Flask, HTML, CSS and JS.",
        }
    ]

    return render_template('projects.html', projects = projects)

@app.route('/experience')
def experience():
    experiences = [
        {
            "company_institution": "CS @ Tecnológico de Monterrey",
            "start_date": "Aug 2021",
            "end_date": "Dec 2025",
        },
        {
            "company_institution": "Web Course Development @ CVA",
            "start_date": "Jul 2022",
            "end_date": "Jun 2023",
        },
        {
            "company_institution": "MLH PE Fellowship",
            "start_date": "Jun 2023",
            "end_date": "Sep 2023",
        }
    ]
    return render_template('experience.html', experiences = experiences)

@app.route('/hobbies')
def hobbies():
    hobbies = [
        {
            "name": "Coding",
            "image": "../static/hobbies/coding.png",
        },
        {
            "name": "Watching movies/series",
            "image": "../static/hobbies/movies.png",
        },
        {
            "name": "Analog photography",
            "image": "../static/hobbies/photography.jpg",
        },
        {
            "name": "Design",
            "image": "../static/hobbies/designs.png",
        },
        {
            "name": "Theatre staff",
            "image": "../static/hobbies/staff.png",
        },
        {
            "name": "Video editing",
            "image": "../static/hobbies/travel_video.gif",
        }
    ]
    return render_template('hobbies.html', hobbies = hobbies)

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
    id = request.form['id']
    TimelinePost.delete_by_id(id)

    return "OK"