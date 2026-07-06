import { ref, get, set, update, remove, push, query, orderByChild, equalTo } from "https://www.gstatic.com/firebasejs/12.2.1/firebase-database.js"
import { db } from "./firebase.js"

import {
    nameValidation,
    biographyValidation,
    imagesValidation,
    birthDateValidation,
    statusValidation,
    awardsCountValidation,
    soldCopiesCountValidation,
    managerPhoneValidation
} from "../utils/author_validation.js";

export async function getAllAuthors() {
    try {
        const authorsRef = ref(db, "autori");
        const snapshot = await get(authorsRef);

        if (!snapshot.exists()) {
            return {
                success: false,
                data: [],
                error: "Аутори нису пронађени."
            };
        }

        const authors = [];

        snapshot.forEach((childSnapshot) => {
            authors.push({
                id: childSnapshot.key,
                ...childSnapshot.val(),
            });
        });

        return {
            success: true,
            data: authors
        };

    } 
    catch (error) {
        console.error(error);
        return {
            success: false,
            data: [],
            error: "Грешка при учитавању аутора."
        };
    }
}

export async function getSingleAuthor() {
    try {
        const params = new URLSearchParams(window.location.search);
        const id = params.get("id");

        if (!id) {
            return {
                success: false,
                data: null,
                error: "Дошло је до неочекиване грешке."
            };
        }

        const authorRef = ref(db, `autori/${id}`);
        const snapshot = await get(authorRef);

        if (!snapshot.exists()) {
            return {
                success: false,
                data: null,
                error: "Аутор није пронађен."
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
        console.error(error);

        return {
            success: false,
            data: null,
            error: "Грешка при учитавању аутора."
        };
    }
}

export async function getAuthorRating() {
    try {
        const params = new URLSearchParams(window.location.search);
        const authorId = params.get("id");

        const loggedUser = JSON.parse(sessionStorage.getItem("loggedUser"));

        if (!loggedUser) {
            return {
                success: true,
                data: 0
            };
        }

        if (!authorId) {
            return {
                success: false,
                data: 0,
                error: "Аутор није пронађен."
            };
        }

        const ratingsRef = ref(db, "ocene");
        const authorRatingsQuery = query(
            ratingsRef,
            orderByChild("idAutora"),
            equalTo(authorId)
        );

        const snapshot = await get(authorRatingsQuery);

        if (!snapshot.exists()) {
            return {
                success: true,
                data: 0
            };
        }

        let rating = 0;

        snapshot.forEach((childSnapshot) => {
            const ratingData = childSnapshot.val();

            if (ratingData.idKorisnika === loggedUser.id) {
                rating = Number(ratingData.vrednost);
            }
        });

        return {
            success: true,
            data: rating
        };

    } 
    catch (error) {
        console.error(error);
        return {
            success: false,
            data: 0,
            error: "Дошло је до неочекиване грешке."
        };
    }
}

export async function saveAuthorRating(rating) {
    try {
        const params = new URLSearchParams(window.location.search);
        const authorId = params.get("id");

        const loggedUser = JSON.parse(sessionStorage.getItem("loggedUser"));

        if (!loggedUser) {
            return {
                success: false,
                error: "Морате бити пријављени да бисте оценили аутора."
            };
        }

        if (!authorId) {
            return {
                success: false,
                error: "Дошло је до неочекиване грешке."
            };
        }

        const ratingsRef = ref(db, "ocene");
        const authorRatingsQuery = query(
            ratingsRef,
            orderByChild("idAutora"),
            equalTo(authorId)
        );

        const snapshot = await get(authorRatingsQuery);

        let existingRatingKey = null;

        if (snapshot.exists()) {
            snapshot.forEach((childSnapshot) => {
                const ratingData = childSnapshot.val();

                if (ratingData.idKorisnika === loggedUser.id) {
                    existingRatingKey = childSnapshot.key;
                }
            });
        }

        const ratingData = {
            vrednost: rating,
            datum: new Date().toISOString().split("T")[0],
            idAutora: authorId,
            idKorisnika: loggedUser.id
        };

        if (existingRatingKey) {
            await set(ref(db, `ocene/${existingRatingKey}`), ratingData);
        } else {
            await set(push(ratingsRef), ratingData);
        }

        return {
            success: true,
            data: rating
        };

    } 
    catch (error) {
        console.error(error);
        return {
            success: false,
            error: "Дошло је до неочекиване грешке."
        };
    }
}

export async function getAuthorAverageRating() {
    try {
        const params = new URLSearchParams(window.location.search);
        const authorId = params.get("id");

        if (!authorId) {
            return {
                success: false,
                data: 0,
                error: "Дошло је до неочекиване грешке."
            };
        }

        const ratingsRef = ref(db, "ocene");
        const authorRatingsQuery = query(
            ratingsRef,
            orderByChild("idAutora"),
            equalTo(authorId)
        );

        const snapshot = await get(authorRatingsQuery);

        if (!snapshot.exists()) {
            return {
                success: true,
                data: 0
            };
        }

        let sum = 0;
        let count = 0;

        snapshot.forEach((childSnapshot) => {
            const ratingData = childSnapshot.val();

            sum += Number(ratingData.vrednost);
            count++;
        });

        return {
            success: true,
            data: count === 0 ? 0 : sum / count
        };

    } 
    catch (error) {
        console.error(error);
        return {
            success: false,
            data: 0,
            error: "Дошло је до неочекиване грешке."
        };
    }
}

export async function getAuthorBooks() {
    try {
        const params = new URLSearchParams(window.location.search);
        const authorId = params.get("id");

        if (!authorId) {
            return {
                success: false,
                data: [],
                error: "Дошло је до неочекиване грешке."
            };
        }

        const booksRef = ref(db, "knjige");
        const booksQuery = query(
            booksRef,
            orderByChild("idAutora"),
            equalTo(authorId)
        );

        const snapshot = await get(booksQuery);

        if (!snapshot.exists()) {
            return {
                success: true,
                data: []
            };
        }

        const books = [];

        snapshot.forEach((childSnapshot) => {
            books.push({
                id: childSnapshot.key,
                ...childSnapshot.val()
            });
        });

        return {
            success: true,
            data: books
        };

    } 
    catch (error) {
        console.error(error);
        return {
            success: false,
            data: [],
            error: "Дошло је до неочекиване грешке."
        };
    }
}

export async function getAuthorById(id) {
    try {
        const authorRef = ref(db, `autori/${id}`);
        const snapshot = await get(authorRef);

        if (!snapshot.exists()) {
            return {
                success: false,
                data: null,
                error: "Аутор није пронађен."
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
        console.error(error);
        return {
            success: false,
            data: null,
            error: "Грешка при учитавању аутора."
        };
    }
}

export async function deleteSingleAuthor(id) {
    if (!id) {
        return {
            success: false,
            error: "Аутор није пронађен."
        };
    }

    try {
        const authorRef = ref(db, `autori/${id}`);

        const ratingsQuery = query(
            ref(db, "ocene"),
            orderByChild("idAutora"),
            equalTo(id)
        );

        const ratingsSnapshot = await get(ratingsQuery);

        if (ratingsSnapshot.exists()) {
            const deletePromises = [];

            ratingsSnapshot.forEach((ratingSnapshot) => {
                deletePromises.push(remove(ref(db, `ocene/${ratingSnapshot.key}`)));
            });

            await Promise.all(deletePromises);
        }

        await remove(authorRef);

        return {
            success: true
        };

    } 
    catch (error) {
        console.error(error);
        return {
            success: false,
            error: "Грешка при брисању аутора."
        };
    }
}

export async function createAuthor(data) {
    const errors = {};

    const firstName = data.firstName;
    const lastName = data.lastName;
    const biography = data.biography;
    const images = data.images;
    const birthDate = data.birthDate;
    const status = data.status;
    const awardsCount = data.awardsCount;
    const soldCopiesCount = data.soldCopiesCount;
    const managerPhone = data.managerPhone;

    const firstNameError = nameValidation(firstName, "Име");
    if (firstNameError) errors.firstName = firstNameError;

    const lastNameError = nameValidation(lastName, "Презиме");
    if (lastNameError) errors.lastName = lastNameError;

    const biographyError = biographyValidation(biography);
    if (biographyError) errors.biography = biographyError;

    const imagesError = imagesValidation(images);
    if (imagesError) errors.images = imagesError;

    const birthDateError = birthDateValidation(birthDate);
    if (birthDateError) errors.birthDate = birthDateError;

    const statusError = statusValidation(status);
    if (statusError) errors.status = statusError;

    const awardsCountError = awardsCountValidation(awardsCount);
    if (awardsCountError) errors.awardsCount = awardsCountError;

    const soldCopiesCountError = soldCopiesCountValidation(soldCopiesCount);
    if (soldCopiesCountError) errors.soldCopiesCount = soldCopiesCountError;

    const managerPhoneError = managerPhoneValidation(managerPhone);
    if (managerPhoneError) errors.managerPhone = managerPhoneError;

    if (Object.keys(errors).length > 0) {
        return {
            success: false,
            errors
        };
    }

    try {
        const authorsRef = ref(db, "autori");
        const newAuthorRef = push(authorsRef);

        const imageUrls = images
            .split("\n")
            .map(image => image.trim())
            .filter(image => image !== "");

        const newAuthor = {
            ime: firstName,
            prezime: lastName,
            biografija: biography,
            slike: imageUrls,
            datumRodjenja: birthDate,
            status: status,
            brojOsvojenihNagrada: Number(awardsCount),
            brojProdatihPrimeraka: Number(soldCopiesCount),
            kontaktTelefonMenadzera: managerPhone
        };

        await set(newAuthorRef, newAuthor);

        return {
            success: true,
            author: {
                id: newAuthorRef.key,
                ...newAuthor
            }
        };

    }
    catch (err) {
        console.log(err);
        return {
            success: false,
            errors: {
                general: "Дошло је до грешке при додавању аутора."
            }
        };
    }
}

export async function editAuthor(id, data) {
    const errors = {};

    const firstName = data.firstName;
    const lastName = data.lastName;
    const biography = data.biography;
    const images = data.images;
    const birthDate = data.birthDate;
    const status = data.status;
    const awardsCount = data.awardsCount;
    const soldCopiesCount = data.soldCopiesCount;
    const managerPhone = data.managerPhone;

    const firstNameError = nameValidation(firstName, "Име");
    if (firstNameError) errors.firstName = firstNameError;

    const lastNameError = nameValidation(lastName, "Презиме");
    if (lastNameError) errors.lastName = lastNameError;

    const biographyError = biographyValidation(biography);
    if (biographyError) errors.biography = biographyError;

    const imagesError = imagesValidation(images);
    if (imagesError) errors.images = imagesError;

    const birthDateError = birthDateValidation(birthDate);
    if (birthDateError) errors.birthDate = birthDateError;

    const statusError = statusValidation(status);
    if (statusError) errors.status = statusError;

    const awardsCountError = awardsCountValidation(awardsCount);
    if (awardsCountError) errors.awardsCount = awardsCountError;

    const soldCopiesCountError = soldCopiesCountValidation(soldCopiesCount);
    if (soldCopiesCountError) errors.soldCopiesCount = soldCopiesCountError;

    const managerPhoneError = managerPhoneValidation(managerPhone);
    if (managerPhoneError) errors.managerPhone = managerPhoneError;

    if (!id) {
        errors.general = "ID аутора није пронађен.";
    }

    if (Object.keys(errors).length > 0) {
        return {
            success: false,
            errors
        };
    }

    try {
        const authorRef = ref(db, `autori/${id}`);
        const authorSnapshot = await get(authorRef);

        if (!authorSnapshot.exists()) {
            return {
                success: false,
                errors: {
                    general: "Аутор није пронађен."
                }
            };
        }

        const imageUrls = images
            .split("\n")
            .map(image => image.trim())
            .filter(image => image !== "");

        const updatedAuthor = {
            ime: firstName,
            prezime: lastName,
            biografija: biography,
            slike: imageUrls,
            datumRodjenja: birthDate,
            status: status,
            brojOsvojenihNagrada: Number(awardsCount),
            brojProdatihPrimeraka: Number(soldCopiesCount),
            kontaktTelefonMenadzera: managerPhone
        };

        await update(authorRef, updatedAuthor);

        return {
            success: true,
            author: {
                id: id,
                ...updatedAuthor
            }
        };

    }
    catch (err) {
        console.log(err);

        return {
            success: false,
            errors: {
                general: "Дошло је до грешке при измени аутора."
            }
        };
    }
}