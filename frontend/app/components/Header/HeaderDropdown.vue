<template>
  <b-nav-item-dropdown right no-caret>
    <template slot="button-content">
      <img src="~static/img/avatars/6.jpg" class="img-avatar" />
    </template>

    <b-dropdown-item @click="logOut"
      ><i class="fa fa-lock"></i> Logout</b-dropdown-item
    >
    <b-dropdown-item @click="logIn">
      <i class="fa fa-unlock"></i> Login
    </b-dropdown-item>
  </b-nav-item-dropdown>
</template>

<script>
import firebase from 'firebase';
export default {
  name: 'HeaderDropdown',
  data: () => {
    return {};
  },
  methods: {
    logOut() {
      localStorage.setItem('refreshToken', null);
      localStorage.setItem('accessToken', null);
      alert('logged out');
      this.$router.replace('/');
    },
    logIn() {
      if (
        localStorage.getItem('refreshToken') !== null &&
        localStorage.getItem('accessToken') !== null
      ) {
        this.$router.push('/login');
      }
    },
  },
};
</script>
