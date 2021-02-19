def check_submission(post):
    is_okay = True
    if post.locked is True:
        is_okay = False
    if post.is_self is True:
        is_okay = False
    if post.stickied is True:
        is_okay = False
    if post.distinguished is True:
        is_okay = False
    return is_okay
