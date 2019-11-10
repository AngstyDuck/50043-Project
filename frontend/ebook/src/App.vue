<template>
  <div @scroll="scrolledToBottom" class="scrollDiv">
    <v-app id="inspire">
      <v-navigation-drawer disable-resize-watcher v-model="drawer" app clipped>
        <v-list dense>
          <v-list-item @click>
            <v-list-item-action>
              <v-icon>mdi-view-dashboard</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Dashboard</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item @click>
            <v-list-item-action>
              <v-icon>mdi-settings</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Settings</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-app-bar app clipped-left>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>Application</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-text-field
          class="ma-2"
          outlined
          label="Search"
          prepend-inner-icon="search"
          background-color="black"
        ></v-text-field>
      </v-app-bar>

      <v-content>
        <router-view></router-view>
      </v-content>

      <v-footer app>
        <span>&copy; 2019</span>
      </v-footer>
    </v-app>
  </div>
</template>

<script>
export default {
  props: {
    source: String
  },

  data: () => ({
    drawer: false
  }),

  created() {
    this.$vuetify.theme.dark = true;
  },
  methods: {
    scrolledToBottom(event) {
      var el = event.srcElement;
      console.log(el.scrollTop + " " + el.scrollHeight + " " + el.clientHeight);
      if (!this.reachedBottom) {
        if (el.scrollTop >= el.scrollHeight - el.clientHeight - 10) {
          console.log("hah");
        }
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
</style>