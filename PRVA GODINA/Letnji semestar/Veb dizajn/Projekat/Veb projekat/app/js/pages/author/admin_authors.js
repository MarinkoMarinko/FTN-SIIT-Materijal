import { getAllAuthors, deleteSingleAuthor } from "../../db/author.js";
import { protectPage } from "../../utils/auth_check.js";
const authorsTableBody = document.getElementById("authorsTableBody");
const deleteModal = document.getElementById("deleteModal");
const confirmDeleteBtn = document.getElementById("confirmDeleteBtn");
const closeStatusModalBtn = document.getElementById("closeStatusModalBtn")

document.addEventListener("DOMContentLoaded", loadAuthors);

async function loadAuthors() {
    protectPage("admin");
    const result = await getAllAuthors();
    if (result.success) {
        renderAuthors(result.data);
    }
    else {
        authorsTableBody.innerHTML = `
            <tr>
                <td colspan="4" class="text-center text-muted">
                    ${result.error}
                </td>
            </tr>
        `;
        return;
    }
}

function renderAuthors(authors) {
    authorsTableBody.innerHTML = "";
    authors.forEach((author) => {
        authorsTableBody.innerHTML += `
            <tr>
                <td>${author.id}</td>
                <td>${author.ime} ${author.prezime}</td>
                <td class="manager-phone">${author.kontaktTelefonMenadzera}</td>
                <td class="text-center">
                    <div class="d-flex justify-content-center gap-2 flex-wrap admin-actions">
                        <a href="./single_author.html?id=${author.id}" class="btn btn-sm btn-admin-details">Детаљније</a>
                        <a href="author_edit.html?id=${author.id}" class="btn btn-sm btn-admin-edit">Измени</a>
                        <button 
                            class="btn btn-sm btn-admin-delete"
                            data-id="${author.id}"
                            data-bs-toggle="modal"
                            data-bs-target="#deleteModal">
                            Обриши
                        </button>
                    </div>
                </td>
            </tr>
        `;
    });
}

deleteModal.addEventListener("show.bs.modal", (e) => {
    const button = e.relatedTarget;     // button that opened the delete modal
    const authorId = button.dataset.id;
    confirmDeleteBtn.dataset.id = authorId;
});

confirmDeleteBtn.addEventListener("click", deleteAuthor);

async function deleteAuthor() {
    const authorId = confirmDeleteBtn.dataset.id;
    if (!authorId) {
        showDeleteStatusModal(false, "Аутор није пронађен.");
        return;
    }

    const result = await deleteSingleAuthor(authorId);

    const deleteModalInstance = bootstrap.Modal.getInstance(deleteModal);
    deleteModalInstance.hide();
    if (result.success) {
        showDeleteStatusModal(true, "Аутор је успешно обрисан.");
    } 
    else {
        showDeleteStatusModal(false, result.error);
    }
}

function showDeleteStatusModal(success, message) {
    const statusTitle = document.getElementById("deleteStatusTitle");
    const statusMessage = document.getElementById("deleteStatusMessage");
    const statusHeader = document.getElementById("deleteStatusHeader");

    statusTitle.innerHTML = success ? "Успешно брисање" : "Грешка";
    statusMessage.innerHTML = message;
    statusHeader.classList.add(success ? "bg-success" : "bg-danger", "text-white");

    const statusModal = new bootstrap.Modal(document.getElementById("deleteStatusModal"));
    statusModal.show();
}

closeStatusModalBtn.addEventListener("click", (e) => {
    window.location.reload();
});