import { getSingleAuthor, getAuthorRating, saveAuthorRating, getAuthorAverageRating, getAuthorBooks } from "../../db/author.js";
import { formatDate, formatNumber } from "../../utils/formatters.js"

const breadcrumbName = document.getElementById("breadcrumbName");
const authorProfile = document.getElementById("authorProfile");
const galleryContainer = document.getElementById("galleryContainer");
const starRatingContainer = document.getElementById("starRatingContainer");
const averageRatingText = document.getElementById("averageRatingText");
const booksCountText = document.getElementById("booksCountText");
const booksContainer = document.getElementById("booksContainer");

document.addEventListener("DOMContentLoaded", initSingleAuthorPage);

async function initSingleAuthorPage() {
    await loadAuthor();
    await loadUserRating();
    await loadAverageRating();
    await loadAuthorBooks();
}

async function loadAuthor() {
    const author = await getSingleAuthor();

    if (author.success) {
        renderAuthorProfile(author.data);
        renderGallery(author.data);
    } else {
        authorProfile.innerHTML = `
            <div class="alert alert-danger text-center rounded-4">
                ${author.error}
            </div>
        `;
    }
}

async function loadUserRating() {
    const ratingResult = await getAuthorRating();

    if (ratingResult.success) {
        renderStars(ratingResult.data);
    } else {
        renderStars(0);
    }
}

async function loadAverageRating() {
    const avgResult = await getAuthorAverageRating();

    if (avgResult.success) {
        averageRatingText.innerHTML = `${avgResult.data.toFixed(1)} / 5`;
    } else {
        averageRatingText.innerHTML = "0 / 5";
    }
}

async function loadAuthorBooks() {
    const authorBooks = await getAuthorBooks();

    if (authorBooks.success) {
        renderAuthorBooks(authorBooks.data);
        booksCountText.innerHTML = `Број књига: ${authorBooks.data.length}`;
    } else {
        renderAuthorBooks([]);
        booksCountText.innerHTML = "Број књига: 0";
    }
}

function renderAuthorProfile(author) {
    breadcrumbName.innerHTML = `${author.ime} ${author.prezime}`;

    authorProfile.innerHTML = `
        <div class="card soft-card shadow-sm rounded-4 overflow-hidden">
            <div class="card-body p-4 p-lg-5">
                <div class="row g-5 align-items-start">
                    <div class="col-lg-4 text-center">
                        <img
                            src="${author.slike?.[0] || "https://picsum.photos/500/500"}"
                            alt="${author.ime} ${author.prezime}"
                            class="author-main-img rounded-circle img-fluid mb-4"
                        >
                    </div>

                    <div class="col-lg-8 text-center text-lg-start author-info-wrap">
                        <div class="d-flex flex-column flex-md-row justify-content-between align-items-center align-items-lg-start gap-3 mb-4 text-center text-lg-start author-header-wrap">
                            <div>
                                <h1 class="section-title display-6 mb-0">
                                    ${author.ime} ${author.prezime}
                                </h1>
                            </div>

                            <a href="authors.html" class="btn btn-outline-dark rounded-pill px-4">
                                <i class="bi bi-arrow-left me-2"></i>Назад на ауторе
                            </a>
                        </div>

                        <div class="row g-3 mb-4 justify-content-center">
                            <div class="col-sm-6 col-xl-4">
                                <div class="stat-box rounded-4 p-3 h-100">
                                    <div class="info-label mb-1">Датум рођења</div>
                                    <div class="fw-semibold fs-5">
                                        ${formatDate(author.datumRodjenja)}
                                    </div>
                                </div>
                            </div>

                            <div class="col-sm-6 col-xl-4">
                                <div class="stat-box rounded-4 p-3 h-100">
                                    <div class="info-label mb-1">Број награда</div>
                                    <div class="fw-semibold fs-5">
                                        ${author.brojOsvojenihNagrada || 0}
                                    </div>
                                </div>
                            </div>

                            <div class="col-sm-6 col-xl-4">
                                <div class="stat-box rounded-4 p-3 h-100">
                                    <div class="info-label mb-1">Продатих примерака</div>
                                    <div class="fw-semibold fs-5">
                                        ${formatNumber(author.brojProdatihPrimeraka)}
                                    </div>
                                </div>
                            </div>

                            <div class="col-sm-6 col-xl-6">
                                <div class="stat-box rounded-4 p-3 h-100">
                                    <div class="info-label mb-1">Телефон менаџера</div>
                                    <div class="fw-semibold fs-5">
                                        ${author.kontaktTelefonMenadzera}
                                    </div>
                                </div>
                            </div>

                            <div class="col-sm-6 col-xl-6">
                                <div class="stat-box rounded-4 p-3 h-100">
                                    <div class="info-label mb-1">Статус</div>
                                    <div class="fw-semibold fs-5">
                                        ${author.status}
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="soft-card rounded-4 p-4">
                            <h3 class="section-title h4 mb-3">
                                <i class="bi bi-person-vcard me-2"></i>Биографија
                            </h3>

                            <p class="mb-0 text-secondary fs-5 lh-lg">
                                ${author.biografija}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function renderGallery(author) {
    const images = author.slike || [];
    const galleryImages = images.slice(1);

    if (galleryImages.length === 0) {
        galleryContainer.innerHTML = `
            <p class="text-center text-secondary fs-5 mb-0">
                Не постоји још слика.
            </p>
        `;
        return;
    }

    galleryContainer.innerHTML = "";

    galleryImages.forEach((image, index) => {
        galleryContainer.innerHTML += `
            <div class="col-md-6 col-lg-3">
                <div class="card gallery-card shadow-sm rounded-4 overflow-hidden h-100">
                    <img 
                        src="${image}" 
                        class="gallery-img" 
                        alt="Галерија ${index + 1}"
                    >
                </div>
            </div>
        `;
    });
}

function renderStars(rating) {
    starRatingContainer.innerHTML = "";

    for (let i = 1; i <= 5; i++) {
        starRatingContainer.innerHTML += `
            <i 
                class="bi ${i <= rating ? "bi-star-fill" : "bi-star"}"
                data-rating="${i}"
                style="cursor: pointer;"
            ></i>
        `;
    }

    const stars = starRatingContainer.querySelectorAll("i");

    stars.forEach((star) => {
        star.addEventListener("click", async () => {
            const selectedRating = Number(star.dataset.rating);
            const result = await saveAuthorRating(selectedRating);

            if (!result.success) {
                return;
            }

            renderStars(result.data);
            await loadAverageRating();
        });
    });
}

function renderAuthorBooks(books) {
    if (books.length === 0) {
        booksContainer.innerHTML = `
            <p class="text-center text-secondary fs-5 mb-0 p-4">
                Аутор нема своје књиге.
            </p>
        `;
        return;
    }

    booksContainer.innerHTML = `
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">Корице</th>
                        <th>Назив књиге</th>
                        <th>Жанр</th>
                        <th class="text-center pe-4">Линк</th>
                    </tr>
                </thead>
                <tbody>
                    ${books.map((book) => `
                        <tr>
                            <td class="ps-4">
                                <img 
                                    src="${book.slike?.[0] || "https://picsum.photos/100/140"}" 
                                    alt="${book.naziv}" 
                                    class="book-cover"
                                >
                            </td>
                            <td class="fw-semibold">${book.naziv}</td>
                            <td>${book.zanr}</td>
                            <td class="text-center pe-4">
                                <a href="../book/single_book.html?id=${book.id}" class="btn book-btn">
                                    Детаљније
                                </a>
                            </td>
                        </tr>
                    `).join("")}
                </tbody>
            </table>
        </div>
    `;
}