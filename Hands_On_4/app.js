// ================================
// TASK 1 - PROMISES & ASYNC/AWAIT
// ================================

// Step 45 - Promise Chaining
function fetchUser(id) {
    return fetch(
        "https://jsonplaceholder.typicode.com/users/" + id
    )
    .then(response => response.json())
    .then(user => {
        console.log("Promise User:", user.name);
        return user;
    });
}

fetchUser(1);

// Step 46 - Async/Await Version
async function fetchUserAsync(id) {
    try {
        const response = await fetch(
            "https://jsonplaceholder.typicode.com/users/" + id
        );

        const user = await response.json();

        console.log("Async User:", user.name);
    }
    catch(error) {
        console.error(error);
    }
}

fetchUserAsync(2);

// Local Course Data
const courses = [
    {
        title: "HTML"
    },
    {
        title: "CSS"
    },
    {
        title: "JavaScript"
    }
];

// Step 47
function fetchAllCourses() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(courses);
        }, 1000);
    });
}

// Step 48
function renderCourses(courseList) {

    const container =
        document.getElementById("courses");

    container.innerHTML = "";

    courseList.forEach(course => {

        container.innerHTML += `
            <div class="card">
                <h3>${course.title}</h3>
            </div>
        `;
    });
}

fetchAllCourses()
    .then(data => {

        document.getElementById(
            "course-loading"
        ).style.display = "none";

        renderCourses(data);
    });

// Step 49 - Promise.all
Promise.all([
    fetch(
        "https://jsonplaceholder.typicode.com/users/1"
    ).then(res => res.json()),

    fetch(
        "https://jsonplaceholder.typicode.com/users/2"
    ).then(res => res.json())
])
.then(users => {

    console.log(
        "Promise.all Users:",
        users[0].name,
        users[1].name
    );
});


// =================================
// TASK 2 - FETCH + ERROR HANDLING
// =================================

// Step 50
async function apiFetch(url) {

    const response = await fetch(url);

    if (!response.ok) {
        throw new Error(
            `HTTP Error: ${response.status}`
        );
    }

    return await response.json();
}

// Step 51 + 52
async function loadPosts() {

    const notifications =
        document.getElementById("notifications");

    const spinner =
        document.getElementById("spinner");

    const errorContainer =
        document.getElementById("error-container");

    const retryBtn =
        document.getElementById("retryBtn");

    spinner.classList.remove("hidden");

    errorContainer.innerHTML = "";
    retryBtn.classList.add("hidden");

    try {

        const posts = await apiFetch(
            "https://jsonplaceholder.typicode.com/posts"
        );

        notifications.innerHTML = "";

        posts.slice(0, 5).forEach((post, index) => {

            const messages = [
                "New JavaScript module has been published.",
                "Assignment submission deadline is approaching.",
                "Your HTML course progress has been updated.",
                "A new coding challenge is available.",
                "Certificate is ready for completed courses."
            ];

            notifications.innerHTML += `
                <div class="card">
                    <h3>📢 Notification ${index + 1}</h3>
                    <p>${messages[index]}</p>
                </div>
            `;
        });

    } catch (error) {

        errorContainer.innerHTML =
            "Unable to load notifications. Please try again.";

        retryBtn.classList.remove("hidden");

    } finally {

        spinner.classList.add("hidden");
    }
}
// Step 53 - Simulate 404
async function test404() {

    try {

        await apiFetch(
            "https://jsonplaceholder.typicode.com/nonexistent"
        );

    }
    catch(error) {

        document.getElementById(
            "error-container"
        ).innerHTML =
            "Oops! Resource not found (404).";

        document
            .getElementById("retryBtn")
            .classList.remove("hidden");
    }
}

test404();

// Step 54 - Retry Button

document
    .getElementById("retryBtn")
    .addEventListener("click", () => {

        loadPosts();
    });


// =================================
// TASK 3 - AXIOS
// =================================

// Step 58 - Request Interceptor
axios.interceptors.request.use(config => {

    console.log(
        "API call started:",
        config.url
    );

    return config;
});

// Step 56
async function axiosFetch(url) {

    const response =
        await axios.get(url);

    return response.data;
}

// Step 57
async function loadUserPosts() {

    try {

        const response =
            await axios.get(
                "https://jsonplaceholder.typicode.com/posts",
                {
                    params: {
                        userId: 1
                    }
                }
            );

        console.log(
            "Axios User Posts:",
            response.data
        );
    }
    catch(error) {

        console.error(error);
    }
}

loadUserPosts();


// =================================
// FETCH vs AXIOS
// =================================

/*

1. Fetch requires response.json()
   Axios parses JSON automatically.

2. Fetch does not throw for 404/500.
   Axios throws automatically.

3. Fetch is built into browsers.
   Axios is an external library.

*/