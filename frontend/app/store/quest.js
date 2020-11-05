export const state = () => ({
  quests: [],
});

export const mutations = {
  incrementUndoneCnt(state, id) {
    const quest = state.quests.find((e) => e.id === id);
    quest.undone++;
  },
  decrementUndoneCnt(state, id) {
    const quest = state.quests.find((e) => e.id === id);
    quest.undone--;
  },
  setName(state, { id, name }) {
    const quest = state.quests.find((e) => e.id === id);
    quest.name = name;
  },
  setQuests(state, quests) {
    state.quests = quests;
  },
  addQuest(state, quest) {
    state.quests = [...state.quests, quest];
  },
  deleteQuest(state, id) {
    const index = state.quests.findIndex((e) => e.id === id);
    state.quests.splice(index, 1);
  },
};

export const actions = {};

export const getters = {
  quests(state) {
    return state.quests;
  },
};
