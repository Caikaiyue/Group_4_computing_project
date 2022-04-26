import csv, pymongo


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

    def __init__(self, id, name, members):

        self._club_id = id
        self._name = name
        self._members = members

class ActivityRecords:

    """
    Encapsulates each activity entity
    """

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
    Encapsulate access to Student collection.

    Methods
    -------
    insert(record)
        Insert a new document from the given record

    get(id) -> dict
        Return a document with the given student id

    all() -> [dict]
        Return a list of all students in dict format

    update_record(id_, field1=value1[, field2=value2, ...])
        Update the document with the given id,
        according to specified keyword arguments.
        Each keyword argument follows field=value format.

    delete_record(id)
        Delete the document with the given id
    """

    def __init__(self, url):
        self._url = url

    def connection(self):
        client = pymongo.MongoClient(self._uri)
        db = client['student_registration']
        coll = db["student"]
        return coll
    
    def insert(self, record):
        coll = self.connection()
        coll.insert_one({
            "student_id": record["student_id"],
            "name": record["name"],
            "age": record["age"],
            "year_enrolled": record["year_enrolled"]
            "graduating_year": record["graduating_year"],
            "class_id": record["class_id"],
            "subjects": record["subjects"],
            "clubs": record["clubs"]
            "activities": record["activities"]
            }
        )
        return

    def get(self, id):
        coll = self.connection()
        doc = coll.find_one({"student_id": id})
        return doc

    def all_students(self):
        coll = self.connection()
        all = list(coll.find())
        return all

    def update(self, id, **kwargs):
        coll = self.connection()
        coll.update_one(
            {"student_id": id},
            {'$set': {kwargs["key"]: kwargs["value"]}}
        )
        return

    def delete(self, id):
        coll = self.connection()
        coll.delete_one({"student_id": id})
        return


class Club:

    def __init__(self, url):
        self._url = url

    def connection(self):
        client = pymongo.MongoClient(self._url)
        db = client['student_registration']
        coll = db["club"]
        return coll

    def insert(self, record): 
        coll = self.connection() 
        coll.insert_one({
            "club_id": record["club_id"],
            "name": record["name"],
            "members": record["members"]
        }
        ) 
        record = StudentRecords()
        return

    def get(self, id):
        coll = self.connection() 
        doc = coll.find_one({"club_id": id}) 
        members = doc["members"] 
        return members

    def all(self):
        coll = self.connection()
        all = list(coll.find())
        return all

    def update(self, id, **kwargs):
        coll = self.connection()
        doc = coll.update_one(
            {"club_id": id},
            {'$set': {kwargs["key"]: kwargs["value"]}}
        )
        return

    def delete(self, id):
        coll = self.connection()
        doc = coll.delete_one({"club_id": id})
        return


class Activity:

    def __init__(self, url):
        self._url = url

    def connection(self):
        client = pymongo.MongoClient(self._url)
        db = client["student_registration"]
        coll = db["activity"]
        return client, coll

    def activity_exists(id):
        client, coll = self.connection()
        doc = list(coll.find({"activity_id": id}))
        client.close()

        if len(doc) == 0:
            return False
        
        else: 
            return True


    def insert(self, record): 
        coll = self.connection()
        coll.insert_one({
            "activity_id": record["activity_id"],
            "start_date": record["start_date"],
            "end_year": record["end_year"],
            "description": record["description"],
            "participants": record["participants"]
        }
        )
        return

    def get_activity_details(self, id):
        """
        Returns a dict
        {"name" : , "id" }
        of ONE activity
        """
        client, coll = self.connection()
        doc = coll.find_one({"activity_id": id})
        details = {}
        details["name"] = doc["description"]
        details["activity_id"] = doc["activity_id"]
        client.close()
        return details

    def get_participants(self, id):
        """
        Returns a list of dicts
        [{"participant_id": , "name": }] 
        of ONE activity
        """
        client, coll = self.connection()
        doc = coll.find_one({"activity_id": id})
        participants = doc["participant_list"] # returns a list of participant id

        db = client["student_registration"]
        coll = db["student"]
        all_students = list(coll.find()) # returns a list of dictionaries
        students = []
        for student in all_students:
            students.append({"student_id": student})

        doc = coll
        

        for participant in participants:

        details = {}



    def get(self, id):
        coll = self.connection()
        doc = coll.find_one({"student_id": id})
        return doc

    def all(self):
        coll = self.connection()
        all = list(coll.find())
        return all

    def update(self, id, **kwargs):
        coll = self.connection()
        coll.update_one(
            {"activity_id": id},
            {'$set': {kwargs["key"]: kwargs["value"]}}
        )
        return

    def delete_record(self, id):
        coll = self.connection()
        coll.delete_one({"activity_id": id})
        return







