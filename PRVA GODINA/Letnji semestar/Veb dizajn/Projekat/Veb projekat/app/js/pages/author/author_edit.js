import { getSingleAuthor, editAuthor } from "../../db/author.js";
import { protectPage } from "../../utils/auth_check.js";

document.addEventListener("DOMContentLoaded", async () => {
    protectPage("admin");
    const result = await getSingleAuthor();
    if (!result.success) {
        console.log(result.error);
        return;
    }
    fillAuthorEditForm(result.data);
});

function fillAuthorEditForm(author) {
    document.getElementById("firstName").value = author.ime;
    document.getElementById("lastName").value = author.prezime;
    document.getElementById("biography").value = author.biografija;
    document.getElementById("birthDate").value = author.datumRodjenja;
    document.getElementById("status").value = author.status;
    document.getElementById("awardsCount").value = author.brojOsvojenihNagrada;
    document.getElementById("soldCopiesCount").value = author.brojProdatihPrimeraka;
    document.getElementById("managerPhone").value = author.kontaktTelefonMenadzera;
    document.getElementById("images").value = author.slike.join("\n");
}

const authorEditForm = document.getElementById("authorEditForm");

authorEditForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    clearAuthorErrors();
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");
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

    const result = await editAuthor(id, data);
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