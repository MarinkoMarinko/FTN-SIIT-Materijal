import { getAllBooksWithAuthors } from "../../db/book.js";

const booksGrid = document.querySelector("#books-section ~ section .row.g-4");
const filterBar = document.querySelector(".filter-bar .d-flex");

// Cache all books so we don't re-fetch on every filter/search
let allBooks = [];

document.addEventListener("DOMContentLoaded", async () => {
    if (!booksGrid) return;

    await fetchBooks();
    renderFilterButtons();
    renderBooks();
    setupSearch();
});

async function fetchBooks() {
    booksGrid.innerHTML = `
        <div class="col-12 text-center py-5">
            <p class="text-muted fs-5">Учитавање књига...</p>
        </div>
    `;

    const result = await getAllBooksWithAuthors();

    if (!result.success) {
        booksGrid.innerHTML = `
            <div class="col-12 text-center py-5">
                <p class="text-danger fs-5">${result.error}</p>
            </div>
        `;
        return;
    }

    allBooks = result.data;
}

function getUniqueGenres() {
    const genres = allBooks.map(b => b.zanr).filter(Boolean);
    return [...new Set(genres)].sort();
}

function renderFilterButtons() {
    if (!filterBar) return;

    const genres = getUniqueGenres();

    // Keep the label, rebuild buttons
    const label = filterBar.querySelector(".filter-label");
    filterBar.innerHTML = "";
    if (label) filterBar.appendChild(label);

    // "All" button
    const allBtn = document.createElement("button");
    allBtn.className = "btn btn-sm rounded-pill filter-btn active";
    allBtn.textContent = "Све";
    allBtn.addEventListener("click", () => handleFilterClick(allBtn));
    filterBar.appendChild(allBtn);

    // One button per genre found in DB
    genres.forEach(genre => {
        const btn = document.createElement("button");
        btn.className = "btn btn-sm rounded-pill filter-btn";
        btn.textContent = genre;
        btn.addEventListener("click", () => handleFilterClick(btn));
        filterBar.appendChild(btn);
    });
}

function handleFilterClick(clickedBtn) {
    filterBar.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
    clickedBtn.classList.add("active");

    renderBooks();
}

function getActiveGenre() {
    const active = filterBar?.querySelector(".filter-btn.active");
    if (!active) return null;
    const text = active.textContent.trim();
    return text === "Све" ? null : text;
}

function getSearchTerm() {
    return document.querySelector(".search-box")?.value.trim().toLowerCase() || "";
}

function highlightMatch(text, term) {
    if (!term) return text;
    const escaped = term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const regex = new RegExp(`(${escaped})`, "gi");
    return text.replace(regex, `<mark>$1</mark>`);
}

function renderBooks() {
    const genre = getActiveGenre();
    const term = getSearchTerm();

    let books = allBooks;

    if (genre) {
        books = books.filter(b => b.zanr === genre);
    }

    if (term) {
        books = books.filter(b => b.naziv.toLowerCase().includes(term));
    }

    if (books.length === 0) {
        booksGrid.innerHTML = `
            <div class="col-12 text-center py-5">
                <p class="text-muted fs-5">Нема пронађених књига.</p>
            </div>
        `;
        return;
    }

    booksGrid.innerHTML = "";

    books.forEach((book) => {
        const cover = book.slike?.[0] || "https://picsum.photos/300/400";
        const highlightedTitle = highlightMatch(book.naziv, term);

        booksGrid.innerHTML += `
            <div class="col-lg-3 col-md-6">
                <div class="book-card h-100">
                    <div class="book-cover-wrapper">
                        <span class="book-genre-badge">${book.zanr}</span>
                        <a href="pages/book/single_book.html?id=${book.id}" class="book-cover-link">
                            <img src="${cover}" alt="${book.naziv}">
                        </a>
                    </div>
                    <div class="book-card-body">
                        <a href="pages/author/single_author.html?id=${book.idAutora}" class="book-author d-block text-decoration-none">
                            ${book.autorName}
                        </a>
                        <a href="pages/book/single_book.html?id=${book.id}" class="book-title d-block">
                            ${highlightedTitle}
                        </a>
                    </div>
                    <div class="book-card-footer">
                        <div class="book-price">${Number(book.cena).toLocaleString("sr-RS")} <span>рсд</span></div>
                        <a href="pages/book/single_book.html?id=${book.id}" class="btn-details">Детаљи</a>
                    </div>
                </div>
            </div>
        `;
    });
}

function setupSearch() {
    const searchInput = document.querySelector(".search-box");
    const searchBtn = document.querySelector(".search-btn");

    if (!searchBtn || !searchInput) return;

    searchBtn.addEventListener("click", () => renderBooks());
    searchInput.addEventListener("input", () => renderBooks());
    
}