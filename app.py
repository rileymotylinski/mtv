from flask import Flask, render_template, request, Response
import os
import random



app = Flask(__name__)

def random_video(): 
    videos = os.listdir("static/videos")
    
    
    chosen_video = videos[random.randrange(len(videos))]
   
    return chosen_video

@app.route("/")
def home():
    return render_template("index.html", video_name=random_video())

@app.route("/video_feed/<video_name>")
def video_feed(video_name):
    video_path = r"C:\Users\smurv\Documents\Progamming\mtv\static\videos\\" + video_name
    with open(video_path, "rb") as video_file:
        return Response(video_file.read())
    


@app.route("/new_music_video", methods=["GET"])
def new_music_video():
    return {"video" : random_video()}
    

    


