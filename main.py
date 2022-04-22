from flask import Flask, render_template, request
from storage import Student, Club, Activity
import view



app = Flask(__name__)



student_coll = Student()
cca_coll = Club()
activity_coll = Activity()



@app.route('/', methods=["GET"])
def index():
    #Index page shows two boxes, activity and club which directs to /activity and /club
    #No arg required
    
    return render_template('index.html')
    pass

@app.route('/activity', methods=['GET'])
def activity():
    # /activity?id=?  --> Show details of activity, & participants
        # POST /activity/add_participant form [activity_id, student_id]

    # If no request args, show all activities

    if 'id' in request.args:
        id_ = request.args['id']
        # Validate request arg id
        # Retrieve activity record
        activity = ...
        # Retrieve participant records
        participants = ...
        return view.activity(activity, participants)
    else:
        # retrieve activities from storage
        return view.all_activity(activities)

@app.route('/activity/add_participant', methods=['GET', 'POST'])
def activity_add_participant():
    if request.method == 'GET':
        # Handle error if request arg does not have activity_id
        activity_id = request.args['activity_id']
        # Validate activity_id
        participants = ...
        return view.add_activity_participant(activity_id, participants)
    elif request.method == 'POST':
        activity_id = request.form['activity_id']
        participant_id = request.form['student']
        # POST: add participant to db
        
    activity_coll...
    return ...

@app.route('/activity/remove_participant', methods=['GET', 'POST'])
def activity_remove_participant():
    #GET: show dropdpwn list of participants

    return view

@app.route('/club', methods=['GET'])
def club():
    # show all clubs
    # /club?id=<id>  --> show 1 club
    # add member: page with dropdown list of students
        # POST /club/add_member form [club_id, student_id]
    # If no request args, show all clubs
    return view.all_clubs()
    # If id in request args,
    # show activity details and participants
    return view.club_with_id(club_id)

@app.route('/club/add_member', methods=['GET', 'POST'])
def club_add_member():
    # GET: show dropdown list for adding student
    return view.add_club_member(club_id)
    # POST: add member to db
    cca_coll...
    return ...



app.run('0.0.0.0')
