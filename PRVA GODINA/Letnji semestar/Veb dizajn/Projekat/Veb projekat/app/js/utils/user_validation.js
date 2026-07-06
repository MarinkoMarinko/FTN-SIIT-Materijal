export function usernameValidation(username) {
    if(!username) {
        return "Корисничко име је обавезно."
    }
    if(username.length < 3) {
        return "Корисничко име мора садржати најмање 3 карактера."
    }
    return ""
}

export function passwordValidation(password) {
    if(!password) {
        return "Лозинка је обавезна."
    }
    if(password.length < 5) {
        return "Лозинка мора садржати најмање 5 карактера."
    }
    return ""
}

export function nameValidation(name, nameType) {
    if (!name) {
        return `${nameType} је обавезно.`;
    }
    if (name.length < 2) {
        return `${nameType} мора садржати најмање 2 карактера.`;
    }
    return "";
}

export function emailValidation(email) {
    if (!email) {
        return "Email је обавезан.";
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        return "Email није у исправном формату.";
    }
    return "";
}

export function birthdateValidation(birthDate) {
    if (!birthDate) {
        return "Датум рођења је обавезан.";
    }
    return "";
}

export function addressValidation(address) {
    if (!address) {
        return "Адреса је обавезна.";
    }
    if (address.length < 6) {
        return "Адреса мора садржати најмање 6 карактера.";
    }
    return "";
}

export function occupationValidation(occupation) {
    if (!occupation) {
        return "Занимање је обавезно.";
    }
    if (occupation.length < 4) {
        return "Занимање мора садржати најмање 4 карактера.";
    }
    return "";
}