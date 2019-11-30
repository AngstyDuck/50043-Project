import Vue from "vue";
import Router from "vue-router";
import Main from "./views/Main.vue";
import Search from "./views/Search.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    // {
    //   path: "/",
    //   name: "Book List",
    //   component: BookList
    // },
    { path: "/", redirect: "/main" },
    {
      path: "/main",
      name: "Main Page",
      component: Main
    },
    {
      path: "/search",
      name: "Search Results",
      component: Search
    }
  ]
});
