import axiosInit from "axios";

const axios = axiosInit.create({
  baseURL: "https://4dc66a06-d5b9-4b9a-b3fb-97020929e416.mock.pstmn.io",
  headers: {
    "Content-Type": "application/json"
  }
});

const state = {
  // id_user_hash: ""
};

const actions = {
  book_list({ commit }, payload) {
    return axios
      .get("/book_list", payload)
      .then(response => {
        console.log(response);
        if (response.status === 200) {
          return response.data;
        } else {
          return 0;
        }
      })
      .catch(() => {
        return 0;
      });
  }
};

const mutations = {};

const getters = {
  // getUser: state => {
  //   return state.id_user_hash;
  // }
};

export const store = {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
