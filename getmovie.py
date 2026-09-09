#!/usr/bin/env python3

from urllib.parse import quote
import sys
import os
import argparse
import requests

YTS_API = "https://movies-api.accel.li/api/v2"
QB_URL = os.getenv('BITTORRENT_URL', '')
QB_API_KEY = os.getenv('BITTORRENT_API_KEY', '')

TRACKERS = [
    "udp://open.demonii.com:1337/announce",
    "udp://tracker.openbittorrent.com:80",
    "udp://tracker.coppersurfer.tk:6969",
    "udp://glotorrents.pw:6969/announce",
    "udp://tracker.opentrackr.org:1337/announce",
    "udp://torrent.gresille.org:80/announce",
    "udp://p4p.arenabg.com:1337",
    "udp://tracker.leechers-paradise.org:6969",
]


def search_movies(query: str, limit: int = 5, page: int = 0) -> list[dict]:
	resp = requests.get(
		f"{YTS_API}/list_movies.json",
		params={"query_term": query, "limit": limit, "page": page}
	)
	resp.raise_for_status()
	data = resp.json()["data"]
	return data.get("movies") or []

def pick_torrent(torrents: list[dict]) -> dict | None:
	# Prefer 1080p BluRay, then 1080p, then 720p
	for quality, source in [("1080p", "bluray"), ("1080p", None), ("720p", None)]:
		for t in torrents:
			if t["quality"] == quality:
				if source is None or source in t.get("type", "").lower():
					return t
	return None

def build_magnet(hash: str, name: str, year: str, quality: str) -> str:
	dn = quote(f"{name} ({year}) [{quality}]")
	trackers = "&".join(f"tr={quote(t)}" for t in TRACKERS)
	return f"magnet:?xt=urn:btih:{hash}&dn={dn}&{trackers}"

def add_to_qbittorrent(magnet: str) -> None:
	headers = {"Authorization": f"Bearer {QB_API_KEY}", "Referer": QB_URL}
	resp = requests.post(
		f"{QB_URL}/api/v2/torrents/add",
		headers=headers,
		data={"urls": magnet, "savepath": "/movies", "seedingTimeLimit": 15}
	)
	if resp.status_code != 200:
		sys.exit(f"Failed to add torrent: {resp.status_code} {resp.text}")

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("query", type=str, help="movie search term")
	parser.add_argument("-s", "--selection", required=False, type=int, help="selection number if multiple movies match query")
	parser.add_argument("-n", "-c", "--count", required=False, type=int, default=5, help="max options to display")
	parser.add_argument("-p", "--page", required=False, type=int, default=0, help="page selection if many movies match query")

	args = parser.parse_args()

	movies = search_movies(
		query=args.query,
		limit=args.count,
		page=args.page,
	)

	if len(movies) == 0:
		sys.exit(f"No results for '{args.query}'")

	if len(movies) > 1 and args.selection is None:
		print(f"\nSpecify which movie:")
		for i, m in enumerate(movies, 1):
			print(f"  {i}. {m['title_long']}")
		print()
		return

	movie_selection = movies[0 if args.selection is None else args.selection-1]
	torrent = pick_torrent(movie_selection["torrents"])
	if not torrent:
		sys.exit(f"No HD torrents available for {movie_selection['title']}")

	magnet = build_magnet(
		hash=torrent["hash"],
		name=movie_selection["title"],
		year=movie_selection["year"],
		quality=torrent["quality"]
	)
	print(f"\nAdding {movie_selection['title']} ({movie_selection['year']}) to Jellyfin...")
	add_to_qbittorrent(magnet)
	print(f"{movie_selection['title']} will be ready soon!\n")


if __name__ == "__main__":
	main()
