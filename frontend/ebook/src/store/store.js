import axiosInit from "axios";

const axios = axiosInit.create({
  baseURL: "https://69f077b0-f0de-4e0e-be4f-9d2756fcd918.mock.pstmn.io",
  headers: {
    "Content-Type": "application/json"
  }
});

const state = {
  // id_user_hash: ""
};

const actions = {
  main_top_row_books({ commit }, payload) {
    console.log("activated")
    return axios
      .get("/main_top_row_books", payload)
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
  main_bot_row_books({ commit }, payload) {
    console.log(payload)
    return axios
      .get("/main_bot_row_books", payload)
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
  },
  search_books({ commit }, payload) {
    console.log(payload)
    return axios
      .get("/search_books", payload)
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
  filter_books({ commit }, payload) {
    console.log(payload)
    return axios
      .get("/filter_books", payload)
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
  categories({ commit }, payload) {
    return axios
      .get("/categories", payload)
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
