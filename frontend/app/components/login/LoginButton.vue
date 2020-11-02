<template>
  <div @click="logIn">
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
    logIn() {
      firebase
        .auth()
        .signInWithPopup(this.provider.provider)
        .then((result) => {
          const user = result.user;
          // console.log('success : ' + user.uid + ' : ' + user.displayName);
          user.getIdToken().then((idToken) => {
            const params = { token: idToken };
            this.$axios
              .get('http://localhost:10000/api/auth', { params })
              .then((res) => {
                const accessToken = res.data.access_token;
                const refreshToken = res.data.refresh_token;
                localStorage.setItem('accessToken', accessToken);
                localStorage.setItem('refreshToken', refreshToken);
              })
              .catch(() => {
                alert('error');
              });
          });
        })
        .catch(() => {
          alert('login error');
        });
    },
  },
};
</script>
