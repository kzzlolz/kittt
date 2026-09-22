<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>My Profile</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@500;600&family=Press+Start+2P&display=swap" rel="stylesheet">

<style>

* {
    box-sizing: border-box;
}

:root {
    --sea-blue: #43c6e8;
    --deep-sea: #147da4;
    --light-blue: #dff9ff;
    --crimson: #b5163c;
    --pink: #ff72ad;

    --glass: rgba(255, 255, 255, 0.40);
    --glass-light: rgba(255, 255, 255, 0.52);

    --text: #12313c;
    --muted: #55747e;
}


/* =====================================================
   PAGE
   ===================================================== */

body {
    margin: 0;
    min-height: 100vh;

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 35px 20px;

    font-family: Arial, Helvetica, sans-serif;

    color: var(--text);

    overflow-x: hidden;

    background:
        linear-gradient(
            135deg,
            #159ac4 0%,
            #73d9ed 30%,
            #d9f8ff 67%,
            #ffffff 100%
        );

    position: relative;
}


/* =====================================================
   OCEAN WAVE BACKGROUND
   ===================================================== */

body::before {
    content: "";

    position: fixed;
    inset: 0;

    z-index: 0;

    pointer-events: none;

    background:
        linear-gradient(
            to bottom,
            rgba(20, 155, 195, 0.28),
            rgba(255, 255, 255, 0.20)
        ),

        url("https://media.giphy.com/media/l0MYB8Ory7HjuBxK0/giphy.gif");

    background-size: cover;
    background-position: center;

    opacity: 0.40;

    mix-blend-mode: multiply;
}


/* =====================================================
   SOFT LIGHT
   ===================================================== */

body::after {
    content: "";

    position: fixed;
    inset: 0;

    pointer-events: none;

    z-index: 1;

    background:
        radial-gradient(
            circle at 15% 20%,
            rgba(255,255,255,0.65),
            transparent 28%
        ),

        radial-gradient(
            circle at 85% 75%,
            rgba(70,210,235,0.35),
            transparent 30%
        );
}


/* =====================================================
   FLOATING HEARTS
   ===================================================== */

.hearts {
    position: fixed;

    inset: 0;

    pointer-events: none;

    z-index: 2;

    overflow: hidden;
}


.heart {
    position: absolute;

    color: var(--crimson);

    font-size: 18px;

    opacity: 0;

    filter:
        drop-shadow(0 0 7px rgba(181,22,60,0.45));

    animation:
        heartFloat linear infinite;
}


.heart:nth-child(1) {
    left: 7%;
    bottom: -30px;
    animation-duration: 9s;
    animation-delay: 0s;
}


.heart:nth-child(2) {
    left: 22%;
    bottom: -30px;
    font-size: 13px;
    animation-duration: 12s;
    animation-delay: 2s;
}


.heart:nth-child(3) {
    left: 43%;
    bottom: -30px;
    font-size: 23px;
    animation-duration: 10s;
    animation-delay: 4s;
}


.heart:nth-child(4) {
    left: 67%;
    bottom: -30px;
    font-size: 15px;
    animation-duration: 13s;
    animation-delay: 1s;
}


.heart:nth-child(5) {
    left: 86%;
    bottom: -30px;
    font-size: 25px;
    animation-duration: 11s;
    animation-delay: 5s;
}


@keyframes heartFloat {

    0% {
        transform:
            translateY(0)
            translateX(0)
            rotate(0deg)
            scale(0.7);

        opacity: 0;
    }

    10% {
        opacity: 0.75;
    }

    50% {
        transform:
            translateY(-50vh)
            translateX(35px)
            rotate(15deg)
            scale(1);
    }

    90% {
        opacity: 0.55;
    }

    100% {
        transform:
            translateY(-115vh)
            translateX(-30px)
            rotate(-15deg)
            scale(1.1);

        opacity: 0;
    }
}


/* =====================================================
   MAIN WIDGET
   ===================================================== */

.widget {

    position: relative;

    z-index: 5;

    width: min(720px, 100%);

    border-radius: 28px;

    overflow: hidden;

    background:
        rgba(255,255,255,0.40);

    border:
        2px solid rgba(63,190,225,0.75);

    box-shadow:
        0 0 10px rgba(40,180,220,0.55),
        0 0 35px rgba(40,180,220,0.25),
        0 25px 70px rgba(0,70,100,0.22);

    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);

    animation:
        widgetEnter 1s ease forwards,
        widgetFloat 7s ease-in-out 1s infinite;

    transition:
        transform 0.35s ease,
        box-shadow 0.35s ease;
}


.widget:hover {

    box-shadow:
        0 0 14px rgba(40,180,220,0.75),
        0 0 45px rgba(40,180,220,0.32),
        0 30px 80px rgba(0,70,100,0.25);
}


@keyframes widgetEnter {

    from {
        opacity: 0;
        transform:
            translateY(25px)
            scale(0.96);
    }

    to {
        opacity: 1;
        transform:
            translateY(0)
            scale(1);
    }
}


@keyframes widgetFloat {

    0%, 100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-5px);
    }
}


/* =====================================================
   TOP PROFILE
   ===================================================== */

.profile {

    padding: 28px 30px 0;

    position: relative;
}


/* =====================================================
   PROFILE HEADER
   ===================================================== */

.profile-header {

    display: flex;

    align-items: center;

    gap: 13px;

    position: relative;

    z-index: 4;

    animation:
        fadeIn 0.8s ease 0.2s both;
}


/* =====================================================
   AVATAR
   ===================================================== */

.avatar-wrapper {

    width: 68px;
    height: 68px;

    position: relative;

    flex-shrink: 0;
}


.avatar {

    width: 60px;
    height: 60px;

    margin: 4px;

    object-fit: cover;

    border-radius: 50%;

    border:
        3px solid rgba(255,255,255,0.9);

    box-shadow:
        0 0 0 3px rgba(54,192,224,0.8),
        0 0 17px rgba(54,192,224,0.75);

    animation:
        avatarGlow 3s ease-in-out infinite;

    position: relative;

    z-index: 2;
}


.avatar-decoration {

    position: absolute;

    inset: -3px;

    border-radius: 50%;

    border:
        3px solid transparent;

    border-top-color: #35d7ee;
    border-right-color: #5ee5ff;
    border-bottom-color: #188db1;

    transform: rotate(-20deg);

    animation:
        decorationSpin 8s linear infinite;

    pointer-events: none;

    z-index: 3;
}


.avatar-decoration::after {

    content: "";

    position: absolute;

    inset: 4px;

    border-radius: 50%;

    border:
        2px dashed rgba(255,255,255,0.8);
}


@keyframes avatarGlow {

    0%, 100% {
        box-shadow:
            0 0 0 3px rgba(54,192,224,0.65),
            0 0 12px rgba(54,192,224,0.5);
    }

    50% {
        box-shadow:
            0 0 0 4px rgba(54,192,224,0.9),
            0 0 25px rgba(54,192,224,0.9);
    }
}


@keyframes decorationSpin {

    from {
        transform: rotate(-20deg);
    }

    to {
        transform: rotate(340deg);
    }
}


/* =====================================================
   USER INFORMATION
   ===================================================== */

.user-info {

    display: flex;

    flex-direction: column;

    gap: 5px;
}


/* =====================================================
   USERNAME
   ===================================================== */

.username {

    margin: 0;

    font-family:
        "Press Start 2P",
        monospace;

    font-size: 17px;

    letter-spacing: 1px;

    background:
        linear-gradient(
            90deg,
            #ffffff 0%,
            #ffffff 18%,
            #2aaed4 50%,
            #ffffff 82%,
            #ffffff 100%
        );

    background-size: 220% auto;

    color: transparent;

    -webkit-background-clip: text;
    background-clip: text;

    animation:
        prismMove 4s linear infinite;

    filter:
        drop-shadow(0 0 5px rgba(34,170,210,0.45));
}


@keyframes prismMove {

    0% {
        background-position: 200% center;
    }

    100% {
        background-position: -20% center;
    }
}


/* =====================================================
   PRONOUNS
   ===================================================== */

.pronouns {

    font-family:
        "Dancing Script",
        cursive;

    font-size: 19px;

    color: var(--pink);

    text-shadow:
        0 0 8px rgba(255,114,173,0.35);

    animation:
        pronounPulse 3s ease-in-out infinite;
}


@keyframes pronounPulse {

    0%, 100% {
        opacity: 0.8;
    }

    50% {
        opacity: 1;
    }
}


/* =====================================================
   ONLINE DOT
   ===================================================== */

.online {

    display: inline-flex;

    align-items: center;

    gap: 5px;

    margin-left: 5px;

    font-size: 10px;

    font-family: Arial, sans-serif;

    color: #277c65;
}


.online-dot {

    width: 7px;
    height: 7px;

    border-radius: 50%;

    background: #43c89b;

    box-shadow:
        0 0 8px rgba(67,200,155,0.9);

    animation:
        onlinePulse 2s infinite;
}


@keyframes onlinePulse {

    0%, 100% {
        opacity: 0.65;
    }

    50% {
        opacity: 1;
    }
}


/* =====================================================
   BANNER
   ===================================================== */

.banner {

    width: 100%;

    height: 155px;

    margin-top: 22px;

    border-radius: 20px;

    overflow: hidden;

    position: relative;

    border:
        1px solid rgba(255,255,255,0.65);

    box-shadow:
        inset 0 0 25px rgba(255,255,255,0.18),
        0 8px 25px rgba(0,80,110,0.13);
}


.banner img {

    width: 100%;
    height: 100%;

    object-fit: cover;

    animation:
        bannerMove 10s ease-in-out infinite alternate;
}


@keyframes bannerMove {

    from {
        transform: scale(1);
    }

    to {
        transform: scale(1.08);
    }
}


.banner::after {

    content: "";

    position: absolute;

    inset: 0;

    background:
        linear-gradient(
            110deg,
            transparent 35%,
            rgba(255,255,255,0.35),
            transparent 65%
        );

    transform:
        translateX(-120%);

    animation:
        bannerShine 6s ease-in-out infinite;

    pointer-events: none;
}


@keyframes bannerShine {

    0%, 55% {
        transform: translateX(-120%);
    }

    75%, 100% {
        transform: translateX(120%);
    }
}


/* =====================================================
   ABOUT ME
   ===================================================== */

.about {

    margin-top: 22px;

    padding: 24px;

    border-radius: 20px;

    background:
        rgba(255,255,255,0.40);

    border:
        1px solid rgba(255,255,255,0.65);

    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.5),
        0 8px 25px rgba(0,80,110,0.08);

    animation:
        sectionAppear 0.8s ease 0.5s both;
}


.about-title {

    margin: 0 0 14px;

    font-size: 13px;

    font-weight: 700;

    text-transform: uppercase;

    letter-spacing: 2px;

    color: #3a6975;
}


.about-text {

    margin: 0;

    font-size: 15px;

    line-height: 1.65;

    color: var(--text);

    min-height: 65px;
}


@keyframes sectionAppear {

    from {
        opacity: 0;
        transform: translateY(15px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* =====================================================
   MUSIC PLAYER
   ===================================================== */

.music-player {

    margin-top: 18px;

    padding: 17px;

    display: flex;

    align-items: center;

    gap: 15px;

    border-radius: 18px;

    background:
        rgba(255,255,255,0.45);

    border:
        1px solid rgba(255,255,255,0.65);

    box-shadow:
        0 8px 22px rgba(0,70,100,0.08);

    animation:
        sectionAppear 0.8s ease 0.65s both;

    transition:
        transform 0.3s ease,
        background 0.3s ease;
}


.music-player:hover {

    transform: translateY(-3px);

    background:
        rgba(255,255,255,0.55);
}


.album-art {

    width: 58px;
    height: 58px;

    flex-shrink: 0;

    border-radius: 13px;

    object-fit: cover;

    box-shadow:
        0 5px 14px rgba(0,0,0,0.16);

    animation:
        albumPulse 4s ease-in-out infinite;
}


@keyframes albumPulse {

    0%, 100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.035);
    }
}


.music-info {

    min-width: 0;

    flex: 1;
}


.song-name {

    margin: 0 0 5px;

    font-size: 15px;

    font-weight: 700;

    white-space: nowrap;

    overflow: hidden;

    text-overflow: ellipsis;
}


.artist {

    margin: 0;

    font-size: 13px;

    color: var(--muted);
}


.progress {

    width: 100%;

    height: 4px;

    margin-top: 10px;

    border-radius: 20px;

    overflow: hidden;

    background:
        rgba(50,130,150,0.16);
}


.progress-fill {

    width: 43%;

    height: 100%;

    border-radius: inherit;

    background:
        linear-gradient(
            90deg,
            #31b6d8,
            #1687aa
        );

    animation:
        progressMove 60s linear infinite;
}


@keyframes progressMove {

    from {
        width: 3%;
    }

    to {
        width: 96%;
    }
}


.play-button {

    width: 42px;
    height: 42px;

    border: none;

    border-radius: 50%;

    background:
        rgba(255,255,255,0.75);

    color: #187f9f;

    font-size: 17px;

    cursor: pointer;

    box-shadow:
        0 4px 12px rgba(0,80,110,0.12);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}


.play-button:hover {

    transform:
        scale(1.12);

    box-shadow:
        0 0 16px rgba(42,176,211,0.45);
}


/* =====================================================
   BUTTONS
   ===================================================== */

.buttons {

    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 15px;

    padding: 22px 0 30px;
}


.social-button {

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 9px;

    padding: 14px;

    border-radius: 16px;

    text-decoration: none;

    font-weight: 700;

    font-size: 14px;

    color: #184e5e;

    background:
        rgba(255,255,255,0.46);

    border:
        1px solid rgba(255,255,255,0.72);

    box-shadow:
        0 6px 16px rgba(0,70,100,0.09);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        background 0.25s ease;
}


.social-button:hover {

    transform:
        translateY(-6px)
        scale(1.025);

    background:
        rgba(255,255,255,0.68);

    box-shadow:
        0 12px 25px rgba(0,90,120,0.18),
        0 0 15px rgba(47,187,218,0.25);
}


.social-icon {

    font-size: 18px;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 600px) {

    body {
        padding: 15px;
    }

    .profile {
        padding: 22px 20px 0;
    }

    .username {
        font-size: 13px;
    }

    .avatar-wrapper {
        width: 61px;
        height: 61px;
    }

    .avatar {
        width: 54px;
        height: 54px;
    }

    .banner {
        height: 125px;
    }

    .about {
        padding: 19px;
    }

    .buttons {
        grid-template-columns: 1fr;
    }
}


/* =====================================================
   REDUCED MOTION
   ===================================================== */

@media (prefers-reduced-motion: reduce) {

    *,
    *::before,
    *::after {

        animation-duration: 0.01ms !important;

        animation-iteration-count: 1 !important;

        transition-duration: 0.01ms !important;
    }
}

</style>
</head>


<body>


<div class="hearts">

    <span class="heart">♥</span>
    <span class="heart">♥</span>
    <span class="heart">♥</span>
    <span class="heart">♥</span>
    <span class="heart">♥</span>

</div>



<main class="widget">


    <section class="profile">


        <div class="profile-header">


            <div class="avatar-wrapper">

                <img
                    class="avatar"
                    src="https://placehold.co/200x200"
                    alt="Avatar"
                >

                <div class="avatar-decoration"></div>

            </div>


            <div class="user-info">

                <h1 class="username">
                    your_username
                </h1>


                <div class="pronouns">
                    she/her

                    <span class="online">
                        <span class="online-dot"></span>
                        online
                    </span>

                </div>

            </div>

        </div>



        <div class="banner">

            <img
                src="https://placehold.co/1200x400"
                alt="Animated profile banner"
            >

        </div>



        <section class="about">

            <h2 class="about-title">
                about me
            </h2>


            <p class="about-text">
                your about me text goes here...
                <br>
                you can replace this whenever you're ready!
            </p>

        </section>



        <section class="music-player">


            <img
                class="album-art"
                src="https://placehold.co/200x200"
                alt="Bad Romance album art"
            >


            <div class="music-info">

                <h3 class="song-name">
                    Bad Romance
                </h3>

                <p class="artist">
                    Lady Gaga
                </p>


                <div class="progress">

                    <div class="progress-fill"></div>

                </div>

            </div>


            <button
                class="play-button"
                id="playButton"
                aria-label="Play music"
            >
                ▶
            </button>


        </section>



        <div class="buttons">


            <a
                class="social-button"
                href="#"
                target="_blank"
            >

                <span class="social-icon">
                    💬
                </span>

                Discord Server

            </a>



            <a
                class="social-button"
                href="#"
                target="_blank"
            >

                <span class="social-icon">
                    🎮
                </span>

                Roblox

            </a>


        </div>


    </section>

</main>



<script>

const playButton =
    document.getElementById("playButton");


let playing = false;


playButton.addEventListener("click", () => {

    playing = !playing;


    if (playing) {

        playButton.textContent = "❚❚";

    } else {

        playButton.textContent = "▶";

    }

});


const widget =
    document.querySelector(".widget");


document.addEventListener("mousemove", (event) => {

    const x =
        (event.clientX / window.innerWidth - 0.5);

    const y =
        (event.clientY / window.innerHeight - 0.5);


    const rotateX =
        y * -2;

    const rotateY =
        x * 2;


    widget.style.transform =
        `translateY(-2px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;

});


document.addEventListener("mouseleave", () => {

    widget.style.transform =
        "translateY(0) rotateX(0) rotateY(0)";

});

</script>


</body>
</html>