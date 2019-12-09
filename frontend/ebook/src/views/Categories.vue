<template>
  <div>
    <div class="loading-top" v-if="loadingCategories">
      <v-progress-circular :size="90" :width="7" color="primary" indeterminate></v-progress-circular>
      <div>Loading categories...</div>
    </div>
    <div v-else>
      <div class="top-row">
        <v-container>
          <v-row>
            <v-col class="section-title">Categories</v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-text-field
                v-model="categorysearch"
                filled
                label="Search Categories"
                prepend-inner-icon="search"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <v-container>
        <v-row>
          <v-col v-for="category in filteredCategory" v-bind:key="category">
            <button
              type="button"
              class="btn"
              @click="filterClick(category)"
              rounded
            >{{ category }}</button>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>
<style scoped>
.loading-top {
  position: absolute;
  left: 40%;
  text-align: center;
  padding-top: 20%;
  font-size: 2rem;
}
.section-title {
  font-size: 2rem;
  font-weight: 400;
}
.top-row {
  background-color: rgb(62, 62, 62);
  width: 100%;
  padding: 0;
}
.btn {
  border: none;
  background-color: rgb(70, 70, 70);
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  display: inline-block;
  box-shadow: 3px 3px 5px rgb(30, 30, 30);
  border-radius: 6px;
}
/* On mouse-over */
.btn:hover {
  background: rgb(110, 110, 110);
}
</style>

<script>
export default {
  data: () => ({
    categories: [],
    categorysearch: "",
    loadingCategories: true
  }),
  computed: {
    filteredCategory() {
      return this.categories.filter(category => {
        return category
          .toLowerCase()
          .includes(this.categorysearch.toLowerCase());
      });
    }
  },
  methods: {
    getFilterList() {
      this.$store.dispatch("store/categories", {}).then(response => {
        if (response != 0) {
          this.categories = response.categories;
          this.loadingCategories = false;
          console.log(this.categories);
        } else {
          console.log("Error retrieving categories");
          console.log(this.categories);
        }
      });
    },
    filterClick(category) {
      if (this.$router.currentRoute.path != "/filter" + category) {
        this.$router.push({ path: "/filter/" + category });
      } else {
        location.reload();
      }
    }
  },
  mounted() {
    this.getFilterList();
  }
};
</script>