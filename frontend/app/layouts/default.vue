<template>
  <div class="app">
    <AppHeader />
    <div class="app-body">
      <Sidebar />
      <main class="main">
        <div class="container-fluid mt-4 px-md-3 px-0">
          <nuxt />
        </div>
      </main>
    </div>
    <AppFooter />
  </div>
</template>

<script>
import {
  Header as AppHeader,
  Sidebar,
  Footer as AppFooter,
} from '~/components/';

export default {
  name: 'Full',
  components: {
    AppHeader,
    Sidebar,
    AppFooter,
  },
  data() {
    return {
      // nav: nav.items,
    };
  },
  computed: {
    name() {
      return this.$route.name;
    },
    list() {
      return this.$route.matched;
    },
  },
};
</script>
