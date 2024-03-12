async function printTweet() {
    const reponse = await fetch("https://jubilant-space-orbit-wqq47rrjpvr29gx5-5000.app.github.dev/api/printTweet/api/printTweet/1");
    const tweet = await reponse.json();
    console.log(tweet);
  }