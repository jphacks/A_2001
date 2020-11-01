<template>
  <b-container>
    <b-row>
      <template v-for="(guild, key) in guilds">
        <b-col :key="key" sm="6" lg="3">
          <div class="social-box">
            <p>hoge</p>
            <ul>
              <li>
                <strong>{{ guild.downloads }}</strong>
                <span>downloads</span>
              </li>
              <li>
                <strong>{{ guild.tasks }}</strong>
                <span>tasks</span>
              </li>
            </ul>
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
