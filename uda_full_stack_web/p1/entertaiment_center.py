import fresh_tomatoes
import media

# Creating movies to describe the instances of the Class Movie
Intersteller = media.Movie(
        "Intersteller",
        """A team of explorers travel through a 
        wormhole in space in an attempt to ensure
         humanity's survival.""",
        "https://goo.gl/4eDrwk",  # Noqa
        "https://www.youtube.com/watch?v=zSWdZVtXT7E")

avatar = media.Movie(
        "Avatar",
        """A marine on an alien planet""",
        "https://goo.gl/YzM3LO", # Noqa
        "https://www.youtube.com/watch?v=-9ceBgWV8io")

the_godfather = media.Movie(
        "The Godfather",
        """The aging patriarch of an organized
         crime dynasty transfers control of his
          clandestine empire to his reluctant son.""",
        "https://goo.gl/sEQhNw", # Noqa
        "https://www.youtube.com/watch?v=sY1S34973zA")

the_shawshank_redemption = media.Movie(
        "Shawshank Redemption",
        """Two imprisoned men bond over a number 
        of years, finding solace and eventual 
        redemption through acts of common decency.""",
        "https://goo.gl/qdrr5e",  # Noqa
        "https://www.youtube.com/watch?v=T2aqnt_EyrA") # 

schindlers_List = media.Movie(
        "Schindler's List",
        """Two imprisoned men bond over a number 
        of years, finding solace and eventual redemption
         through acts of common decency.""",
        "https://goo.gl/Hxmd3r", # Noqa
        "https://www.youtube.com/watch?v=m2hJ1spax6Y")

inception = media.Movie(
        "Inception",
        """Two imprisoned men bond over a number of 
        years, finding solace and eventual redemption
         through acts of common decency.""",
        "https://goo.gl/cE6K5x", # Noqa
        "https://www.youtube.com/watch?v=8hP9D6kZseM")

# Movies array, contains the list of movies as input, which
# is passed to the function "open_movies_page". This function
# translates this list into a web page when we run the
# "entertainment_center.py" file.
# 
movies = [the_shawshank_redemption, 
        schindlers_List, 
        inception, 
        Intersteller, 
        avatar, 
        the_godfather]
        
fresh_tomatoes.open_movies_page(movies)
