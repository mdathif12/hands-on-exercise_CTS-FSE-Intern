const searchInput = document.getElementById("searchInput");
const resultCount = document.getElementById("resultsCount");
const cards = document.querySelectorAll(".course-card");

searchInput.addEventListener("input", () => {

    const searchTerm =
        searchInput.value.toLowerCase();

    let count = 0;

    cards.forEach(card => {

        const content =
            card.textContent.toLowerCase();

        if(content.includes(searchTerm)){
            card.style.display = "block";
            count++;
        }
        else{
            card.style.display = "none";
        }

    });

    resultCount.textContent =
        `${count} courses found`;

});

cards.forEach(card => {

    card.addEventListener("click", () => {

        const course =
            card.querySelector("h3").textContent;

        alert(`Opening ${course}`);

    });

    card.addEventListener("keydown", (event) => {

        if(event.key === "Enter"){
            card.click();
        }

    });

});

const menuBtn =
    document.getElementById("menuBtn");

const navMenu =
    document.getElementById("navMenu");

menuBtn.addEventListener("click", () => {

    const expanded =
        menuBtn.getAttribute("aria-expanded") === "true";

    menuBtn.setAttribute(
        "aria-expanded",
        !expanded
    );

    navMenu.style.display =
        expanded ? "flex" : "none";

});