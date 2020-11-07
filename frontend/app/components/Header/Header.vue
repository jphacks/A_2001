<template>
  <header class="app-header navbar">
    <button
      class="navbar-toggler mobile-sidebar-toggler d-lg-none"
      type="button"
      @click="mobileSidebarToggle"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <button
      class="navbar-toggler sidebar-toggler d-md-down-none"
      type="button"
      @click="sidebarToggle"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <b-navbar-nav>
      <b-nav-item class="px-3" to="/status" nuxt>Status</b-nav-item>
      <!-- <b-nav-item class="px-3" to="/guild" nuxt>Guild</b-nav-item>
      <b-nav-item class="px-3" to="/" nuxt>Ranking</b-nav-item> -->
    </b-navbar-nav>

    <b-navbar-nav class="ml-auto">
      <HeaderDropdown v-if="$store.state.login.isLoggedin" class="mr-5" />
      <nuxt-link v-else class="btn btn-primary mr-5" to="/login"
        >login</nuxt-link
      >
    </b-navbar-nav>
  </header>
</template>

<script>
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
  },
};
</script>
