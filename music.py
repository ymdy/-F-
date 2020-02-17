from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import os
import test

class Music():

  def youtube_search(self, options):
      #APi使用において必要な設定
      DEVELOPER_KEY = "AIzaSyD08VCKuLEo3JkL0ClICg9ytHXRVjJfuKk"
      YOUTUBE_API_SERVICE_NAME = "youtube"
      YOUTUBE_API_VERSION = "v3"
      videoinfomation = []
      youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
      developerKey=DEVELOPER_KEY)

      #youtube data apiのserch関数で検索かけてます。optionsの中身に関してはsetkeywords参照
      search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
      ).execute()

      videos = []
      channels = []
      playlists = []

      #リスト形式で帰ってきた検索結果の属性がvideoであるもののみ格納しています。
      for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
          videoinfomation.append(search_result["snippet"]["title"])
          videoinfomation.append(search_result["id"]["videoId"])
          videoinfomation.append(search_result["snippet"]["thumbnails"]["high"]["url"])

      #もし該当する動画がなかった場合にここで処理を終了させてもよかったんですが、何となく検索結果0を反すようにしました。
      if len(videoinfomation) == 0:
          videoinfomation[0] = '検索結果0'
          videoinfomation[1] = 'NULL'

      return videoinfomation

  def setkeywords(self, serch_keyword):
      try:
          #youtube.serch().list().execute()に投げるコマンドラインの生成
          argparser.add_argument("--q", help="Search term", default=serch_keyword + 'の日に聞きたい曲')
          argparser.add_argument("--max-results", help="Max results", default=50)
          args = argparser.parse_args()
          result = Music.youtube_search(0, args)
          return result

      except HttpError as e:
          print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
