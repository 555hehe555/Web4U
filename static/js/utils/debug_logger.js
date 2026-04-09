import formatDate from "./index.js"
const originalConsole = {
    log: console.log,
    warn: console.warn,
    error: console.error,
    info: console.info,
    debug: console.debug,
};

export function debugMode() {
    return true; // потім треба буде дістати це з .env
}


export function log(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - LOG: \n${message}`;
    if (debugMode())  { originalConsole.log(formattedMessage, ...args); }
}

export function error(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - ERROR: \n${message}`;
    if (debugMode()) { originalConsole.error(formattedMessage, ...args); }
}

export function warn(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - WARNING: \n${message}`;
    if (debugMode()) { originalConsole.warn(formattedMessage, ...args); }
}

export function info(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - INFO: \n${message}`;
    if (debugMode()) { originalConsole.info(formattedMessage, ...args); }
}

export function debug(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - DEBUG: \n${message}`;
    if (debugMode()) { originalConsole.debug(formattedMessage, ...args); }
}

export function TheAlert(file, line, message, ...args) {
    const timestamp = new Date().toISOString();
    const formattedMessage = `[${timestamp}] ${file}:${line} - ALERT: \n${message}`;
    if (debugMode()) { alert(formattedMessage); }
}