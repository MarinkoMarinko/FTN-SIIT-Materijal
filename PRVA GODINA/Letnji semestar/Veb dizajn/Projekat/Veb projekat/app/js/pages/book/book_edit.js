import { getSingleBook, updateBook, getAllBooksWithAuthors } from "../../db/book.js";
import { getAllAuthors } from "../../db/author.js";
import { protectPage } from "../../utils/auth_check.js";    

const ISBN_REGEX = /^(978|979)-?\d{1,5}-?\d{1,7}-?\d{1,6}-?\d$/;

const params = new URLSearchParams(window.location.search);
const bookId = params.get("id");


document.addEventListener("DOMContentLoaded", async () => {
    protectPage("admin");
    await populateAuthors();

    const booksResult = await getAllBooksWithAuthors();
    if (booksResult.success) {
        setupGenreAutocomplete(booksResult.data);
        populateFormats(booksResult.data);
    }

    await prefill(); 

    document.querySelector("form").addEventListener("submit", async (e) => {
        e.preventDefault();
        clearErrors();

        if (!validate()) return;

        const result = await updateBook(bookId, collectData());

        if (result.success) {
            window.location.href = "admin_books.html";
        } else {
            showError("naziv", result.error);
        }
    });
});


function setupGenreAutocomplete(allBooks) {
    const existingGenres = [...new Set(allBooks.map(b => b.zanr).filter(Boolean))];
    const input = document.getElementById("zanr");
    const dropdown = document.getElementById("genreDropdown");

    input.addEventListener("input", () => {
        const term = input.value.trim().toLowerCase();
        dropdown.innerHTML = "";

        if (!term) {
            dropdown.classList.remove("open");
            return;
        }

        const matches = existingGenres.filter(g => g.toLowerCase().includes(term));

        matches.forEach(genre => {
            const div = document.createElement("div");
            div.className = "genre-option";
            div.textContent = genre;
            div.addEventListener("mousedown", () => {
                input.value = genre;
                dropdown.classList.remove("open");
            });
            dropdown.appendChild(div);
        });

        const exactMatch = existingGenres.some(g => g.toLowerCase() === term);
        if (!exactMatch) {
            const div = document.createElement("div");
            div.className = "genre-option new-genre";
            div.textContent = `Додај нови жанр: "${input.value.trim()}"`;
            div.addEventListener("mousedown", () => {
                dropdown.classList.remove("open");
            });
            dropdown.appendChild(div);
        }

        dropdown.classList.toggle("open", dropdown.children.length > 0);
    });

    input.addEventListener("blur", () => {
        setTimeout(() => dropdown.classList.remove("open"), 150);
    });

    input.addEventListener("focus", () => {
        dropdown.innerHTML = "";
        existingGenres.forEach(genre => {
            const div = document.createElement("div");
            div.className = "genre-option";
            div.textContent = genre;
            div.addEventListener("mousedown", () => {
                input.value = genre;
                dropdown.classList.remove("open");
            });
            dropdown.appendChild(div);
        });
        if (existingGenres.length > 0) dropdown.classList.add("open");
    });
}

function populateFormats(allBooks) {
    const existingFormats = [...new Set(allBooks.map(b => b.format).filter(Boolean))].sort();
    const input = document.getElementById("format");
    const dropdown = document.getElementById("formatDropdown");

    input.addEventListener("input", () => {
        const term = input.value.trim().toLowerCase();
        dropdown.innerHTML = "";

        if (!term) { dropdown.classList.remove("open"); return; }

        const matches = existingFormats.filter(f => f.toLowerCase().includes(term));
        matches.forEach(fmt => {
            const div = document.createElement("div");
            div.className = "genre-option";
            div.textContent = fmt;
            div.addEventListener("mousedown", () => { input.value = fmt; dropdown.classList.remove("open"); });
            dropdown.appendChild(div);
        });

        const exactMatch = existingFormats.some(f => f.toLowerCase() === term);
        if (!exactMatch) {
            const div = document.createElement("div");
            div.className = "genre-option new-genre";
            div.textContent = `Додај нови формат: "${input.value.trim()}"`;
            div.addEventListener("mousedown", () => { dropdown.classList.remove("open"); });
            dropdown.appendChild(div);
        }

        dropdown.classList.toggle("open", dropdown.children.length > 0);
    });

    input.addEventListener("blur", () => setTimeout(() => dropdown.classList.remove("open"), 150));

    input.addEventListener("focus", () => {
        dropdown.innerHTML = "";
        existingFormats.forEach(fmt => {
            const div = document.createElement("div");
            div.className = "genre-option";
            div.textContent = fmt;
            div.addEventListener("mousedown", () => { input.value = fmt; dropdown.classList.remove("open"); });
            dropdown.appendChild(div);
        });
        if (existingFormats.length > 0) dropdown.classList.add("open");
    });
}  


async function populateAuthors() {
    const result = await getAllAuthors();
    if (!result.success) return;

    const select = document.getElementById("id_autora");
    select.innerHTML = `<option value="">Изабери аутора</option>`;

    result.data.forEach((a) => {
        select.innerHTML += `<option value="${a.id}">${a.ime} ${a.prezime}</option>`;
    });
}

async function prefill() {
    if (!bookId) return;

    const result = await getSingleBook(bookId);
    if (!result.success) return;

    const b = result.data;

    document.getElementById("naziv").value        = b.naziv || "";
    document.getElementById("id_autora").value    = b.idAutora || "";
    document.getElementById("opis").value         = b.opis || "";
    document.getElementById("slike").value        = (b.slike || []).join("\n");
    document.getElementById("zanr").value         = b.zanr || "";
    document.getElementById("format").value       = b.format || "";
    document.getElementById("cena").value         = b.cena || "";
    document.getElementById("broj_strana").value  = b.brojStrana || "";
    document.getElementById("isbn").value         = b.isbn || "";
}

function collectData() {
    return {
        naziv: document.getElementById("naziv").value.trim(),
        idAutora: document.getElementById("id_autora").value,
        opis: document.getElementById("opis").value.trim(),
        slike: document.getElementById("slike").value.trim().split("\n").map(s => s.trim()).filter(Boolean),
        zanr: document.getElementById("zanr").value,
        format: document.getElementById("format").value,
        cena: Number(document.getElementById("cena").value),
        brojStrana: Number(document.getElementById("broj_strana").value),
        isbn: document.getElementById("isbn").value.trim()
    };
}

function validate() {
    let ok = true;

    const naziv = document.getElementById("naziv").value.trim();
    if (!naziv) {
        showError("naziv", "Назив је обавезан.");
        ok = false;
    }

    const idAutora = document.getElementById("id_autora").value;
    if (!idAutora) {
        showError("id_autora", "Аутор је обавезан.");
        ok = false;
    }

    const opis = document.getElementById("opis").value.trim();
    if (!opis) {
        showError("opis", "Опис је обавезан.");
        ok = false;
    }

    const zanr = document.getElementById("zanr").value;
    if (!zanr) {
        showError("zanr", "Жанр је обавезан.");
        ok = false;
    }

    const format = document.getElementById("format").value;
    if (!format) {
        showError("format", "Формат је обавезан.");
        ok = false;
    }

    const cena = Number(document.getElementById("cena").value);
    if (!cena || cena <= 0) {
        showError("cena", "Цена мора бити већа од 0.");
        ok = false;
    }

    const brojStrana = Number(document.getElementById("broj_strana").value);
    if (!brojStrana || brojStrana <= 0) {
        showError("broj_strana", "Број страна мора бити већи од 0.");
        ok = false;
    }

    const isbn = document.getElementById("isbn").value.trim();
    if (!isbn) {
        showError("isbn", "ISBN је обавезан.");
        ok = false;
    } else if (!ISBN_REGEX.test(isbn)) {
        showError("isbn", "ISBN није у исправном формату.");
        ok = false;
    }

    return ok;
}

function showError(fieldId, message) {
    const label = document.querySelector(`label.error-label[for="${fieldId}-greska"]`);

    if (label) {
        label.textContent = message;
        label.style.display = "block";
    }
}

function clearErrors() {
    document.querySelectorAll("label.error-label").forEach(el => {
        el.textContent = "";
        el.style.display = "none";
    });
}