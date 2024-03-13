// Fonction pour afficher un message d'alerte
function messageAlert(message, type) {
    const alertBox = document.getElementById('alertBox');
    alertBox.textContent = message;
    if (type === 0) {
        alertBox.style.backgroundColor = 'green'; // Succès
    } else if (type === 1) {
        alertBox.style.backgroundColor = 'yellow'; // Avertissement
    } else {
        alertBox.style.backgroundColor = 'red'; // Erreur
    }
    alertBox.style.display = 'block';
    setTimeout(function() {
        alertBox.style.display = 'none';
    }, 3000); // Masquer l'alerte après 3 secondes
}

// Fonction pour afficher un tweet dans la section "Tweets"
function displayTweet(author, message) {
    const listeTweets = document.getElementById('liste-tweets');

    // Création des éléments HTML pour le tweet
    const li = document.createElement('li');
    const divContenuTweet = document.createElement('div');
    const strong = document.createElement('strong');
    const p = document.createElement('p');

    // Ajout du contenu au tweet
    strong.textContent = author;
    strong.classList.add('nom-utilisateur'); // Ajout de la classe pour le nom d'utilisateur
    p.textContent = message;

    // Construction de la structure du tweet
    divContenuTweet.appendChild(strong);
    divContenuTweet.appendChild(p);
    li.appendChild(divContenuTweet);

    // Ajout du tweet à la liste des tweets
    listeTweets.appendChild(li);
}

// Fonction pour ajouter un tweet
async function addTweet() {
    const inputUsername = document.getElementById('zone-texte-username');
    const inputTweet = document.getElementById('zone-texte-tweet');
    const username = inputUsername.value;
    const tweet = inputTweet.value;

    const url = 'http://127.0.0.1:5000/api/tweeter';
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "username": username,
            "message": tweet
        })
    });
    const data = await response.json();
    if (data.success) {
        messageAlert("Tweet ajouté.", 0);  // Afficher un message de succès
        displayTweet(username, tweet); // Afficher le tweet ajouté dans la section "Tweets"
    }
    else
        messageAlert("Tweet n'a pas été ajouté.", 2);  // Afficher un message d'erreur
}

// Récupération du formulaire par son ID
const tweetForm = document.getElementById('tweetForm');

// Ajout d'un gestionnaire d'événements pour la soumission du formulaire
tweetForm.addEventListener('submit', async function(event) {
    event.preventDefault(); // Empêche la soumission du formulaire par défaut

    await addTweet(); // Appel de la fonction pour ajouter le tweet

    // Effacer le contenu des textarea après avoir ajouté le tweet
    document.getElementById('zone-texte-username').value = '';
    document.getElementById('zone-texte-tweet').value = '';
});
