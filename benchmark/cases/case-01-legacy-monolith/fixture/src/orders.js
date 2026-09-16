const { state, saveState } = require("./store");
const { appendAudit } = require("./audit");
const { sendReceiptEmail } = require("./mailer");
const { getRuntimeConfig } = require("./app");

async function createOrder(input) {
  if (!input.customerEmail || !Array.isArray(input.items) || input.items.length === 0) {
    return { status: 400, body: "missing customerEmail or items" };
  }

  const order = {
    id: `order-${state.orders.length + 1}`,
    email: input.customerEmail,
    total: input.items.reduce((sum, item) => sum + item.price, 0),
    items: input.items,
  };

  state.orders.push(order);
  state.lastCustomerEmail = input.customerEmail;
  appendAudit(`created ${order.id}`);
  await sendReceiptEmail(getRuntimeConfig().receiptFrom, order.email, order);
  saveState();

  return { status: 201, body: renderOrderHtml(order) };
}

function renderOrderHtml(order) {
  return `<h1>Order ${order.id}</h1><p>Total: ${order.total}</p>`;
}

module.exports = { createOrder, renderOrderHtml };

