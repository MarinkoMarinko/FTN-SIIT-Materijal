export function nameValidation(name, nameType) {
    if (!name) {
        return `${nameType} је обавезно.`;
    }
    if (name.length < 2) {
        return `${nameType} мора садржати најмање 2 карактера.`;
    }
    return "";
}

export function biographyValidation(biography) {
    if (!biography) {
        return "Биографија је обавезна.";
    }
    if (biography.length < 20) {
        return "Биографија мора садржати најмање 20 карактера.";
    }
    return "";
}

export function imagesValidation(images) {
    if (!images) {
        return "Потребно је унети бар једну слику.";
    }

    const imageUrls = images
        .split("\n")
        .map(url => url.trim())
        .filter(url => url !== "");
    if (imageUrls.length === 0) {
        return "Потребно је унети бар једну слику.";
    }

    const urlRegex = /^(https?:\/\/)[^\s$.?#].[^\s]*$/;
    for (const url of imageUrls) {
        if (!urlRegex.test(url)) {
            return "Свака слика мора бити исправан URL.";
        }
    }
    return "";
}

export function birthDateValidation(birthDate) {
    if (!birthDate) {
        return "Датум рођења је обавезан.";
    }
    return "";
}

export function statusValidation(status) {
    if (!status) {
        return "Статус је обавезан.";
    }
    const allowedStatuses = ["Активан", "У пензији", "Преминуо"];
    if (!allowedStatuses.includes(status)) {
        return "Статус је обавезан.";
    }

    return "";
}

export function awardsCountValidation(awardsCount) {
    if (awardsCount === "") {
        return "Број освојених награда је обавезан.";
    }

    if (Number(awardsCount) < 0) {
        return "Број освојених награда не може бити негативан.";
    }

    return "";
}

export function soldCopiesCountValidation(soldCopiesCount) {
    if (soldCopiesCount == "") {
        return "Број продатих примерака је обавезан.";
    }
    if (Number(soldCopiesCount) < 0) {
        return "Број продатих примерака не може бити негативан.";
    }
    return "";
}

export function managerPhoneValidation(managerPhone) {
    if (!managerPhone) {
        return "Контакт телефон менаџера је обавезан.";
    }
    const phoneRegex = /^\+381\s\d{2}\s\d{3}-\d{3,4}$/;
    if (!phoneRegex.test(managerPhone)) {
        return "Телефон мора бити у формату +381 XX XXX-XXX(X).";
    }
    return "";
}