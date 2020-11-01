<template>
  <div>
    <b-jumbotron :header="questName" lead="questの説明">
      <TaskList />
    </b-jumbotron>
  </div>
</template>

<script>
import TaskList from '~/components/quest/TaskList';

export default {
  component: {
    TaskList,
  },
  asyncData({ params }) {
    return {
      questName: params.quest,
    };
  },
};
</script>
