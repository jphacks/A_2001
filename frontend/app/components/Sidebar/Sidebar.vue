<template>
  <div class="sidebar">
    <nav class="sidebar-nav">
      <ul class="nav">
        <template v-for="item in navItems">
          <template v-if="item.title">
            <SidebarNavTitle
              :key="item.key"
              :name="item.name"
              :classes="item.class"
              :wrapper="item.wrapper"
            />
          </template>
          <template v-else-if="item.divider">
            <SidebarNavDivider :key="item.key" :classes="item.class" />
          </template>
          <template v-else-if="item.button">
            <SidebarNavItem :key="item.key" :classes="item.class">
              <b-button block variant="primary" @click="addQuest">+</b-button>
            </SidebarNavItem>
          </template>
          <template v-else>
            <SidebarNavItem :key="item.key" :classes="item.class">
              <SidebarNavLink
                :name="item.name"
                :url="item.url"
                :icon="item.icon"
                :badge="item.badge"
                :variant="item.variant"
              />
            </SidebarNavItem>
          </template>
        </template>
      </ul>
    </nav>
  </div>
</template>
<script>
import SidebarNavDivider from './SidebarNavDivider';
import SidebarNavLink from './SidebarNavLink';
import SidebarNavTitle from './SidebarNavTitle';
import SidebarNavItem from './SidebarNavItem';

export default {
  name: 'Sidebar',
  components: {
    SidebarNavDivider,
    SidebarNavLink,
    SidebarNavTitle,
    SidebarNavItem,
  },
  async fetch() {
    const res = await this.$api
      .$get('/api/quests')
      .catch((err) => console.log(err));
    const items = [
      {
        title: true,
        name: 'Quest',
        class: '',
        wrapper: {
          element: '',
          attributes: {},
        },
      },
      { divider: true },
      ...res.quests.map((e) => this.response2item(e)),
      { button: true },
    ];
    this.navItems = items;
  },
  fetchOnServer: false,
  data() {
    return {
      navItems: [],
    };
  },
  methods: {
    addQuest() {
      this.$api
        .$post(`/api/quests`, {
          name: 'Untitled',
          category: '',
          description: '',
        })
        .then((res) => {
          this.navItems.splice(
            this.navItems.length - 1,
            0,
            this.response2item(res)
          );
        })
        .catch((err) => console.log(err));
    },
    response2item(response) {
      return {
        id: response.id,
        name: response.name,
        url: '/quests/' + response.id,
        badge: {
          variant: 'primary',
          text: response.undone,
        },
      };
    },
  },
};
</script>

<style lang="css">
.nav-link {
  cursor: pointer;
}
</style>
