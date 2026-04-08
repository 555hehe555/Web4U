export function formatDate(dateString) {
  const d = new Date(dateString);

  return d.toLocaleString("uk-UA", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit"
  });
}

export function getShortDate(date) {
  return date ? String(date).split("T")[0] : "";
}
