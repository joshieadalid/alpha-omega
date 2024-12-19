document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("login-form");
    const registerForm = document.getElementById("register-form");
    const showLoginButton = document.getElementById("show-login");
    const showRegisterButton = document.getElementById("show-register");

    // Alternar entre formularios
    showLoginButton.addEventListener("click", () => {
        loginForm.classList.add("active");
        registerForm.classList.remove("active");
    });

    showRegisterButton.addEventListener("click", () => {
        registerForm.classList.add("active");
        loginForm.classList.remove("active");
    });

    async function apiRequest(url, method, body = null, token = null) {
        const headers = { "Content-Type": "application/json" };
        if (token) headers["Authorization"] = `Bearer ${token}`;

        const response = await fetch(url, {
            method,
            headers,
            body: body ? JSON.stringify(body) : null
        });

        return response;
    }

    function getAuthToken() {
        return localStorage.getItem("token");
    }

    async function accessMeetingPage() {
        const token = getAuthToken();
        if (!token) {
            alert("You must log in first!");
            window.location.href = "/";
            return;
        }

        try {
            const response = await apiRequest("/modes/meeting", "GET", null, token);
            if (response.ok) {
                window.location.href = "/modes/meeting"; // Redirigir directamente
            } else {
                const data = await response.json();
                alert(data.message || "Access denied");
            }
        } catch (error) {
            console.error("Error accessing meeting page:", error);
            alert("An error occurred while trying to access the page");
        }
    }

    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const username = document.getElementById("login-username").value;
        const password = document.getElementById("login-password").value;

        try {
            const response = await apiRequest("/auth/login", "POST", { username, password });
            const data = await response.json();

            if (response.ok) {
                localStorage.setItem("token", data.token);
                alert("Login successful! Redirecting to meeting page...");
                accessMeetingPage();
            } else {
                alert(data.message || "Login failed");
            }
        } catch (error) {
            console.error("Error during login:", error);
            alert("An error occurred during login");
        }
    });

    registerForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        try {
            const response = await apiRequest("/auth/register", "POST", { username, password });
            const data = await response.json();

            if (response.ok) {
                alert("Registration successful! You can now log in.");
                showLoginButton.click();
            } else {
                alert(data.message || "Registration failed");
            }
        } catch (error) {
            console.error("Error during registration:", error);
            alert("An error occurred during registration");
        }
    });
});
