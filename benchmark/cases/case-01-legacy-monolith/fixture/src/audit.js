const { state } = require("./store");

function appendAudit(message) {
  state.auditTrail.push({ message, at: new Date().toISOString() });
}

module.exports = { appendAudit };

