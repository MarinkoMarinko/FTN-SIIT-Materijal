export function getLoggedUser() {
    const user = sessionStorage.getItem("loggedUser");
    return JSON.parse(user); 
}

export function isAdmin() {
    const user = getLoggedUser();
    if (!user) {
        return false;
    }
    return user.username == "маринко" || user.username == "душан";
}

export function protectPage(requiredRole = "user") {
    const user = getLoggedUser();

    if (!user) {
        window.location.href = "/app/index.html";
        return;
    }

    if (requiredRole === "admin" && !isAdmin(user)) {
        window.location.href = "/app/index.html";
        return;
    }
}