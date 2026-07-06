import { getAllBooks, deleteBook } from "../../db/book.js";
import { protectPage } from "../../utils/auth_check.js";

const tbody = document.querySelector(".admin-table tbody");
let bookToDeleteId = null;

document.addEventListener("DOMContentLoaded", async () => {
    protectPage("admin");
    await loadBooks();

    // Confirm delete button inside modal
    document.getElementById("confirmDeleteBtn").addEventListener("click", async () => {
        if (!bookToDeleteId) return;
        const result = await deleteBook(bookToDeleteId);
        if (result.success) {
            const modal = bootstrap.Modal.getInstance(document.getElementById("deleteModal"));
            modal.hide();
            await loadBooks();
        } else {
            alert(result.error);
        }
    });
});

async function loadBooks() {
    const result = await getAllBooks();
    if (!result.success) {
        tbody.innerHTML = `<tr><td colspan="5" class="text-center text-danger">${result.error}</td></tr>`;
        return;
    }

    tbody.innerHTML = "";
    result.data.forEach((book, index) => {
        tbody.innerHTML += `
            <tr>
                <td>${index + 1}</td>
                <td>${book.naziv}</td>
                <td>${book.zanr}</td>
                <td>${book.isbn}</td>
                <td class="text-center">
                    <div class="d-flex justify-content-center gap-2 flex-wrap admin-actions">
                        <a href="single_book.html?id=${book.id}" class="btn btn-sm btn-admin-details">Детаљи</a>
                        <a href="book_edit.html?id=${book.id}" class="btn btn-sm btn-admin-edit">Измени</a>
                        <button 
                            class="btn btn-sm btn-admin-delete" 
                            data-bs-toggle="modal" 
                            data-bs-target="#deleteModal"
                            data-id="${book.id}">
                            Обриши
                        </button>
                    </div>
                </td>
            </tr>
        `;
    });

    // Attach delete id to each delete button
    tbody.querySelectorAll(".btn-admin-delete").forEach((btn) => {
        btn.addEventListener("click", () => {
            bookToDeleteId = btn.dataset.id;
        });
    });
}