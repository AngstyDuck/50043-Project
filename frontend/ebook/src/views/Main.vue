<template>
  <div>
    <v-dialog v-model="bookDialog" min-height="900" width="1700">
      <Book :book="selectedBook" />
    </v-dialog>
    <div class="loading-top" v-if="loadingBookList">
      <v-progress-circular :size="90" :width="7" color="primary" indeterminate></v-progress-circular>
      <div>Loading books...</div>
    </div>
    <div v-else>
      <div class="top-row">
        <v-container>
          <v-row>
            <v-expansion-panels>
              <v-expansion-panel>
                <v-expansion-panel-header class="dropheader">Categories</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-row>
                    <v-col v-for="category in categories" v-bind:key="category.category">
                      <v-btn @click="filterClick(category.category)" rounded>{{ category.category }}</v-btn>
                    </v-col>
                  </v-row>
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
          </v-row>
          <v-row>
            <v-col class="section-title">Our Recommendations</v-col>
          </v-row>
          <v-row>
            <v-col
              v-for="book in pagedRecommendedBooks"
              v-bind:key="book.asin"
              cols="12"
              xs="6"
              sm="4"
              md="3"
              lg="2"
            >
              <v-hover v-slot:default="{ hover }">
                <v-card
                  :elevation="hover ? 12 : 2"
                  @click="selectBook(book)"
                  class="mx-auto"
                  max-width="344"
                >
                  <v-img :src="book.imUrl" min-height="130px"></v-img>
                  <!-- <v-card-title>{{ asin }}</v-card-title> -->
                </v-card>
              </v-hover>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col>
              <v-pagination
                v-model="pageRecommended"
                :length="parseInt(recommendedBooks.length/6) +1"
              ></v-pagination>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col class="section-title">Bestselling Books</v-col>
          </v-row>
          <v-row>
            <v-col
              v-for="book in pagedBestBooks"
              v-bind:key="book.asin"
              cols="12"
              xs="6"
              sm="4"
              md="3"
              lg="2"
            >
              <v-hover v-slot:default="{ hover }">
                <v-card
                  :elevation="hover ? 12 : 2"
                  @click="selectBook(book)"
                  class="mx-auto"
                  max-width="344"
                >
                  <v-img :src="book.imUrl" min-height="130px"></v-img>
                  <!-- <v-card-title>{{ asin }}</v-card-title> -->
                </v-card>
              </v-hover>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col>
              <v-pagination v-model="pageBest" :length="parseInt(bestBooks.length/6) +1"></v-pagination>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <v-container class="bot-row">
        <v-row>
          <v-col class="section-title">Browse our collection</v-col>
        </v-row>
        <v-row>
          <v-col
            v-for="book in collection"
            v-bind:key="book.asin"
            cols="12"
            xs="6"
            sm="4"
            md="3"
            lg="2"
          >
            <v-hover v-slot:default="{ hover }">
              <v-card
                :elevation="hover ? 12 : 2"
                @click="selectBook(book)"
                class="mx-auto"
                max-width="344"
              >
                <v-img :src="book.imUrl" min-height="130px"></v-img>
                <!-- <v-card-title>{{ asin }}</v-card-title> -->
              </v-card>
            </v-hover>
          </v-col>
        </v-row>
        <v-row v-if="collectionLoading">
          <v-col>
            <div class="loading-collection">
              <v-progress-circular :size="90" :width="7" color="primary" indeterminate></v-progress-circular>
              <div>Loading collection...</div>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<style scoped>
.book {
  padding: 0 10px;
}
.loading-top {
  position: absolute;
  left: 40%;
  text-align: center;
  padding-top: 20%;
  font-size: 2rem;
}
.loading-collection {
  left: 40%;
  text-align: center;
  font-size: 2rem;
}
.top-row {
  background-color: rgb(62, 62, 62);
  width: 100%;
  padding: 0;
}
.section-title {
  font-size: 2rem;
  font-weight: 400;
}
.dropheader {
  font-size: 2rem;
}
</style>

<script>
import Book from "../components/Book.vue";
import EventBus from "../EventBus";

export default {
  components: {
    Book
  },
  computed: {
    pagedBestBooks() {
      if (this.bestBooks) {
        return this.bestBooks.slice(
          (this.pageBest - 1) * 6 > this.bestBooks.length
            ? this.bestBooks.length
            : (this.pageBest - 1) * 6,
          this.pageBest * 6
        );
      } else {
        return [];
      }
    },
    pagedRecommendedBooks() {
      if (this.recommendedBooks) {
        return this.recommendedBooks.slice(
          (this.pageRecommended - 1) * 6 > this.recommendedBooks.length
            ? this.recommendedBooks.length
            : (this.pageRecommended - 1) * 6,
          this.pageRecommended * 6
        );
      } else {
        return [];
      }
    }
  },
  data: () => ({
    scrolledToBottom: false,
    pageBest: 1,
    pageRecommended: 1,
    bookDialog: false,
    collection: [],
    selectedBook: null,
    loadingBookList: true,
    recommendedBooks: [],
    bestBooks: [],
    seed: 0,
    fetchLength: 18,
    collectionLoading: false,
    categories: [{category: 'default 1'}, {category: 'default 2'}, {category: 'default 3'}, {category: 'default 4'}],
    category: ""
  }),
  methods: {
    filterClick(category) {
      this.category = category
      if (this.$router.currentRoute.path != "/filter"+ this.category ) {
        this.$router.push({ path: "/filter/" + this.category });
      } else {
        location.reload();
      }
    },
    getFilterList() {
      this.$store.dispatch("store/categories", {}).then(response => {
        if (response != 0) {
          this.categories = response.categories;
        } else {
          console.log("Error retrieving categories");
          console.log(this.categories);
        }
      });
    },
    getTopRowBooks() {
      this.$store.dispatch("store/main_top_row_books", {}).then(response => {
        if (response != 0) {
          this.recommendedBooks = response.recommended;
          this.bestBooks = response.best;
          this.loadingBookList = false;
        } else {
          console.log("Error retrieving book_list");
        }
      });
    },
    getBotRowBooks() {
      this.collectionLoading = true;
      this.$store
        .dispatch("store/main_bot_row_books", {
          params: {
            start_list: this.collection.length,
            end_list: this.collection.length + this.fetchLength - 1,
            seed: this.seed
          }
        })
        .then(response => {
          if (response != 0) {
            this.collection.push.apply(this.collection, response.collection);
            this.collectionLoading = false;
          } else {
            console.log("Error retrieving book_collection");
          }
        });
    },
    selectBook(book) {
      this.selectedBook = null;
      this.setBook(book.asin);
    },
    setBook(asin) {
      this.bookDialog = true;
      EventBus.$emit("FULL_LOADING_TRUE", "");
      const payload = { asin: asin };
      this.$store.dispatch("store/single_book", payload).then(response => {
        if (response != 0) {
          console.log(response)
          EventBus.$emit("FULL_LOADING_FALSE", "");
          const book = response.book;
          this.selectedBook = book;
          EventBus.$emit("LOAD_REVIEWS", book);
        } else {
          console.log("Error retrieving single book");
          EventBus.$emit("FULL_LOADING_FALSE", "");
          this.bookDialog = false;
        }
      });
    },
    onScroll({ target: { scrollTop, clientHeight, scrollHeight } }) {
      if (scrollTop + clientHeight >= scrollHeight) {
        this.loadMorePosts();
      }
    }
  },
  mounted() {
    this.seed = Math.floor(Math.random() * 1000 + 1);
    this.getFilterList();
    this.getTopRowBooks();
    this.getBotRowBooks();
    EventBus.$on("CHANGE_BOOK", payload => {
      this.setBook(payload);
    });
    EventBus.$on("CLOSE_BOOK_DIALOG", payload => {
      this.bookDialog = false;
    });
    EventBus.$on("GET_BOT_ROW_BOOKS", payload => {
      if (!this.collectionLoading) {
        this.getBotRowBooks();
      }
    });
  }
};
</script>
