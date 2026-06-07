print("Welcome to XCinema. These are our movies for today:\n")

movies = {"movie1": "1hr 13m",
            "movie2": "1hr 45m",
            "movie3": "2hr 21m",
            "movie4": "55m"}
movies_num = {1: "movie1",
            2: "movie2",
            3: "movie3",
            4: "movie4"}
s=1
for movie in movies:
    print(str(s) + "." + movie + "\n")
    s=s+1

usr_opinion_time = input("Would you like to see times of film. If would you like, choose number of film\n") 
if usr_opinion_time:
    for i in movies_num:
        if usr_opinion_time == str(i):
            selected_movies = movies_num.get(i)
            print("Time of " + selected_movies + " is " + movies.get(selected_movies))
        continue
    if not selected_movies:
        print("You don't choose right number of film") 

else:    print("You don't want to see times of film")

