import axiosInit from "axios";

const axios = axiosInit.create({
  baseURL: "https://8ae48f56-65d6-4ded-85b8-6519961968ac.mock.pstmn.io",
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
  single_book({ commit }, payload) {
    return axios
      .get("/single_book/" + payload.asin, payload)
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
