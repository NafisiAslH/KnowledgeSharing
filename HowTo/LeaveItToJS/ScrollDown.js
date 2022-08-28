async function scrollDown(how_many, delay=3000) {
    for (let i=0; i<how_many; i++) {
        window.scrollTo(0, document.body.scrollHeight);
        await new Promise(r => setTimeout(r, delay));
    }
}
await scrollDown(10)
