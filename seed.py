import model
import csv


def load_users(session):
    table = open("seed_data/u.user")
    all_lines_lists = table.read().splitlines()
    new_list = []
    for line in all_lines_lists:  
        new_list.append(line.split('|'))
    
    for l in new_list: 
        new_user = model.User(id=l[0], age=l[1], zipcode=l[4])
        session.add(new_user)
    
    session.commit()

def load_movies(session):
    table = open("seed_data/u.item").read().splitlines()
    new_list = []
    for line in table:
        new_list.append(line.split('|'))

    for l in new_list:
        l[1] = l[1][:-6].strip() 
        new_movie = model.Movies(id=l[0], name=l[1], release_date =l[2], imdb_url=l[3])
        session.add(new_movie)

    session.commit()

def load_ratings(session):
    table = open("seed_data/u.data").read().splitlines()
    new_list = []
    for line in table:
        new_list.append(line.split())
    
    for l in new_list:
        new_rating = model.Ratings(user_id=l[0], movie_id=l[1], rating=l[2])
        session.add(new_rating)

    session.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    pass

if __name__ == "__main__":
    s= model.connect()
    main(s)
