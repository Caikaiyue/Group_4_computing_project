from flask import Flask, render_template, request, abort
from storage import Student, Club, Activity
import view
import validate


app = Flask(__name__)
uri = 'mongodb://Group_4:ESSD8GMd3nLct74@cluster0-shard-00-00.qbwtc.mongodb.net:27017,cluster0-shard-00-01.qbwtc.mongodb.net:27017,cluster0-shard-00-02.qbwtc.mongodb.net:27017/student_registration?ssl=true&replicaSet=atlas-u0fo68-shard-0&authSource=admin&retryWrites=true&w=majority'

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
        if not validate.activity_id(activity_coll, activity_id):
            abort(400)

        # Retrieve activity record
        activity_detail = activity_coll.get_activity_detail(activity_id)

        # Retrieve participant records
        participants, non_participants = activity_coll.get_participants_detail(
            activity_id)
        #breakpoint()

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

        if not validate.activity_id(activity_coll, activity_id):
            abort(400)

        #get all the students that are not participants
        participants, non_participants = activity_coll.get_participants_detail(
            activity_id)

  
        return view.add_activity_participant(activity_id, non_participants)

    else:

        activity_id = request.form['activity_id']
        
        student_id = request.form['student']  #an id
        
        #validate both ids
        if not (validate.activity_id(activity_coll, activity_id)
                and validate.student_id(student_coll, student_id)):
            abort(400)
        
        # add participant to db
        activity_coll.add_participant(activity_id, student_id)  #it never add

        #get the student details from student_id
        student_detail = student_coll.get_student_detail(student_id)

        return view.add_activity_participant_success(student_detail)


@app.route('/clubs', methods=['GET'])
def clubs():
    # /club?id=?  --> Show details of club, & members
    # POST /club/add_member form [club_id, student_id]

    #If id in args -> view club details
    if 'id' in request.args:

        club_id = request.args['id']

        # Validate request arg id
        if not validate.club_id(club_coll, club_id):
            abort(400)

        # Retrieve club record
        club_detail = club_coll.get_club_detail(club_id)
        #["name", "club_id"]

        # Retrieve member records
        members, non_members = club_coll.get_members_detail(club_id)
 
        return view.club_with_id(club_detail, members)

    #if no request args, show all clubs
    else:
        # retrieve clubs from storage
        all_clubs = club_coll.all_clubs()
        return view.all_clubs(all_clubs)


@app.route('/clubs/add_member', methods=['GET', 'POST'])
def clubs_add_member():
    #If the page is GET request -> choose which club

    if 'success' not in request.args:

        # Handle error if request arg does not have club_id
        club_id = request.args['id']

        # Validate club_id
        if not validate.club_id(club_coll, club_id):
            abort(400)

        #get all the members from this club
        members, non_members = club_coll.get_members_detail(club_id)
        return view.add_club_member(club_id, non_members)

    #if its a POST request -> add members
    else:

        club_id = request.form['club_id']
        student_id = request.form['student']


        #validate both ids
        if not validate.club_id(club_coll, club_id):
            abort(400)

        
        # add member to db
        club_coll.add_member(club_id, student_id)

        #get the student details from st7dent_id
        student_detail = student_coll.get_student_detail(student_id)
        return view.add_club_member_success(student_detail)



app.run('0.0.0.0')
