<template>
  <b-nav-item-dropdown right no-caret>
    <template slot="button-content">
      <img src="~static/img/avatars/6.jpg" class="img-avatar" />
    </template>

    <b-dropdown-item v-if="$store.state.login.isLoggedin" @click="logout"
      ><i class="fa fa-lock"></i> Logout</b-dropdown-item
    >
    <b-dropdown-item v-else @click="login">
      <i class="fa fa-unlock"></i> Login
    </b-dropdown-item>
  </b-nav-item-dropdown>
</template>

<script>
import firebase from 'firebase';

export default {
  name: 'HeaderDropdown',
  data: () => {},

  methods: {
    logout() {
      localStorage.setItem('refreshToken', null);
      localStorage.setItem('accessToken', null);
      this.$store.commit('login/storeLogout');
      alert('logged out');
    },
    login() {
      this.$router.push('/login');
    },
  },
};
</script>
