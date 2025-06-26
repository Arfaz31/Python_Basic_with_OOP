from abc import ABC, abstractmethod

class Description:
    def __init__(self, description):
        self.__description = description  # private attribute

    def get_description(self):
        return self.__description

class Media(ABC):
    def __init__(self, title, duration):  
        self.title = title
        self.duration = duration

    @abstractmethod
    def play(self): 
        pass

class Music(Media, Description): # multiple inheritance
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)

    def play(self):
        print(f"Playing Music {self.title}")
    
    def info(self):
        print(f"Title: {self.title} - Duration: {self.duration} - Description: {self.get_description()}")


class Video(Media, Description): # multiple inheritance
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)

    def play(self):
        print(f"Playing Video {self.title}")
    
    def info(self):
        print(f"Title: {self.title} - Duration: {self.duration} - Description: {self.get_description()}")

class AudioBook(Media, Description): # multiple inheritance
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)

    def play(self):
        print(f"Playing AudioBook {self.title}")
    
    def info(self):
        print(f"Title: {self.title} - Duration: {self.duration} - Description: {self.get_description()}")

class Library:
    def __init__(self):
        self.__media_items = []
        self.__media_by_genre = {}
        self.__genre = ""


    def get_media_items(self):
        return self.__media_items

    def get_media_by_genre(self):
        return self.__media_by_genre
    

    def add_media(self, media):
        if isinstance(media,Music):
            self.__genre = "Music"
        if isinstance(media,Video):
            self.__genre = "Video"
        if isinstance(media,AudioBook):
            self.__genre = "AudioBook"


        if self.__genre in self.__media_by_genre:
            self.__media_by_genre[self.__genre].append(media)  #if the genre is already in the dictionary add the media
        else:
            self.__media_by_genre[self.__genre] = [media,] # if the genre is not in the dictionary create a new key and add the media
        self.__media_items.append(media)
        

class User(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def play_media(self):
        pass

class FreeUser(User):
    def __init__(self, name):
        super().__init__(name)
        print("User name:", self.get_name())

    def play_media(self, library):
        for media in library.get_media_items():
            media.play()

class PremiumUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.__favourite_genre =""

    def set_favourite_genre(self, genre):
        self.__favourite_genre = genre

    def get_favourite_genre(self):
       return self.__favourite_genre


    def play_media(self, library):
       if self.__favourite_genre in library.get_media_by_genre(): 
        for media in library.get_media_by_genre()[self.__favourite_genre]: 
            media.play()
       else:
        print("No media available in this genre")
    

  


# Create object and test
library = Library()
music1 = Music("The Starry Night", "8", "Vincent Van Gogh")
video = Video("The Matrix", "2", "Action")
audio = AudioBook("The Lord of the Rings", "3", "Fantasy")
library.add_media(music1)
library.add_media(video)
library.add_media(audio)

free_user = FreeUser("John")
free_user.play_media(library)

premium_user = PremiumUser("Jane")
# premium_user.set_favourite_genre("Music")
# premium_user.play_media(library)
