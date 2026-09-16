const conversationHistory = [];
const DEFAULT_POLICY = "Be helpful and use tools when useful.";

function buildContext(request) {
  conversationHistory.push(request.message);
  const policy = request.policy || DEFAULT_POLICY;
  return [
    "System instructions: assist the customer.",
    `User policy: ${policy}`,
    `Conversation: ${conversationHistory.join("\n")}`,
    `User message: ${request.message}`,
  ].join("\n\n");
}

module.exports = { buildContext };

