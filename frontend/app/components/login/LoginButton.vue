<template>
  <div @click="signIn">
    <b-card :no-body="true">
      <b-card-body class="p-0 clearfix">
        <i
          :class="`fa fa-${provider.name} bg-${provider.color} p-3 font-2xl mr-3 float-left `"
        ></i>
        <div :class="`h5 text-${provider.color} mb-0 pt-3`">
          {{ provider.name }}でログイン
        </div>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
import firebase from 'firebase';

export default {
  props: {
    provider: {
      type: Object,
      required: true,
    },
  },
  methods: {
    async signIn() {
      const provider = new firebase.auth.GoogleAuthProvider();
      const result = await firebase.auth().signInWithRedirect(provider);
      alert(result);
    },
  },
};
</script>
