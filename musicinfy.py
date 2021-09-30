import os, time,sys
from typing import OrderedDict
import requests,json
import pandas as pd
from t import *
from styless import *

col = Colors()
#globally used 
opt = ["n","no"]
user_data = {}
supported_formats = [".mp3",".mp4",".wav",".m4a"]
all_files = []
notfound = []
found = []
links = []
added_tracks = []
#musicinfy
musicinfy_full ="""

                  ============ MUSICINFY =============

"""
#types out
def prints(txt):
  for t in txt:
    time.sleep(.01)
    sys.stdout.write(t)
    sys.stdout.flush()
  print("\n")

#type out input text
def inputs(txt):
  prints(txt)
  print(col.red + user_data["display_name"]+ " > ", end="")
  return input()

#clears screen 
def clear_screen(): 
  os.system('cls' if os.name == 'nt' else 'clear')

#sends redirect notice
def redirect_notice():
  prints(col.green+musicinfy_full)
  prints("Welcome to Musicinfy!"+col.u_end)
  prints(col.purple+"""
  To get started we need you to allow us to make changes to your spotify 
  account (includes playlist creation, updation and deletion).
  And dont't worry this data isn't stored anywhere. 

  You will now be redirected to spotify authentication page.""")

#get profile 
def get_profile():
  profile_url = "https://api.spotify.com/v1/me"
  res = requests.request("GET", profile_url, headers=headers, data={})
  if res.status_code not in list(range(200,206)):
    prints(col.red+"Error "+str(res.status_code)+ ": "+res.reason)
    exit()
  else:
    user_data = res.json()
    return user_data

#get playlist info from user
def playlist_details():
  public = True
  prints(col.green + col.bold + "Thank you " + user_data["display_name"] +"! Now we need some details for the playlist that you wanna create."+ col.u_end)
  prints(col.yellow+ col.u_yellow +"Note that anything other than (yes/no), (y/n) [not case sesnsitive] would be considered a yes."+col.u_end)
  time.sleep(1)
  name_confirm = False
  while (not name_confirm):
    playlist_name = ""
    while playlist_name=="":
      playlist_name = inputs(col.blue+"Please enter the name you wanna give to the playlist: ")
      clear_screen()
    req_desc = inputs(col.blue+"Do you want to give the playlist a description? (Y/N) ")
    clear_screen()
    if req_desc.lower() not in opt:
      desc = inputs(col.blue+"Please enter the description: ")
      clear_screen()
    else: desc =""
    if inputs(col.blue+"Do you want to make the playlist private? (Y/N) ").lower() not in opt:
      public = False
    clear_screen()
    prints("Please confirm the details below:")
    prints("Playlist name: "+ playlist_name)
    if req_desc.lower() not in opt:
      prints("Playlist description: "+ desc)
    else: prints("No description provided.")
    if public:
      prints("The playlist will be public.")
    else: prints("The playlist will be private.")
    inp = inputs(col.blue+"Do you confirm the details? (Y/N) ")
    clear_screen()
    if inp.lower() not in opt:
      name_confirm =  True 
    else: prints("Please enter modified details.")
  return playlist_name , desc ,public

#playlist creation
def create_playlist():
  prints("Creating playlist...")
  clear_screen()
  create_playlist_url = "https://api.spotify.com/v1/users/"+id+"/playlists?="
  new_headers = headers
  new_headers["Content-Type"] = "application/json"
  data = json.dumps({
  "name": playlist_name,
  "description": desc,
  "public": public
  })
  res = requests.request("POST", create_playlist_url, headers=headers, data=data)
  if res.status_code not in list(range(200,206)):
    print (col.red+"Error "+str(res.status_code)+ ": "+res.reason)
    exit()
  else:
    time.sleep(0.05)
    prints("Playlist successfully created!")
    time.sleep(0.2)
    clear_screen()
    return res.json()["id"]

#fetches file name from the given location
def fetch_file_names():
  fpath = None #default
  path_input = inputs(col.blue+"Enter the absolute location of the folder with all the song files (press enter if it's in the root directory): ")
  if path_input:
    fpath = path_input
  # files = next(os.walk(fpath))[2]
  allfiles = [i for i in os.listdir(fpath) if i[-4:] in supported_formats]
  return allfiles

#format the retrieved file name into meaningful search terms
def format_name(name):
  arr_name_bits = name[:-4].replace(" ","_").replace(".","").split("_")
  tmp = arr_name_bits
  arr_name_bits = [b for b in tmp if not b.isnumeric()]
  formatted_name = " ".join(arr_name_bits)
  return formatted_name

# #searches the link from fetch link response
# def get_link_from_respose(res):
#   #
#   return res["tracks"].items[0].href 
#   #check for tracks keyword in url


#searches for the song via api
def fetch_song_link(name,formatted_name):
  clear_screen()
  prints("Now searching "+formatted_name+" on spotify...")
  clear_screen()
  prints("......")
  if "-" in formatted_name:
    sub_name = formatted_name.split("-")[1]
  else: sub_name = formatted_name
  url = "https://api.spotify.com/v1/search?q="+ sub_name+ "&type=track&limit=5"
  res = requests.request("GET", url, headers=headers, data={})
  link = ""
  if res.status_code in list(range(200,206)):
    if not res.json()["tracks"]["items"]:
      notfound.append(name)
      files.remove(name)
    else:
      prints("Track found.")
      clear_screen()
      found.append(name)
      all_files.append(formatted_name)
      # print(res.json()["tracks"]["items"][0]["href"])
      link = res.json()["tracks"]["items"][0]["external_urls"]["spotify"]
      links.append(link)
    return link
  else:
    prints(col.red+"Error "+str(res.status_code)+ ": "+res.reason)
    exit()

#exports songs 
def export_report_for_found_songs():
  merged = list(zip(found,links))
  df = pd.DataFrame(merged, columns=["Name","Link to spotify"])
  df.to_csv("success_report.csv")

#list of not found
def dump_unfound():
  df = pd.DataFrame(notfound, columns=["Name"])
  df.to_csv("dump.csv")
#gets uri for post  request
def get_uri(link):
  chk = "spotify:track:"+link.split("/")[len(link.split("/"))-1]
  return chk

#add to spotify playlist by link
def add_by_link(link):
  url = "https://api.spotify.com/v1/playlists/"+created_playlist_id+"/tracks?uris="+get_uri(link)
  res = requests.request("POST", url, headers=headers, data={})
  if res.status_code not in list(range(200,206)):
    prints(col.red+"Error "+str(res.status_code)+ ": "+res.reason+ ". Track wasn't added to playlist.")
    return False
  else:
    return True

#adding the tracks to the created playlist
def add_to_playlist():
  clear_screen()
  prints("Adding fetched songs to the playlist. Please wait..")
  time.sleep(0.05)
  clear_screen()
  prints("......")
  clear_screen()
  prints("......")
  clear_screen()
  prints("......")
  for name in files:
    formatted_name = format_name(name)
    link = fetch_song_link(name,formatted_name)
    if link != "":
      prints("Now adding "+ formatted_name +" to your playlist..." )
      clear_screen()
      added = add_by_link(link)
      if added:
        added_tracks.append(link)
        prints(formatted_name + " was just added to your playlist. Onto the next one now")
      else: 
        prints(formatted_name+" could not be added to your playlist.")
  prints("Playlist update successful!")
  time.sleep(0.6)
  prints("Exporting information as csv...")
  clear_screen()
  export_report_for_found_songs()
  dump_unfound()
  prints("Export successful.")
  time.sleep(0.2)
  clear_screen()
  prints("You can now enjoy your old tracks and get nostalgic. \nThank you for using me.")

clear_screen()
redirect_notice()
time.sleep(5)
auth_token, refresh_token = Auth().user_authentication()
# headers
headers = {
    "Authorization": f"Bearer {auth_token}"
  }

clear_screen()
print(auth_token)
time.sleep(5)
user_data = get_profile()
id = user_data["id"]
playlist_name , desc ,public = playlist_details()
created_playlist_id = create_playlist()
files = fetch_file_names()
add_to_playlist()
# i=0
# for link in links:
#   i+=1
#   print(str(i)+ " : "+link) 