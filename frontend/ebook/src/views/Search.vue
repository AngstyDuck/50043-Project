<template>
  <div>
    <v-dialog v-model="bookDialog" min-height="900" width="1700">
      <Book :book="selectedBook" />
    </v-dialog>
    <div class="loading" v-if="loadingBookList">
      <v-progress-circular :size="90" :width="7" color="primary" indeterminate></v-progress-circular>
      <div>Loading books related to {{searchtext}}...</div>
    </div>
    <v-container v-else>
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
    $route(to, from) {
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
    loadingBookList: true,
    searchtext: "",
    fetchLength: 21,
    filtertext: ""
  }),
  methods: {
    getBooks(searchtext, filtertext) {
      this.$store
        .dispatch("store/search_books", {
          params: {
            start_list: this.books.length,
            end_list: this.books.length + this.fetchLength - 1,
            searchtext: this.searchtext,
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
            console.log(this.searchtext);
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
    this.searchtext = this.$route.params.searchtext;
  },
  mounted() {
    this.getBooks();
    EventBus.$on("CHANGE_BOOK", payload => {
      console.log("payload")
      console.log(payload)
      this.setBook(payload);
    });
    EventBus.$on("CLOSE_BOOK_DIALOG", payload => {
      this.bookDialog = false;
    });
  }
};
</script>
