import { getSingleBook, getBookReviews, addReview } from "../../db/book.js";
import { getAuthorById } from "../../db/author.js";
import { ref, get } from "https://www.gstatic.com/firebasejs/12.2.1/firebase-database.js";
import { db } from "../../db/firebase.js";

const params = new URLSearchParams(window.location.search);
const bookId = params.get("id");

document.addEventListener("DOMContentLoaded", async () => {
    await loadBook();
    await loadReviews();
    setupReviewForm();
});

async function loadBook() {
    if (!bookId) return;

    const result = await getSingleBook(bookId);
    if (!result.success) return;

    const b = result.data;

    // Cover
    document.querySelector(".book-cover-main").src = b.slike?.[0] || "";
    document.querySelector(".book-cover-main").alt = b.naziv;

    // Badges
    document.querySelector(".badge-genre").innerHTML  = `<i class="bi bi-bookmark-fill me-1"></i> ${b.zanr}`;
    document.querySelector(".badge-format").innerHTML = `<i class="bi bi-journal me-1"></i> ${b.format}`;

    // Title & price
    document.querySelector(".book-title").textContent = b.naziv;
    document.querySelector(".price-line").innerHTML =
        `${Number(b.cena).toLocaleString("sr-RS")} <span class="price-currency">рсд</span>`;

    // About
    const aboutTexts = document.querySelectorAll(".about-text");
    if (aboutTexts[0]) aboutTexts[0].textContent = b.opis;
    if (aboutTexts[1]) aboutTexts[1].textContent = "";

    // Stats (pages, isbn, jezik)
    const statValues = document.querySelectorAll(".stat-value");
    if (statValues[0]) statValues[0].textContent = b.brojStrana;
    if (statValues[1]) statValues[1].textContent = b.isbn;
    // statValues[2] = jezik — leave as-is (static "Српски")

    // Breadcrumb
    const breadcrumbActive = document.querySelector(".breadcrumb-item.active");
    if (breadcrumbActive) breadcrumbActive.textContent = b.naziv;

    // Details table rows
    const detailsValues = document.querySelectorAll(".details-value");
    if (detailsValues[0]) detailsValues[0].textContent = b.naziv;
    // detailsValues[1] = author — filled below
    if (detailsValues[2]) detailsValues[2].textContent = b.zanr;
    if (detailsValues[3]) detailsValues[3].textContent = b.format;
    if (detailsValues[4]) detailsValues[4].textContent = b.brojStrana;
    if (detailsValues[5]) detailsValues[5].textContent = `${Number(b.cena).toLocaleString("sr-RS")} рсд`;
    if (detailsValues[6]) detailsValues[6].innerHTML = `<span class="details-badge">${b.isbn}</span>`;
    if (detailsValues[7]) detailsValues[7].innerHTML = `<span class="details-badge">${b.idAutora}</span>`;

    // Author name
    if (b.idAutora) {
        const authorResult = await getAuthorById(b.idAutora);

        if (authorResult.success) {
            const a = authorResult.data;
            const fullName = `${a.ime} ${a.prezime}`.trim();
            const authorHref = `../author/single_author.html?id=${b.idAutora}`;

            // Author line under title
            const authorLink = document.querySelector(".author-link");
            if (authorLink) {
                authorLink.textContent = fullName;
                authorLink.href = authorHref;
            }

            // Details table author cell
            if (detailsValues[1]) {
                detailsValues[1].innerHTML =
                    `<a href="${authorHref}" class="details-author-link">${fullName}</a>`;
            }
        }
    }
}

const MESECI = [
    "јануар", "фебруар", "март", "април", "мај", "јун",
    "јул", "август", "септембар", "октобар", "новембар", "децембар"
];

function formatDate(dateStr) {
    if (!dateStr) return "";

    const [y, m, d] = dateStr.split("-");
    return `${parseInt(d)}. ${MESECI[parseInt(m) - 1]} ${y}.`;
}

async function loadReviews() {
    if (!bookId) return;

    const bookResult = await getSingleBook(bookId);
    const bookName = bookResult.success ? bookResult.data.naziv : "";

    const result = await getBookReviews(bookId);
    const reviewsCol = document.querySelector(".reviews-wrapper .col-lg-8");
    const countBadge = document.querySelector(".review-count-badge");

    reviewsCol.querySelectorAll(".review-card").forEach(el => el.remove());
    reviewsCol.querySelectorAll(".no-reviews-text").forEach(el => el.remove());

    if (!result.success || result.data.length === 0) {
        if (countBadge) countBadge.textContent = "0 рецензија";
        reviewsCol.innerHTML += `<p class="text-secondary fst-italic mt-3 no-reviews-text">Нема рецензија за ову књигу.</p>`;
        return;
    }

    if (countBadge) countBadge.textContent = `${result.data.length} рецензија`;

    for (const review of result.data) {
        let displayName = review.korisnikIme || "Непознат корисник";
        let initials = "??";

        if (review.korisnikIme) {
            const parts = review.korisnikIme.trim().split(" ");
            initials = parts.length >= 2
                ? `${parts[0][0]}${parts[1][0]}`.toUpperCase()
                : parts[0].slice(0, 2).toUpperCase();
        }

        if (!review.korisnikIme && review.idKorisnika) {
            try {
                const userSnap = await get(ref(db, `korisnici/${review.idKorisnika}`));

                if (userSnap.exists()) {
                    const u = userSnap.val();
                    displayName = `${u.ime} ${u.prezime}`.trim();
                    initials = `${u.ime?.[0] || ""}${u.prezime?.[0] || ""}`.toUpperCase() || "??";
                }
            } catch (e) {
                console.log(e);
            }
        }

        const dateStr = formatDate(review.datum);

        reviewsCol.innerHTML += `
            <div class="card rounded-4 shadow-sm mb-3 review-card">
                <div class="card-body p-4">
                    <div class="d-flex align-items-center gap-3 mb-3">
                        <div class="review-avatar d-flex align-items-center justify-content-center rounded-circle fw-bold flex-shrink-0">
                            ${initials}
                        </div>
                        <div>
                            <div class="fw-semibold review-author-name">${displayName}</div>
                            <div class="review-date">${dateStr}</div>
                        </div>
                    </div>
                    <p class="fst-italic mb-3 review-text">${review.tekst}</p>
                    <div class="review-book-tag">
                        <i class="bi bi-journal me-1"></i>${bookName}
                    </div>
                </div>
            </div>
        `;
    }
}

function setupReviewForm() {
    const textarea  = document.querySelector("textarea.review-input");
    const charCount = document.querySelector(".review-char-count");
    const submitBtn = document.querySelector(".review-submit-btn");

    textarea?.addEventListener("input", () => {
        charCount.textContent = `${textarea.value.length} / 2000 карактера`;
    });

    submitBtn?.addEventListener("click", async () => {
        if (!bookId) return;

        const text = textarea.value.trim();
        if (!text) return;

        const loggedUser = JSON.parse(sessionStorage.getItem("loggedUser"));

        if (!loggedUser) {
            alert("Морате бити пријављени да бисте оставили рецензију.");
            return;
        }

        const result = await addReview(bookId, text);

        if (result.success) {
            textarea.value = "";
            charCount.textContent = "0 / 2000 карактера";
            await loadReviews();
        } else {
            alert(result.error);
        }
    });
}