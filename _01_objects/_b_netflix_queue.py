class Movie:
    def __init__(self, title, stars):
        self.title = title
        self.stars = stars

    def to_string(self):
        return "\"" + self.title + "\" - " + str(self.stars) + " stars"

    def get_ticket_price(self):
        if self.stars > 2:
            return "That will be $12 please."
        elif 'twilight' in self.title.lower():
            return "This movie is so bad, we'll pay YOU to watch it!"
        else:
            return "Don't waste your money on this horrible rubbish."


class NetflixQueue:
    def __init__(self):
        self.movies = list()

    def get_best_movie(self):
        self.sort_movies_by_rating()
        return self.movies[0]

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movie(self, movie_number):
        return self.movies[movie_number]
    def get_second_best_movie(self):
        self.sort_movies_by_rating()
        return self.movies[1]

    def sort_movies_by_rating(self):
        self.movies.sort(key=lambda movie: movie.stars, reverse=True)

    def print_movies(self):
        print("Your Netflix queue contains: ")

        for movie in self.movies:
            print(movie.to_string())


if __name__ == '__main__':

    # Use Movie and NetflixQueue classes above to complete the following changes:

    # 1. Instantiate some Movie objects (at least 5).
    insideOut = Movie('Inside Out', 4.5)
    maxSteel = Movie('Max Steel', 1)
    emojiMovie = Movie('Emoji Movie', 2)
    happyFeet = Movie('Happy Feet', 4)
    sonicMovie = Movie('Sonic Movie', 3.5)
    # 2. Use the Movie class to get the ticket price of one of your movies.
    print(insideOut.get_ticket_price())

    # 3. Instantiate a NetflixQueue.
    netflixQueue = NetflixQueue()
    # 4. Add your movies to the Netflix queue.
    netflixQueue.add_movie(insideOut)
    netflixQueue.add_movie(maxSteel)
    netflixQueue.add_movie(emojiMovie)
    netflixQueue.add_movie(happyFeet)
    netflixQueue.add_movie(sonicMovie)

    # 5. Print all the movies in your queue.
    netflixQueue.print_movies()
    # 6. Use your NetflixQueue object to finish the sentence "the best movie is...."
    print('The best movie is ' + netflixQueue.get_best_movie().to_string())
    # 7. Use your NetflixQueue to finish the sentence "the second best movie is...."
    print('The second best movie is ' + netflixQueue.get_second_best_movie().to_string())
