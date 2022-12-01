#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mastodon import Mastodon
import json, logging, schedule, time

_client: Mastodon = None  # type: ignore

# load values from json formatted .config file
config = json.load(open(".config", 'r'))

def create() -> Mastodon:
	client: Mastodon
	try:
		logging.info("Creating client...")
		client = Mastodon(
				client_id = config["key"],
				client_secret = config["secret"],
				access_token = config["token"],
				api_base_url = config["api_base_url"],
				user_agent = "GUID Waster v2.0 (using mastodonpy)"
			)
	except Exception as error:
		logging.error(repr(error))
		exit()
	return client

def client_start():
	global _client
	if _client is None:
		_client = create()

def get_display() -> str:
	global current
	formatted = ""
	index = 0
	for d in current:
		if index in (8, 12, 16, 20):
			formatted += "-"
		# display single digit in hex
		formatted += format(d, "1X")
		index += 1
	return formatted

def guid_count_post():
	# get display formatted guid
	logging.info("formatting: %s", current)
	toot_text = get_display()
	logging.info("formatted: %s", toot_text)

	# make sure client exists
	client_start()
	_client.status_post(toot_text)
	# increment guid
	increment()

def scheduler_start():
	logging.info("Starting scheduler")
	schedule.every().day.at('12:01').do(guid_count_post)
	# use listener to read user stream
	while True:
		schedule.run_pending()
		time.sleep(1)

def main():
	global current
	logging.basicConfig(filename='guid_waster.log',
                     	format='%(asctime)s %(message)s',
											level=logging.DEBUG)
	logging.info("GUIDs wasted!")
	scheduler_start()

if __name__ == "__main__":
	main()
