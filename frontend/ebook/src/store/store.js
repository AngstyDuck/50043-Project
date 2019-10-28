import axiosInit from "axios";

const axios = axiosInit.create({
  baseURL: "https://97b3c554-e623-4b57-be3b-2e13f9929d3e.mock.pstmn.io",
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
  },
  review_list({ commit }, payload) {
    return axios
      .get("/review_list/" + payload.asin, payload)
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
  },
  helpful_review({ commit }, payload) {
    return axios
      .put("/helpful_review", payload)
      .then(response => {
        console.log(response);
        if (response.status === 200) {
          return 1;
        } else {
          return 0;
        }
      })
      .catch(() => {
        return 0;
      });
  },
  post_new_review({ commit }, payload) {
    return axios
      .post("/post_new_review", payload)
      .then(response => {
        console.log(response);
        if (response.status === 200) {
          return 1;
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
