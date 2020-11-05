<template>
  <div class="card">
    <h3 class="card-header">
      <b-container v-if="!isNameTyping" fluid class="text-left text-bold">
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
          id="quest-name"
          v-model="tmpName"
          class="quest-name"
          placeholder="クエスト名を入力"
          @blur="updateQuestName"
          @keydown.enter="updateQuestName"
        />
      </div>
    </h3>
    <div class="card-body">
      <h5 class="card-title">{{ quest.description }}</h5>
      <TaskList :tasks="tasks" />
    </div>
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
          this.$store.commit('quest/setName', { id: res.id, name: res.name });
        })
        .catch((err) => console.log(err));
    },
    deleteQuest() {
      const questId = parseInt(this.$route.params.quest);
      this.$api
        .$delete(`/api/quests/${questId}`)
        .then(() => {
          this.$store.commit('quest/deleteQuest', questId);
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
