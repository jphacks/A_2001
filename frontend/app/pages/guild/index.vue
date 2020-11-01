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
          <GuildCard :guild="guild" />
        </b-col>
      </template>
    </b-row>
  </b-container>
</template>

<script>
import GuildCard from '~/components/guild/GuildCard';
export default {
  component: {
    GuildCard,
  },
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
