from flask import render_template



def all_clubs():
    # return html result with list of all clubs
    pass

def club_with_id(id: int):
    # return html result with details and members of club id
    # display add member button
    pass

def add_club_member(club_id: int):
    # return html result with dropdown list showing students
    pass

def all_activities(activity_list: list):
    # return html result with list of all activities
    return render_template("activity.html", activities=activity_list)
    

def activity_with_id(id: int):
    # return html result with details and participants of activity id
    # display add participant button
    pass

def add_activity_participant(activity_id: int, participant_list: list):
    # return html result with dropdown list showing students
    return render_template(
        "addstudent.html",
        action="",
        entity="participant",
        items=activity_list,
    )

def add_club_member(club_list: list):
    return render_template(
        "addstudent.html",
        action="",
        entity="member",
        items=club_list,
    )