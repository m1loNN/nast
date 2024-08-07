function getHeroInfo() {
    const heroSelect = document.getElementById('hero-select');
    const heroName = heroSelect.value;

    if (!heroName) {
        alert('Пожалуйста, выберите героя.');
        return;
    }

    fetch('/get_hero_info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ hero_name: heroName })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);  // Debug output
        displayHeroInfo(data);
    })
    .catch(error => console.error('Error:', error));
}

function displayHeroInfo(data) {
    const heroInfoDiv = document.getElementById('hero-info');
    heroInfoDiv.innerHTML = ''; // Clear previous content

    if (data.error) {
        heroInfoDiv.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
        return;
    }

    const heroCard = document.createElement('div');
    heroCard.className = 'hero-card row';

    const heroImageDiv = document.createElement('div');
    heroImageDiv.className = 'col-md-3';
    const heroImage = document.createElement('img');
    heroImage.src = data.image_url;
    heroImage.className = 'img-fluid';
    heroImageDiv.appendChild(heroImage);
    heroCard.appendChild(heroImageDiv);

    const heroDetailsDiv = document.createElement('div');
    heroDetailsDiv.className = 'col-md-9';

    const heroName = document.createElement('h2');
    heroName.textContent = data.hero_name;
    heroDetailsDiv.appendChild(heroName);

    const prosConsDiv = document.createElement('div');
    prosConsDiv.className = 'pros-cons';

    const prosTitle = document.createElement('h3');
    prosTitle.textContent = 'Плюсы:';
    prosConsDiv.appendChild(prosTitle);

    const prosList = document.createElement('ul');
    data.pros.forEach(pro => {
        const li = document.createElement('li');
        li.textContent = pro;
        prosList.appendChild(li);
    });
    prosConsDiv.appendChild(prosList);

    const consTitle = document.createElement('h3');
    consTitle.textContent = 'Минусы:';
    prosConsDiv.appendChild(consTitle);

    const consList = document.createElement('ul');
    data.cons.forEach(con => {
        const li = document.createElement('li');
        li.textContent = con;
        consList.appendChild(li);
    });
    prosConsDiv.appendChild(consList);

    heroDetailsDiv.appendChild(prosConsDiv);

    const countersItemsDiv = document.createElement('div');
    countersItemsDiv.className = 'counters-items';

    const countersTitle = document.createElement('h3');
    countersTitle.textContent = 'Контрпики:';
    countersItemsDiv.appendChild(countersTitle);

    const countersList = document.createElement('div');
    countersList.className = 'images';
    data.counters.forEach(counter => {
        const img = document.createElement('img');
        img.src = counter.image_url;
        img.alt = counter.name;
        img.title = counter.name;
        countersList.appendChild(img);
    });
    countersItemsDiv.appendChild(countersList);

    const itemsTitle = document.createElement('h3');
    itemsTitle.textContent = 'Контрартефакты:';
    countersItemsDiv.appendChild(itemsTitle);

    const itemsList = document.createElement('div');
    itemsList.className = 'images';
    data.counter_items.forEach(item => {
        const img = document.createElement('img');
        img.src = item.image_url;
        img.alt = item.name;
        img.title = item.name;
        itemsList.appendChild(img);
    });
    countersItemsDiv.appendChild(itemsList);

    heroDetailsDiv.appendChild(countersItemsDiv);

    heroCard.appendChild(heroDetailsDiv);
    heroInfoDiv.appendChild(heroCard);
}
