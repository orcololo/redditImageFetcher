from utils.reddit_helper.reddit import reddit
from utils.checks.submissions_check import check_submission
from utils.checks.dir_checker import check_if_dir_exists
from utils.checks.filter import filter_links


def fetch_all_user_posts(username, posts_limit=10):
    user_path = check_if_dir_exists(username, "user")
    download_links = list()
    user = reddit.redditor(username)
    submissions = user.submissions.hot(limit=posts_limit)
    for item in submissions:
        if check_submission(item):
            download_links.append(item.url)
    return user_path, filter_links(download_links)


def get_subreddit(action_type, sub_name, posts_limit=100):
    sub_path = check_if_dir_exists(sub_name, "subreddit")
    if action_type == 'users':
        user_list = list()
        posts = reddit.subreddit(sub_name).hot(limit=posts_limit)
        for post in posts:
            if check_submission(post):
                user_list.append(post.author.name)
        return user_list

    if action_type == "links":
        download_links = list()

        posts = reddit.subreddit(sub_name).hot(limit=posts_limit)
        for post in posts:
            if check_submission(post):
                download_links.append(post.url)

        return sub_path, filter_links(download_links)
