const boutonEnvoi = document.querySelector('#bouton-envoi'); //lien au bouton tweeter de la page html

boutonEnvoi.addEventListener('click', (evenement) => {
  evenement.preventDefault(); // Empêche le comportement par défaut de soumission du formulaire

  const nomUtilisateur = 'Utilisateur 1'; // On verra plus atrd pour l'utilisateur 
  const contenuTweet = document.querySelector('#textarea-tweet').value;

  const donnees = {
    nomUtilisateur,
    tweet: contenuTweet
  };

  fetch('/api/tweeter', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(donnees)
  })
  .then(reponse => reponse.json())
  .then(donnees => {
    console.log('Succès:', donnees);
    // maintenant faut afficher le tweet dans la page et modif le html
  })
  .catch((erreur) => {
    console.error('Erreur:', erreur);
  });
});
