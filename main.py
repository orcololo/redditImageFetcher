from utils.reddit_helper.fetcher import fetch_all_user_posts, get_subreddit


def main():
    path, links = get_subreddit('links', 'aww', 400)
    for link in links:
        print(link)


if __name__ == '__main__':
    main()
