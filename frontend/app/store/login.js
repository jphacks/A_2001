export const state = () => ({
  isLoggedin: false,
});

export const mutations = {
  storeLogin(state) {
    state.isLoggedin = true;
  },
  storeLogout(state) {
    state.isLoggedin = false;
  },
};

export const actions = {};

export const getters = {
  isLoggedin(state) {
    return state.isLoggedin;
  },
};
