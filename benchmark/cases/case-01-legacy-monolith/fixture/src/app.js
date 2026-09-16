const http = require("node:http");
const orders = require("./orders");

function getRuntimeConfig() {
  return { receiptFrom: "orders@example.test" };
}

const server = http.createServer(async (request, response) => {
  if (request.method === "POST" && request.url === "/orders") {
    let body = "";
    request.on("data", (chunk) => { body += chunk; });
    request.on("end", async () => {
      const result = await orders.createOrder(JSON.parse(body || "{}"));
      response.writeHead(result.status, { "content-type": "text/html" });
      response.end(result.body);
    });
    return;
  }

  response.writeHead(404);
  response.end("not found");
});

module.exports = { getRuntimeConfig, server };

