from typing import Dict

class langs:
    _eng: Dict[str, str] 
    _ru: Dict[str, str]

    def __init__(self):
        self._eng = {
            "welcome": "Welcome to wordle! You have 6 attempt to guess the word.",
            "word request": "Enter your guess: ",
            "congrats" : "Congratulations! You guessed the word!",
            "bad guess" : "Try again!",
            "bad result" : "Unfortunately, 6 attempts were not enough for you to guess the word...",
            "num attempts" : "You have {} more attempts",
            "last attempt" : "You have the last attempt!",
            "leng error" : "Your word should consist of 5 letters!",
            "register error" : "Your word shoud consist of letters of lower register!",                 "not_letters_error" : "Your word shoud consist of letters only!",
            "not letters error" : "Your word shoud consist of letters only!",
            "language error" : "You should enter word in English!"
            }
        self._ru = {
            "welcome": "Добро пожаловать в wordle! У вас есть 6 попыток, чтобы угадать слово. ",
            "word request": "Введите ваше слово: ",
            "congrats" : "Поздравляем! Вы угадали слово!",
            "bad guess" : "Попробуйте ещё раз!",
            "bad result" : "К сожалению, вам не хватило 6 попыток, чтобы угадать слово...",
            "num attempts" : "У вас осталось ещё {} попытки(-ток)",
            "last attempt" : "У вас осталась последняя попытка!",
            "leng error" : "Ваше слово должно состоять из 5 букв!",
            "register error" : "Ваше слово должно состоять только из букв нижнего регистра!",
            "not letters error" : "Ваше слово должно состоять только из букв!",
            "language error" : "Вы должны ввести слово на русском!"
            }

    def get_phrase(self, lang: str, meaning: str) -> str:
        if lang == "eng":
            return self._eng[meaning]
        elif lang == "ru":
            return self._ru[meaning]
        else:
            raise Exception("There is no such language")