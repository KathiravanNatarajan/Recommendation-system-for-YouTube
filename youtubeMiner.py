from apiclient.discovery import build #pip install google-api-python-client
from apiclient.errors import HttpError #pip install google-api-python-client
import pandas as pd #pip install pandas
import oauth2client.tools as oauthtools
# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
# https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

DEVELOPER_KEY = "AIzaSyDocqHwYw1G1wpJ6wTL80N5cyAleFfiNvo" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(words):
	reload(oauthtools) # changing argument of argparser did not work
	oauthtools.argparser.add_argument("--q", help="Search term", default=words)
	#change the default to the search term you want to search
	oauthtools.argparser.add_argument("--max-results", help="Max results", default=50)
	#default number of results which are returned. It can very from 0 - 100
	args = oauthtools.argparser.parse_args()
	options = args
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
	# Call the search.list method to retrieve results matching the specified
	 # query term.
	search_response = youtube.search().list(
	 q=options.q,
	 type="video",
	 part="id,snippet",
	 maxResults=options.max_results
	).execute()

	videos = {}
	# Add each result to the appropriate list, and then display the lists of
	 # matching videos.
	 # Filter out channels, and playlists.
	for search_result in search_response.get("items", []):
	 if search_result["id"]["kind"] == "youtube#video":
	 #videos.append("%s" % (search_result["id"]["videoId"]))
	    videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]
	#print "Videos:\n", "\n".join(videos), "\n"
	s = ','.join(videos.keys())
	videos_list_response = youtube.videos().list(
	 id=s,
	 part='id,statistics'
	).execute()
	#videos_list_response['items'].sort(key=lambda x: int(x['statistics']['likeCount']), reverse=True)
	#res = pd.read_json(json.dumps(videos_list_response['items']))
	res = []
	for i in videos_list_response['items']:
	 temp_res = dict(v_id = i['id'], v_title = videos[i['id']])
	 temp_res.update(i['statistics'])
	 res.append(temp_res)
	df = pd.DataFrame.from_dict(res)
	df.to_csv('YTlaughable123.csv', mode='a',encoding='utf-8')



terms = ["laugh", "prank", "funny", "humorous", "ludicrous", "ridiculous", "joking", \
  "amusing", "fun", "for grins", "humor", "comical", "jolly", "hilarious",  "witty", \
  "comic", "droll", "facetious", "jocular", "jokey", "chuckle", "goofy", "chortle", \
  "wacky"]
for i in terms:
	youtube_search(i)