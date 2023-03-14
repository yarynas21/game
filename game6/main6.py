import game6

your_location = game6.Street("Вулиця Козельницька 2a")
your_location.set_description("З цього місця розпочинається твоя подорож за кавою.")

frank = game6.Street("Вулиця Івана Франка")
frank.set_description("Вулиця, де жив геніальний письменник!")

shota = game6.Street("Вулиця Шота Руставелі")
shota.set_description("Вулиця з старовинними будинками та найсмачнішими круасаними!")

taras = game6.Street("Проспект Тараса Шевченка")
taras.set_description("Названий в честь нашого батька:)")

oleg = game6.Enemy("Олег", "Лотр - негідник, розбійник, грабіжник.")
oleg.set_conversation("Знімай кульчики!!!")
oleg.set_weakness("bat")
frank.set_character(oleg)

dima = game6.Enemy("Діма", "Батяр - гульвіса, п'яничка.")
dima.set_conversation("Ти така красива, дай на горілку!")
dima.set_weakness("spray bottle")
taras.set_character(dima)

baa = game6.Item("spray bottle")
baa.set_description("Перчений, як перець.")
frank.set_item(baa)

stick = game6.Item("bat")
stick.set_description("Will kill будь - кого!")
taras.set_item(stick)

friend = game6.Friend("Вікторія", "Найкраща людина y світі", False)
friend.set_conversation("Я допоможу тобі вижити:),\n але вибір за тобою, ти можеш випробувати удачу:)")
shota.set_character(friend)

your_location.link_room(frank, "south")
frank.link_room(your_location, "north")
frank.link_room(shota, "west")
shota.link_room(frank, "east")
shota.link_room(taras, "north")
taras.link_room(shota, "south")

current_street = your_location
backpack = []
dead = False

rules_instance = game6.Rules()
rules_instance.rules()

# Чекаємо, поки користувач натисне Enter
input("Натисніть Enter, щоб продовжити...")

# Все йде далі
print("Продовжуємо game...")
health = 100

while not dead:
    print("\n")
    current_street.get_details()
    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()
    command = input("> ")
    if command in ["south", "west", "north", "east"]:
        current_street = current_street.move(command)
    elif command == "help":
        print("""Всього y game є шість команди:
        1. Вибрати напрямок(west abo east)
        2. talk - поговорити з ворогом
        3. take - взяти предмет
        4. fight - побитися з ворогом
        5. live - можливість полікуватися
        6. help - можливі команди
        """)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("Немає з ким поговорити:(")
    elif command == "take":
        if item is not None:
            print("Ти поклав " + item.get_name() + " y свій рюкзак!")
            backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print("Немає що взяти:(")
    elif command == "fight":
        if inhabitant.enemy:
            if inhabitant is not None:
                # Fight with the inhabitant, if there is one
                print("Чим ти хочеш битися?")
                fight_with = input("> ")
                # Do I have this item?
                if fight_with in backpack:

                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("Horey, ти виграв битву!")
                        current_street.character = None
                        if inhabitant.get_defeated() == 2:
                            print("Вітаю, ти пройшов цей довгий шлях, знайшовся та отримав своєї заповітної кавусі!")
                            dead = True
                    else:
                        # What happens if you lose?
                        print("Ти програв цю битву:(")
                        health = inhabitant.reduce_health(health)
                        print(f"Рівень твого життя - {health}")
                        if health > 50:
                            print(f'Рівень твого життя - {health}')
                            dead = True
                        elif health == 0:
                            print("Ти програв y цій game!")
                            dead = True
                            break       
                else:
                    print("Ти не маєш " + fight_with)
            else:
                print("Тут немає з ким битися!")
        else:
            print("Ти не можеш битися з другом!")
    elif command == 'live':
        if not inhabitant.enemy:
            if inhabitant is not None:
                health = inhabitant.increase_health(health)
                current_street.character = None
                print(f'Рівень твого життя - {health}')
            else:
                print("Тут немає нікого")
        else:
            print("Ти не можеш попросити ворога про допомогу")
    else:
        print("Я не знаю як пройти на " + command)
    