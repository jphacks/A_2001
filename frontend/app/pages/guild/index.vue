<template>
  <b-container>
    <b-row>
      <b-col class="mb-3">
        <b-input-group>
          <b-input-group-prepend>
            <b-input-group-text>
              <i class="fa fa-search"></i>
            </b-input-group-text>
          </b-input-group-prepend>
          <input
            id="prependedInput"
            class="form-control"
            size="16"
            type="text"
            placeholder="ギルドを検索"
          />
          <b-input-group-append>
            <b-button variant="primary">Search</b-button>
          </b-input-group-append>
        </b-input-group>
      </b-col>
    </b-row>
    <b-row>
      <template v-for="(guild, key) in guilds">
        <b-col :key="key" col lg="4" md="4" sm="1">
          <div>
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
          </div>
        </b-col>
      </template>
    </b-row>
  </b-container>
</template>

<script>
export default {
  data: () => {
    return {
      guilds: [
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
        { downloads: 100, tasks: 1 },
      ],
    };
  },
};
</script>
