window.onload = function() {
    request({
        url: '/api/v1/club/',
        func: showClubs,
    });
}

function showClubs(data) {
    console.log(data);
    let inner_text = '';
    data.clubs.forEach((item) => {
        inner_text += `<div class="club-info" data-id="${item.id}" onclick="get_club_info(this)">
                            <h6>${item.name}</h6>
                            <img src="${item.photo}" alt="">
                        </div>`;
    });

    document.querySelector('.club-block').insertAdjacentHTML('beforeEnd', inner_text);
}

function get_club_info(elem) {
    let id = elem.dataset.id;
    
    request({
        url: `/api/v1/club/${id}/`,
    }).then(data => {
        let section_club = document.querySelector('.section-club');
        section_club.style.display = 'flex';
        let player_list_block = document.querySelector('.main-player-list-block');
        let inner_html = '';
        data.player.forEach(player => {
            inner_html += `<div class="player-card">
                                <div class="player-img-block" ondblclick="show_add_player(${player.id})">
                                    <img src="${player.photo}" alt="" class="player-img">
                                </div>
                                <h3 class="player-title">${player.surname} ${player.name} ${player.middle_name}</h3>
                                <div class="player-info">
                                    <p class="player-number">Номер: ${player.number}</p>
                                    <p class="player-country">Страна: ${player.country_of_birth.name}</p>
                                </div>
                            </div>`;
        });
        player_list_block.insertAdjacentHTML('beforeEnd', inner_html);

        let club_img = document.querySelector('.club-img');
        let club_title = document.querySelector('.club-title');
        let club_desc = document.querySelector('.club-desc');
        let club_country = document.querySelector('.club-country');
        let club_coach_title = document.querySelector('.club_coach-title');
        // let club_coach_country = document.querySelector('.club-coach-country');

        club_img.src = data.photo;
        club_title.innerText = data.name;
        club_desc.innerText = data.description;
        club_country.innerText = data.country.name;
        club_coach_title.innerText = `${data.coach.surname} ${data.coach.name} ${data.coach.middle_name}`;
        // club_coach_country.innerText = data.coach.country.name;

    });
}


function close_club_info() {
    let section_club = document.querySelector('.section-club');
    section_club.style.display = 'none';
    let player_list_block = document.querySelector('.main-player-list-block');
    player_list_block.innerHTML = ''
}

/**
 * 
 */

