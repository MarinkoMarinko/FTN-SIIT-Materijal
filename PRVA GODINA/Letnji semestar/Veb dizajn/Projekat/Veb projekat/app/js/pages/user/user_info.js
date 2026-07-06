import { getUser, getUserReviews, getUserRatings } from "../../db/user.js"
import { protectPage } from "../../utils/auth_check.js";
import { formatDate } from "../../utils/formatters.js"

const reviewsList = document.getElementById("userReviewsList");
const ratingsList = document.getElementById("userRatingsList");

document.addEventListener("DOMContentLoaded", initUserPage);

async function initUserPage() {
    protectPage("user");
    const loggedUser = JSON.parse(sessionStorage.getItem("loggedUser"));
    await loadUser(loggedUser.id);
    await loadUserReviews(loggedUser.id);
    await loadUserRatings(loggedUser.id);
}

async function loadUser(id) {
    const user = await getUser(id);
    if (user.success) {
        renderUser(user.data)
    }
    else {
        
    }
}

async function loadUserReviews(id) {
    const reviews = await getUserReviews(id);
    if (!reviews.success) {
        reviewsList.innerHTML = `<p class="mb-0">Дошло је до грешке при учитавању.</p>`;
        return;
    }
    if (reviews.data.length === 0) {
        reviewsList.innerHTML = `<p class="mb-0">Корисник нема рецензије.</p>`;
        return;
    }
    renderUserReviews(reviews.data);
}

async function loadUserRatings(id) {
    const ratings = await getUserRatings(id);
    if (!ratings.success) {
        ratingsList.innerHTML = `<p class="mb-0">Дошло је до грешке при учитавању.</p>`;
        return;
    }
    if (ratings.data.length === 0) {
        ratingsList.innerHTML = `<p class="mb-0">Корисник нема оцене.</p>`;
        return;
    }
    renderUserRatings(ratings.data);
}

function renderUser(user) {
    document.getElementById("profileFirstName").innerHTML = user.ime || "";
    document.getElementById("profileLastName").innerHTML = user.prezime || "";
    document.getElementById("profileEmail").innerHTML = user.email || "";
    document.getElementById("profileAddress").innerHTML = user.adresa || "";
    document.getElementById("profileBirthDate").innerHTML = formatDate(user.datumRodjenja) || "";
    document.getElementById("profileOccupation").innerHTML = user.zanimanje || "";
}

function renderUserReviews(reviews) {
    reviewsList.innerHTML = "";
    reviews.forEach((review) => {
        reviewsList.innerHTML += `
            <div class="custom-list-item">
                <p class="review-text">${review.tekst || ""}</p>
                <p class="meta-text mb-0 text-end">
                    Рецензија је додељена књизи:
                    <a href="../book/single_book.html?id=${review.knjigaId}" class="item-link">
                        ${review.knjigaNaziv}
                    </a>
                </p>
            </div>
        `;
    });
}

function renderStars(value) {
    let stars = "";
    for (let i = 1; i <= 5; i++) {
        stars += i <= value ? "★" : "☆";
    }
    return stars;
}

function renderUserRatings(ratings) {
    ratingsList.innerHTML = "";
    ratings.forEach((rating) => {
        ratingsList.innerHTML += `
            <div class="custom-list-item">
                <div class="rating-badge">
                    <span class="stars">${renderStars(rating.vrednost)}</span> ${rating.vrednost}/5
                </div>
                <p class="meta-text mb-0 text-end">
                    Оцена је додељена аутору:
                    <a href="../author/single_author.html?id=${rating.idAutora}" class="item-link">
                        ${rating.autorIme}
                    </a>
                </p>
            </div>
        `;
    });
}