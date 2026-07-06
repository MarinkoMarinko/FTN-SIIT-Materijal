import { createAuthor } from "../../db/author.js";
import { protectPage } from "../../utils/auth_check.js";

document.addEventListener("DOMContentLoaded", () => {
    protectPage("admin");
});

const authorAddForm = document.getElementById("authorAddForm");

authorAddForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    clearAuthorErrors();
    const data = {
        firstName: document.getElementById("firstName").value.trim(),
        lastName: document.getElementById("lastName").value.trim(),
        biography: document.getElementById("biography").value.trim(),
        images: document.getElementById("images").value.trim(),
        birthDate: document.getElementById("birthDate").value.trim(),
        status: document.getElementById("status").value.trim(),
        awardsCount: document.getElementById("awardsCount").value.trim(),
        soldCopiesCount: document.getElementById("soldCopiesCount").value.trim(),
        managerPhone: document.getElementById("managerPhone").value.trim()
    };
    const result = await createAuthor(data);
    if (!result.success) {
        showAllAuthorErrors(result.errors);
        return;
    }
    window.location.href = "./admin_authors.html";
});


function clearAuthorErrors() {
    const errorIds = [
        "firstNameError",
        "lastNameError",
        "biographyError",
        "imagesError",
        "birthDateError",
        "statusError",
        "awardsCountError",
        "soldCopiesCountError",
        "managerPhoneError"
    ];

    errorIds.forEach((id) => {
        const span = document.getElementById(id);
        span.textContent = "";
        span.classList.add("d-none");
    });
}

function showAuthorError(errorId, message) {
    const span = document.getElementById(errorId);
    span.textContent = message;
    span.classList.remove("d-none");
}

function showAllAuthorErrors(errors) {
    const errorMap = {
        firstName: "firstNameError",
        lastName: "lastNameError",
        biography: "biographyError",
        images: "imagesError",
        birthDate: "birthDateError",
        status: "statusError",
        awardsCount: "awardsCountError",
        soldCopiesCount: "soldCopiesCountError",
        managerPhone: "managerPhoneError"
    };

    for (const key in errorMap) {
        if (errors[key]) {
            showAuthorError(errorMap[key], errors[key]);
        }
    }

    if (errors.general) {
        showAuthorError("managerPhoneError", errors.general);
    }
}