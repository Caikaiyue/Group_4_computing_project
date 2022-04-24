from flask import render_template



def all_clubs(club_list: list):
    # return html result with list of all clubs
    return render_template(
        "clubs.html",
        clubs=club_list
    )

def club_with_id(club: dict, member_list: list):
    # return html result with details and members of club id
    # display add member button
    return render_template(
        "activity.html",
        action="",
        club = club,
        members=member_list
    )

def add_club_member(club_id: int, member_list: list):
    # return html result with dropdown list showing students
    return render_template(
        "add_member.html",
        action="",
        members=member_list,
    )

def all_activities(activity_list: list):
    # return html result with list of all activities
    return render_template(
        "activities.html",
        activities=activity_list
    )
    

def activity_with_id(activity: dict, participant_list: list):
    # return html result with details and participants of activity id
    # display add participant button
    return render_template(
        "activity.html",
        action="",
        activity = activity,
        participants=participant_list
    )

def add_activity_participant(activity_id: int, participant_list: list):
    # return html result with dropdown list showing students

    return render_template(
        "add_participant.html",
        action="",
        participants=participant_list,
    )

