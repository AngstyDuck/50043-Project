import Vue from "vue";
import Router from "vue-router";
import Main from "./views/Main.vue";
import Search from "./views/Search.vue";
import Filter from "./views/Filter.vue";

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
      path: "/search/:searchtext",
      name: "Search Results",
      component: Search
    },
    {
      path: "/filter/:filtertext",
      name: "Filter Results",
      component: Filter
    }
  ]
});
