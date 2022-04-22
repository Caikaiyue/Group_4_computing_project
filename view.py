from flask import render_template



#activity methods
#in the form of render_template(...) so I can directly return all_activities()

def all_activity():
    # return html result with list of all activities
    # basic what you will expect in the /activity page
    #/activity page needs to pass in "activity_id" as a form arg
    pass

def activity_with_id(id: int):
    # return html result with details and participants of activity id
    # display add participant button and remove button
    
    pass

def add_activity_participant(activity_id: int):
    # return html result with dropdown list showing students
    pass

def all_club():
    # return html result with list of all clubs
    pass

def club_with_id(id: int):
    # return html result with details and members of club id
    # display add member button
    pass

def add_club_member(club_id: int):
    # return html result with dropdown list showing students
    pass
