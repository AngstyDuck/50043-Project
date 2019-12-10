<template>
  <div>
    <v-dialog v-model="bookDialog" min-height="900" width="1700">
      <Book :book="selectedBook" />
    </v-dialog>
    <div class="loading-top" v-if="loadingBookList">
      <v-progress-circular :size="90" :width="7" color="primary" indeterminate></v-progress-circular>
      <div>Loading {{filtertext}} books...</div>
    </div>
    <div v-else>
      <v-container>
        <v-row>
          <v-col v-for="book in books" v-bind:key="book.asin" cols="12" xs="6" sm="4" md="3" lg="2">
            <v-hover v-slot:default="{ hover }">
              <v-card
                :elevation="hover ? 12 : 2"
                @click="selectBook(book)"
                class="mx-auto"
                max-width="344"
              >
                <v-img v-if="book.imUrl" :src="book.imUrl" min-height="130px"></v-img>
              <v-img v-else min-height="130px"></v-img>
              </v-card>
            </v-hover>
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
.dropheader {
  font-size: 2rem;
}
</style>

<script>
import Book from "../components/Book.vue";
import EventBus from "../EventBus";

export default {
  watch: {
    $route(to, from) {
      this.filtertext = to.params.filtertext;
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
    loadingBookList: true,
    filtertext: "",
    collectionLoading: false,
    fetchLength: 21
  }),
  methods: {
    getBooks(filtertext) {
      const payload = { filtertext: this.filtertext };
      this.$store
        .dispatch("store/filter_books", {
          params: {
            start_list: this.books.length,
            end_list: this.books.length + this.fetchLength - 1,
            filtertext: this.filtertext
          }
        })
        .then(response => {
          if (response != 0) {
            this.books.push.apply(this.books, response.books);
            this.loadingBookList = false;
            console.log(this.books);
          } else {
            console.log("Error retrieving searched books_list");
            console.log(this.filtertext);
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
          console.log(response);
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
    }
  },
  created() {
    this.filtertext = this.$route.params.filtertext;
  },
  mounted() {
    this.getBooks();
    EventBus.$on("CHANGE_BOOK", payload => {
      this.setBook(payload);
    });
    EventBus.$on("CLOSE_BOOK_DIALOG", payload => {
      this.bookDialog = false;
    });
  }
};
</script>
