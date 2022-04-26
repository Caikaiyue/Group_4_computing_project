from flask import Flask, render_template, request
from storage import Student, Club, Activity
import view
import validate



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


    #If id in args -> view activity details
    if 'activity_id' in request.args:
        activity_id = request.args['activity_id']
        
        # Validate request arg id
        if not validate.activity_id(activity_id):
            abort(400)
            

        # Retrieve activity record
        activity = activity_coll.get_activity_details(id_)
        
        # Retrieve participant records
        participants = activity_coll.get_participants(id_)
        return view.activity(activity, participants)
        
    #if no request args, show all activities
    else:
        # retrieve activities from storage
        return view.all_activity()


@app.route('/activity/add_participant', methods=['GET', 'POST'])
def activity_add_participant():
    #If the page is GET request -> choose which activity
    if request.method == 'GET':
        
        # Handle error if request arg does not have activity_id
        if "activity_id" not in request.arg:
            abort(400)
            
        activity_id = request.args['activity_id']
        # Validate activity_id

        if not validate.activity_id(activity_id):
            abort(400)

        #get all the participants from this activity
        participants = activity_coll.get_participants(activity_id)

        return view.add_activity_participant(activity_id, participants)

    #if its a POST request -> add participant 
    elif request.method == 'POST':
        activity_id = request.form['activity_id']
        student_id = request.form['student_id']

        #validate both ids
        if not (
            validate.activity_id(activity_id)
            and validate.participant_id(student_id)
        ):
            abort(400)

        # add participant to db
        activity_coll.add_participant(activity_id, student_id)

        return view.add_participant_success()



@app.route('/activity/remove_participant', methods=['GET', 'POST'])
def activity_remove_participant():
    #GET: show dropdpwn list of participants
    if request.method == "GET":

        #handle error: if activity_id not in request.arg
        if "activity_id" not in request.arg:
            abort(400)

        activity_id = request.arg["activity_id"]
        participants = activity_coll.get_participants(id_)
        return view.activity(activity, participants)

    elif request.method == 'POST':
        
        activity_id = request.form['activity_id']
        participant_id = request.form['participant_id']

        activity_coll.remove_participant(activity_id, participant_id)


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
    return view.club(club_id)

@app.route('/club/add_member', methods=['GET', 'POST'])
def club_add_member():
    # GET: show dropdown list for adding student
    return view.add_club_member(club_id)
    # POST: add member to db
    cca_coll...
    return ...



app.run('0.0.0.0')
