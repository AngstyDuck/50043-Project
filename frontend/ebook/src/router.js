import Vue from "vue";
import Router from "vue-router";
import Main from "./views/Main.vue";
import Search from "./views/Search.vue";
import Filter from "./views/Filter.vue";
import Categories from "./views/Categories.vue"

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
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
    },
    {
      path: "/categories",
      name: "Categories",
      component: Categories
    }
  ]
});
