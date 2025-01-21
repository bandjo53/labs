import time
import random
import sys
print("Добро пожаловать в Элендрию — галактику с тысячами планет, каждая из которых хранит \n"
      "много загадок.Вы — искатель приключений, чья история начинается с планеты Тенебисс.\n"
      "Исследуйте живописные ландшафты, от густых лесов до мрачных подземелий, находя снаряжение,\n"
      "оружие и различные зелья, принимайте решения, способные изменить ход истории. Ваш выбор \n"
      "определит вашу судьбу: станете ли вы героем или умрете?!\n")

name = input("Введите имя персонажа ")
print("Характеристики вашего персонажа:")
damage = random.randint(5,7)
print(f"Атака-{damage}")
protection = random.randint(4,5)
print(f"Защита-{protection}")
health = random.randint(5,10)
print(f"Здоровье-{health}")
max_health = health
time.sleep(2)
izmena_har = int(input("\nЖелаете ли вы изменить характеристики вашего персонажа?"
                       "\n1.Пропустить""\n2.Изменить характеристики персонажа\n"))

sum_har = damage + protection + health

def izmenenie_har(izmena_har):
    if izmena_har == 2:
        global damage,protection,health
        print(f"Сумма ваших очков-{sum_har}")
        damage = int(input("Введите количество очков для атаки-"))
        print(f"Сумма ваших очков-{sum_har - damage}")
        protection = int(input("Введите количество очков для защиты-"))
        print(f"Сумма ваших очков-{sum_har - damage - protection}")
        health = int(input("Введите количество очков для здоровья-") )
        if damage + protection + health > sum_har:
            print("У вас недостаточно очков, попробуйте снова\n")
            return izmenenie_har(izmena_har)
        else:
            return (f"\nНовые характеристики вашего персонажа \nАтака-{damage}"
                    f"\nЗащита-{protection}\nЗдоровье-{health}")
    return "Характеристики не были изменены"
print(izmenenie_har(izmena_har))
vrag = 1
inventar = [""]
vrag_damage = (random.randint(6, 7))
vrag_protection = random.randint(2, 4)
vrag_health = random.randint(6,10)
marker_boi = ""
def vrag(vrag):
    global damage, protection, health,vrag_health,vrag_damage,vrag_protection,marker_boi
    print(f"Ваши характеристики {' '*20} характеристики врага\n"
          f"урон-    {damage}{40 * ' '}{vrag_damage}\n"
          f"Защита-  {protection}{40 * ' '}{vrag_protection}\n"
          f"Здоровье-{health}{40 * ' '}{vrag_health}\n")
    while vrag_health >0 or health > 0:
        if health <= 0:
            health = 0
            if "Камень воскрешения" in inventar:
                health = max_health //2
                print(f"Сработал камень воскрешения.Теперь вы снова можете вступить в бой\n"
                      f"Ваше здоровье-{health}")
            else:
                print("Вы повержены")
                sys.exit()
        vibor_vrag = int(input("Выбирите действие \n1.Ударить\n"
                               "2.Уклониться\n3.Открыть инвентарь\n"))
        if vibor_vrag == 1:
            if marker_boi == "just":
                print("Вы наносите удар по противнику...\n")
                vrag_health = vrag_health - ((damage + random.randint(-1, 2)) - vrag_protection)
                if vrag_health < 0:
                    vrag_health = 0
                print(f"Ваше здоровье {20 * ' '} здоровье врага\n",
                      health, 36 * " ", vrag_health, "\n")
                if vrag_health <= 0:
                    marker_boi = ""
                    return "Противник повержен"
                print("Враг наносит ответный удар...")
                print(f"Ваше здоровье {20 * ' '} здоровье врага")
                shanz_plusa_onaki = random.randint(-2, 1)
                if ((vrag_damage + shanz_plusa_onaki) - protection) <= 0:
                    health = health
                    print(health, 36 * " ", vrag_health)
                if ((vrag_damage + shanz_plusa_onaki) - protection) > 0:
                    health = health - ((vrag_damage + shanz_plusa_onaki) - protection)
                    if health >= 0:
                        health = health
                    else:
                        health = 0
                    print(health, 36 * " ", vrag_health)
                if health <= 0:
                    health = 0
                    print("Вы повержены")
                    sys.exit()
            if marker_boi == "poizon":
                print("Вы наносите удар по противнику...\n")
                vrag_health = vrag_health - ((damage + random.randint(-1, 2)) - vrag_protection)
                if vrag_health < 0:
                    vrag_health = 0
                print(f"Ваше здоровье {20 * ' '} здоровье врага\n",
                      health, 36 * " ", vrag_health, "\n")
                if vrag_health <= 0:
                    marker_boi = ""
                    return "Противник повержен"
                print("Враг наносит ответный удар...")
                print(f"Ваше здоровье {20 * ' '} здоровье врага")
                shanz_plusa_onaki = random.randint(-2, 1)
                if ((vrag_damage + shanz_plusa_onaki) - protection) <= 0:
                    health = health
                    print(health, 36 * " ", vrag_health)
                if ((vrag_damage + shanz_plusa_onaki) - protection) > 0:
                    health = health - ((vrag_damage + shanz_plusa_onaki) - protection)
                    if health >= 0:
                        health = health
                    else:
                        health = 0
                    print(health, 36 * " ", vrag_health)
                if health <= 0:
                    health = 0
                    print("Вы повержены")
                    sys.exit()
                period_poizon = random.randint(2,3)
                for i in range(period_poizon):
                    print("Яд противника действует на вас")
                    print(f"Ваше здоровье{20*' '} здоровье врага")
                    health -=1
                    time.sleep(2)
                    print(health,36*' ',vrag_health)

                    if health == 0:
                        print("Вы повержены")
                        sys.exit()
        if vibor_vrag == 2:
            shanz_otaki = random.randint(1,2)
            if shanz_otaki == 1:
                print(f"Вы увернулись от атаки противника\n")
                print("Вы наносите удар по противнику...\n")
                vrag_health = (vrag_health-((damage + random.randint(-1,2))-vrag_protection))
                if vrag_health < 0:
                    vrag_health = 0
                print(f"Ваше здоровье {20 * ' '} здоровье врага\n",
                health,36*' ',vrag_health,"\n")
                if vrag_health <= 0:
                    marker_boi == ""
                    return "Противник повержен"
            else:
                print("У вас не получилось увернуться от атаки противника")
                print(f"Ваше здоровье {20 * ' '} здоровье врага")
                shanz_plusa_onaki = random.randint(-2, 1)
                if ((vrag_damage + shanz_plusa_onaki) - protection) <= 0:
                    health = health
                    print(health, 36 * " ", vrag_health)
                if ((vrag_damage + shanz_plusa_onaki) - protection) > 0:
                    health = health - ((vrag_damage + shanz_plusa_onaki) - protection)
                    if health >= 0:
                        health = health
                    else:
                        health = 0
                    print(health, 36 * " ", vrag_health)
                if health <= 0:
                    health = 0
                    print("Вы повержены")
                    sys.exit()
        if vibor_vrag == 3:
            if len(inventar) == 1:
                print("\nВаш инвентарь пуст\n")
            else:
                print("Содержимое вашего инвентаря:")
                for i in range(1,len(inventar)):
                    print(f"{i}.{inventar[i]}")
                vibor_inventar = inventar[int(input("Что хотите использовать?\n"))]
                def global_effects(vibor_inventar):
                    global health
                    if vibor_inventar == "Зелье здоровья":
                        if health == max_health:
                            return print("У вас максимальное количество здоровья")
                        else:
                            health = max_health
                            return print("Здоровье восстановлено")
                print(global_effects(vibor_inventar))
ravnina = True
les = True
podzemelya = True
global_region = 1
def global_regioni(global_region):
    region = int(input("\nКуда хотите отправиться?\n1.Равнины\n2.Лес\n3.Подземелье\n"))
    def regioni(region):
        global vrag_damage,vrag_health,vrag_protection
        if region == 1:
            global ravnina
            if ravnina == True:
                print("Вы отправляетесь в равнины...")
                time.sleep(2)
                print("Перед вами открываются удивительные просторы планеты")
                time.sleep(2)
                print("В далеке вы замечаете небольшой охотничий домик с "
                      "растопленным камином внутри")
                time.sleep(2)
                vibor_ravnini = int(input("1.Отправиться к домику\n2.Выйти из равнин\n"))
                def vibor_ravnin(vibor_ravnini):
                    global damage,protection,marker_boi
                    if vibor_ravnini == 1:
                        print("Войдя в дом, вы сталкиваетесь с разбойником\n")
                        marker_boi = "just"
                        time.sleep(2)
                        print(vrag(vrag))
                        inventar.append("Зелье здоровья")
                        damage += 9
                        protection += 10
                        print("В сундуке разбойника вы находите зелье здоровья и кольчужную броню\n"
                              "В ваш инвентарь добавлено зелье здоровья\n"
                              "ваши характеристики улучшены:\n"
                              "+Зелье здоровья\n"
                              "+Урон\n"
                              "+Защита")
                        return global_regioni(global_region)
                    if vibor_ravnini == 2:
                        return global_regioni(global_region)
                ravnina = False
                return vibor_ravnin(vibor_ravnini)
            else:
                print("Вы уже побывали в этой локации")
                return global_regioni(global_region)
        if region == 2:
            global les
            if les == True:
                print("Вы отправляетесь в могущественный лес...")
                time.sleep(2)
                print("Пройдя в глубь леса, вы натыкаетесь на маленькую деревню у небольшого озера, состоящую из сарая,домика и таверны.")
                time.sleep(2)
                vibor_derevnia = int(input("1.Войти в сарай\n2.Войти в домик\n3.Войти в таверну\n4.Выйти из леса\n"))

                def vibor_sarai(vibor_derevnia):
                    global health,vrag_health,vrag_damage,vrag_protection,marker_boi
                    if vibor_derevnia == 1:
                        print("Подойдя к двери, вы, навалившись, начали пытаться ее открыть...")
                        time.sleep(3)
                        print("Внезапно дверь открылась.Осмотревшись, вы ничего не нашли, кроме костей. ")
                        time.sleep(2)
                        vibor_derevnia = int(
                        input("1.Войти в сарай\n2.Войти в домик\n3.Войти в таверну\n4.Выйти из леса\n"))
                        return vibor_sarai(vibor_derevnia)
                    if vibor_derevnia == 2:
                        print("Войдя в дом,вас встречает торговец.Он начинает распрашивать вас и у вас завязывается беседа, в ходе которой\n"
                            "торговец просит вас избавить таверну от монстров взамен на что-нибудь из его ассортимента. ")
                        vibor_derevnia = int(input("1.Войти в сарай\n2.Войти в домик\n3.Войти в таверну\n4.Выйти из леса\n"))
                        return vibor_sarai(vibor_derevnia)
                    if vibor_derevnia == 3:
                        flag_taverna = True
                        print("Вы входите в заброшенную таверну. Её обветшалые стены,\n"
                              "покрытые мхом, и разбитые окна создают атмосферу заброшенности. \n"
                              "Внутри пыльные столы и остатки мебели напоминают о былом уюте, а \n"
                              "старый камин и потемневшие картины хранят забытые истории.Тишину \n"
                              "нарушает лишь ветер, шепчущий о таинственных легендах и сокровищах,\n"
                              "скрытых в её темных углах. ")
                        def taverna(flag_taverna):
                            global marker_boi
                            if flag_taverna == True:
                                vibor_taverna = int(input("\n1.Пройти в гостинную\n2.Пойти в левую комнату\n3.Подняться на второй этаж\n"
                                                          "4.Спуститься в подвал \n5.Выйти из таверны\n"))

                                if vibor_taverna == 1:
                                    print("Пройдя вперед, вы ничего не нашли.Вокруг ничего не было, кроме паутины в углах комнаты")
                                    vibor_taverna = int(input( "\n1.Пройти в гостинную\n2.Пойти в левую комнату\n3.Подняться на второй этаж\n"
                                                       "4.Спуститься в подвал \n5.Выйти из таверны\n"))

                                    return taverna(vibor_taverna)
                                if vibor_taverna == 2:
                                    flag_vebber_forst = True
                                    print("Пройдя в левую комнату таверны, вы нарываетесь на огромного паука")
                                    if flag_vebber_forst == True:
                                        marker_boi = "poizon"
                                        print(vrag(vrag))
                                        vibor_taverna = int(input("\n1.Пройти в гостинную\n2.Пойти в левую комнату\n3.Подняться на второй этаж\n"
                                                "4.Спуститься в подвал \n5.Выйти из таверны\n"))
                                        flag_vebber_forst = False
                                        return taverna(vibor_taverna)
                                    else:
                                        print("Вы уже побывали в этой локации")
                                        vibor_taverna = int(input("\n1.Пройти в гостинную\n2.Пойти в левую комнату\n3.Подняться на второй этаж\n"
                                               "4.Спуститься в подвал \n5.Выйти из таверны\n"))
                                        return taverna(vibor_taverna)
                                if vibor_taverna(vibor_taverna) == 3:
                                    print("Вы поднимаетесь на второй этаж таверны...")
                                    time.sleep(2)
                                    print("Поднявшись ,вы находите железные доспехи в углу комнаты")
                                    print("Ваши характеристики улучшены:\n")
                                    print("+Защита")
                                    protection += 3
                                if vibor_taverna == 4:
                                    print("Вы спускаетесь в подвал...")
                                    print("Как только вы спустились , на вас напал ")
                        return taverna(flag_taverna)
                    if vibor_derevnia == 4:
                        return global_regioni(global_region)
                print(vibor_sarai(vibor_derevnia))
                les = False
                return global_regioni(global_region)
            else:
                print("Вы уже побывали в этой локации")
                return global_regioni(global_region)

    return regioni(region)

print(global_regioni(global_region))