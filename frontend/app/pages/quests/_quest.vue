<template>
  <div>
    <b-jumbotron :header="quest.name" :lead="quest.description">
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
        name: '',
        description: '',
      },
      tasks: [],
    };
  },
  mounted() {
    this.$api
      .$get(`/api/quests/${this.$route.params.quest}`)
      .then((res) => {
        const quest = res.quest;
        this.quest = quest;
        this.tasks = quest.tasks;
      })
      .catch((err) => console.log(err));
  },
};
</script>
