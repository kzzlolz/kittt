const content = document.getElementById("content");

const commandsButton = document.getElementById("commands-button");
const interactButton = document.getElementById("interact-button");
const widgetsButton = document.getElementById("widgets-button");

function showContent(html) {
    content.innerHTML = html;

    content.style.animation = "none";
    void content.offsetWidth;
    content.style.animation = "contentAppear 0.5s ease";
}

commandsButton.addEventListener("click", () => {
    showContent(`
        <h2 class="panel-title">✦ 𝒞𝑜𝓂𝓂𝒶𝓃𝒹𝓈 ✦</h2>

        <div class="command-card">
            <strong>🍜 /feeditsuki</strong>
            <span>Feed Itsuki during her hunger event!</span>
        </div>

        <div class="command-card">
            <strong>🌸 /dashboard</strong>
            <span>Open Itsuki's dashboard.</span>
        </div>

        <div class="command-card">
            <strong>✨ More coming soon...</strong>
            <span>Itsuki is still learning!</span>
        </div>
    `);
});

interactButton.addEventListener("click", () => {
    showContent(`
        <h2 class="panel-title">✦ 𝓘𝓷𝓽𝓮𝓻𝓪𝓬𝓽 ✦</h2>

        <div class="interact-card">
            <strong>🍙 Interact with Itsuki</strong>
            <span>
                You need the special role to interact with Itsuki.
            </span>
        </div>

        <div class="interact-card">
            <strong>🔒 Role Required</strong>
            <span>@Special Role!</span>
        </div>
    `);
});

widgetsButton.addEventListener("click", () => {
    showContent(`
        <h2 class="panel-title">✦ 𝒲𝒾𝒹𝑔𝑒𝓉 𝒞𝑒𝓃𝑡𝑒𝓇 ✦</h2>

        <div class="widget-card">
            <strong>🧩 Widget Center</strong>
            <span>
                Nothing here yet... ♡
            </span>
        </div>

        <div class="widget-card">
            <strong>✨ Coming Soon</strong>
            <span>
                We're gonna fill this place with cute little widgets!
            </span>
        </div>
    `);
});
