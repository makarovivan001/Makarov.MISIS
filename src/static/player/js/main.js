function show_add_player(id=null) {
    document.querySelector('.add-player-window').style.display = "flex";

    get_player_form();
    if (id) {
        get_player_by_id(id);
        document.getElementById('player_save_btn').dataset.id = id;
    }
}

function hide_add_player() {
    document.querySelector('.add-player-window').style.display = "none";
    document.getElementById("country_of_birth_id").innerHTML = '';
    document.getElementById("club_id").innerHTML = '';
}

function get_player_values() {
    let formData = new FormData();
    let surname = document.getElementById('surname').value;
    if (surname !== '') {
        formData.append('surname', surname);
    } else {
        alert('Вы не заполнили имя');
        throw {}
    }
    formData.append('name', document.getElementById('name').value);
    formData.append('middle_name', document.getElementById('middle_name').value);
    formData.append('number', document.getElementById('number').value);
    formData.append('country_of_birth_id', document.getElementById('country_of_birth_id').value);
    formData.append('club_id', document.getElementById('club_id').value);
    let playerPhotoInput = document.getElementById('player_photo');
    if (playerPhotoInput.files.length !== 0) {
        let playerPhotoFile = playerPhotoInput.files[0];
        formData.append('photo', playerPhotoFile);
    }

    return formData;
}

function add_player() {
    let formData= get_player_values();

    request({
        url: '/api/v1/player/',
        form_data: formData,
        method: 'POST',
    }).then(data => {
        hide_add_player();
    });
}

function edit_player(id) {
    let formData = get_player_values();
    formData.append('id', id);

    request({
        url: '/api/v1/player/',
        form_data: formData,
        method: 'PATCH',
    }).then(data => {
        hide_add_player();
    });
}

function get_player_form() {
    request({
        url: '/api/v1/player/form/',
    }).then(data => {
        let selectCountry = document.getElementById("country_of_birth_id");
        data.countries.forEach(country => {
            let option = document.createElement("option");
            option.value = country.id;
            option.text = country.name;
            selectCountry.appendChild(option);
        });

        let selectClub = document.getElementById("club_id");
        data.clubs.forEach(club => {
            let option = document.createElement("option");
            option.value = club.id;
            option.text = club.name;
            selectClub.appendChild(option);
        });

    });
}

function get_player_by_id(id) {
    request({
        url: `/api/v1/player/${id}/`,
    }).then(data => {
        console.log("player data", data);

        // Получите элементы формы и установите их значения
        document.getElementById('surname').value = data.surname;
        document.getElementById('name').value = data.name;
        document.getElementById('middle_name').value = data.middle_name;
        document.getElementById('number').value = data.number;

        // Для select элементов, вы должны установить значения, но нужно учесть, что эти значения должны
        // быть доступны в списке опций
        document.getElementById('country_of_birth_id').value = data.country_of_birth.id;
        document.getElementById('club_id').value = data.club.id;

        // Установите data-id кнопки сохранения как id игрока
        document.getElementById('player_save_btn').dataset.id = data.id;

        if (data.photo) {
            document.querySelector('.player_photo_block img').src = data.photo;
        }
    });
}

function player_save(elem) {
    let id = elem.dataset.id;
    if (id) {
        edit_player(id);
    } else {
        add_player();
    }
}