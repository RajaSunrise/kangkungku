const API_URL = "";

async function login(username, password) {
    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);

    try {
        const response = await fetch(`${API_URL}/auth/token`, {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || "Login failed");
        }

        const data = await response.json();
        localStorage.setItem("token", data.access_token);

        // Decode token to get role
        const payload = JSON.parse(atob(data.access_token.split('.')[1]));
        localStorage.setItem("role", payload.role);
        localStorage.setItem("username", payload.sub);

        if (payload.role === "admin") {
            window.location.href = "/admin.html";
        } else {
            window.location.href = "/dashboard.html";
        }
    } catch (error) {
        alert(error.message);
    }
}

async function register(username, email, password) {
    try {
        const response = await fetch(`${API_URL}/auth/register`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, email, password }),
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || "Registration failed");
        }

        alert("Registration successful! Please login.");
        window.location.href = "/login.html";
    } catch (error) {
        alert(error.message);
    }
}

function logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("role");
    localStorage.removeItem("username");
    window.location.href = "/login.html";
}

function checkAuth() {
    const token = localStorage.getItem("token");
    if (!token) {
        window.location.href = "/login.html";
    }
    return token;
}

function checkAdmin() {
    const token = checkAuth();
    const role = localStorage.getItem("role");
    if (role !== "admin") {
        alert("Access denied. Admin only.");
        window.location.href = "/dashboard.html";
    }
    return token;
}

function getToken() {
    return localStorage.getItem("token");
}

function getUserInfo() {
    return {
        username: localStorage.getItem("username"),
        role: localStorage.getItem("role")
    };
}
