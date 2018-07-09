

class Movie:
    def __init__(self, movie_title, movie_storyline, poster_cover, poster_image, trailer_link, rating, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_cover
        self.thumbnail = poster_image
        self.trailer_youtube_url = trailer_link
        self.rating = rating
        self.release_date = release_date
