import os


def check_if_dir_exists(path, action_type):
    download_path = f"{os.getcwd()}/downloads/"
    subreddit_path = f"{os.getcwd()}/downloads/subreddit/"
    user_path = f"{os.getcwd()}/downloads/user/"
    if not os.path.isdir(download_path):
        os.mkdir(download_path)
    if not os.path.isdir(user_path):
        os.mkdir(user_path)
    if not os.path.isdir(subreddit_path):
        os.mkdir(subreddit_path)
    if action_type == "user":
        sub_path = f"{user_path}/{path}"
        if not os.path.isdir(sub_path):
            os.mkdir(sub_path)
        return sub_path
    if action_type == "subreddit":
        sub_path = f'{subreddit_path}/{path}'
        if not os.path.isdir(sub_path):
            os.mkdir(sub_path)
        return sub_path
