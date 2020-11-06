<template>
  <div @click="login">
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
import firebase from 'firebase/app';
import 'firebase/auth';
export default {
  props: {
    provider: {
      type: Object,
      required: true,
    },
  },
  methods: {
    login() {
      const p = new this.provider.Provider();
      firebase
        .auth()
        .signInWithPopup(p)
        .then((result) => {
          const user = result.user;
          user.getIdToken().then((idToken) => {
            const params = { token: idToken };
            this.$axios
              .get('/api/auth', { params })
              .then((res) => {
                const accessToken = res.data.access_token;
                const refreshToken = res.data.refresh_token;
                localStorage.setItem('accessToken', accessToken);
                localStorage.setItem('refreshToken', refreshToken);
                this.$store.commit('login/storeLogin');
                this.$store.commit(
                  'login/storeIcon',
                  firebase.auth().currentUser.photoURL
                );
                // access tokenとrefresh tokenだけ保持していればいいのでfirebaseからはすぐログアウト
                firebase
                  .auth()
                  .signOut()
                  .then(() => {
                    this.$router.replace('/status');
                  });
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
