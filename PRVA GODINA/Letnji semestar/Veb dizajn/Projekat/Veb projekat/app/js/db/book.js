import { ref, get, push, set, remove, query, orderByChild, equalTo }
from "https://www.gstatic.com/firebasejs/12.2.1/firebase-database.js";
import { db } from "./firebase.js";

export async function getAllBooks() {
    try {
        const booksRef = ref(db, "knjige");
        const snapshot = await get(booksRef);

        if (!snapshot.exists()) {
            return { success: false, data: [], error: "Књиге нису пронађене." };
        }

        const books = [];
        snapshot.forEach((childSnapshot) => {
            books.push({ id: childSnapshot.key, ...childSnapshot.val() });
        });

        return { success: true, data: books };
    } catch (error) {
        console.error(error);
        return { success: false, data: [], error: "Грешка при учитавању књига." };
    }
}

export async function getSingleBook(id) {
    try {
        if (!id) {
            const params = new URLSearchParams(window.location.search);
            id = params.get("id");
        }

        if (!id) {
            return { success: false, data: null, error: "ID књиге није пронађен." };
        }

        const bookRef = ref(db, `knjige/${id}`);
        const snapshot = await get(bookRef);

        if (!snapshot.exists()) {
            return { success: false, data: null, error: "Књига није пронађена." };
        }

        return { success: true, data: { id: snapshot.key, ...snapshot.val() } };
    } catch (error) {
        console.error(error);
        return { success: false, data: null, error: "Грешка при учитавању књиге." };
    }
}

export async function addBook(data) {
    try {
        const booksRef = ref(db, "knjige");
        const newBookRef = push(booksRef);

        await set(newBookRef, data);

        return { success: true, id: newBookRef.key };
    } catch (error) {
        console.error(error);
        return { success: false, error: "Грешка при додавању књиге." };
    }
}

export async function updateBook(id, data) {
    try {
        const bookRef = ref(db, `knjige/${id}`);

        await set(bookRef, data);

        return { success: true };
    } catch (error) {
        console.error(error);
        return { success: false, error: "Грешка при измени књиге." };
    }
}

export async function deleteBook(id) {
    try {
        // Delete all reviews for this book
        const reviewsRef = ref(db, "recenzije");
        const reviewsQuery = query(reviewsRef, orderByChild("idKnjige"), equalTo(id));
        const snapshot = await get(reviewsQuery);

        if (snapshot.exists()) {
            const deletePromises = [];
            snapshot.forEach((child) => {
                deletePromises.push(remove(ref(db, `recenzije/${child.key}`)));
            });
            await Promise.all(deletePromises);
        }

        // Delete the book
        await remove(ref(db, `knjige/${id}`));

        return { success: true };
    } catch (error) {
        console.error(error);
        return { success: false, error: "Грешка при брисању књиге." };
    }
}

export async function getBookReviews(bookId) {
    try {
        const reviewsRef = ref(db, "recenzije");
        const reviewsQuery = query(
            reviewsRef,
            orderByChild("idKnjige"),
            equalTo(bookId)
        );

        const snapshot = await get(reviewsQuery);

        if (!snapshot.exists()) {
            return { success: true, data: [] };
        }

        const reviews = [];

        for (const [reviewId, reviewData] of Object.entries(snapshot.val())) {
            let korisnikIme = "Непознат корисник";

            const userSnapshot = await get(ref(db, `korisnici/${reviewData.idKorisnika}`));

            if (userSnapshot.exists()) {
                const user = userSnapshot.val();
                korisnikIme = `${user.ime} ${user.prezime}`.trim();
            }

            reviews.push({
                id: reviewId,
                ...reviewData,
                korisnikIme
            });
        }

        return { success: true, data: reviews };
    } 
    catch (error) {
        console.error(error);
        return { success: false, data: [], error: "Грешка при учитавању рецензија." };
    }
}

export async function addReview(bookId, text) {
    try {
        const loggedUser = JSON.parse(sessionStorage.getItem("loggedUser"));

        if (!loggedUser) {
            return { success: false, error: "Морате бити пријављени." };
        }

        const reviewsRef = ref(db, "recenzije");
        const newReviewRef = push(reviewsRef);

        await set(newReviewRef, {
            tekst: text,
            datum: new Date().toISOString().split("T")[0],
            idKnjige: bookId,
            idKorisnika: loggedUser.id
        });

        return { success: true, id: newReviewRef.key };
    } catch (error) {
        console.error(error);
        return { success: false, error: "Грешка при додавању рецензије." };
    }
}

export async function getAllBooksWithAuthors() {
    try {
        const [booksSnap, authorsSnap] = await Promise.all([
            get(ref(db, "knjige")),
            get(ref(db, "autori"))
        ]);

        if (!booksSnap.exists()) {
            return { success: false, data: [], error: "Књиге нису пронађене." };
        }

        const authorsMap = {};

        if (authorsSnap.exists()) {
            authorsSnap.forEach((child) => {
                authorsMap[child.key] = child.val();
            });
        }

        const books = [];

        booksSnap.forEach((child) => {
            const book = { id: child.key, ...child.val() };
            const author = authorsMap[book.idAutora];

            book.autorName = author
                ? `${author.ime} ${author.prezime}`.trim()
                : book.idAutora;

            books.push(book);
        });

        return { success: true, data: books };
    } catch (error) {
        console.error(error);
        return { success: false, data: [], error: "Грешка при учитавању." };
    }
}