class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre_value):
        if genre_value not in cls.genres:
            cls.genres.append(genre_value)
        else:
            print("Genre already exists.")
    @classmethod
    def add_to_artists(cls, artist_value):
        if artist_value not in cls.artists:
            cls.artists.append(artist_value)
        else:
            print("Artist already exists.")

    @classmethod
    def add_to_genre_count(cls, genre_count_value):
        if genre_count_value not in cls.genre_count:
            cls.genre_count[genre_count_value] = 1
        else:
            cls.genre_count[genre_count_value] += 1
    
    @classmethod
    def add_to_artists_count(cls, artist_count_value):
        if artist_count_value not in cls.artist_count:
            cls.artist_count[artist_count_value] = 1
        else:
            cls.artist_count[artist_count_value] += 1
