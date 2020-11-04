<template>
  <div>
    <b-jumbotron>
      <template #header>
        <b-container
          fluid
          class="text-left display-3 text-bold"
          v-if="!isNameTyping"
        >
          <b-row>
            <b-col class="mr-auto p-3" @click="toggleQuestName">
              {{ quest.name }}</b-col
            >
            <b-col cols="auto" class="p-3 text-danger">
              <i class="fa fa-sm fa-trash-o" @click="deleteQuest" />
            </b-col>
          </b-row>
        </b-container>
        <div v-else class="quest-name">
          <input
            v-model="tmpName"
            id="quest-name"
            class="quest-name"
            placeholder="クエスト名を入力"
            @blur="updateQuestName"
            @keydown.enter="updateQuestName"
          />
        </div>
      </template>

      <template #lead>
        {{ quest.description }}
      </template>
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
      isNameTyping: false,
      tmpName: '',
    };
  },
  mounted() {
    this.$api
      .$get(`/api/quests/${this.$route.params.quest}`)
      .then((res) => {
        const quest = res.quest;
        this.quest = quest;
        this.tasks = quest.tasks;
        this.tmpName = quest.name;
      })
      .catch((err) => console.log(err));
  },
  methods: {
    toggleQuestName() {
      this.isNameTyping = true;
      this.tmpName = this.quest.name;
      this.$nextTick(() => document.getElementById('quest-name').focus());
    },
    updateQuestName(e) {
      if (e.keyCode && e.keyCode !== 13) return; // 日本語入力確定を除外
      this.isNameTyping = false;
      if (this.tmpName.length === 0) {
        return;
      }

      this.$api
        .$patch(`/api/quests/${this.$route.params.quest}`, {
          name: this.tmpName,
        })
        .then((res) => {
          this.quest = res;
        })
        .catch((err) => console.log(err));
    },
    deleteQuest() {
      this.$api
        .$delete(`/api/quests/${this.$route.params.quest}`)
        .then((res) => {
          this.$router.push('/');
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style>
.quest-name {
  width: 100%;
  border: none;
  border-radius: 0.2em;
  outline: none;
  height: 100%;
}
</style>
