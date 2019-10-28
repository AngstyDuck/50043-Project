import axiosInit from "axios";

const axios = axiosInit.create({
  baseURL: "https://306a7002-ca11-49c0-87a9-ab04c51ea4ba.mock.pstmn.io",
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
