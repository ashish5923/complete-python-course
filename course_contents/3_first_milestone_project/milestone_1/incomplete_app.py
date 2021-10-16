# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = ['Deadpool','jhbd','2010',
          'ironman','robert',2009
]


def add.movies():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })



def list.movies():
    for movie in movies:
        print(f"tittle:{movie[tittle]}")
        print(f"Director:{movie[Director]}")
        print(f"Year:{movie[Year]}")

    
def find.movies():
    search_tittle = input("enter your tittle")
    if movie["tittle"] == search_tittle:
        print(f"tittle:{movie[tittle]}")
        print(f"Director:{movie[Director]}")
        print(f"Year:{movie[Year]}")
def menu():        
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add.movies()

        elif selection == "l":
            list.movies()

        elif selection == "f":
            find.movies()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)
        
menu()



