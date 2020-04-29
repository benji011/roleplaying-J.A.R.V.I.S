import os
import random

from discord import RequestsWebhookAdapter, Webhook

BENJI = os.environ['BENJI']
ANDO = os.environ['ANDO']
DANNY = os.environ['DANNY']
DARREN = os.environ['DARREN']

JARVIS_FETISH_LIST = os.environ['JARVIS_FETISH_LIST']
JARVIS_HOBBIES_LIST = os.environ['JARVIS_HOBBIES_LIST']
JARVIS_LIFE_CHOICES_LIST = os.environ['JARVIS_LIFE_CHOICES_LIST']
JARVIS_PROFESSIONS_LIST = os.environ['JARVIS_PROFESSIONS_LIST']

DISCORD_TOKEN_ID = os.environ['DISCORD_TOKEN_ID_JARVIS']
DISCORD_TOKEN = os.environ['DISCORD_TOKEN_JARVIS']

GENDER = random.choice(["M", "F"])
GITHUB_LINK = "https://github.com/benji011/roleplaying-J.A.R.V.I.S"


def get_random_inaka_boisss():
    """Get a random person to send a random article to."""
    inaka_boisss = [BENJI, ANDO, DANNY, DARREN]
    return random.choice(inaka_boisss)


def get_profession():
    """Get profession."""
    with open(JARVIS_PROFESSIONS_LIST) as f:
        content = f.read().splitlines()
        return random.choice(content)


def get_interest():
    """Get interest."""
    interest = ["with a passion in", "that likes", "who loves"]
    return random.choice(interest)


def get_hobby():
    """Get hobby."""
    with open(JARVIS_HOBBIES_LIST) as f:
        content = f.read().splitlines()
        return random.choice(content)


def get_addiction():
    """Get addiction."""
    addiction = ["has a raging fetish", "with a burning desire", "is addicted"]
    return random.choice(addiction)


def get_fetish():
    """Get fetish."""
    with open(JARVIS_FETISH_LIST) as f:
        content = f.read().splitlines()
        return random.choice(content)


def get_age():
    """Get random age."""
    MIN_AGE = 23
    MAX_AGE = 82
    age = random.randrange(MIN_AGE, MAX_AGE)
    return age


def get_time_of_day():
    time_of_day = ["morning", "afternoon", "evening", "night"]
    return random.choice(time_of_day)


def get_gender():
    """Get gender."""
    male = {
        "SUBJECT_PRONOUN": "he",
        "POSESSIVE_ADJECTIVE": "his"
    }
    female = {
        "SUBJECT_PRONOUN": "she",
        "POSESSIVE_ADJECTIVE": "her"
    }
    return male if GENDER == "M" else female


def get_life_choices():
    """Get life choices."""
    with open(JARVIS_LIFE_CHOICES_LIST) as f:
        content = f.read().splitlines()
        return random.choice(content)


def compose_message():
    """Compose message."""
    recipent = "<@{user_id}>".format(
        user_id=get_random_inaka_boisss()
    )
    msg = (
        "we can roleplay as a {age} year old {profession} "
        "{interest} {hobby} and {addiction} "
        "for {fetish} but every {time_of_day} "
        "{subject_pronoun} contemplates "
        "{posessive_adjective} {life_choices}."
    ).format(
        age=get_age(),
        profession=get_profession(),
        interest=get_interest(),
        hobby=get_hobby(),
        addiction=get_addiction(),
        fetish=get_fetish(),
        time_of_day=get_time_of_day(),
        subject_pronoun=get_gender().get("SUBJECT_PRONOUN"),
        posessive_adjective=get_gender().get("POSESSIVE_ADJECTIVE"),
        life_choices=get_life_choices()
    )
    github_url_msg = (
        "\n\nbeep bop I'm a bot\n"
        "My source code is here - {github_link}"
    ).format(
        github_link=GITHUB_LINK
    )
    msg = recipent + " " + msg + github_url_msg
    return msg


def send_message(msg):
    """Send message."""
    webhook = Webhook.partial(
        DISCORD_TOKEN_ID,
        DISCORD_TOKEN,
        adapter=RequestsWebhookAdapter()
    )
    webhook.send(msg)


def main():
    """The main function."""
    msg = compose_message()
    send_message(msg)


if __name__ == "__main__":
    main()
