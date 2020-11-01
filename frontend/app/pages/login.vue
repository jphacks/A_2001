<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="8">
          <b-card-group>
            <b-card no-body class="p-4">
              <b-card-body>
                <h1>Login</h1>
                <p class="text-muted">Sign In to your account</p>
                <template v-for="(provider, key) in providers">
                  <login-button :key="key" :provider="provider" />
                </template>
              </b-card-body>
            </b-card>
          </b-card-group>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
import LoginButton from '~/components/login/LoginButton';
export default {
  components: {
    LoginButton,
  },
  data: () => {
    return {
      providers: [
        { name: 'twitter', color: 'info' },
        { name: 'google', color: 'danger' },
      ],
    };
  },
};
</script>
