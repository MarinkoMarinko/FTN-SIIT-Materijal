import { ref, get, push, set, query, orderByChild, equalTo } 
from "https://www.gstatic.com/firebasejs/12.2.1/firebase-database.js";
import { db } from "./firebase.js"

import {
    usernameValidation,
    passwordValidation,
    nameValidation,
    emailValidation,
    birthdateValidation,
    addressValidation,
    occupationValidation
} from "../utils/user_validation.js";

export async function login(data) {
    let errors = {}
    
    const usernameError = usernameValidation(data.username);
    if (usernameError) errors.username = usernameError;

    const passwordError = passwordValidation(data.password);
    if (passwordError) errors.password = passwordError;

    if (Object.keys(errors).length > 0) {
        return {
            success: false,
            errors
        };
    }

    try {
        const usersRef = ref(db, "korisnici");
        const usernameQuery = query(
            usersRef,
            orderByChild("korisnickoIme"),
            equalTo(data.username)
        );
        const snapshot = await get(usernameQuery);
        if (!snapshot.exists()) {
            return {
                success: false,
                errors: {
                    general: "Погрешни креденцијали."
                } 
            };
        }
        const result = snapshot.val();
        const loggedUserID = Object.keys(result)[0];
        const loggedUser = result[loggedUserID];
        if (loggedUser.korisnickoIme != data.username || loggedUser.lozinka != data.password) {
            return {
                success: false,
                errors: {
                    general: "Погрешни креденцијали."
                }
            };
        }
        const userSession = {
            id: loggedUserID,
            username: loggedUser.korisnickoIme
        }
        sessionStorage.setItem("loggedUser", JSON.stringify(userSession));
        return {
            success: true,
            user: userSession
        }
    }
    catch (err) {
        return {
            success: false,
            errors: {
                general: "Грешка приликом пријаве.",
            }
        };
    }
}

export async function register(data) {
    const errors = {};

    const username = data.username;
    const password = data.password;
    const firstName = data.firstName;
    const lastName = data.lastName;
    const email = data.email;
    const birthDate = data.birthDate;
    const address = data.address;
    const occupation = data.occupation;

    const usernameError = usernameValidation(username);
    if (usernameError) errors.username = usernameError;

    const passwordError = passwordValidation(password);
    if (passwordError) errors.password = passwordError;

    const firstNameError = nameValidation(firstName, "Име");
    if (firstNameError) errors.firstName = firstNameError;

    const lastNameError = nameValidation(lastName, "Презиме");
    if (lastNameError) errors.lastName = lastNameError;

    const emailError = emailValidation(email);
    if (emailError) errors.email = emailError;

    const birthdateError = birthdateValidation(birthDate);
    if (birthdateError) errors.birthDate = birthdateError;

    const addressError = addressValidation(address);
    if (addressError) errors.address = addressError;

    const occupationError = occupationValidation(occupation);
    if (occupationError) errors.occupation = occupationError;

    if (Object.keys(errors).length > 0) {
        return {
            success: false,
            errors
        };
    }
    try {
        const usersRef = ref(db, "korisnici");
        const usernameQuery = query(
            usersRef,
            orderByChild("korisnickoIme"),
            equalTo(username)
        );
        const usernameSnapshot = await get(usernameQuery);
        if (usernameSnapshot.exists()) {
            return {
                success: false,
                errors: {
                    username: "Корисничко име је већ заузето."
                }
            };
        }
        const newUserRef = push(usersRef);      // forms new ID
        await set(newUserRef, {
            id: newUserRef.key,
            korisnickoIme: username,
            lozinka: password,
            ime: firstName,
            prezime: lastName,
            email: email,
            datumRodjenja: birthDate,
            adresa: address,
            zanimanje: occupation
        });
        const userSession = {
            id: newUserRef.key,
            username: username
        };
        sessionStorage.setItem("loggedUser", JSON.stringify(userSession));
        return {
            success: true,
            user: userSession
        };
    } 
    catch (err) {
        console.log(err)
        return {
            success: false,
            errors: {
                general: "Дошло је до грешке при регистрацији."
            }
        };
    }
}