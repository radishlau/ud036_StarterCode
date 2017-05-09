import webbrowser

class Movie(object):
	""" This class provides a way to store movie related information."""
	
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
		
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = "https://www.youtube.com/watch?v=" + trailer_youtube
		
		pass

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
		pass


		