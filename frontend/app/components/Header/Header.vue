<template>
  <header class="app-header navbar">
    <button
      class="navbar-toggler mobile-sidebar-toggler d-lg-none"
      type="button"
      @click="mobileSidebarToggle"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <b-link class="navbar-brand" to="#"></b-link>
    <button
      class="navbar-toggler sidebar-toggler d-md-down-none"
      type="button"
      @click="sidebarToggle"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <b-navbar-nav class="d-md-down-none">
      <b-nav-item class="px-3" to="/" nuxt>Status</b-nav-item>
      <b-nav-item class="px-3" to="/guild" nuxt>Guild</b-nav-item>
      <b-nav-item class="px-3" to="/" nuxt>Ranking</b-nav-item>
    </b-navbar-nav>

    <b-navbar-nav class="ml-auto">
      <b-button @click="userInfo">userinfo</b-button>
      <HeaderDropdown />
    </b-navbar-nav>
  </header>
</template>

<script>
import firebase from 'firebase';
import HeaderDropdown from './HeaderDropdown.vue';

export default {
  name: 'CHeader',
  components: {
    HeaderDropdown,
  },

  methods: {
    sidebarToggle(e) {
      e.preventDefault();
      document.body.classList.toggle('sidebar-hidden');
    },
    mobileSidebarToggle(e) {
      e.preventDefault();
      document.body.classList.toggle('sidebar-mobile-show');
    },
    userInfo() {
      console.log(firebase.auth().currentUser);
      console.log(localStorage.getItem('accessToken'));
      console.log(localStorage.getItem('refreshToken'));
    },
  },
};
</script>
