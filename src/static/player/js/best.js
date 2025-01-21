function get_bests() {
    request({
        url: '/api/v1/player/best/',
        func: showbests
    });
}

function showbests(data) {
    document.querySelector('.best-up-block').insertAdjacentHTML('beforeEnd', show_best_block(data.best_minutes_played, 'best_minutes_played'));
    document.querySelector('.best-up-block').insertAdjacentHTML('beforeEnd', show_best_block(data.best_goals, 'best_goals'));
    document.querySelector('.best-middle-block').insertAdjacentHTML('beforeEnd', show_best_block(data.best_assists, 'best_assists'));
    document.querySelector('.best-middle-block').insertAdjacentHTML('beforeEnd', show_best_block(data.best_yellow_card, 'best_yellow_card'));
    document.querySelector('.best-down-block').insertAdjacentHTML('beforeEnd', show_best_block(data.best_red_card, 'best_red_card'));
    document.querySelector('.best-down-block').insertAdjacentHTML('beforeEnd', show_best_block(data.best_rating, 'best_rating'));
}

function show_best_block(player, category) {
    let category_text = '';
    if (category === 'best_minutes_played') {
        category_text = 'Больше всего сыгранных минут';
    }
    else if (category === 'best_goals') {
        category_text = 'Лучший бомбардир';
    }
    else if (category === 'best_assists') {
        category_text = 'Лучший ассистент';
    }
    else if (category === 'best_yellow_card') {
        category_text = 'Больше всего жёлтых каточек';
    }
    else if (category === 'best_red_card') {
        category_text = 'Больше всего красных карточек';
    }
    else if (category === 'best_rating') {
        category_text = 'Лучший рейтинг';
    }

    inner_html = ` <div class="best-card-block">
                        <div class="best-card-category">
                            <h1>${category_text}</h1>
                        </div>
                        <div class="best-card-content">
                            <div class="best-card-img">
                                <img src="${player.photo}" alt="">
                            </div>
                            <div class="best-card-info">
                                <h4 class="best-info">${player.full_name}</h4>
                                <h4 class="best-info"> Клуб: ${player.club.name}</h4>
                                <h4 class="best-info">Игровой номер: ${player.number}</h4>
                                <h4 class="best-info">Голы: ${player.goals}</h4>
                                <h4 class="best-info">Ассисты: ${player.assists}</h4>
                                <h4 class="best-info">Желтые карточки: ${player.yellow_card}</h4>
                                <h4 class="best-info">Красные карточки: ${player.red_card}</h4>
                                <h4 class="best-info">Сыгранные минуты:${player.minutes_played} </h4>
                                <h4 class="best-info">Рейтинг: ${player.rating}</h4>
                            </div>
                        </div>
                    </div>`;


    return inner_html;
}


a = {
    "best_minutes_played": {
        "photo": "/media/players/%D0%94%D0%98%D0%92%D0%95%D0%95%D0%92_%D0%98%D0%93%D0%9E%D0%A0%D0%AC.jpeg",
        "full_name": "Дивеев Игорь",
        "number": 78,
        "club": {
            "id": 2,
            "name": "ЦСКА",
            "photo": "/media/clubs/CSKA_bFOue8z.png"
        },
        "minutes_played": 1620,
        "goals": 5,
        "assists": 0,
        "yellow_card": 1,
        "red_card": 0,
        "rating": 7.33
    },
    "best_goals": {
        "photo": "/media/players/%D0%A3%D0%93%D0%90%D0%9B%D0%AC%D0%94%D0%95_%D0%9C%D0%90%D0%9D%D0%A4%D0%A0%D0%95%D0%94.jpeg",
        "full_name": "Угальде Манфред",
        "number": 9,
        "club": {
            "id": 8,
            "name": "Спартак",
            "photo": "/media/clubs/Spartak.png"
        },
        "minutes_played": 1445,
        "goals": 15,
        "assists": 2,
        "yellow_card": 2,
        "red_card": 0,
        "rating": 7.59
    },
    "best_assists": {
        "photo": "/media/players/%D0%94%D0%95_%D0%A1%D0%9E%D0%A3%D0%97%D0%90_%D0%9C%D0%90%D0%A0%D0%95%D0%A1_%D0%96%D0%9E%D0%90%D0%9E_%D0%9F%D0%90%D0%A3%D0%9B%D0%9E.jpeg",
        "full_name": "Бителло Жуан Пауло",
        "number": 10,
        "club": {
            "id": 3,
            "name": "Динамо",
            "photo": "/media/clubs/Dinamo.png"
        },
        "minutes_played": 1245,
        "goals": 1,
        "assists": 8,
        "yellow_card": 2,
        "red_card": 0,
        "rating": 7.51
    },
    "best_yellow_card": {
        "photo": "/media/players/%D0%91%D0%90%D0%A2%D0%A0%D0%90%D0%9A%D0%9E%D0%92_%D0%90%D0%9B%D0%95%D0%9A%D0%A1%D0%95%D0%99.jpeg",
        "full_name": "Батраков Алексей",
        "number": 83,
        "club": {
            "id": 6,
            "name": "Локомотив",
            "photo": "/media/clubs/Lokomotiv_sy6pmmg.png"
        },
        "minutes_played": 1475,
        "goals": 10,
        "assists": 6,
        "yellow_card": 6,
        "red_card": 0,
        "rating": 7.67
    },
    "best_red_card": {
        "photo": "/media/players/%D0%A2%D0%AE%D0%9A%D0%90%D0%92%D0%98%D0%9D_%D0%9A%D0%9E%D0%9D%D0%A1%D0%A2%D0%90%D0%9D%D0%A2%D0%98%D0%9D.jpeg",
        "full_name": "Тюкавин Константин",
        "number": 70,
        "club": {
            "id": 3,
            "name": "Динамо",
            "photo": "/media/clubs/Dinamo.png"
        },
        "minutes_played": 1482,
        "goals": 7,
        "assists": 2,
        "yellow_card": 0,
        "red_card": 3,
        "rating": 6.98
    },
    "best_rating": {
        "photo": "/media/players/%D0%91%D0%90%D0%A0%D0%9A%D0%9E_%D0%AD%D0%A1%D0%95%D0%9A%D0%AC%D0%95%D0%9B%D0%AC_%D0%9E%D0%9C%D0%90%D0%A0.jpeg",
        "full_name": "Барко Эсекьель",
        "number": 5,
        "club": {
            "id": 8,
            "name": "Спартак",
            "photo": "/media/clubs/Spartak.png"
        },
        "minutes_played": 1510,
        "goals": 8,
        "assists": 6,
        "yellow_card": 2,
        "red_card": 0,
        "rating": 7.84
    }
}