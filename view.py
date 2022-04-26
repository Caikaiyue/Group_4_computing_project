from flask import render_template



def all_clubs(club_list: list):
    # return html result with list of all clubs
    return render_template(
            'clubs.html',
            picked="no",
            clubs=club_list
        )

def club_with_id(club_picked: dict, member_list: list):
    # return html result with details and members of club id
    # display add member button
    return render_template(
            'clubs.html',
            picked='yes',
            club=club_picked,
            members=member_list
        )

def add_club_member(student_list: list):
    # return html result with dropdown list showing students
    return render_template(
            "add_member.html",
            page_type='new',
            action="/clubs/add_member?success",
            students=student_list
        )

def add_club_member_success(student_picked: dict):
    # return html result with success and student that has been added
    return render_template(
            "add_member.html",
            page_type='success',
            student=student_picked
        )

def all_activities(activity_list: list):
    # return html result with list of all activities
    return render_template(
            'activities.html',
            picked="no",
            activities=activity_list
        )
    

def activity_with_id(activity_picked: dict, participant_list: list):
    # return html result with details and participants of activity id
    # display add participant button
    return render_template(
            'activities.html',
            picked='yes',
            activity=activity_picked,
            participants=participant_list
        )

def add_activity_participant(student_list: list):
    # return html result with dropdown list showing students

    return render_template(
            "add_participant.html",
            page_type='new',
            action="/activities/add_participant?success",
            students=student_list
        )
    
def add_activity_participant_success(student_picked: dict):
    # return html result with success and student that has been added
    return render_template(
            "add_participant.html",
            page_type='success',
            student=student_picked
        )
