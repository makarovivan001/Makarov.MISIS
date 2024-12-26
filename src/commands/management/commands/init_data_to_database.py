from django.core.management.commands.migrate import Command as MigrateCommand
from lending.models import *


class Command(MigrateCommand):
    def handle(self, *args, **options):
        countries = [
            "Россия", "Канада", "Мексика", "Бразилия",
            "Аргентина", "Чили", "Великобритания", "Германия",
            "Италия", "Франция", "Испания", "США",
            "Китай", "Япония", "Южная Корея", "Индия",
            "Австралия", "Новая Зеландия", "ЮАР", "Египет",
            "Марокко", "ОАЭ", "Турция",
            "Норвегия", "Швеция", "Финляндия", "Дания",
            "Нидерланды", "Бельгия"
        ]

        if Country.objects.count() == 0:
            for country in countries:
                Country.objects.create(name=country)

        clubs = [
            {
                'photo': 'clubs/CSKA.png',
                'name': 'ПФК ЦСКА',
                'description': """
                    ПФК ЦСКА (Профессиональный футбольный клуб ЦСКА) — 
                    российский профессиональный футбольный клуб из Москвы. 
                    В прошлом — часть Центрального спортивного клуба Армии. 2
                    Один из старейших и самых титулованных клубов в 
                    постсоветской истории российского футбола, ведущий свою 
                    историю от команды ОЛЛС (Общество любителей лыжного спорта), 
                    основанной в 1911 году. Некоторые достижения: семикратный 
                    чемпион СССР, пятикратный обладатель Кубка СССР, 
                    пятикратный чемпион России, семикратный обладатель Кубка 
                    России и шестикратный обладатель Суперкубка России. Первый 
                    российский клуб, выигравший европейский клубный турнир — 
                    Кубок УЕФА (2004/05).""",
                'country_id': 1,
                'coach': {
                    'photo': 'coaches/НИКОЛИЧ_МАРКО.jpeg',
                    'surname': 'Осинькин',
                    'name': 'Игорь',
                    'middle_name': 'Витальевич',
                    'country_id': 1,
                },
                'player': [
                    {
                        'photo': 'players/БАНДИКЯН_АРТЁМ.jpeg',
                        'surname': 'Обляков',
                        'name': 'Иван',
                        'middle_name': 'Андреевич',
                        'country_of_birth_id': 1,
                        'number': 11,
                    },
                    {
                        'photo': 'players/БИСТРОВИЧ_КРИСТИЯН.jpeg',
                        'surname': 'Иванов',
                        'name': 'Сергей',
                        'middle_name': 'Олегович',
                        'country_of_birth_id': 1,
                        'number': 7,
                    },
                    {
                        'photo': 'players/ВАКУЛИЧ_АЛЕКСАНДР.jpeg',
                        'surname': 'Роналду',
                        'name': 'Илья',
                        'middle_name': 'Сергеевич',
                        'country_of_birth_id': 1,
                        'number': 1,
                    },
                    {
                        'photo': 'players/ГАЙИЧ_МИЛАН.jpeg',
                        'surname': 'Иванченко',
                        'name': 'Пётр',
                        'middle_name': 'Витальевич',
                        'country_of_birth_id': 1,
                        'number': 28,
                    },
                    {
                        'photo': 'players/ГУАРИРАПА_САУЛЬ.jpeg',
                        'surname': 'Макаров',
                        'name': 'Иван',
                        'middle_name': 'Сергеевич',
                        'country_of_birth_id': 1,
                        'number': 19,
                    },
                    {
                        'photo': 'players/КОЙТА_СЕКУ.jpeg',
                        'surname': 'Ивасин',
                        'name': 'Костя',
                        'middle_name': 'Ильин',
                        'country_of_birth_id': 1,
                        'number': 21,
                    },
                ]
            },
            {
                'photo': 'clubs/Lokomotiv.png',
                'name': 'Локомотив',
                'description': """
                    «Локомотив» — российский футбольный клуб из Москвы. 
                    Выступает в Российской премьер-лиге. Основан 23 июля 
                    1922 года. Один из старейших футбольных клубов России, 
                    ведущий свою историю с момента основания команды «Казанка» 
                    при Московско-Казанской железной дороге, затем 
                    неоднократно менявший своё название. """,
                'country_id': 1,
                'coach': {
                    'photo': 'coaches/Галактионов_Михаил_Михайлович.jpeg',
                    'surname': 'Галактионов',
                    'name': 'Михаил',
                    'middle_name': 'Михайлович',
                    'country_id': 1,
                },
                'player': [
                    {
                        'photo': 'players/МУСАЕВ_ТАМЕРЛАН.jpeg',
                        'surname': 'Мусаев',
                        'name': 'Тамеран',
                        'middle_name': None,
                        'country_of_birth_id': 1,
                        'number': 18,
                    },
                    {
                        'photo': 'players/МУХИН_МАКСИМ.jpeg',
                        'surname': 'Мухин',
                        'name': 'Максим',
                        'middle_name': 'Олегович',
                        'country_of_birth_id': 1,
                        'number': 9,
                    },
                    {
                        'photo': 'players/ОБЛЯКОВ_ИВАН.jpeg',
                        'surname': 'Сидоров',
                        'name': 'Алексей',
                        'middle_name': 'Алексеевич',
                        'country_of_birth_id': 1,
                        'number': 5,
                    },
                    {
                        'photo': 'players/ЖЕМАЛЕТДИНОВ_РИФАТ.jpeg',
                        'surname': 'Жемалетдинов',
                        'name': 'Рифат',
                        'middle_name': 'Тагирович',
                        'country_of_birth_id': 1,
                        'number': 14,
                    },
                    {
                        'photo': 'players/ЗДЕЛАР_САША.jpeg',
                        'surname': 'Зделар',
                        'name': 'Саша',
                        'middle_name': 'Иванович',
                        'country_of_birth_id': 1,
                        'number': 4,
                    },
                    {
                        'photo': 'players/КИСЛЯК_МАТВЕЙ.jpeg',
                        'surname': 'Кисляк',
                        'name': 'Матвей',
                        'middle_name': 'Олегович',
                        'country_of_birth_id': 1,
                        'number': 12,
                    },
                ]
            },
        ]

        if Club.objects.count() == 0:
            for club in clubs:
                coach = Coach.objects.create(
                    photo=club['coach']['photo'],
                    surname=club['coach']['surname'],
                    name=club['coach']['name'],
                    middle_name=club['coach']['middle_name'],
                    country_id=club['coach']['country_id'],
                )
                club_obj = Club.objects.create(
                    photo=club['photo'],
                    name=club['name'],
                    description=club['description'],
                    country_id=club['country_id'],
                    coach_id=coach.id,
                )
                for player in club['player']:
                    Player.objects.create(
                        photo=player['photo'],
                        surname=player['surname'],
                        name=player['name'],
                        middle_name=player['middle_name'],
                        country_of_birth_id=player['country_of_birth_id'],
                        number=player['number'],
                        club_id=club_obj.id,
                    )
