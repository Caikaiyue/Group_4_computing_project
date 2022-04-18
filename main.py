from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET"])
def splash():
    pass

@app.route('/index', methods=["GET"])
def index():
    # link to cca
    # link to events
    pass

@app.route('/event', methods=["GET", "POST"])
def event():
    # list of all events
    # REQUEST ARGS
    # when clicked, goes to /event?event=<event name>
    # indiv event page has
    # - link to event_add_participant, goes to /event/add_partipant?event=<event_id>
    # - link to event_remove_participant
    pass

@app.route('/event/add_participant', methods=["GET", "POST"])
def event_add_participant():
    # Required request arg: event=<event_id>
    # display list of students who are not participants
    # When form submitted, send POST request to /event
    # with event_id and participant_id
    pass

@app.route('/event/remove_participant', methods=["GET", "POST"])
def event_remove_participant():
    pass

@app.route('/cca', methods=["GET"])
def cca():
    # list of all cca
    # when clicked, passes name=<cca name> as request arg
    # each cca has
    # - link to cca_add_member
    # - link to cca_remove_member
    pass

@app.route('/cca/add_member', methods=["GET", "POST"])
def cca_add_member():
    pass

@app.route('/cca/remove_member', methods=["GET", "POST"])
def cca_remove_member():
    pass

app.run('0.0.0.0')