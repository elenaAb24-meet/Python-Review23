def create_youtube_video (title, description):

youtube_video={'Title': title, 'Description': description, 'likes' : 0 , 'Dislikes': 0 , 'comments':{'Username' : ''}}

return youtube_video
def likes(youtube_video):
	if 'likes' in youtube_video:
		likes +=1
		return youtube_video

def dislikes(youtube_video):
	if 'dislikes' in youtube_video:
		dislikes +=1
		return youtube_video

def add_comment(youtube_video, username, comment_text)

	comments={'username':comment_text}
	return comments

	youtube = create_youtube_video('How to make slime', 'slime with no borax')

	print(youtube)