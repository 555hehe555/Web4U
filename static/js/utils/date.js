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

export function getShortTime(time, parts = 2) {
  if (!time) return "";

  const d = new Date(time);

  const timeParts = [
    String(d.getHours()).padStart(2, "0"),
    String(d.getMinutes()).padStart(2, "0"),
    String(d.getSeconds()).padStart(2, "0"),
    String(d.getMilliseconds()).padStart(3, "0"),
  ];

  return timeParts.slice(0, parts).join(":")
}