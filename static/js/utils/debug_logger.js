function debugMode() {
    return true; // потім треба буде дістати це з .env
}


export function log(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - LOG: ${message}`;
    if (debugMode())  { console.log(formattedMessage, ...args); }
}

export function error(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - ERROR: ${message}`;
    if (debugMode()) { console.error(formattedMessage, ...args); }
}

export function warn(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - WARNING: ${message}`;
    if (debugMode()) { console.warn(formattedMessage, ...args); }
}

export function info(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - INFO: ${message}`;
    if (debugMode()) { console.info(formattedMessage, ...args); }
}

export function debug(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - DEBUG: ${message}`;
    if (debugMode()) { console.debug(formattedMessage, ...args); }
}

export function TheAlert(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - ALERT: ${message}`;
    if (debugMode()) { alert(formattedMessage); }
}