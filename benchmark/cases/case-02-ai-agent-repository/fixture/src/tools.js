async function sendEmail(args) {
  return { sent: true, to: args.to, body: args.body };
}

async function archiveAccount(args) {
  return { archived: true, accountId: args.accountId };
}

async function issueRefund(args) {
  return { refunded: true, orderId: args.orderId, amount: args.amount };
}

const connectors = { sendEmail, archiveAccount, issueRefund };

function callTool(name, argumentsForTool) {
  return connectors[name](argumentsForTool);
}

module.exports = { callTool };

