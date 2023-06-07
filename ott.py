import sys;
import sqlite3;
import re  

conn=sqlite3.connect("ott.db")
cur=conn.cursor()

# Define a base class for media content
class MediaContent:
    def __init__(self, title, director, genre, rating, year):
        self.__title = title
        self.__director = director
        self.__genre = genre
        self.__rating = rating
        self.__year = year

    # Define get and set functions for the title, director, genre, rating, and year
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_director(self):
        return self.__director

    def set_director(self, director):
        self.__director = director

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def display_details(self):
        print(f"Title: {self.__title}")
        print(f"Director: {self.__director}")
        print(f"Genre: {self.__genre}")
        print(f"Rating: {self.__rating}")
        print(f"Year: {self.__year}")

# Define a subclass for movies that inherits from the base MediaContent class
class Movie(MediaContent):
    def __init__(self,title, director, genre, rating, year, duration):
        super().__init__(title, director, genre, rating, year)
        self.__duration = duration

    # Define get and set functions for the duration
    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def display_details(self):
        super().display_details()
        print(f"Duration: {self.__duration} mins")

# Define a subclass for TV shows that inherits from the base MediaContent class
class TVShow(MediaContent):
    def __init__(self, title, director, genre, rating, year, seasons, episodes):
        super().__init__(title, director, genre, rating, year)
        self.__seasons = seasons
        self.__episodes = episodes

    # Define get and set functions for the seasons and episodes
    def get_seasons(self):
        return self.__seasons

    def set_seasons(self, seasons):
        self.__seasons = seasons

    def get_episodes(self):
        return self.__episodes

    def set_episodes(self, episodes):
        self.__episodes = episodes

    def display_details(self):
        super().display_details()
        print(f"Seasons: {self.__seasons}")
        print(f"Episodes: {self.__episodes}")


class Series(MediaContent):
    def __init__(self, title, director, genre, rating, year, language,subtitles):
        super().__init__(title, director, genre, rating, year)
        self.__language = language
        self.__subtitles = subtitles

    # Define get and set functions for the seasons and episodes
    def get_language(self):
        return self.__language

    def set_language(self, language):
        self.__language = language

    def get_subtitles(self):
        return self.__subtitles

    def set_subtitles(self, subtitles):
        self.__subtitles = subtitles

    def display_details(self):
        super().display_details()
        print(f"Language: {self.__language}")
        print(f"Subtitles: {self.__subtitles}")



# Define a function to add a new movie to the database
def add_movie():
    #conn.execute('''create table movies(title text,director text,genre text,rating number,year number,duration text)''')
    title = input("Enter the title: ")
    director = input('Enter the director: ')
    genre=input('enter the genre: ')
    rating=input('enter the rating:')
    year=input('enter the year: ')
    duration=input('enter the duration: ')
    mobj=MediaContent(title, director, genre, rating, year)
    movobj=Movie(title, director, genre, rating, year,None)
    movobj.set_duration(duration)
   
    conn.execute('insert into movies values(?,?,?,?,?,?)',(movobj.get_title(),movobj.get_director(),movobj.get_genre(),movobj.get_rating(),movobj.get_year(),movobj.get_duration()))
    print("Movie Added")
def add_tv():
    #conn.execute('''create table tv(title text,director text,genre text,rating number,year number,seasons number,episodes number)''')
    title = input("Enter the title: ")
    director = input('Enter the director: ')
    genre=input('enter the genre: ')
    rating=input('enter the rating:')
    year=input('enter the year: ')
    seasons=input('enter the season: ')
    episodes=input('enter the episodes: ')
    mobj=MediaContent(title, director, genre, rating, year)
    tvobj=TVShow(title, director, genre, rating, year,None,None)
    tvobj.set_seasons(seasons)
    tvobj.set_episodes(episodes)
   
    conn.execute('insert into tv values(?,?,?,?,?,?,?)',(tvobj.get_title(),tvobj.get_director(),tvobj.get_genre(),tvobj.get_rating(),tvobj.get_year(),tvobj.get_seasons(),tvobj.get_episodes()))
    print("TV Show added")
def add_series():
    #conn.execute('''create table series(title text,director text,genre text,rating number,year number,language text,subtitles text)''')
    title = input("Enter the title: ")
    director = input('Enter the director: ')
    genre=input('enter the genre: ')
    rating=input('enter the rating:')
    year=input('enter the year: ')
    language=input('enter the language: ')
    subtitles=input('enter the subtitles: ')
    mobj=MediaContent(title, director, genre, rating, year)
    serobj=Series(title, director, genre, rating, year,None,None)
    serobj.set_language(language)
    serobj.set_subtitles(subtitles)
   
    conn.execute('insert into series values(?,?,?,?,?,?,?)',(serobj.get_title(),serobj.get_director(),serobj.get_genre(),serobj.get_rating(),serobj.get_year(),serobj.get_language(),serobj.get_subtitles()))
   
    print("Series added")
def display(a,b,c):
    cur.execute("SELECT * FROM %s where %s=?" % (a,b), (c,))
    records=cur.fetchall()
    for n in records:
        print("Title: ",n[0],"\nDirector: ",n[1],"\nGenre: ",n[2],"\nrating: ",n[3],"\nyear: ",n[4])
        if(a=='movies'):
            print("\nDuration: ",n[5])
        elif a=='tv':
            print("\nSeasons: ",n[5],"\nEpisodes: ",n[6])
        else:
            print("\nLanguage: ",n[5],"\nSubtitles: ",n[6])
    
def get_choice():
    print("1. Add Movie")
    print("2. Add TV Show")
    print("3. Add Series")
    print("4. Display Based on:")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        add_movie()
    elif choice==2:
        add_tv()
    elif choice==3:
        add_series();
    elif choice==4:
        a=input('enter your choice(movies,tv,series): ')
        if a=='movies':
            b=input('enter on what basis you want to search(title, director, genre, rating, year, duration): ')
        elif a=='tv':
            b=input('enter on what basis you want to search(title, director, genre, rating, year, seasons, episodes): ')
        elif a=='series':
            b=input('enter on what basis you want to search(title, director, genre, rating, year, language, subtitles): ')
        c=input('enter the value: ')
        display(a,b,c)
    else:
        print('HAPPY NETFLIX AND CHILL::::')
        sys.exit
while(1):
    get_choice()

