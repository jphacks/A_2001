<template>
  <b-nav-item-dropdown right no-caret>
    <template slot="button-content">
      <img src="~static/img/avatars/6.jpg" class="img-avatar" />
    </template>

    <b-dropdown-item v-if="$store.state.login.isLoggedin" @click="logout"
      ><i class="fa fa-lock"></i> Logout</b-dropdown-item
    >
  </b-nav-item-dropdown>
</template>

<script>
export default {
  name: 'HeaderDropdown',

  methods: {
    logout() {
      localStorage.setItem('refreshToken', null);
      localStorage.setItem('accessToken', null);
      this.$store.commit('login/storeLogout');
      this.$router.replace('/');
    },
  },
};
</script>
