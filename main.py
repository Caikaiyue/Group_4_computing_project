from flask import Flask, render_template, request
from storage import Student, Club, Activity


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
    # Show all activities

    return render_template('activity.html', activity_list = activity_coll.all_activity())

    # /activity?id=?  --> Show details of activity, & participants
    # add participant: page with dropdown list of students
        # POST /activity/add_participant form [activity_id, student_id]

@app.route('/acitivity/add_participant', methods=['GET', 'POST'])
def activity_add_participant():
    student_list = activity_coll.
    
@app.route('/club', methods=['GET'])
    # show all clubs
    # /club?id=<id>  --> show 1 club
    # add member: page with dropdown list of students
        # POST /club/add_member form [club_id, student_id]



app.run('0.0.0.0')
