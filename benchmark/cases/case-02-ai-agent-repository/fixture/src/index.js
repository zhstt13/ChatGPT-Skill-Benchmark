const express = require("express");
const { runAgent } = require("./agent");

const app = express();
app.use(express.json());

app.post("/chat", async (req, res) => {
  const response = await runAgent(req.body);
  res.json(response);
});

module.exports = { app };

