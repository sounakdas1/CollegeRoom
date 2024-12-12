import hashlib

def get_gravatar_url(email, size=80, default='identicon', rating='g'):
    """
    Generate the Gravatar URL for a given email address.

    :param email: The email address of the user.
    :param size: The size of the Gravatar image (default 80px).
    :param default: The default image to show if the user doesn't have a Gravatar (e.g., 'identicon').
    :param rating: The rating of the Gravatar image ('g', 'pg', 'r', 'x').

    :return: The Gravatar image URL.
    """
    # Normalize email (strip whitespace and convert to lowercase)
    email = email.strip().lower()

    # MD5 hash the email address
    email_hash = hashlib.md5(email.encode('utf-8')).hexdigest()

    # Construct the Gravatar URL
    gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d={default}&r={rating}"

    return gravatar_url
