from session_maker import session_maker

def store_people_db(people, session):
    #session.add_all(people.people)
    for obj in people.people: 
        session.add(obj)
    #print("Mike table: ", Person.__table__)
    print("Mike session: ", session.new)
    session.commit()