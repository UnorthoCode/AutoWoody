#!/user/bin/env python
import requests
import shutil
def main():
	params = {
		'client_id' : '<YOURCLIENTIDHERE>',
		'limit' : 1,
		'offset' : 0,
		'linked_partitioning' : 1,
		'app_version' : 1532422103,
		'app_locale' : 'en'
	}

	r = requests.get('https://api-v2.soundcloud.com/stream/users/142410747', params=params)
	
	track_data = r.json()['collection'][0]['track']
	
	title = track_data['title']
	print('Title:\t\t{}'.format(title))
	print('Description\t{}'.format(track_data['description']))
	print('Created\t\t{}'.format(track_data['created_at']))
	print('Duration\t{}'.format(track_data['duration']))
	print('Download URL:\t{}'.format(track_data['download_url']))
	print('Downloading...')
	
	media_file = requests.get(track_data['download_url'], params={'client_id' : '<YOURCLIENTIDHERE>'}, stream=True)
	
	with open(title + '.mp3', 'wb') as out_file:
		shutil.copyfileobj(media_file.raw, out_file)
	
	print('Done')
if __name__ == "__main__":
	main()