async function sendReceiptEmail(from, to, order) {
  return { from, to, subject: `Receipt for ${order.id}` };
}

module.exports = { sendReceiptEmail };

