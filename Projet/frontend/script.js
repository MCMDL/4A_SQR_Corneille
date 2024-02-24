async function printTweet() {
    const reponse = await fetch("http://localhost:5000/api/printTweet/1");
    const tweet = await reponse.json();
    console.log(tweet);
  }