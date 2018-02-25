import webbrowser
class Movie():
    def __init__(self,title,director,story,trailer):
        self.title = title
        self.director = director
        self.story = story
        self.trailer = trailer
    def show_trailer(self):
        webbrowser.open(self.trailer)
