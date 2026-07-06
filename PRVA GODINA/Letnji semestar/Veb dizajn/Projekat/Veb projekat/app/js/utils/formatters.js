export function formatDate(date) {
    if (!date) return "Непознато";
    const [year, month, day] = date.split("-");
    return `${day}.${month}.${year}.`;
}

export function formatNumber(number) {
    if (!number) return "0";
    return Number(number).toLocaleString("sr-RS");
}