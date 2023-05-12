import glob
import math
import os
import random
import datetime
from colorama import init, Fore
init()

input_text = ""
current_element = {}
menu_need = True
file = ""

move_history = [0]

def get_user_input():
    user_input = input(Fore.BLUE + f"[User]: ")
    writetofile(f"[User]: {user_input}\n")
    return user_input

def print_response(text):
    print(Fore.LIGHTRED_EX + f"[Bot]: {text}")
    writetofile(f"[Bot]: {text}\n")

def create_file():
    global file
    now = datetime.datetime.now()
    filename = f"dialog-{now.strftime('%Y-%m-%d %H:%M:%S')}.txt"
    file = open(filename, "w")

def writetofile(text):
    global file
    file.write(text)

def close_file():
    global file
    file.close()

def print_menu_info():
    global current_element

    menu_info = f"В якому блоці ви перебуваєте: {current_element['description']}"

    list_of_windows = get_list_of_windows('string')
    if len(list_of_windows) > 0:
        menu_info += f"\n\nДоступні теми: {list_of_windows}"

    list_of_actions = get_list_of_actions('string')
    if len(list_of_actions) > 0:
        menu_info += f'\n\nДоступні дії до теми: {list_of_actions}'

    menu_info += '\n\nДодаткові дії: Назад (н)  Допомога (д)   Вихід (в)'

    print_response(menu_info)

def move_back():
    global move_history
    if (len(move_history) != 0):
        move_history.pop()

def move_to(access):
    global current_element
    global move_history
    newWindowIndex = -1

    for i, window in enumerate(current_element["windows"]):
        if window["access"].lower() == access.lower() or window["description"].lower() == access.lower():
            newWindowIndex = i
            break

    if newWindowIndex != -1:
        move_history.append(i)
        return True
    else:
        return False

def action(access):
    global current_element
    actionIndex = -1

    for i, action in enumerate(current_element["actions"]):
        if action["access"].lower() == access.lower() or action["description"].lower() == access.lower():
            actionIndex = i
            break

    if actionIndex != -1:
        current_element["actions"][actionIndex]["function"]()
        return True
    else:
        return False

def get_list_of_windows(type="array"):
    global current_element
    list_of_windows = []
    list_of_windows_as_string = ""
    for i, window in enumerate(current_element["windows"]):
        list_of_windows.append(f"{window['description']} ({window['access']})")

        if i < len(current_element["windows"]):
            list_of_windows_as_string += "\n"

        list_of_windows_as_string += f"""\t - {window['description']} ({window['access']})"""

    if type == "string":
        return list_of_windows_as_string
    else:
        if type == "array":
            return list_of_windows

def set_current_element():
    global current_element
    for i, elementIndex in enumerate(move_history):
        if i == 0:
            current_element = menu[elementIndex]
        else:
            current_element = current_element["windows"][elementIndex]

def get_list_of_actions(type="array"):
    global current_element
    list_of_actions = []
    list_of_actions_as_string = ""
    for i, action in enumerate(current_element["actions"]):
        list_of_actions.append(f"{action['description']} ({action['access']})")

        if i < len(current_element["actions"]):
            list_of_actions_as_string += f"\n"

        list_of_actions_as_string += f"""\t- {action['description']} ({action['access']})"""

    if type == "string":
        return list_of_actions_as_string
    else:
        if type == "array":
            return list_of_actions

def exit():
   global move_history
   move_history = []
   return

def help():
    global current_element
    print_response("В тебе виникли труднощі, але я з радістю допоможу!\n Для того, щоб повернутися до вибору тем достатньо просто написати \"назад\" або ж просто \"н\".\nДля того, щоб завершити спілкування достатньо написати \"вихід\" або ж просто \"в\".")
    return

def hello():
    print_response ("Вітаю! Мене звати Люси. Я завжди готова допомогти вам з вирішеннями складних завдань.\nНижче ви побачите список тем з якими я вам можу допомогти, скоріше обирай!")
    return

def calculate_coulombs_law():
    print_response("Ось формула для обчислення: F = k * q1 * q2 / r^2. Введіть заряд першої частинки в Кл:  ")
    q1 = int(get_user_input())
    print_response("Введіть заряд другої частинки в Кл: ")
    q2 = int(get_user_input())
    print_response("Тепер введіть відстань у метрах: ")
    r = int(get_user_input())
    k = 8.9875517923 * 10 ** 9
    F = k * q1 * q2 / r ** 2
    print_response(f" Сила електростатичної взаємодії між зарядами {q1} Кл та {q2} Кл на відстані {r} м дорівнює {F} Н")
    return

def calculate_boyles_law():
    print_response("""Ocь формула для обчислення: P1 * V1 = Р2 * V2.\nЩо б ви хотіли визначити:  Р1 або V1?""")
    input = get_user_input()
    if input == "Р1":
        print_response("Супер, напишіть значення значення V1:")
        V1 = int(get_user_input())
        print_response("Напишіть значення значення Р2:")
        Р2 = int(get_user_input())
        print_response("Напишіть значення значення V2:")
        V2 = int(get_user_input())
        Р1 = float(str(Р2 * V2 / V1))
        print_response(f"Ось результат обчислення: P1={str(Р1)}")
    if input == "V1":
        print_response("Супер, напишіть значення Р1:")
        Р1 = int(get_user_input())
        print_response("Напишіть значення Р2:")
        Р2 = int(get_user_input())
        print_response("Напишіть значення V2:")
        V2 = int(get_user_input())
        V1 = float (str(Р2 * V2 / Р1))
        print_response(f"Ось результат обчислення: V1={str(V1)}")
    return

def get_coulombs_constant():
    print_response("""Кулонівська стала дорівнює 8,9875517923(14) × 10^9 Н·м²/Кл².""")
    return

def distance():
    print_response("""Ось формула для обчислення: dist = math.sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2 + (z2 - z1) ^ 2.\nВведіть координати першої точки у форматі x1,y1,z1 без ком: """)
    x1, y1, z1 = int(get_user_input())
    print_response("""Введіть координати другої точки у форматі x2,y2,z2 без ком: """)
    x2, y2, z2 = int(get_user_input())
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print_response(f" Відстань між цими двома точками дорівнює {dist}")
    return

def arc_length():
    print_response("""Ось формула для обчислення: L = r*angle, де r - радіус кола, а angle - кут між двома точками на колі.\n
    Введіть радіус кола:""")
    radius = int(get_user_input())
    print_response("""Введіть кут в радіанах: """)
    angle = int(get_user_input())
    arc_length = radius * angle
    print_response(f"""Довжина дуги кола дорівнює {arc_length}.""")
    return

def segment_length():
    print_response("""Ось формула для обчислення: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).\nВведіть координати першого вектора у форматі x1,y1 без ком: """)
    x1, y1 = int(get_user_input())
    print_response("""Введіть координати другого вектора у форматі x2,y2 без ком: """)
    x2, y2 = int(get_user_input())
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print_response(f"Довжина відрізка між точками ({x1}, {y1}) і ({x2}, {y2}) дорівнює {distance}.")
    return

def circle_area():
    print_response("""Ось формула для обчислення: S = pi * r ^ 2. Введіть радіус кола: """)
    r = int(get_user_input())
    pi = float(3.14)
    S = float(pi * r ** 2)
    print_response(f" Площа кола дорівнює {S}.")
    return

def number():
    print_response("""У серпні 2009 року японські вчені вирахували число «пі» з точністю до 2 трильйонів 576 мільярдів 980 мільйонів 377 тисяч 524 знаків після коми.\n
    Я напишу вам скоречене число π: 3.141592653589793238462643...""")
    return

def coordinates():
    print_response("""Ось формула для обчислення: det = x1 * y2 - x2 * y1.\n
     Введіть координати векторів першої прямої у форматі x1,y1 без ком: """)
    x1, y1 = int(get_user_input())
    print_response("Введіть координати векторів другої прямої у форматі x2,y2 без ком: ")
    x2, y2 = int(get_user_input())
    det = x1 * y2 - x2 * y1
    if det == 0:
        print_response( "Прямі паралельні, немає точки перетину.")
    else:
        x = (y2 * x1 - y1 * x2) / det
        y = (x2 * y1 - x1 * y2) / det
        print_response(f"Точка перетину двох прямих: ({x}, {y})")
    return

def ocean():
    print_response("Найбільшим океаном за площею є Тихий океан (165.25 млн квадратних кілометрів).")
    return

def mainland():
    print_response("Найбільший материк на Землі - це Євразія. Він займає площу більше 54 мільйонів квадратних кілометрів і об'єднує території Європи та Азії.\n"
                  "До Євразії належать такі країни, як росія, Китай, Індія, Франція, Німеччина та багато інших.")
    return

def desert():
    print_response("Після Сахари, найбільшою пустелею є Пустеля Аравії (Аравійська пустеля) з площею близько 2,3 мільйонів км².\n"
                  "Вона розташована на південному заході Азії, на території країн Саудівської Аравії, Ємену, Оману та Об'єднаних Арабських Еміратів.")
    return

def planets():
    print_response("У Сонячній системі це Юпітер і Сатурн. Уран та Нептун також є планетами гігантами, але їх класифікують як крижаних гігантів.")
    return

def stars():
    print_response("Існує багато типів зір, але основним параметром для класифікації є їх спектральний клас, який визначається на основі характеристик їх спектрів. Основні типи зір за спектральним класом поділяються на такі категорії:\n"
    "1) Зорі класу O - це найбільш гарячі та яскраві зірки, з температурою близько 30 000-50 000 К. Вони мають спектральні лінії гелію та водню.\n"
    "2) Зорі класу B - це гарячі зірки з температурою близько 10 000-30 000 К. Вони мають спектральні лінії гелію та водню, а також спектральні лінії заліза та кремнію.\n"
    "3) Зорі класу A - це білі зірки з температурою близько 7 500-10 000 К. Вони мають спектральні лінії водню та заліза.\n"
    "4) Зорі класу F - це жовті зірки з температурою близько 6 000-7 500 К. Вони мають спектральні лінії кальцію та водню.\n"
    "5) Зорі класу G - це жовті зірки з температурою близько 5 200-6 000 К. Серед них є наша зоря Сонце. Вони мають спектральні лінії кальцію та заліза.\n"
    "6) Зорі класу K - це помаранчеві зірки з температурою близько 3 700-5 200 К. Вони мають спектральні лінії металів та водню.\n"
    "7) Зорі класу M - це червоні зірки з температурою менше 3 700 К. Вони мають спектральні лінії металів та молекул.")
    return

def missions():
    print_response("Програма \"Аполлон\": це була серія американських пілотованих місій на Місяць, проведених в 1969-1972 роках. Кожна місія передбачала посадку на Місяць космічного корабля з командою астронавтів, що дозволяло здійснювати дослідження поверхні, а також збирати і привозити на Землю місячні грунти та скелі.\n"
                  "Місія \"Лунохід\": це була серія радянських безпілотних місій на Місяць у 1970-х роках. Луноходи були телероботами, які висаджувалися на поверхню Місяця, щоб досліджувати його та збирати дані про склад ґрунту.\n"
                  "Місія \"Клементін\": це була незмінна місія NASA на Місяць, запущена в 1994 році. Космічний апарат здійснював віддалені дослідження Місяця, зображуючи його поверхню та збираючи дані про склад ґрунту.\n"
                  "Місія \"Чандраян-1\": це була перша індійська місія на Місяць, запущена в 2008 році. Її метою було дослідження місячної поверхні та збір даних про її склад.\n"
                  "Місія \"Луна-25\": це місія Роскосмосу на Місяць, яка відбулася в 2021 році. Метою місії є дослідження місячної поверхні та збір даних про її склад.")
    return

def black_holes():
    print_response("Чорна діра – це місце в космосі, куди сила тяжіння затягує настільки сильно, що навіть світло не може чинити опір.\n"
                  "Сила тяжіння там настільки сильна, тому що речовина була стиснута в крихітний простір.\n"
                  "Чорна діра може виникнути, коли зірка вмирає. Оскільки світло не виходить, люди не можуть бачити чорні діри.")
    return

def times_in_eng():
    print_response(f"[В англійській мові є 12 часових форм, які можуть бути поділені на три основні категорії: прості часи, складні часи та форми дійсного часу. Кожен з цих часів вказує на певний часовий період, коли відбувається дія або подія. Ось список усіх 12 часових форм:\n"
                   f" 1. Простий Present (Present Simple) - час, що відповідає на запитання \"What do/does + підмет + verb (дієслово)\" і вживається для вираження регулярних дій або загальних фактів, наприклад: \"I drink coffee every morning\" (Я п'ю каву кожного ранку).\n"
                   f" 2. Простий Past (Past Simple) - час, що відповідає на запитання \"What did + підмет + verb (дієслово)\" і вживається для вираження дій, що відбувалися в минулому, наприклад: \"I went to the store yesterday\" (Я пішов у магазин вчора).\n"
                   f" 3. Простий Future (Future Simple) - час, що відповідає на запитання \"What will + підмет + verb (дієслово)\" і вживається для вираження дій, які відбудуться у майбутньому, наприклад: \"I will call you tomorrow\" (Я зателефоную вам завтра).\n"
                   f" 4. Present Continuous (Present Progressive) - складний час, що відповідає на запитання \"What am/is/are + підмет + verb + -ing (дієслово з закінченням -ing)\" і вживається для вираження дій, які відбуваються в даний момент часу, наприклад: \"I am watching TV right now\" (Я зараз дивлюся телевізор).\n"
                   f" 5. Past Continuous (Past Progressive) - складний час, що відповідає на запитання \"What was/were + підмет + verb + -ing (дієслово з закінченням -ing)\" і вживається для вираження дій, які відбувалися у певний момент минулого, наприклад: \"I was walking in the park when it started raining\" (Я гуляв у парку, коли почалася дощ).\n"
                   f" 6. Future Continuous (Future Progressive) - складний час, що відповідає на запитання \"What will be + підмет + verb + -ing (дієслово з закінченням -ing)\" і вживається для вираження дій, які будуть відбуватися протягом певного часового періоду у майбутньому, наприклад: \"I will be studying for my exam all weekend\" (Я буду вчитися на моєму екзамені весь вікенд).\n"
                   f" 7.Present Perfect (Present Perfect Simple) - форма дійсного часу, що відповідає на запитання \"Have/has + підмет + past participle (дієприкметник минулого часу)\" і вживається для вираження дій, які сталися в минулому, але є зв'язок з теперішнім часом, наприклад: \"I have visited Paris twice\" (Я двічі був у Парижі).\n"
                   f" 8.Present Perfect Continuous (Present Perfect Progressive) - складна форма дійсного часу, що відповідає на запитання \"Have/has + підмет + been + verb + -ing (дієслово з закінченням -ing)\" і вживається для вираження тривалих дій, які почалися в минулому і тривають досі, наприклад: \"I have been working on this project for two weeks\" (Я працюю над цим проектом два тижні).\n"
                   f" 9. Past Perfect (Past Perfect Simple) - форма дійсного часу, що відповідає на запитання \"Had + підмет + past participle (дієприкметник минулого часу)\" і вживається для вираження дій, які сталися до певного моменту в минулому, наприклад: \"I had finished my homework before I went to bed\" (Я закінчив свої домашні завдання до того, як пішов спати).\n"
                   f" 10. Past Perfect Continuous (Past Perfect Progressive) - складна форма дійсного часу, що відповідає на запитання \"Had + підмет + been + verb + -ing (дієслово з закінченням -ing)\" і вживається для вираження тривалих дій, які почалися до певного моменту в минулому і тривали до цього моменту, наприклад: \"I had been working for six hours before I took a break\" (Я працював шість годин до того, як зробити перерву).\n"
                   f" 11. Future Perfect (Future Perfect Simple) - форма дійсного часу, що відповідає на запитання \"Will have + підмет + past participle (дієприкметник минулого часу)\" і вживається для вираження дій, які будуть вже закінчені до певного моменту в майбутньому, наприклад: \"By next year, I will have graduated from university\" (До наступного року я вже закінчу університет).\n"
                   f" 12. Future Perfect Continuous (Future Perfect Progressive) - складна форма дійсного часу, що відповідає на запитання \"Will have + підмет + been + verb + -ing (дієслово з закінченням -ing)\" і вживається для вираження тривалих дій, які будуть тривати до певного моменту в майбутньому, наприклад: \"By the time I finish this project, I will have been working on it for three months\" (До того часу, коли я закінчу цей проект, я буду працювати над ним три місяці).\n"
                   f" Це не повний список всіх часів, що існують в англійській мові, але ці основні форми допоможуть вам зрозуміти, як вживати різні часи вірно і ефективно.")
    return

def ua():
    print_response(f"В українській мові є шість відмінків:\n"
                     f" Називний відмінок (кличний відмінок в іменниках чоловічого роду однини) - відповідає на запитання хто? що? і вживається для позначення іменника в ролі підмета речення.\n"
                     f" Родовий відмінок - відповідає на запитання кого? чого? і вживається для позначення іменника в ролі присвійника, обставини, об'єкта дії, залежного слова у прикметниковій і займенниковій залежності.\n"
                     f" Давальний відмінок - відповідає на запитання кому? чому? і вживається для позначення іменника в ролі адресата, бенефіціара, реципієнта, об'єкта дії в певних виразах.\n"
                     f" Знахідний відмінок - відповідає на запитання кого? що? і вживається для позначення іменника в ролі об'єкта дії.\n"
                     f" Орудний відмінок - відповідає на запитання ким? чим? і вживається для позначення іменника в ролі знаряддя, засобу, способу дії.\n"
                     f" Місцевий відмінок - відповідає на запитання про місце знаходження кого? чого? і вживається для позначення місця знаходження іменника.\n"
                     f"Крім того, українська мова має два числа - однина і множина - та три роди - чоловічий, жіночий та середній. Комбінація числа та роду визначає форму іменника для кожного відмінка.")
    return

def difference_ua():
    print_response(f"Іменник та прикметник - це два різні частини мови, які мають різні функції у реченні.\n"
                     f"Іменник - це частина мови, яка позначає назву людини, тварини, речі, місця, явища та іншого існуючого предмета. Він може мати різні відмінкові форми в залежності від його ролі в реченні. Наприклад, \"кіт\", \"дім\", \"любов\", \"думка\" - це іменники.\n"
                     f"Прикметник - це частина мови, яка додає якусь якість, ознаку чи властивість до іменника. Він може вживатися перед іменником або після нього та мати різні форми в залежності від ступеня порівняння (позитив, порівняльний, найвищий). Наприклад, \"білий\" кіт, \"великий\" дім, \"щаслива\" любов, \"цікава\" думка - це прикметники.\n"
                     f"Отже, основна різниця між іменником та прикметником полягає у їх функції у реченні: іменник позначає предмет, а прикметник описує його властивості.")
    return

def difference_eng():
    print_response(f"Present Simple та Present Continuous є двома часовими формами, які вживаються для опису дій, які відбуваються в даний момент часу.\n"
                   f" Present Simple вживається для опису регулярних або постійних дій. Ця форма описує дію, яка відбувається завжди, зазвичай, регулярно або постійно. Наприклад: \"I always drink coffee in the morning. (Я завжди п'ю каву вранці.)\" або \"The sun rises in the east. (Сонце сходить на сході.)\".\n"
                   f" Present Continuous вживається для опису дій, які відбуваються в даний момент часу. Ця форма описує дію, яка відбувається саме зараз, в даний момент часу. Наприклад: \"I am drinking coffee right now. (Я зараз п'ю каву.)\" або \"He is studying for his exam this week. (Він вчиться на свій іспит цього тижня.)\".\n"
                   f" Отже, основна різниця між Present Simple та Present Continuous полягає в тому, що Present Simple вживається для опису регулярних або постійних дій, тоді як Present Continuous вживається для опису дій, які відбуваються саме зараз, в даний момент часу.")
    return

def play_game():
    print_response("Супер! Обирай камінь, ножиці або папір: ")
    options = ['камінь',
               "ножиці",
               "папір"]
    h = random.choice(options)
    c = get_user_input().lower();
    while c != 'камінь' and c != 'ножиці' and c != 'пaпip':
        print_response("Необхідно ввести камінь, ножиці або папір")
        c = get_user_input().lower()
    print_response(f"Я обрала {h}.")
    if (c == 'камінь' and h == 'ножиці') or (c == 'пaпip' and h == 'камінь') or (c == 'ножиці' and h == 'папір'):
       print_response("Гравець переміг!")
    elif (c == 'камінь' and h == 'ножиці') or (c == 'папір' and h == 'ножиЦі') or (c == 'ножиці' and h == 'камінь'):
       print_response("Я перемогла!!!")
    if c == h:
       print_response("Нічия!")
    return

def season():
    month = datetime.datetime.now().month
    if month in [12, 1, 2]:
        print_response(Fore.RED + 'Зараз зима.')
    elif month in [3, 4, 5]:
        print_response(Fore.RED + 'Зараз весна.')
    elif month in [6, 7, 8]:
        print_response(Fore.RED + 'Зараз літо.')
    else:
        print_response(Fore.RED + 'Зараз осінь.')
    return

def month():
    month = datetime.datetime.now().strftime('%B')
    print_response(Fore.RED + f'[Bot]: Зараз {month}.')
    return

def game_history():
    print_response("Чудово! Це гра питань: хто, де, коли, що. Для початку напишіть 'хто?'")
    who = get_user_input()
    print_response("Тепер 'де?'")
    where = get_user_input()
    print_response("Тепер 'коли?'")
    when = get_user_input()
    print_response("Тепер 'що?'")
    what = get_user_input()

    texts = [f"""Жив-був колись {who} у {where} у {when}. Він/вона займався/ла {what}.""",
            f"""Жив-був {who}, який/яка був/ла {what} у {where} у {when}""",
            f"""Існує легенда про {who}, який/яка жив/ла у {where} у {when}. Він/вона був/ла {what}.""",
            f"""{who} був/ла знаменитим/ою {what} у {where} у {when}.""",
            f"""{who} жив/ла у {where} у {when} і займався/ла {what}."""]

    t = random.choice(texts)
    print_response(f"{t}")
    return

def poems():
    list = [f"""\nЩе не вмерла України і слава, і воля.\nЩе нам, браття українці, усміхнеться доля.\nЗгинуть наші вороженьки, як роса на сонці,\nЗапануєм і ми, браття, у своїй сторонці.\nДушу й тіло ми положим за нашу свободу,\nІ покажем, що ми, браття, козацького роду.\nСтанем, браття, в бій кривавий від Сяну до Дону,\nВ ріднім краю панувати не дамо нікому;\nЧорне море ще всміхнеться, дід Дніпро зрадіє,\nЩе у нашій Україні доленька наспіє.\nДушу й тіло ми положим за нашу свободу,\nІ покажем, що ми, браття, козацького роду.\nА завзяття, праця щира свого ще докаже,\nЩе ся волі в Україні піснь гучна розляже,\nЗа Карпати відоб'ється, згомонить степами,\nУкраїни слава стане поміж ворогами.\nДушу й тіло ми положим за нашу свободу,\nІ покажем, що ми, браття, козацького роду.\n""",
             f"""\nТече вода в синє море,\nТа не витікає,\nШука козак свою долю,\nА долі немає.\n\nПішов козак світ за очі;\nГрає синє море,\nГрає серце козацькеє,\nА думка говорить:\n\n«Куди ти йдеш, не спитавшись?\nНа кого покинув\nБатька, неньку старенькую,\nМолоду дівчину?\n\nНа чужині не ті люде —\nТяжко з ними жити!\nНі з ким буде поплакати,\nНі поговорити».\n\nСидить козак на тім боці,\nГрає синє море.\nДумав, доля зустрінеться —\nСпіткалося горе.\nА журавлі летять собі\nДодому ключами.\nПлаче козак — шляхи биті\nЗаросли тернами.\n""",
             f"""\nРеве та стогне Дніпр широкий,\nСердитий вітер завива.\nДодолу верби гне високі,\nГорами хвилю підійма.\nІ блідний місяць на ту пору\nІз хмари де-де виглядав,\nНеначе човен в синім морі,\nТо виринав, то потопав.\nЩе треті півні не співали,\nНіхто нігде не гомонів,\nСичі в гаю перекликались,\nТа ясен раз у раз скрипів.\n""",
             f"""\nА й правда, крилатим ґрунту не треба.\nЗемлі немає, то буде небо.\nНемає поля, то буде воля.\nНемає пари, то будуть хмари.\nВ цьому, напевно, правда пташина...\nА як же людина? А що ж людина?\nЖиве на землі. Сама не літає.\nА крила має. А крила має!\nВони, ті крила, не з пуху-пірʼя,\nА з правди, чесноти і довірʼя.\nУ кого — з вірності у коханні.\n У кого — з вічного поривання.\nУ кого — з щирості до роботи.\nУ кого — з щедрості на турботи.\nУ кого — з пісні, або з надії,\nАбо з поезії, або з мрії.\nЛюдина нібито не літає...\nА крила має. А крила має!\n""",
             f"""\nЯк умру, то поховайте\nМене на могилі\nСеред степу широкого\nНа Вкраїні милій,\n\nЩоб лани широкополі,\nІ Дніпро, і кручі\nБуло видно, було чути,\nЯк реве ревучий.\n\nЯк понесе з України\nУ синєє море\nКров ворожу... отойді я\nІ лани і гори —\n\nВсе покину, і полину\nДо самого Бога\nМолитися... а до того\nЯ не знаю Бога.\n\nПоховайте та вставайте,\nКайдани порвіте\nІ вражою злою кров’ю\nВолю окропіте.\n\nІ мене в сем’ї великій,\nВ сем’ї вольній, новій,\nНе забудьте пом’янути\nНезлим тихим словом."""]
    q = random.choice(list)
    print_response(f"{q}")
    return

menu = [{
    "access": "головне меню",
    "description": "Головне меню",
    "helpText": f"У головному меню...",
    "actions": [
        {
            "access": "скоріше обирай тему!",
            "description": "У головному меню я можу тільки привітатися з тобой, але після вибору теми ти побачиш тут дії з якими я можу працювати...",
            "function": hello
        }
    ],
    "windows": [
        {
            "access": "матем",
            "description": "Математика",
            "helpText": "Тут можна вирішувати завдання з математики",
            "windows": [

            ],
            "actions": [
                {
                    "access": "відстань",
                    "description": "Обчислення відстані між двома точками в просторі",
                    "function": distance,
                },
                {
                    "access": "дуга",
                    "description": "Обчислення довжини дуги кола",
                    "function": arc_length,
                },
                {
                    "access": "відрізок",
                    "description": "Обчислення довжини відрізка між двома точками на площині",
                    "function": segment_length,
                },
                {
                    "access": "площа кола",
                    "description": "Обчислення площі кола",
                    "function": circle_area,
                },
                {
                    "access": "пі",
                    "description": "Вивід числа пі",
                    "function": number,
                },
                {
                    "access": "координати",
                    "description": "Координати точки перетину двох прямих",
                    "function": coordinates,
                },
            ]
        },
        {
            "access": "фіз",
            "description": "Фізика",
            "helpText": "Тут можна вирішувати завдання з фізики",
            "windows": [

            ],
            "actions": [
                {
                    "access": "кулон",
                    "description": "Закон Кулона",
                    "function": calculate_coulombs_law,
                },
                {
                    "access": "бойля",
                    "description": "Закон Бойля-Маріотта!",
                    "function": calculate_boyles_law,
                },
                {
                    "access": "стала, 3",
                    "description": "Виведення кулонівської сталої",
                    "function": get_coulombs_constant,
                },
            ],
        },
        {
            "access": "геог",
            "description": "Географія",
            "helpText": "Тут можна вирішувати завдання з географії",
            "windows": [

            ],
            "actions": [
                {
                    "access": "океан",
                    "description": "Який океан найбільший за площею?",
                    "function": ocean,
                },
                {
                    "access": "материк",
                    "description": "Який материк найбільший за площею?",
                    "function": mainland,
                },
                {
                    "access": "пустеля",
                    "description": "Країна, У якій знаходиться найбільша пустеля після Сахари",
                    "function": desert,
                },
            ],
        },
        {
            "access": "астрон",
            "description": "Астрономія",
            "helpText": "Тут можна вирішувати завдання з астрономії",
            "windows": [

            ],
            "actions": [
                {
                    "access": "планети",
                    "description": "Які планети є газовими гігантами?",
                    "function": planets
                },
                {
                    "access": "місії",
                    "description": "Які наукові місії здійснювалися на Місяці?",
                    "function": missions
                },
                {
                    "access": "чорні діри",
                    "description": "Що таке чорні діри та як вони виникають&",
                    "function": black_holes
                },
                {
                    "access": "зірки",
                    "description": "Які типи зір відомі в астрономії?",
                    "function": stars
                },
            ],
        },
        {
            "access": "філол",
            "description": "Філологія",
            "helpText": "Тут можна вирішувати завдання з філології",
            "windows": [

            ],
            "actions": [
                {
                    "access": "часи",
                    "description": "Які часи є в англійській мові?",
                    "function": times_in_eng
                },
                {
                    "access": "відмінки",
                    "description": "Які є відмінки в українській мові?",
                    "function": ua
                },
                {
                    "access": "імен та прикм",
                    "description": "Яка різниця між іменником та прикметником?",
                    "function": difference_ua
                },
                {
                    "access": "різниця",
                    "description": "Яка різниця між Present Simple та Present Continuous?",
                    "function": difference_eng
                },
            ],
        },
        {
            "access": "загал",
            "description": "Загальні питання",
            "helpText": "Тут можна вирішувати завдання з загальних питань",
            "windows": [

            ],
            "actions": [
                {
                    "access": "гра",
                    "description": "Гра у камінь-ножиці-папір",
                    "function": play_game
                },
                {
                    "access": "історія",
                    "description": "Гра \"історія\"",
                    "function": game_history
                },
                {
                    "access": "вірш",
                    "description": "Зачитування вірша",
                    "function": poems
                },
                {
                    "access": "пора року",
                    "description": "Яка зараз пора року?",
                    "function": season
                },
                {
                    "access": "місяць",
                    "description": "Який зараз місяць?",
                    "function": month,
                },
            ]
        }
    ]
}]

pattern = "*.txt"
files = glob.glob(pattern)
for file in files:
   os.remove(file)

create_file()
print_response("Вітаю, мене звати Люсі. Я завжди готова допомогти вам з вирішеннями складних завдань. Нижче ви зможете побачити список тем та завдань, які я можу вирішити.")
while True:
    if len(move_history) == 0:
        break

    set_current_element()

    if menu_need == True:
        print_menu_info()

        menu_need = False

    try:
        input_text = get_user_input()
    except KeyboardInterrupt:
        break

    if input_text.lower() == "д" or input_text.lower() == "допомога":
        help()
        continue
    if input_text.lower() == "н" or input_text.lower() == "назад":
        menu_need = True
        move_back()
        continue
    if input_text.lower() == "в" or input_text.lower() == "вихід":
        exit()
        continue

    if move_to(input_text) == True:
        menu_need = True
        continue
    else:
        if action(input_text.lower()) == True:
            continue
        else:
            print_response("Я не можу відповісти на це питання...Спробуйте ще раз!")
            continue

print_response("Рада була допомогти, до побачення!")
close_file()

