class Movie:
    def __init__(self, movie_id, name, director, language, rating):
        self.movie_id = movie_id
        self.name = name
        self.director = director
        self.language = language
        self.rating = rating

    def display(self):
        print("Movie ID:", self.movie_id)
        print("Movie Name:", self.name)
        print("Director:", self.director)
        print("Language:", self.language)
        print("Rating:", self.rating)
        print("-------------------")


m1 = Movie(1, "Titanic", "James Cameron", "English", 9)
m2 = Movie(2, "3 Idiots", "Rajkumar Hirani", "Hindi", 9)
m3 = Movie(3, "Avatar", "James Cameron", "English", 8)
m4 = Movie(4, "Dangal", "Nitesh Tiwari", "Hindi", 9)
m5 = Movie(5, "Jawan", "Atlee", "Hindi", 8)

m1.display()
m2.display()
m3.display()
m4.display()
m5.display()