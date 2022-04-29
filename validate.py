import storage

def activity_id(activity_coll, inputstr: str):
    """
    Validate the given inputstr and ensure it is a valid id.
    Valid id is an integer.

    Check if this activity id exists in the database using function storage.activity_exist(activity_id)


    Return True if valid and exists, else return False.
    """
    if inputstr.isdigit() and activity_coll.activity_exists(inputstr):
        return True
    else:        
        return False


def student_id(student_coll, inputstr: str):
    """
    Validate the given inputstr and ensure it is a valid id.
    Valid id is an integer.
    Check if this student id exists in the database using storage.student_exist(student_id)

    Return True if valid and exists, else return False.
    """
    if inputstr.isdigit() and student_coll.student_exists(inputstr):
        return True
    else:
        return False

def club_id(club_coll, inputstr: str):
    if inputstr.isdigit() and club_coll.club_exist(inputstr):
        return True
    else:
        return False

