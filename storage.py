import csv, pymongo


    # idk whether need this LOLOL
    # def __init__(self, name, age, year_enrolled, graduating_year, class_id, subjects, clubs, activities):
    #     self._name = name
    #     self._age = age
    #     self._year_enrolled = year_enrolled
    #     self._graduating_year = graduating_year
    #     self._class_id = class_id
    #     self._subjects = subjects
    #     self._clubs = clubs
    #     self._activities = activities
class Student:
    """
    Encapsulate access to Student collection.

    Methods
    -------
    insert_record(record)
        Insert a new document from the given record

    get(id) -> dict
        Return a document with the given id

    all() -> [dict]
        Return all documents in the collection

    update_record(id_, field1=value1[, field2=value2, ...])
        Update the document with the given id,
        according to specified keyword arguments.
        Each keyword argument follows field=value format.

    delete_record(id)
        Delete the document with the given id
    """
    def __init__(self, uri):
        self.uri = uri

    def connection(self):
        client = pymongo.MongoClient(self.uri)
        db = client['student_registration']
        coll = db["student"]
        return coll
    
    # if don't have the __init__ then can remove the self. and then the parameter include in all the keys
    def insert_record(self, record):
        coll = self.connection()
        coll.insert_one({
            "student_id": self._student_id,
            "name": self._name,
            "age": self._age,
            "year_enrolled": self._year_enrolled
            "graduating_year": self._graduating_year,
            "class_id": self._class_id,
            "subjects": self._subjects,
            "clubs": self._clubs
            "activities": self._activities
            }
        )

    #steady
    def get(self, id_):
        coll = self.connection()
        doc = coll.find_one({"student_id": id_})
        return doc

    def all(self):
        """
        return list of all students in dict format

        dict keys:
        {
            "student_id":2,
            "name": "cky" 
        }
        """
    #steady
    def update_record(self, id_, **kwargs):
        coll = self.connection()
        coll.update_one(
            {"student_id": kwargs["student_id"]},
            {'$set': {kwargs["key"]: kwargs["value"]}}
        )
        return

    #steady
    def delete_record(self, id_):
        coll = self.connection()
        coll.delete_one({"student_id": id_})
        return


class Club:

    # def __init__(self, club_id, name, members):

    #     # class Club attributes
    #     self._club_id = club_id
    #     self._name = name
    #     self._members = members

    # class Club method to establish a connection with MongoDB and access the database and collection
    def connection(self):
        client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.ryteu.mongodb.net/student_registration?retryWrites=true&w=majority")
        db = client['student_registration']
        coll = db["club"]
        return coll

    # class Club method to insert one club record into the Club collection
    def insert_record(self): # if don't have the __init__ then can remove the self. and then the parameter include in all the keys
        coll = self.connection() # establish a connection to MongoDB and access the database, collection
        coll.insert_one({
            "club_id": self._club_id,
        "name": self._name,
        "members": self._members
        }
        ) 
        return

    #steady
    # class Club method to retrieve all the members of a club
    def get_members(self, club_id):
        coll = self.connection() # access the club collection
        doc = coll.find_one({"club_id": club_id}) # retrieve a document matching the club_id
        members = doc["members"] # retrieve a list of members under a club field
        return members

    def get(self, id_):
        coll = self.connection()
        return doc

    def all(self):
        pass

    #steady
    def update_record(self, **kwargs):
        coll = self.connection()
        doc = coll.update_one(
            {"club_id": kwargs["club_id"]},
            {'$set': {kwargs["key"]: kwargs["value"]}}
        )
        return

    #steady
    def delete_record(self, club_id):
        coll = self.connection()
        doc = coll.delete_one({"club_id": club_id})
        return

# function to insert all the required records from a csv file into a collection belonging to the student_registration database
# BUT THEN this one need the __init__ function in the Club class for it to work LOLOL, but it works :)))
def csv_to_db(file, coll):

    file = open(file) # open the csv file
    data = [row for row in csv.DictReader(file)] # read the data from the csv file into a list
    file.close()

    for record in data : # loop through each record in the data list
        club = Club(int(record["id"]), record["name"], []) # instantiate each record under the class Club
        # only include the id and name as attributes
        club.insert_record() # insert its id and name attributes into the club collection

    return 

# done: csv_to_db("cca.csv", "club")


class Activity:

    # def __init__(self, activity_id, start_date, end_date, description, participants):
        
    #     self._activity_id = activity_id
    #     self._start_date = start_date
    #     self._end_date = end_date
    #     self._description = description
    #     self._participants = participants

    def connection(self):
        client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.ryteu.mongodb.net/student_registration?retryWrites=true&w=majority")
        db = client["student_registration"]
        coll = db["activity"]
        return coll

    def insert_record(self): # if don't have the __init__ then can remove the self. and then the parameter include in all the keys
        coll = self.connection()
        coll.insert_one({
            "activity_id": self._activity_id,
            "start_date": self._start_date,
            "end_year": self._end_year,
            "description": self._description,
            "participants": self._participants
        }
        )
        return

    #steady
    def get_participants(self, activity_id):
        coll = self.connection()
        doc = coll.find_one({"activity_id": activity_id})
        participants = doc["participants"]
        return participants

    def get(self, id_):
        coll = self.connection()
        doc = coll.find_one({"student_id": student_id})
        return doc

    def all(self):
        pass

    #steady
    def update_record(self, **kwargs):
        coll = self.connection()
        coll.update_one(
            {"activity_id": kwargs["activity_id"]},
            {'$set': {kwargs["key"]: kwargs["value"]}}
        )
        return

    #steady
    def delete_record(self, activity_id):
        coll = self.connection()
        coll.delete_one(
            {"activity_id": activity_id}
        )
        return






