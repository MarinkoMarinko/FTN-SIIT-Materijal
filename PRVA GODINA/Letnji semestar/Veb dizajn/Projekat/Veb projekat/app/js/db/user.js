import { ref, get, query, orderByChild, equalTo } 
from "https://www.gstatic.com/firebasejs/12.2.1/firebase-database.js";
import { db } from "./firebase.js"

export async function getUser(id) {
    if (!id) {
        return {
            success: false,
            error: "Корисник није пронађен."
        };
    }

    try {
        const userRef = ref(db, `korisnici/${id}`);
        const snapshot = await get(userRef);

        if (!snapshot.exists()) {
            return {
                success: false,
                error: "Корисник није пронађен."
            };
        }

        return {
            success: true,
            data: {
                id: snapshot.key,
                ...snapshot.val()
            }
        };
    } 
    catch (error) {
        return {
            success: false,
            error: "Грешка при учитавању корисника."
        };
    }
}

export async function getUserReviews(id) {
    if (!id) {
        return {
            success: false,
            error: "Корисник није пронађен."
        };
    }

    try {
        const reviewsRef = ref(db, "recenzije");
        const reviewsQuery = query(
            reviewsRef,
            orderByChild("idKorisnika"),
            equalTo(id)
        );

        const snapshot = await get(reviewsQuery);

        if (!snapshot.exists()) {
            return {
                success: true,
                data: []
            };
        }

        const reviews = [];

        for (const [reviewId, reviewData] of Object.entries(snapshot.val())) {
            let knjigaNaziv = "Непозната књига";

            const bookSnapshot = await get(ref(db, `knjige/${reviewData.idKnjige}`));

            if (bookSnapshot.exists()) {
                const book = bookSnapshot.val();
                knjigaNaziv = book.naziv;
            }

            reviews.push({
                id: reviewId,
                ...reviewData,
                knjigaNaziv
            });
        }

        return {
            success: true,
            data: reviews
        };
    } 
    catch (error) {
        console.log(error);

        return {
            success: false,
            error: "Грешка при учитавању рецензија."
        };
    }
}

export async function getUserRatings(id) {
    if (!id) {
        return {
            success: false,
            error: "Корисник није пронађен."
        };
    }

    try {
        const ratingsRef = ref(db, "ocene");
        const ratingsQuery = query(
            ratingsRef,
            orderByChild("idKorisnika"),
            equalTo(id)
        );

        const snapshot = await get(ratingsQuery);

        if (!snapshot.exists()) {
            return {
                success: true,
                data: []
            };
        }

        const ratings = [];

        for (const [ratingId, ratingData] of Object.entries(snapshot.val())) {
            let autorIme = "Непознат аутор";

            const authorSnapshot = await get(ref(db, `autori/${ratingData.idAutora}`));

            if (authorSnapshot.exists()) {
                const author = authorSnapshot.val();
                autorIme = `${author.ime} ${author.prezime}`.trim();
            }

            ratings.push({
                id: ratingId,
                ...ratingData,
                autorIme
            });
        }

        return {
            success: true,
            data: ratings
        };

    } 
    catch (error) {
        console.log(error);

        return {
            success: false,
            error: "Грешка при учитавању оцена."
        };
    }
}