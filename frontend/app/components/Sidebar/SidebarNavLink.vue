<template>
  <div v-if="isExternalLink">
    <a :href="url" :class="classList">
      <i :class="icon"></i> {{ name }}
      <b-badge
        v-if="badge && (badge.text || badge.text === 0)"
        :variant="badge.variant"
        >{{ badge.text }}</b-badge
      >
    </a>
  </div>
  <div v-else>
    <router-link :to="url" :class="classList" class="d-flex align-items-center">
      <i :class="icon"></i>
      <span class="text-truncate" style="width: 100px">{{ name }}</span>
      <b-badge
        v-if="badge && (badge.text || badge.text === 0)"
        class="ml-auto text-center"
        :variant="badge.variant"
        >{{ badge.text }}</b-badge
      >
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'SidebarNavLink',
  props: {
    name: {
      type: String,
      default: '',
    },
    url: {
      type: String,
      default: '',
    },
    icon: {
      type: String,
      default: '',
    },
    badge: {
      type: Object,
      default: () => {},
    },
    variant: {
      type: String,
      default: '',
    },
    classes: {
      type: String,
      default: '',
    },
  },
  computed: {
    classList() {
      return ['nav-link', this.linkVariant, ...this.itemClasses];
    },
    linkVariant() {
      return this.variant ? `nav-link-${this.variant}` : '';
    },
    itemClasses() {
      return this.classes ? this.classes.split(' ') : [];
    },
    isExternalLink() {
      if (this.url.substring(0, 4) === 'http') {
        return true;
      } else {
        return false;
      }
    },
  },
};
</script>
