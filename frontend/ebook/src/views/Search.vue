<template>
  <div>
    <v-dialog v-if="selectedBook" v-model="bookDialog" min-height="900" width="1700">
      <Book :book="selectedBook" />
    </v-dialog>
    <div class="loading" v-if="loadingBookList">
      <v-progress-circular :size="90" :width="7" color="primary" indeterminate></v-progress-circular>
      <div>Loading books...</div>
    </div>
    <v-container v-else>
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
        <v-col v-for="book in books" v-bind:key="book.asin" cols="12" xs="6" sm="4" md="3" lg="2">
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
</template>

<style scoped>
.book {
  padding: 0 10px;
}
.loading {
  position: absolute;
  left: 40%;
  text-align: center;
  padding-top: 20%;
  font-size: 2rem;
}
.dropheader {
  font-size: 2rem;
}
</style>

<script>
import Book from "../components/Book.vue";
import EventBus from "../EventBus";

export default {
  watch: {
    '$route' (to,from) {
      this.searchtext = to.params.searchtext;
      this.getBooks();
    }
  },
  components: {
    Book
  },
  data: () => ({
    bookDialog: false,
    books: [],
    selectedBook: null,
    loadingBookList: false,
    searchtext: "",
    categories: [],
    category: "",
    collectionLoading: false,
    fetchLength: 21,
    filtertext: ""
  }),
  methods: {
    filterClick(category) {
      this.category = category
      this.books = []
      console.log(this.searchtext);
      console.log(this.category);
      this.getBooks(this.searchtext,this.category)
    },
    getBooks(searchtext,filtertext) {
      this.collectionLoading = true;
      this.$store.dispatch("store/search_books", {
          params: {
            start_list: this.books.length,
            end_list: this.books.length + this.fetchLength - 1,
            searchtext: this.searchtext,
            filtertext: this.filtertext
          }
        }).then(response => {
        if (response != 0) {
          this.books.push.apply(this.books,response.books);
          this.categories = response.categories
          this.collectionLoading = false;
          console.log(this.books);
        } else {
          console.log("Error retrieving searched books_list");
          console.log(this.searchtext);
          console.log(this.categories);
        }
      });
    },
    selectBook(book) {
      this.selectedBook = book;
      EventBus.$emit("SELECT_BOOK", book);
      console.log(this.selectedBook);
      this.bookDialog = true;
    }
  },

  created() {
    this.searchtext = this.$route.params.searchtext;
  },

  mounted() {
    this.getBooks();
    EventBus.$on("CHANGE_BOOK", payload => {
      this.selectBook(payload);
    });
    EventBus.$on("CLOSE_BOOK_DIALOG", payload => {
      this.bookDialog = false;
    });
    EventBus.$on("GET_BOT_ROW_BOOKS", payload => {
      if (!this.collectionLoading) {
        this.getBooks();
      }
    });
  }
};
</script>
