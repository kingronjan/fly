import random
import string

from captcha.image import ImageCaptcha


def create_random_captcha():
    """
    ord A-Z 65-90
    ord a-z 97-122
    ord 0-9 48-57

    # ords = list(range(48, 58))
    # ords.extend(range(65, 91))
    # ords.extend(range(97, 123))
    """
    letters = string.ascii_letters + string.digits

    text = ''.join(random.choice(letters) for i in range(4))

    i = ImageCaptcha()
    image = i.generate(text, 'PNG')

    return text, image


if __name__ == '__main__':
    text, c = create_random_captcha()
    print(c)
    print(text)
