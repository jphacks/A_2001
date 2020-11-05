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
    this.$store.commit('quest/setQuests', res.quests);
  },
  fetchOnServer: false,
  computed: {
    navItems() {
      return [
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
        ...this.$store.state.quest.quests.map((e) => this.quests2item(e)),
        { button: true },
      ];
    },
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
          this.$store.commit('quest/addQuest', { ...res, undone: 0 });
        })
        .catch((err) => console.log(err));
    },
    quests2item(quests) {
      return {
        id: quests.id,
        name: quests.name,
        url: '/quests/' + quests.id,
        badge: {
          variant: 'primary',
          text: quests.undone,
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
