<template>
  <div>
    <b-jumbotron :header="quest.content" :lead="quest.description">
      <TaskList :tasks="tasks" />
    </b-jumbotron>
  </div>
</template>

<script>
import TaskList from '~/components/quest/TaskList';

export default {
  component: {
    TaskList,
  },
  data() {
    return {
      quest: {
        content: '',
        description: '',
      },
      tasks: [],
    };
  },
  fetchOnServer: false,
  mounted() {
    const promises = [];
    promises.push(
      this.$api
        .$get(`/api/quests/${this.$route.params.quest}`)
        .then((res) => {
          this.quest = res.quest;
        })
        .catch((err) => console.log(err))
    );
    promises.push(
      this.$api
        .$get(`/api/quests/${this.$route.params.quest}/tasks`)
        .then((res) => {
          this.tasks = res.tasks;
        })
        .catch((err) => console.log(err))
    );
    Promise.all(promises);
  },
};
</script>
