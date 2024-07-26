from magic_classes_2 import paladin
from magic_classes_2 import magicman
from Racec import racec
from Racec import elfrace
from Chelovek import Chelovek_gorod
from Elf import Elf_gorod
from Gnom import Gnom_gorod
from Ork import Ork_gorod
from Neco import Neco_gorod




def game ():
      print("1.Человек     2.Эльф     3.Гном", "4.Орк         5.Зверолюд", sep='\n')
      race = int(input("Выберите рассу персонажа:"))
      if race == 5:
            race = racec()
      elif race == 2:
            race == elfrace()
      print("1.Воин     2.Берсерк     3.Паладин",
            "4.Маг      5.Лучник      6.Рейнджер",
            "7.Клерик   8.Бард", sep='\n')
      classes = int(input("Выберите класс вашего перснонажа:"))
      return  race, classes

r,c = game()
if c == 1:
      cls = "Воин"
elif c == 2:
      cls = "Берсерк"
elif c == 3:
      cls = paladin(c)
elif c == 4:
      cls = magicman(c)
elif c == 5:
      cls = "Лучник"
elif c == 6:
      cls = "Рейнджер"
elif c == 7:
      cls = "Клерик"
elif c == 8:
      cls = "Бард"

if r == 1:
      r = "Человек"
elif r == 2:
      r = "Эльф"
elif r == 3:
      r = "Гном"
elif r == 4:
      r = "Орк"
elif r == 5:
      r = "Зверолюд"




name = input("Как хотите чтобы звали вашего персонажа?")

print(f"Ваши характеристики: Ур. 1 Имя:{name}, Класс: {cls}, Расса: {r}")
start = int(input("Готовы начать приключение? Вы начнёте в городе вашей рассы.      1.Готов             2.Нет, я ухожу, игра плохая"))
if start == 1:
      if r == "Человек":
            p = Chelovek_gorod()
      if r == "Тёмный эльф" or r == "Светлый эльф":
            p = Elf_gorod()
      if r == "Гном":
            p = Gnom_gorod()
      if r == "Орк":
            p = Chelovek_gorod()
      if r == "Минотавр" or r == "Кинокефал" or r == "Драконит" or r == "Нага" or r == "Гарпия" or r == "Русалка" or r == "Кентавр" or r == "Неко":
            p = Chelovek_gorod()
else:
      print("Ну и не надо, ну и пожалуйста")

if p == 1:
      p = Chelovek_gorod()
elif p == 3:
      p= Elf_gorod()
elif p== 4:
      p = Gnom_gorod()
elif p == 2:
      p = Ork_gorod()
elif p == 5:
      p = Neco_gorod()
