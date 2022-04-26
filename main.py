from flask import Flask, render_template, request
from storage import Student, Club, Activity
import view
import validate



app = Flask(__name__)
uri = "mongodb+srv://admin:admin@cluster0.ryteu.mongodb.net/student_registration?retryWrites=true&w=majority"


student_coll = Student(uri)
club_coll = Club(uri)
activity_coll = Activity(uri)



@app.route('/', methods=["GET"])
def index():
    #Index page shows two boxes, activity and club which directs to /activity and /club
    #No arg required
    
    return render_template('index.html')
    pass

#activity
@app.route('/activities', methods=['GET'])
def activities():
    # /activity?id=?  --> Show details of activity, & participants
        # POST /activity/add_participant form [activity_id, student_id]


    #If id in args -> view activity details
    if 'id' in request.args:
        activity_id = request.args['id']
        
        # Validate request arg id
        if not validate.activity_id(activity_id):
            abort(400)

        # Retrieve activity record
        activity_detail = activity_coll.get_activity_details(activity_id)
        
        # Retrieve participant records
        participants, non_participants = activity_coll.get_participant_detail(activity_id)
        return view.activity_with_id(activity_detail, participants) 
        
    #if no request args, show all activities
    else:
        # retrieve activities from storage
        all_activities = activity_coll.all_activities()
        return view.all_activities(all_activities)


@app.route('/activities/add_participant', methods=['GET', 'POST'])
def activities_add_participant():
    #If the page is GET request -> choose which activity
    if 'success' not in request.args:

        activity_id = request.args['id']
        # Validate activity_id

        if not validate.activity_id(activity_id):
            abort(400)

        #get all the students that are not participants
        participants, non_participants = activity.coll.get_participant_detail(activity_id)
        
        return view.add_activity_participant(activity_id, non_participants)

    else:
        activity_id = request.form['activity_id']
        student_id = request.form['student'] #an id
        
        #validate both ids
        if not (
            validate.activity_id(activity_id)
            and validate.student_id(student_id)
        ):
            abort(400)
        
        # add participant to db
        activity_coll.add_participant(activity_id, student_id)

        #get the student details from student_id
        student_detail = student_coll.get_student_detail(student_id)
        return view.add_activity_participants(student_detail)


@app.route('/activities/remove_participant', methods=['GET', 'POST'])
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



@app.route('/clubs', methods=['GET'])
def club():
    # /club?id=?  --> Show details of club, & members
        # POST /club/add_member form [club_id, student_id]

    #If id in args -> view club details
    if 'id' in request.args:
        club_id = request.args['id']
        
        # Validate request arg id
        if not validate.club_id(club_id):
            abort(400)
            
        # Retrieve club record
        club_detail = club_coll.get_club_details(club_id)
        
        # Retrieve member records
        members, non_members = club_coll.get_member_detail(club_id)
        return view.club_with_id(club_detail, members)
        
    #if no request args, show all clubs
    else:
        # retrieve clubs from storage
        all_clubs = club_coll.all_clubs()
        return view.all_club(all_clubs)

@app.route('/clubs/add_member', methods=['GET', 'POST'])
def clubs_add_member():
    #If the page is GET request -> choose which club
    if 'success' not in request.args:
        
        # Handle error if request arg does not have club_id          
        club_id = request.args['id']
        # Validate club_id
        if not validate.club_id(club_id):
            abort(400)

        #get all the members from this club
        members, non_members = club_coll.get_member_detail(club_id)
        return view.add_club_members(club_id, non_members)

    #if its a POST request -> add members 
    else:
        club_id = request.form['club_id']
        student_id = request.form['student']

        #validate both ids
        if not (
            validate.club_id(club_id)
            and validate.members_id(student_id)
        ):
            abort(400)

        # add member to db
        club_coll.add_member(club_id, student_id)

        #get the student details from st7dent_id
        student_detail = student_coll.get_student_detail(student_id)
        return view.add_club_members(student_detail)


@app.route('/club/remove_member', methods=['GET', 'POST'])
def club_remove_member():
    #GET: show dropdpwn list of members
    if request.method == "GET":

        #handle error: if club_id not in request.arg
        if "club_id" not in request.arg:
            abort(400)

        club_id = request.arg["club_id"]
        members = club_coll.get_members(id_)
        return view.club(club, members)

    elif request.method == 'POST':
        
        club_id = request.form['club_id']
        member_id = request.form['member_id']

        club_coll.remove_member(club_id, member_id)




app.run('0.0.0.0')
