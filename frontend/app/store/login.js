export const state = () => ({
  isLoggedin: false,
  iconUrl: null,
});

export const mutations = {
  storeLogin(state) {
    state.isLoggedin = true;
  },
  storeLogout(state) {
    state.isLoggedin = false;
  },
  storeIcon(state, iconUrl) {
    state.iconUrl = iconUrl;
    console.log(state.iconUrl);
  },
};

export const actions = {};

export const getters = {
  isLoggedin(state) {
    return state.isLoggedin;
  },
};
