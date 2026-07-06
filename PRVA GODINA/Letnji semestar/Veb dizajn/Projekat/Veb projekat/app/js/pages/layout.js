import { login, register } from "../db/auth.js"
import { getLoggedUser } from "../utils/auth_check.js";

document.addEventListener("DOMContentLoaded", () => {
    const user = getLoggedUser();
    const guestSection = document.getElementById("guestSection");
    const userSection = document.getElementById("userSection");
    const adminSection = document.getElementById("adminSection")
    if (user) {
        guestSection?.classList.add("d-none");
        guestSection?.classList.remove("d-flex");
        userSection?.classList.remove("d-none");
        userSection?.classList.add("d-flex");
    } 
    else {
        guestSection?.classList.remove("d-none");
        guestSection?.classList.add("d-flex");
        userSection?.classList.add("d-none");
        userSection?.classList.remove("d-flex");
    }
    if (user && (user.username == "маринко" || user.username == "душан")) {
        adminSection?.classList.remove("d-none")
    }
});

const loginForm = document.getElementById("loginForm");

if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        clearLoginErrors();
        const data = {
            username: document.getElementById("loginUsername").value.trim(),
            password: document.getElementById("loginPassword").value.trim()
        };
        const result = await login(data);
        if (!result.success) {
            showAllLoginErrors(result.errors);
            return;
        }
        window.location.reload();
    });
}

function clearLoginErrors() {
    const errorIds = [
        "logUsernameError",
        "logPasswordError",
    ];

    errorIds.forEach((id) => {
        const small = document.getElementById(id);
        small.textContent = "";
        small.classList.add("d-none");
    });
}

function showLoginError(errorId, message) {
    const small = document.getElementById(errorId);
    small.textContent = message;
    small.classList.remove("d-none");
}

function showAllLoginErrors(errors) {
    const errorMap = {
        username: "logUsernameError",
        password: "logPasswordError",
    };

    for (const key in errorMap) {
        if (errors[key]) {
            showLoginError(errorMap[key], errors[key]);
        }
    }
    if (errors.general)
        showLoginError("logPasswordError", errors.general);
}

const registerForm = document.getElementById("registerForm");

if (registerForm) {
    registerForm.addEventListener("submit", async(e) => {
        e.preventDefault();
        clearRegisterErrors();
        const data = {
            username: document.getElementById("regUsername").value.trim(),
            password: document.getElementById("regPassword").value.trim(),
            firstName: document.getElementById("regName").value.trim(),
            lastName: document.getElementById("regSurname").value.trim(),
            email: document.getElementById("regEmail").value.trim(),
            birthDate: document.getElementById("regBirthdate").value.trim(),
            address: document.getElementById("regAddress").value.trim(),
            occupation: document.getElementById("regOccupation").value.trim()
        };
        const result = await register(data);
        if(!result.success) {
            showAllRegisterErrors(result.errors);
            return;
        }
        window.location.reload();
    });
}

function clearRegisterErrors() {
    const errorIds = [
        "regUsernameError",
        "regPasswordError",
        "regNameError",
        "regSurnameError",
        "regEmailError",
        "regBirthdateError",
        "regAddressError",
        "regOccupationError"
    ];

    errorIds.forEach((id) => {
        const small = document.getElementById(id);
        small.textContent = "";
        small.classList.add("d-none");
    });
}

function showRegisterError(errorId, message) {
    const small = document.getElementById(errorId);
    small.textContent = message;
    small.classList.remove("d-none");
}

function showAllRegisterErrors(errors) {
    const errorMap = {
        username: "regUsernameError",
        password: "regPasswordError",
        firstName: "regNameError",
        lastName: "regSurnameError",
        email: "regEmailError",
        birthDate: "regBirthdateError",
        address: "regAddressError",
        occupation: "regOccupationError"
    };
    for (const key in errorMap) {
        if (errors[key]) {
            showRegisterError(errorMap[key], errors[key]);
        }
    }
    if (errors.general)
        showRegisterError("regOccupationError", errors.general)
}

const logoutBtn = document.getElementById("logoutBtn");

if(logoutBtn) {
    logoutBtn.addEventListener("click", () => {
    sessionStorage.removeItem("loggedUser");
    window.location.href = "/app/index.html";
    });
}

document.getElementById("currentYear").innerHTML = new Date().getFullYear();