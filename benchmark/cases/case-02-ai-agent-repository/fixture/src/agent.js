const { buildContext } = require("./context");
const { callTool } = require("./tools");

const model = {
  async complete(context) {
    return { text: context, toolName: null, arguments: {} };
  },
};

async function runAgent(request) {
  const context = buildContext(request);
  const firstPass = await model.complete(context);
  if (firstPass.toolName) {
    return callTool(firstPass.toolName, firstPass.arguments);
  }
  return { text: firstPass.text };
}

module.exports = { runAgent };

