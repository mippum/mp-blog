document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".md-ellipsis").forEach(el => {
        console.log(`md-ellipsis querySelectorAll ${el.textContent}`);
        el.textContent = el.textContent.replace('Index로 돌아가기', '연재글로 돌아가기');
    });
});