class Movie:
    def __init__(self, title: str, year: int, time: str, rating: float,
                 rating_count: int, top_250_rating: int, image_url: str):
        self.title = title
        self.year = year
        self.time = time
        self.rating = rating
        self.rating_count = rating_count
        self.top_250_rating = top_250_rating
        self.image_url = image_url

    def __str__(self):
        return (f'{self.time}, ({self.year}), {self.time}, {self.rating},'
                f'{self.rating_count}, {self.top_250_rating}')
