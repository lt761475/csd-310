#Leon Trong, 11/20/2026, 6.2 Assignment

""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode
 
import dotenv # to use .env file
from dotenv import dotenv_values


#using our .env file
secrets = dotenv_values(".env")
 
""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}
#MySQL: mysql_test.py. Connection test codetry:
try:
    """ try/catch block for handling potential MySQL database errors """ 
 
    db = mysql.connector.connect(**config) # connect to the movies database 
    
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    db_cursor = db.cursor() #create curser name for execution
    
    
    #Query 1
    
    db_cursor.execute("SELECT * FROM studio") #mysql query
    studios = db_cursor.fetchall() #get results
    print("\n--DISPLAYING Studio RECORDS--")
    for studio in studios: #display studios
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0],studio[1]))
        
        
    #Query 2
    
    db_cursor.execute("SELECT * FROM genre") #mysql query
    genres = db_cursor.fetchall() #get genres
    print("\n--DISPLAYING Studio RECORDS--")
    for genre in genres: #display genre
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0],genre[1]))
        
    
    #Query 3
    
    db_cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120") #mysql query
    
    shortFilms = db_cursor.fetchall() #get short films
    print("\n--DISPLAYING Short Film RECORDS--")
    for shortFilm in shortFilms: #display short films
        print("Film Name: {}\nRuntime: {}\n".format(shortFilm[0],shortFilm[1]))
        

    #query 4

    db_cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director") #mysql query
    
    directors = db_cursor.fetchall() #get directors
    print("\n--DISPLAYING director RECORDS--")
    for director in directors: #display directors
        print("Film Name: {}\nDirector: {}\n".format(director[0],director[1]))
        
    
 
except mysql.connector.Error as err:
    """ on error code """
 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
 
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
 
    else:
        print(err)
 
finally:
    """ close the connection to MySQL """
 
    db.close()
