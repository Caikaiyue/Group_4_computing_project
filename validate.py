import storage

def activity_id(inputstr: str):
    """
    Validate the given inputstr and ensure it is a valid id.
    Valid id is an integer.

    Check if this activity id exists in the database using function storage.activity_exist(activity_id)


    Return True if valid and exists, else return False.
    """
    if inputstr.isdigit() and storage.activity_exist(inputstr):
        return True
    else:        
        return False


def student_id(inputstr: str):
    """
    Validate the given inputstr and ensure it is a valid id.
    Valid id is an integer.
    Check if this student id exists in the database using storage.student_exist(student_id)

    Return True if valid and exists, else return False.
    """
    if inputstr.isdigit() and storage.student_exist(inputstr):
        return True
    else:
        return False

def club_id(inputstr: str):
    if inputstr.isdigit() and storage.club _exist(inputstr):
        return True
    else:
        return False