import { courses } from "./data.js";

/* ==========================
   Task 1: ES6+ Practice
========================== */

// Destructuring
courses.forEach(course => {
    const { name, credits } = course;
    console.log(`${name} - ${credits} credits`);
});

// map()
const formattedCourses = courses.map(
    ({ code, name, credits }) =>
        `${code} — ${name} (${credits} credits)`
);

console.log("Formatted Courses:");
console.log(formattedCourses);

// filter()
const highCreditCourses = courses.filter(
    course => course.credits >= 4
);

console.log("Courses with credits >= 4:");
console.log(highCreditCourses);

console.log(
    `Count: ${highCreditCourses.length}`
);

// reduce()
const totalCredits = courses.reduce(
    (total, course) => total + course.credits,
    0
);

console.log(`Total Credits: ${totalCredits}`);

/* ==========================
   Task 2: DOM Rendering
========================== */

const courseGrid =
    document.querySelector(".course-grid");

const totalCreditsText =
    document.getElementById("total-credits");

function renderCourses(courseList) {
    courseGrid.innerHTML = "";

    const fragment =
        document.createDocumentFragment();

    courseList.forEach(course => {
        const article =
            document.createElement("article");

        article.className = "course-card";

        article.dataset.id = course.id;

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p><strong>Code:</strong> ${course.code}</p>
            <p><strong>Credits:</strong> ${course.credits}</p>
        `;

        fragment.appendChild(article);
    });

    courseGrid.appendChild(fragment);

    const credits = courseList.reduce(
        (sum, course) => sum + course.credits,
        0
    );

    totalCreditsText.textContent =
        `Total Credits: ${credits}`;
}

renderCourses(courses);

/* ==========================
   Task 3: Interactivity
========================== */

const searchInput =
    document.getElementById("search-courses");

const sortButton =
    document.getElementById("sort-btn");

const selectedCourse =
    document.getElementById("selected-course");

// Search
searchInput.addEventListener("input", e => {
    const searchValue =
        e.target.value.toLowerCase();

    const filteredCourses =
        courses.filter(course =>
            course.name
                .toLowerCase()
                .includes(searchValue)
        );

    renderCourses(filteredCourses);
});

// Sort
sortButton.addEventListener("click", () => {
    const sortedCourses =
        [...courses].sort(
            (a, b) => b.credits - a.credits
        );

    renderCourses(sortedCourses);
});

// Event Delegation
courseGrid.addEventListener("click", event => {
    const card =
        event.target.closest(".course-card");

    if (!card) return;

    const courseId =
        Number(card.dataset.id);

    const selected =
        courses.find(
            course => course.id === courseId
        );

    selectedCourse.textContent =
        `Selected Course: ${selected.name} | Grade: ${selected.grade}`;

    alert(
        `${selected.name} - Grade: ${selected.grade}`
    );
});