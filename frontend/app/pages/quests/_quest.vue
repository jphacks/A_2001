<template>
  <div class="card">
    <div class="card-header">
      <h3>
        <div id="quest-name-wrapper" class="m-3 d-flex align-items-center">
          <input
            id="quest-name"
            class="w-100 text-bold"
            v-model="quest.name"
            placeholder="クエスト名を入力"
            autocomplete="off"
            @blur="updateQuestName"
            @keydown.enter="updateQuestName"
          />
          <i
            class="ml-auto mr-5 fa fa-sm fa-trash-o icon-button text-danger"
            v-b-modal.modal-quest-delete
          />
          <b-modal id="modal-quest-delete" @ok="deleteQuest">
            <p>クエストを削除しますか？</p>
          </b-modal>
        </div>
      </h3>

      <div class="d-flex align-items-cente ml-3">
        <p class="d-inline-block mb-1">{{ doneCnt }}個実行済み</p>
        <b-button
          v-if="!displayDoneTask"
          variant="link"
          size="sm"
          @click="displayDoneTask = !displayDoneTask"
          >表示</b-button
        >
        <b-button
          v-else
          variant="link"
          size="sm"
          @click="displayDoneTask = !displayDoneTask"
          >非表示</b-button
        >
      </div>
    </div>

    <div class="card-body">
      <div class="card border-primary mb-3">
        <div class="card-header bg-info font-weight-bold">
          <i class="fa fa-lg fa-thumb-tack" />実行中
          <b-spinner
            v-if="isDoing"
            small
            variant="light"
            type="grow"
          ></b-spinner>
        </div>
        <template v-if="isDoing">
          <template v-for="task in tasks">
            <DoingTask
              v-if="task.start !== null"
              :key="task.id"
              :task="task"
              class="mb-5"
            />
          </template>
        </template>
        <h4 v-else class="text-muted text-center my-2">
          現在実行中のタスクはありません。ピン留め<i
            class="fa fa-lg fa-thumb-tack text-dark"
          />をしてタスクを実行しましょう
        </h4>
      </div>
      <div class="card my-5">
        <div class="card-header">未実行</div>
        <div class="card-body">
          <TaskList :tasks="tasks" />
        </div>
      </div>

      <div v-if="displayDoneTask" class="card my-5">
        <div class="card-header">実行済</div>
        <div class="card-body">
          <TaskList :tasks="tasks" :display-done-task="displayDoneTask" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TaskList from '~/components/quest/TaskList';
import DoingTask from '~/components/quest/DoingTask';

export default {
  component: {
    TaskList,
    DoingTask,
  },
  data() {
    return {
      quest: {
        name: '',
        description: '',
      },
      tasks: [],
      displayDoneTask: false,
    };
  },
  computed: {
    isDoing() {
      for (const task of Object.values(this.tasks)) {
        if (task.start) {
          return true;
        }
      }
      return false;
    },
    doneCnt() {
      let cnt = 0;
      for (const task of this.tasks) {
        if (task.done) {
          cnt++;
        }
      }
      return cnt;
    },
  },
  mounted() {
    this.$api
      .$get(`/api/quests/${this.$route.params.quest}`)
      .then((res) => {
        const quest = res.quest;
        this.quest = quest;
        this.tasks = quest.tasks;
        // 実行中のタスクがある場合はisDoingをtrueにする
      })
      .catch((err) => console.log(err));
  },
  methods: {
    updateQuestName(e) {
      if (e.keyCode && e.keyCode !== 13) return; // 日本語入力確定を除外
      if (this.quest.name.length === 0) this.quest.name = 'Untitled';
      this.$api
        .$patch(`/api/quests/${this.$route.params.quest}`, {
          name: this.quest.name,
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

<style scoped>
.icon-button::before {
  cursor: pointer;
}

#quest-name-wrapper {
  outline: none;
}

#quest-name {
  background-color: #ddd0;
  border: none;
  outline: none;
}
</style>
