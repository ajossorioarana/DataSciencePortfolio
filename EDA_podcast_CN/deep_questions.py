import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'a53c2653cd49444dbd820d6f3e143d74'
secret = '24a5ef4308e94cb7921757ce7722e752'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Create a list of podcast episodes

podcast_id = '0e9lFr3AdJByoBpM6tAbxD' # Hard-coded podcast id
endpoint_url = 'https://api.spotify.com/v1/search' 

podcast = sp.show(podcast_id, market='US')  # Obtain podcast info
total_episodes = podcast['total_episodes']  # Obtain total number of episodes

eps_ids = []
eps_names = []
eps_desc = []
eps_duration = []
eps_release_date = []
eps_ext_url = []
eps_uri = []

counter = 1
offset = 0
rounds = total_episodes//50 + 1

while counter <= rounds:

    episodes = sp.show_episodes(podcast_id, limit=50, offset=offset, market='US')

    for episode in episodes['items']:
        eps_ids.append(episode['id'])
        eps_names.append(episode['name'])
        eps_desc.append(episode['description'])
        eps_duration.append(episode['duration_ms'])
        eps_release_date.append(episode['release_date'])
        eps_ext_url.append(episode['external_urls'])
        eps_uri.append(episode['uri'])

    counter += 1
    offset += 50

all_ep = pd.DataFrame()

all_ep['id'] = eps_ids
all_ep['name'] = eps_names
all_ep['description'] = eps_desc
all_ep['duration_ms'] = eps_duration
all_ep['release_date'] = eps_release_date
all_ep['external_url'] = eps_ext_url
all_ep['uri'] = eps_uri

aux_df = all_ep['name'].str.extract(r'(?P<ep_header>Ep.\s+)(?P<num_ep>\d+)(?P<connector>:\s+)(?P<title>.*)')
aux_df.drop(columns=['ep_header', 'connector'], inplace=True)
all_ep.drop(columns='name', inplace=True)

all_ep = pd.concat([all_ep, aux_df], axis=1)

search_terms = ['career', 'plan']

df = all_ep

for term in search_terms:
    df = df.loc[df['description'].str.contains(term, case=False)]

print(df)