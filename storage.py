import csv, pymongo
from types import MemberDescriptorType


class StudentRecords:

    """
    Encapsulates each student entity
    """

    # each student entity has the following attributes
    def __init__(self, student_id, name, age, year_enrolled, graduating_year, class_id, subjects, clubs, activities):
        self._student_id
        self._name = name
        self._age = age
        self._year_enrolled = year_enrolled
        self._graduating_year = graduating_year
        self._class_id = class_id
        self._subjects = subjects
        self._clubs = clubs
        self._activities = activities

class ClubRecords:

    """
    Encapsulates each club entity
    """

    # each club entity has the following attributes
    def __init__(self, id, name, members):

        self._club_id = id
        self._name = name
        self._members = members

class ActivityRecords:

    """
    Encapsulates each activity entity
    """

    # each activity has the following attributes
    def __init__(self, id, start_date, end_date, description, participants):
        
        self._activity_id = id
        self._start_date = start_date
        self._end_date = end_date
        self._description = description
        self._participants = participants

    
# function to insert all the required records from a csv file into a collection belonging to the student_registration database
def csv_to_db(file, url):


    file = open(file) # open the csv file
    data = [row for row in csv.DictReader(file)] # read the data from the csv file into a list
    file.close()

    client = pymongo.MongoClient(url)
    db = client['student_registration']
    coll = db["student"]

    for record in data : # loop through each record in the data list
        student = Student(field for field in record) # instantiate each record
        

    return 

# done: csv_to_db("cca.csv", "club")


class Student():

    """
    Encapsulates access to the Student Collection
    """

    def __init__(self, url):
        self._url = url

    def connection(self): # establish the conection to the Student Collection
        client = pymongo.MongoClient(self._url)
        db = client['student_registration']
        coll = db["student"]
        return client, coll
    
    def add_student(self, record):
        """
        Insert a record into the students collection
        """
        client, coll = self.connection() # get the connection first
        coll.insert_one({
            "student_id": record["student_id"],
            "name": record["name"],
            "age": record["age"],
            "year_enrolled": record["year_enrolled"],
            "graduating_year": record["graduating_year"],
            "class_id": record["class_id"],
            "subjects": record["subjects"],
            "clubs": record["clubs"],
            "activities": record["activities"]
            }
        ) # insert the student's record into the Student Collection
        client.close() # close the connection
        return

    def get_student_detail(self, id): # tested
        """
        Returns a dict 
        {"name": , "student_id": }
        containing the details
        of only ONE student
        """
        client, coll = self.connection() # get the connection first
        doc = coll.find_one({"student_id": id}) # retrieve the ONE student record
        data = {"name": doc["name"], "student_id": doc["student_id"]} # only return the student's name and id in the dict
        client.close() # close the connection
        return data

    def all_students(self): # tested
        """
        Returns a list of dict
        {"name" : , "id" }
        containing details
        of ALL students
        """
        client, coll = self.connection() # establish connection
        all_students = list(coll.find()) # retrieve all the records from the Student Collection into a list
        
        data = [] # initialise a list to contain a list of dict {"name": , "student_id": } to be returned

        for student in all_students: # loop through each record in the all_students list
            data.append({"name": student["name"], "student_id": student["student_id"]}) # append only the student's name and id into the dict
        
        client.close() # close the connection
        return data

    # def update(self, id, **kwargs):
    #     coll = self.connection()
    #     coll.update_one(
    #         {"student_id": id},
    #         {'$set': {kwargs["key"]: kwargs["value"]}}
    #     )
    #     return

    # def delete(self, id):
    #     coll = self.connection()
    #     coll.delete_one({"student_id": id})
    #     return


class Club:

    def __init__(self, url):
        self._url = url

    def connection(self): # establish the conection to the Student Collection
        client = pymongo.MongoClient(self._url)
        db = client['student_registration']
        coll = db["club"]
        return client, coll

    def club_exists(self, id): # tested
        """
        Check if club exists in the database.
        """
        client, coll = self.connection() # get the connection first
        doc = list(coll.find({"club_id": id})) # find whether the club_id exists
        client.close() # close the connection

        if len(doc) == 0: # no such club
            return False
        
        else: # club exists
            return True

    def add_participant(self, club_id, student_id): # tested
        """
        Insert a new student_id into the member_list for ONE club
        """
        client, coll = self.connection() # get the connection first
        doc = coll.find_one({"club_id": club_id}) # retrieve the ONE club record
        members = doc["member_list"] # retrieve the member_list field of the ONE club record
        members.append(student_id) # append the new student_id into the existing member_list field
        coll.update_one(
            {"club_id": club_id},
            {'$set': {"member_list": members}}
        ) # update the member_list field of the ONE club record
        client.close() # close the connection
        return

    # def insert(self, record): 
    #     client, coll = self.connection() 
    #     coll.insert_one({
    #         "club_id": record["club_id"],
    #         "name": record["name"],
    #         "members": record["members"]
    #     }
    #     ) 
    #     record = StudentRecords()
    #     client.close()
    #     return

    def get_club_detail(self, id): # tested
        """
        Returns a dict
        {"name" : , "id" }
        of ONE club
        """
        client, coll = self.connection()
        doc = coll.find_one({"club_id": id}) # find the ONE club
        details = {} # a dict to store the name and club_id to be returned
        details["name"] = doc["name"] # get the club name
        details["club_id"] = doc["club_id"] # get the club_id
        client.close()
        return details
    
    def get_members_detail(self, id): # tested
        """
        Returns two list of dicts
        members = [{"student_id": , "name": }] 
        non_members = [{"student_id": , "name": }] 
        of ONE club
        """
        client, coll = self.connection()
        doc = coll.find_one({"club_id": id}) # find the ONE club
        member_list = doc["member_list"] # returns a list of member_id

        db = client["student_registration"] 
        coll = db["student"] # access the student collection
        all_students = list(coll.find()) # retrieve all the student records

        students = [] # to contain a list of dict {"student_id": , "name": }
        for student in all_students: # loop through all student records 
            # just append the student_id and name to the students list in dict format
            students.append({"student_id": student["student_id"], "name": student["name"]})

        members = [] # to contain a list of dicts {"student_id": , "name": } if only the student_id is found in the participant list
        non_members = [] # to contain a list of dicts {"student_id": , "name": } if the student_id is not found in the participant list

        for student in students:
            if student["student_id"] in member_list:
                members.append({"student_id": student["student_id"], "name": student["name"]})
            else: non_members.append({"student_id": student["student_id"], "name": student["name"]})

        client.close()

        return members, non_members

    def all_clubs(self): # tested
        """
        Returns a list of dict
        [{"club_id": , "name": }]
        basically retrieve the club_id and name of all club
        """
        client, coll = self.connection() 
        all_clubs = list(coll.find()) # retrieve all the records from the Club collection
        
        data = [] # to contain a list of dict {"club_id": , "name": } to be returned

        for club in all_clubs:
            data.append({"club_id": club["club_id"], "name": club["name"]})

        client.close()
        return data

    # def get(self, id):
    #     client, coll = self.connection() 
    #     doc = coll.find_one({"club_id": id}) 
    #     members = doc["members"] 
    #     client.close()
    #     return members

    # def all(self):
    #     client, coll = self.connection()
    #     all = list(coll.find())
    #     client.close()
    #     return all

    # def update(self, id, **kwargs):
    #     client, coll = self.connection()
    #     doc = coll.update_one(
    #         {"club_id": id},
    #         {'$set': {kwargs["key"]: kwargs["value"]}}
    #     )
    #     client.close()
    #     return

    # def delete(self, id):
    #     client, coll = self.connection()
    #     doc = coll.delete_one({"club_id": id})
    #     client.close()
    #     return


class Activity:

    def __init__(self, url):
        self._url = url

    def connection(self):
        client = pymongo.MongoClient(self._url)
        db = client["student_registration"]
        coll = db["activity"]
        return client, coll

    def activity_exists(self, id): # tested
        """
        Check if activity exists in the database.
        """
        client, coll = self.connection()
        doc = list(coll.find({"activity_id": id})) # find whether the activity_id exists
        client.close()

        if len(doc) == 0: # no such activity_id
            return False
        
        else: # activity_id exists
            return True

    def add_participant(self, activity_id, student_id): # tested
        """
        Insert a new student_id into the participant_list for ONE activity
        """
        client, coll = self.connection()
        doc = coll.find_one({"activity_id": activity_id})
        participants = doc["participant_list"]
        participants.append(student_id)
        coll.update_one(
            {"activity_id": activity_id},
            {'$set': {"participant_list": participants}}
        )
        client.close()
        return


    # def insert(self, record): 
    #     """
    #     Inserts a record into the Activity collection
    #     """
    #     client, coll = self.connection()
    #     coll.insert_one({
    #         "activity_id": record["activity_id"],
    #         "start_date": record["start_date"],
    #         "end_year": record["end_year"],
    #         "description": record["description"],
    #         "participants": record["participants"]
    #     }
    #     )
    #     client.close()
    #     return

    def get_activity_detail(self, id): # tested
        """
        Returns a dict
        {"name" : , "id" }
        of ONE activity
        """
        client, coll = self.connection()
        doc = coll.find_one({"activity_id": id}) # find the ONE activity
        details = {} # a dict to store the name and activity_id to be returned
        details["name"] = doc["description"] # get the activity description
        details["activity_id"] = doc["activity_id"] # get the activity_id
        client.close()
        return details

    def get_participants_detail(self, id): # tested
        """
        Returns two list of dicts
        participants = [{"participant_id": , "name": }] 
        non_participants = [{"participant_id": , "name": }] 
        of ONE activity
        """
        client, coll = self.connection()
        doc = coll.find_one({"activity_id": id}) # find the ONE activity
        all_participants = doc["participant_list"] # returns a list of participant id

        db = client["student_registration"] 
        coll = db["student"] # access the student collection
        all_students = list(coll.find()) # retrieve all the student records

        students = [] # to contain a list of dict {"student_id": , "name": }
        for student in all_students: # loop through all student records 
            # just append the student_id and name to the students list in dict format
            students.append({"student_id": student["student_id"], "name": student["name"]})

        participants = [] # to contain a list of dicts {"student_id": , "name": } if only the student_id is found in the participant list
        non_participants = [] # to contain a list of dicts {"student_id": , "name": } if the student_id is not found in the participant list

        for student in students:
            if student["student_id"] in all_participants:
                participants.append({"participant_id": student["student_id"], "name": student["name"]})
            else: non_participants.append({"participant_id": student["student_id"], "name": student["name"]})

        client.close()

        return participants, non_participants

    def all_activities(self): # tested
        """
        Returns a list of dict
        [{"activity_id": , "name": }]
        basically retrieve the activity_id and name of all activities
        """
        client, coll = self.connection() 
        all_activities = list(coll.find()) # retrieve all the records from the Activity collection
        
        data = [] # to contain a list of dict {"activity_id": , "name": } to be returned

        for activity in all_activities:
            data.append({"activity_id": activity["activity_id"], "name": activity["name"]})

        client.close()
        return data

    # def update(self, id, **kwargs):
    #     coll = self.connection()
    #     coll.update_one(
    #         {"activity_id": id},
    #         {'$set': {kwargs["key"]: kwargs["value"]}}
    #     )
    #     return

    # def delete_record(self, id):
    #     coll = self.connection()
    #     coll.delete_one({"activity_id": id})
    #     return







