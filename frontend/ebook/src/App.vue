<template>
  <div @scroll="scrolledToBottom" class="scrollDiv">
    <v-app id="inspire">
      <v-app-bar app clipped-left>
        <!-- <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon> -->
        <v-btn @click="goHome()" text icon color="blue lighten-2">
          <v-icon>home</v-icon>
        </v-btn>
        <v-toolbar-title>eBook Browser</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-btn @click="goCategory()" class="category-btn">
          <v-icon left>category</v-icon>Categories
        </v-btn>
        <v-text-field
          class="mt-6"
          outlined
          label="Search"
          prepend-inner-icon="search"
          background-color="black"
          dense
          v-model="searchWord"
          v-on:keyup.enter="searchEnter"
          v-bind:searchWord="searchWord"
        ></v-text-field>
      </v-app-bar>

      <v-content>
        <router-view></router-view>
      </v-content>
    </v-app>
  </div>
</template>

<script>
import EventBus from "./EventBus";

export default {
  props: {
    source: String
  },

  data: () => ({
    drawer: false,
    searchWord: ""
  }),

  created() {
    this.$vuetify.theme.dark = true;
  },
  methods: {
    scrolledToBottom(event) {
      var el = event.srcElement;
      if (!this.reachedBottom) {
        if (el.scrollTop >= el.scrollHeight - el.clientHeight - 10) {
          EventBus.$emit("GET_BOT_ROW_BOOKS", "");
        }
      }
    },
    searchEnter() {
      if (this.$router.currentRoute.path != "/search" + this.searchWord) {
        this.$router.push({ path: "/search/" + this.searchWord });
      } else {
        location.reload();
      }
    },
    goHome() {
      if (this.$router.currentRoute.path != "/main") {
        this.$router.push({ path: "/main" });
      } else {
        location.reload();
      }
    },
    goCategory() {
            if (this.$router.currentRoute.path != "/categories") {
        this.$router.push({ path: "/categories" });
      } else {
        location.reload();
      }
    }
  }
};
</script>

<style scoped>
.scrollDiv {
  max-height: 100vh;
  overflow: auto;
}
.category-btn {
  margin-right: 30px;
}
</style>