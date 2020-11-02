<template>
  <b-card no-body style="max-width: 20rem">
    <b-card-body>
      <b-card-title>quest title</b-card-title>
      <b-card-text> discription </b-card-text>
      <div>
        <b-form-rating
          id="rating-readonly"
          class="p-0"
          value="3.6536"
          readonly
          no-border
          inline
          size="sm"
        ></b-form-rating>
        <p class="d-inline mb-1 text-muted">100</p>
      </div>
      <b-button
        type="button"
        variant="primary"
        size="sm"
        :to="{ name: 'guild-id', params: { id: '00' } }"
        nuxt
        >show more</b-button
      >
    </b-card-body>
  </b-card>
</template>

<script>
export default {
  props: { guild: { type: Object, required: true } },
};
</script>
