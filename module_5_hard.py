from time import sleep


class Video:

    def __init__(self, title, duration, adult_mode=False, time_now=0):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title

    def __repr__(self):
        return self.title


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other.nickname

    def get_info(self):
        return self.nickname, self.password


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.curent_user = None

    # def __str__(self):
    # return str(self.users)

    def __repr__(self):
        return repr(self.videos)

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search):
        count_video = 0
        for video in self.videos:
            if search.upper() in video.title.upper():
                print(f"Найденое видео: {video}\n")
                count_video += 1
        if count_video == 0:
            print(f"Видео {search} не надено\n")

    def watch_video(self, title):
        count_watch_video = 0
        if self.curent_user is None:
            print('Войдите в аккаунт, что бы смотреть видео\n')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode == False:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        sleep(1)
                    video.time_now = 0
                    print("Конец видео\n")
                    count_watch_video += 1
                elif video.adult_mode and self.curent_user.age >= 18:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        sleep(1)
                    video.time_now = 0
                    print("Конец видео\n")
                    count_watch_video += 1
                else:
                    print("Вам нет 18\n")
                    count_watch_video += 1
                    break
        if count_watch_video == 0:
            print(f'Просмотр не возможен, видео {title} не найдено\n')

    def register(self, *users):
        for user in users:
            if user not in self.users:
                self.users.append(user)
                print(f"Регистрация прошла успешно. Здравствуйте {user.nickname}.\n")
            else:
                print(f"Пользователь с ником {user.nickname} уже существует.\n")

    def log_in(self, nickname, password):
        count_user = 0
        for user in self.users:
            if self.curent_user is None:
                if nickname == user.nickname and hash(password) == user.password:
                    self.curent_user = user
                    print(f"Добро пожаловать {nickname}!\n")
                    count_user += 1
                    break
            else:
                print(f"Выйдите из аккауна {ur.curent_user}\n")
                count_user += 1
                break
        if count_user == 0:
            print("Неверный логин или пароль\n")

    def log_out(self):
        self.curent_user = None


ur = UrTube()

# создание объектов класса Video
v1 = Video("Неустрашимый", 5)
v2 = Video("Дедпул", 5, True)
v3 = Video("Неусмиримый", 5, True)
v4 = Video("Кингсман", 5)
v5 = Video("Кингсман", 5)

# заполнение баззы данных, убираем одинаковое видео V4, V5
ur.add(v1, v2, v3, v4, v5)
print(f"{ur}\n")

# Поиск видео
ur.get_videos("де")
ur.get_videos("неу")

# Поиск несуществующего видео
ur.get_videos("мин")

# создание объектов класса User
us1 = User("Коля", 111, 18)
us2 = User("Гена", 222, 16)
us3 = User("Коля", 333, 33)

# регистрация объектов класса User
ur.register(us1, us2)

# добавление существующего пользователя
ur.register(us3)

# просмотр видео без входа в аккаут
ur.watch_video("Дедпул")

# вход в аакаунт и просмотр видео 18+
ur.log_in("Коля", 111)
ur.watch_video("Дедпул")

# Просмотр несуществующего видео
ur.watch_video("Тор")

# вход в другой аккаунт
ur.log_in("Гена", 222)
print(ur.curent_user)

# выход из аккаунта
ur.log_out()
print(ur.curent_user)

# вход в другой аккаунт просмотр видео без возростного ограничения
ur.log_in("Гена", 222)
ur.watch_video("Неустрашимый")

# просмотр видео 18+ лицом не достигшим 18 лет
ur.watch_video("Неусмиримый")