import Vue from "vue";
import Router from "vue-router";
import BookList from "./views/BookList.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Book List",
      component: BookList
    }
  ]
});
