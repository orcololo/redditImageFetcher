from utils.reddit_helper.fetcher import fetch_all_user_posts, get_subreddit
from utils.downloads.file_download import download_multiple


def main():
    path, links = get_subreddit('links', 'aww', None)
    download_multiple(path, links)


if __name__ == '__main__':
    main()
