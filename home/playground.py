

class TextEditor:
    def __init__(self):
        self.text = "Geburtstag aansd"


    def append(self, text):
        new_text = input("What you want to to the text?\n")
        try:
            int(new_text)
            return "Just text"
        except str(new_text):
            self.text.append(new_text)
            return f"New text {new_text} addet to your text\n Text: {self.text}"


    def len_check(self, option_word):
        l = self.text.split()  # slit the word and do them in a list
        if len(l) == 1:
            choice_w_or_l = input(f"Your text is only one word. {option_word} word(1) or letter(2)")
            text_or_letter = "letter"
        else:
            text_or_letter = "word"
            choice_w_or_l = 0
        return choice_w_or_l, text_or_letter


    def change_word_or_letter(self):
        l = self.text.split() # slit the word and do them in a list
        index = 0
        choice_w_or_l, text_or_letter = self.len_check("edit")
        if choice_w_or_l == 1:
            l = input("type in the new word\n>>>")
            self.text = l
            print(f"changed {text_or_letter} {''.join(l)} to {self.text}")
            return True

        for w in l:
            print(f"{index} = {w}\n")
            index += 1
        choice = int(input(f"which {text_or_letter} you want to edit?\n>>>"))
        try:
            int(choice)
            if choice > index:
                return "number was too big"
            prev_word = l[choice]
            l[choice] = input(f"Please type in the new {text_or_letter} ...\n>>>")
            print(f"changed {text_or_letter} {prev_word} to {l[choice]}")
            self.text = " ".join(l)
            print(f"current text: {self.text}")
            return True
        except str(choice):
            return " please type in a number"

    def delete(self):
        choice = input("1 = delete all \n"
                       "2 = delete speciffic word\n")
        if choice == 1:
            self.text = ""
            print("Text successfully deleted")
            return True
        choice_w_or_l, text_or_letter = self.len_check("edit")
        l = self.text.split()
        if len(l) < 1:
            for w in l:
                if choice_w_or_l == 1






editor = TextEditor()
editor.change_word()







while True:
    choice = input("what you want to do with that text editor?\n"
                   "1 = add\n"
                   "2 = delete\n"
                   "3 = change \n"
                   "4 = double\n")

    if choice == 2:








"""


Sicher, hier ist eine Python-Herausforderung für fortgeschrittene Programmierer:

Aufgabe: Implementieren Sie einen einfachen Texteditor

Ihr Texteditor sollte die folgenden Operationen unterstützen:

append(W): Fügt den Text W am Ende des aktuellen Textes an.
delete(k): Löscht die letzten k Zeichen des aktuellen Textes.
print(k): Gibt das k-te Zeichen des aktuellen Textes aus.
undo(): Macht die letzte (nicht-undo) Operation rückgängig, die entweder append oder delete war.
Sie sollten eine Klasse TextEditor implementieren, die diese Operationen unterstützt. Die Operationen sollten effizient
sein, d.h., sie sollten in konstanter oder logarithmischer Zeit ausgeführt werden können.

Beispiel:

editor = TextEditor()
editor.append("abc")
editor.print(3)  # Sollte "c" ausgeben
editor.append("def")
editor.delete(3)
editor.print(3)  # Sollte "b" ausgeben
editor.undo()
editor.print(6)  # Sollte "f" ausgeben
Diese Herausforderung testet Ihre Kenntnisse in Datenstrukturen und Ihre Fähigkeit, effizienten Code zu schreiben. Viel Spaß beim Lösen! 😊



"""