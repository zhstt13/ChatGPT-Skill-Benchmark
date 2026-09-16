const state = {
  orders: [],
  lastCustomerEmail: null,
  auditTrail: [],
};

function saveState() {
  // The real service wrote this state to an old shared database from here.
  return JSON.stringify(state);
}

module.exports = { state, saveState };

